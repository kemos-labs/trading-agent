"""Paper-trading runtime — live-feed aware, no real orders.

Reuses Phase 3's cost/lag discipline: close-decided, next-bar-executed,
10 bps proportional cost per unit turnover by default. State is
persisted to CSV so the process can restart without losing history.
Every run appends to an append-only journal — the only place trades are
recorded. No brokerage API is ever called.
"""

from __future__ import annotations

import json
import warnings
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Callable, Dict, Iterable

import pandas as pd

from quantkit.data_loader import compute_returns
from quantkit.live import load_store
from quantkit.strategies import (
    donchian_breakout_position,
    dual_sma_position,
    vol_targeted_momentum_position,
)

# Reuse paper costs from Phase 3
DEFAULT_PTC = 0.001
DEFAULT_JOURNAL = Path("data/paper/journal.csv")
DEFAULT_STATE = Path("data/paper/state.json")

STRATEGY_MAP: Dict[str, Callable] = {
    "dual_sma_9_45": lambda close, rets: dual_sma_position(
        close, fast=9, slow=45, long_only=True
    ),
    "donchian_50_20": lambda close, rets: donchian_breakout_position(
        close, entry_window=50, exit_window=20
    ),
    "vol_mom_252_60_10pct": lambda close, rets: vol_targeted_momentum_position(
        close,
        rets,
        momentum_lookback=252,
        vol_lookback=60,
        target_vol=0.10,
        max_weight=1.5,
    ),
}


@dataclass
class PaperPosition:
    symbol: str
    strategy: str
    target: float  # last decided target (to be executed next bar)
    exposure: float  # currently held (prev target)
    entry_price: float | None
    bar_date: str  # ISO date of last processed bar


@dataclass
class PaperState:
    capital: float
    ptc: float
    positions: Dict[str, PaperPosition]  # key f"{symbol}:{strategy}"
    equity: float
    peak: float
    last_update: str | None = None
    halted: bool = False
    halt_reason: str | None = None

    def to_json(self) -> str:
        d = asdict(self)
        # positions is dict of dataclass -> dict
        return json.dumps(d, indent=2)

    @classmethod
    def from_json(cls, s: str) -> "PaperState":
        d = json.loads(s)
        pos = {k: PaperPosition(**v) for k, v in d.get("positions", {}).items()}
        d["positions"] = pos
        return cls(**d)


def _load_state(path: Path) -> PaperState | None:
    if not path.exists():
        return None
    try:
        return PaperState.from_json(path.read_text())
    except Exception as exc:  # pragma: no cover
        warnings.warn(f"state {path} unreadable ({exc}); starting fresh")
        return None


def _save_state(state: PaperState, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(state.to_json())
    tmp.replace(path)


def _journal_path(journal: str | Path) -> Path:
    p = Path(journal)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not p.exists():
        p.write_text("timestamp,symbol,strategy,bar_date,close,target,exposure,delta,cost,equity,peak,note\n")
    return p


class PaperTrader:
    """Incremental paper trader — one bar at a time, paper only.

    Parameters
    ----------
    capital: starting capital, split equally across symbol/strategy legs
    ptc: proportional cost per unit turnover (0.001 = 10 bps)
    symbols: e.g. ("SPY","QQQ","TLT")
    strategies: subset of STRATEGY_MAP keys
    store_dir: where live.py writes per-symbol CSVs
    state_path: persisted PaperState JSON
    journal_path: append-only CSV of decisions
    """

    def __init__(
        self,
        *,
        capital: float = 1_000_000.0,
        ptc: float = DEFAULT_PTC,
        symbols: Iterable[str] = ("SPY", "QQQ", "TLT"),
        strategies: Iterable[str] = ("dual_sma_9_45", "vol_mom_252_60_10pct"),
        store_dir: str | Path = "data/live",
        state_path: str | Path = DEFAULT_STATE,
        journal_path: str | Path = DEFAULT_JOURNAL,
        max_drawdown: float | None = None,
        max_position: float | None = None,
    ):
        if capital <= 0:
            raise ValueError("capital must be positive")
        if ptc < 0:
            raise ValueError("ptc must be >= 0")
        if max_drawdown is not None and not 0 < max_drawdown < 1:
            raise ValueError("max_drawdown must be in (0,1)")
        if max_position is not None and max_position <= 0:
            raise ValueError("max_position must be >0")
        self.capital = float(capital)
        self.ptc = float(ptc)
        self.max_drawdown = float(max_drawdown) if max_drawdown is not None else None
        self.max_position = float(max_position) if max_position is not None else None
        self.symbols = tuple(s.strip().upper() for s in symbols)
        self.strategies = tuple(strategies)
        for s in self.strategies:
            if s not in STRATEGY_MAP:
                raise ValueError(f"unknown strategy {s!r}; choices {sorted(STRATEGY_MAP)}")
        self.store_dir = Path(store_dir)
        self.state_path = Path(state_path)
        self.journal_path = _journal_path(journal_path)
        # Load or init state
        loaded = _load_state(self.state_path)
        if loaded is not None:
            self.state = loaded
        else:
            positions: Dict[str, PaperPosition] = {}
            for sym in self.symbols:
                for strat in self.strategies:
                    k = f"{sym}:{strat}"
                    positions[k] = PaperPosition(
                        symbol=sym,
                        strategy=strat,
                        target=0.0,
                        exposure=0.0,
                        entry_price=None,
                        bar_date="1970-01-01",
                    )
            self.state = PaperState(
                capital=self.capital,
                ptc=self.ptc,
                positions=positions,
                equity=self.capital,
                peak=self.capital,
                last_update=None,
            )

    def _strategy_fn(self, name: str) -> Callable:
        return STRATEGY_MAP[name]

    def step(self, *, dry_run: bool = False) -> pd.DataFrame:
        """Process the latest closed bar for every symbol/strategy leg.

        - Loads the store CSV for each symbol (fail-closed if missing).
        - Computes the target at the last close (point-in-time safe).
        - The trade decided at bar T is for execution at T+1; we log
          `target` now and flip `exposure = target` for *next* step's
          P&L. Costs are `ptc * |delta| * (capital / n_legs)` and
          reduce `equity` immediately (cash-at-decision, as in
          BacktestEngine).
        - `dry_run=True` computes and journals with note=dry_run but
          does not persist state (useful for --offline replay tests).

        Returns a DataFrame of this step's decisions (one row per leg).
        """
        # Kill-switch: halted state persists until reset
        if self.state.halted:
            warnings.warn(f"paper halted ({self.state.halt_reason}); no new targets (reset state.json to resume)")
            return pd.DataFrame(columns=["timestamp","symbol","strategy","bar_date","close","target","exposure","delta","cost","equity","peak","note"])
        # Pre-step drawdown check
        if self.max_drawdown is not None and self.state.peak > 0:
            dd = (self.state.peak - self.state.equity) / self.state.peak
            if dd >= self.max_drawdown:
                self.state.halted = True
                self.state.halt_reason = f"drawdown {dd:.2%} >= max {self.max_drawdown:.2%}"
                _save_state(self.state, self.state_path)
                warnings.warn(f"paper halted: {self.state.halt_reason}")
                return pd.DataFrame(columns=["timestamp","symbol","strategy","bar_date","close","target","exposure","delta","cost","equity","peak","note"])
        n_legs = len(self.symbols) * len(self.strategies)
        capital_per_leg = self.state.equity / n_legs if n_legs else self.state.equity
        rows = []
        now_iso = pd.Timestamp.now("UTC").isoformat()

        for sym in self.symbols:
            df = load_store(sym, self.store_dir)
            if df is None or len(df) < 2:
                raise RuntimeError(
                    f"store for {sym} missing or too short at {self.store_dir}; "
                    f"run live.py update_store or use --offline replay from data/research/phase3"
                )
            close = df["close"]
            rets = compute_returns(close, log=False)

            bar_date = close.index[-1]
            bar_date_str = bar_date.strftime("%Y-%m-%d")
            bar_close = float(close.iloc[-1])

            for strat in self.strategies:
                k = f"{sym}:{strat}"
                pos = self.state.positions[k]
                # Skip if we've already processed this bar for this leg
                if pos.bar_date == bar_date_str:
                    continue

                fn = self._strategy_fn(strat)
                # Full series -> point-in-time target at last bar
                target_series = fn(close, rets)
                target = float(target_series.iloc[-1])
                # Position cap (kill-switch)
                if self.max_position is not None:
                    target = float(np.clip(target, -self.max_position, self.max_position))
                    if abs(target) >= self.max_position - 1e-9 and abs(float(target_series.iloc[-1])) > self.max_position:
                        warnings.warn(f"{sym}:{strat} target clipped to max_position {self.max_position}")
                # Exposure held *during* the bar that just closed was the
                # previous target; delta is the new decision's change.
                prev_target = pos.target
                delta = target - prev_target
                cost = self.ptc * abs(delta) * capital_per_leg

                # Update equity for costs (paper cash)
                new_equity = self.state.equity - cost
                # Note: true P&L from market move will be realized on the
                # *next* bar when exposure = target is held; we don't
                # fabricate next-bar return here — paper equity is
                # cost-aware and tracks exposure for next step.

                # Prepare next exposure
                new_exposure = target

                rows.append(
                    {
                        "timestamp": now_iso,
                        "symbol": sym,
                        "strategy": strat,
                        "bar_date": bar_date_str,
                        "close": bar_close,
                        "target": target,
                        "exposure": new_exposure,
                        "delta": delta,
                        "cost": cost,
                        "equity": new_equity,
                        "peak": max(self.state.peak, new_equity),
                        "note": "paper_only; execution next bar" + ("; dry_run" if dry_run else ""),
                    }
                )

                if not dry_run:
                    # Persist per-leg
                    pos.target = target
                    pos.exposure = new_exposure
                    pos.bar_date = bar_date_str
                    if target != 0 and pos.entry_price is None:
                        pos.entry_price = bar_close
                    if target == 0:
                        pos.entry_price = None

                    self.state.equity = new_equity
                    self.state.peak = max(self.state.peak, new_equity)
                    self.state.last_update = now_iso

        if not rows:
            return pd.DataFrame(columns=["timestamp","symbol","strategy","bar_date","close","target","exposure","delta","cost","equity","peak","note"])

        out = pd.DataFrame(rows)
        # Append to journal (always, even dry_run — but dry_run adds note)
        with self.journal_path.open("a") as f:
            out.to_csv(f, header=False, index=False)

        if not dry_run:
            _save_state(self.state, self.state_path)

        return out

    def equity(self) -> float:
        return float(self.state.equity)

    def positions_df(self) -> pd.DataFrame:
        return pd.DataFrame([asdict(p) for p in self.state.positions.values()])
