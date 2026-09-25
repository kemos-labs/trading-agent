#!/usr/bin/env python
"""Predeclared Phase 3 strategy research harness.

Real adjusted daily data only; fails closed if Yahoo is unavailable.
Equal-weight SPY/QQQ/TLT, 10 bps turnover cost, one-bar execution lag,
fixed 2019-01-01 holdout, no parameter search on OOS.

Reproducible inputs are saved under data/research/phase3/; reruns from
those CSVs must yield identical metrics. This script is the single
source of truth for Phase 3 numbers — do not edit results by hand.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Allow `PYTHONPATH=src` or direct execution from project root.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from quantkit.backtest import performance_summary, vectorized_backtest
from quantkit.data_loader import compute_returns, load_yfinance
from quantkit.strategies import (
    donchian_breakout_position,
    dual_sma_position,
    vol_targeted_momentum_position,
)

# ---------------------------------------------------------------------------
# Predeclared protocol constants — changing these is a protocol change,
# not a parameter tweak. Record the change in the markdown report.
# ---------------------------------------------------------------------------
SYMBOLS = ("SPY", "QQQ", "TLT")
START = "2010-01-01"
END = "2025-01-01"  # exclusive in yfinance; last bar is 2024-12-31
DEV_END = "2018-12-31"
OOS_START = "2019-01-01"
PTC = 0.001  # 10 bps per unit of turnover
ANNUALIZATION = 252

STRATEGIES = {
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
        annualization=ANNUALIZATION,
    ),
}

DATA_DIR = Path(__file__).resolve().parents[1] / "data" / "research" / "phase3"
REPORT_PATH = (
    Path(__file__).resolve().parents[1]
    / "knowledge"
    / "strategy-research"
    / "phase3-results.md"
)


def _ohlcv_path(symbol: str) -> Path:
    return DATA_DIR / f"ohlcv_{symbol}.csv"


def _hash_file(path: Path) -> str:
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()[:12]


def load_or_download(symbol: str) -> pd.DataFrame:
    """Load OHLCV from Yahoo, saving a reproducible CSV, or fail closed."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    cached = _ohlcv_path(symbol)
    # Explicit offline mode: use cached CSV without hitting the network.
    if "--offline" in sys.argv:
        if not cached.exists():
            print(f"[fatal] --offline requested but no cached {cached}", file=sys.stderr)
            sys.exit(2)
        df = pd.read_csv(cached, index_col=0, parse_dates=True)
        from quantkit.data_loader import normalize_columns, validate_ohlcv

        df = normalize_columns(df)
        df = validate_ohlcv(df)
        print(f"[offline] {symbol}: {len(df)} bars {df.index.min().date()} → {df.index.max().date()} ← {cached} sha256:{_hash_file(cached)}")
        return df
    try:
        df = load_yfinance(symbol, start=START, end=END, interval="1d", auto_adjust=True)
    except Exception as exc:  # fail closed — never fall back to mock data
        if cached.exists():
            print(f"[fatal] yfinance failed for {symbol}: {exc}", file=sys.stderr)
            print(f"A cached file exists at {cached} — rerun with --offline to use it.", file=sys.stderr)
        else:
            print(f"[fatal] yfinance unavailable for {symbol}: {exc}", file=sys.stderr)
        print("Refusing to continue with mock/simulated data (see AGENTS.md).", file=sys.stderr)
        sys.exit(2)
    # Persist the validated frame for reproducibility.
    out = cached
    df.to_csv(out, index_label="date")
    print(f"[ok] {symbol}: {len(df)} bars {df.index.min().date()} → {df.index.max().date()} → {out} sha256:{_hash_file(out)}")
    return df


def _summarize_returns(rets: pd.Series, label: str) -> dict:
    s = performance_summary(rets, periods_per_year=ANNUALIZATION)
    # add human-readable label
    s["label"] = label
    return s


def main() -> None:
    print("=== Phase 3 — strategy research (predeclared protocol) ===")
    print(f"Symbols: {', '.join(SYMBOLS)}  {START} → {END}  DEV through {DEV_END}  OOS from {OOS_START}  PTC={PTC}")
    print(f"Strategies: {', '.join(STRATEGIES)}  (fixed, no search)")
    print()

    # 1. Load data (real only)
    frames: dict[str, pd.DataFrame] = {}
    for sym in SYMBOLS:
        frames[sym] = load_or_download(sym)

    # Align indices — all three ETFs should share the same calendar.
    common_idx = frames[SYMBOLS[0]].index
    for sym in SYMBOLS[1:]:
        if not frames[sym].index.equals(common_idx):
            # Intersection fallback (should not happen for these ETFs, but be explicit)
            common_idx = common_idx.intersection(frames[sym].index)
    if len(common_idx) < 1000:
        print(f"[fatal] insufficient overlapping bars: {len(common_idx)}", file=sys.stderr)
        sys.exit(2)
    for sym in SYMBOLS:
        frames[sym] = frames[sym].loc[common_idx]

    # 2. Per-symbol returns and positions
    closes: dict[str, pd.Series] = {s: frames[s]["close"] for s in SYMBOLS}
    rets_simple: dict[str, pd.Series] = {
        s: compute_returns(closes[s], log=False).rename("ret") for s in SYMBOLS
    }

    # Basket buy-and-hold (equal-weight, buy at first close, hold)
    bh_position = {s: pd.Series(1.0, index=common_idx, name="position") for s in SYMBOLS}

    # Collect results
    per_symbol_bt: dict[str, dict[str, pd.DataFrame]] = {name: {} for name in STRATEGIES}
    per_symbol_bt["buy_hold"] = {}
    bh_portfolio_net = None
    strat_portfolio_nets: dict[str, pd.Series] = {}

    # Also keep per-symbol net series for hit-rate checks
    per_symbol_nets: dict[str, dict[str, pd.Series]] = {name: {} for name in STRATEGIES}
    per_symbol_nets["buy_hold"] = {}

    for sym in SYMBOLS:
        rets = rets_simple[sym]
        close = closes[sym]
        # buy-and-hold baseline (costed identically)
        bh_bt = vectorized_backtest(rets, bh_position[sym], ptc=PTC, ffc=0.0)
        per_symbol_bt["buy_hold"][sym] = bh_bt
        per_symbol_nets["buy_hold"][sym] = bh_bt["net"]

        for name, fn in STRATEGIES.items():
            pos = fn(close, rets)
            # sanity: no look-ahead — position at t must not depend on close[t+1]
            bt = vectorized_backtest(rets, pos, ptc=PTC, ffc=0.0)
            per_symbol_bt[name][sym] = bt
            per_symbol_nets[name][sym] = bt["net"]
            # persist per-symbol backtest
            out = DATA_DIR / f"backtest_{name}_{sym}.csv"
            bt.to_csv(out, index_label="date")

    # 3. Equal-weight portfolio nets (mean of per-symbol nets)
    for name in list(STRATEGIES.keys()) + ["buy_hold"]:
        # stack nets
        stacked = pd.concat([per_symbol_nets[name][s] for s in SYMBOLS], axis=1)
        stacked.columns = list(SYMBOLS)
        port_net = stacked.mean(axis=1)
        if name == "buy_hold":
            bh_portfolio_net = port_net
        else:
            strat_portfolio_nets[name] = port_net
        # persist
        port_path = DATA_DIR / f"portfolio_{name}_net.csv"
        port_net.to_csv(port_path, header=True)
        stacked.to_csv(DATA_DIR / f"per_symbol_{name}_nets.csv", index_label="date")

    assert bh_portfolio_net is not None

    # 4. Performance summaries — dev, oos, full
    def _slice(s: pd.Series, start: str | None = None, end: str | None = None) -> pd.Series:
        if start is not None:
            s = s.loc[start:]
        if end is not None:
            s = s.loc[:end]
        return s

    # Build markdown report
    lines: list[str] = []
    lines.append("# Phase 3 — Strategy research results (predeclared OOS)")
    lines.append("")
    lines.append(f"Generated by `research/run_phase3.py` on {pd.Timestamp.now(tz='UTC'):%Y-%m-%d %H:%M UTC}.")
    lines.append("Do not edit numbers by hand — rerun the script from `data/research/phase3/`.")
    lines.append("")
    lines.append("## Protocol")
    lines.append("")
    lines.append(f"- Universe: {', '.join(SYMBOLS)} (adjusted daily OHLCV via yfinance, `auto_adjust=True`).")
    lines.append(f"- Window: {START} → 2024-12-31. Development ≤ {DEV_END}. **Held-out OOS ≥ {OOS_START}**.")
    lines.append(f"- Execution: close-decision → next-bar execution via `vectorized_backtest` (`position.shift(1)`), 10 bps proportional cost per unit turnover, no look-ahead, equal-weight portfolio.")
    lines.append("- Fixed hypotheses (no OOS search):")
    lines.append("  - `dual_sma_9_45` — long when SMA(9) > SMA(45), flat otherwise.")
    lines.append("  - `donchian_50_20` — long/flat breakout: enter above prior 50-bar high, exit below prior 20-bar low (channels are prior-bar extrema; position persists; executed next bar).")
    lines.append("  - `vol_mom_252_60_10pct` — long when 252-day momentum > 0, scaled to 10% annual vol on a 60-day window, capped at 1.5×.")
    lines.append("- Baseline: equal-weight buy-and-hold (daily mean of asset simple returns, same cost model).")
    lines.append("- PASS (all): OOS total return > 0, OOS Sharpe > buy-and-hold Sharpe, OOS max DD shallower than buy-and-hold, and positive OOS return on ≥ 2/3 assets. Otherwise REJECT.")
    lines.append("")
    lines.append("## Data snapshot")
    lines.append("")
    lines.append("| Symbol | Bars | First | Last | SHA256 (12) |")
    lines.append("|---|---|---|---|---|")
    for sym in SYMBOLS:
        p = _ohlcv_path(sym)
        df = frames[sym]
        h = _hash_file(p) if p.exists() else "—"
        lines.append(f"| {sym} | {len(df)} | {df.index.min().date()} | {df.index.max().date()} | `{h}` |")
    lines.append("")
    lines.append(f"Common aligned bars: {len(common_idx)} ({common_idx.min().date()} → {common_idx.max().date()}).")
    lines.append("")

    # Helper to format performance dict
    def _fmt_perf(d: dict) -> str:
        # total_return as %, cagr %, ann_vol %, sharpe, max_dd %, dd_duration, mar
        return (
            f"{d['total_return']*100:6.2f}% | {d['cagr']*100:6.2f}% | {d['ann_vol']*100:5.2f}% | "
            f"{d['sharpe']:5.2f} | {d['max_drawdown']*100:6.2f}% | {int(d['dd_duration']):4d} | {d['mar']:5.2f}"
        )

    # Portfolio tables
    for label, start, end in [
        ("Full (2010-01-01 → 2024-12-31)", None, None),
        (f"Development (≤ {DEV_END})", None, DEV_END),
        (f"OOS / holdout (≥ {OOS_START})", OOS_START, None),
    ]:
        lines.append(f"## Portfolio — {label}")
        lines.append("")
        lines.append("| Strategy | Total | CAGR | Ann vol | Sharpe | Max DD | DD days | MAR |")
        lines.append("|---|---:|---:|---:|---:|---:|---:|---:|")
        bh_perf = _summarize_returns(_slice(bh_portfolio_net, start, end), "buy_hold")
        lines.append(f"| buy_hold (EW) | {_fmt_perf(bh_perf)} |")
        for name in STRATEGIES:
            perf = _summarize_returns(_slice(strat_portfolio_nets[name], start, end), name)
            lines.append(f"| {name} | {_fmt_perf(perf)} |")
        lines.append("")

    # Per-symbol OOS breakdown
    lines.append(f"## Per-symbol OOS (≥ {OOS_START}, 10 bps, one-bar lag)")
    lines.append("")
    lines.append("| Symbol | Strategy | Total | CAGR | Sharpe | Max DD | DD days | Verdict* |")
    lines.append("|---|---|---:|---:|---:|---:|---:|---|")
    # Determine pass/fail per strategy portfolio
    bh_oos_perf = _summarize_returns(_slice(bh_portfolio_net, OOS_START, None), "buy_hold")
    verdicts: dict[str, str] = {}
    for name in STRATEGIES:
        port_oos = _slice(strat_portfolio_nets[name], OOS_START, None)
        perf = _summarize_returns(port_oos, name)
        # per-symbol positivity
        pos_count = sum(
            1
            for sym in SYMBOLS
            if _summarize_returns(_slice(per_symbol_nets[name][sym], OOS_START, None), sym)["total_return"] > 0
        )
        conds = [
            ("total_return>0", perf["total_return"] > 0),
            ("Sharpe>BH", perf["sharpe"] > bh_oos_perf["sharpe"]),
            ("DD shallower", perf["max_drawdown"] > bh_oos_perf["max_drawdown"]),  # less negative
            (f"≥2/3 assets + ({pos_count}/3)", pos_count >= 2),
        ]
        ok = all(v for _, v in conds)
        verdicts[name] = "PASS" if ok else "REJECT"
        for sym in SYMBOLS:
            p = _summarize_returns(_slice(per_symbol_nets[name][sym], OOS_START, None), sym)
            tag = verdicts[name] if sym == SYMBOLS[0] else ""
            lines.append(
                f"| {sym} | {name} | {p['total_return']*100:6.2f}% | {p['cagr']*100:5.2f}% | {p['sharpe']:5.2f} | {p['max_drawdown']*100:6.2f}% | {int(p['dd_duration']):4d} | {tag} |"
            )
        lines.append(f"| EW portfolio | {name} | {perf['total_return']*100:6.2f}% | {perf['cagr']*100:5.2f}% | {perf['sharpe']:5.2f} | {perf['max_drawdown']*100:6.2f}% | {int(perf['dd_duration']):4d} | {verdicts[name]} |")
        # add condition breakdown as comment row
        lines.append(f"|  |  |  |  |  |  |  | {'; '.join(f'{k}={v}' for k,v in conds)} |")
    lines.append("")
    lines.append("* Portfolio verdict uses all four conditions above; per-symbol rows show the same portfolio verdict for reference.")
    lines.append("")
    lines.append("## Costs and turnover")
    lines.append("")
    # Report average daily turnover per strategy (mean |Δpos| across assets)
    lines.append("| Strategy | Mean daily turnover (per asset, |Δpos|) |")
    lines.append("|---|---:|")
    for name in STRATEGIES:
        # recompute mean abs delta across symbols on OOS
        vals = []
        for sym in SYMBOLS:
            close = closes[sym]
            pos = STRATEGIES[name](close, rets_simple[sym])
            pos_oos = pos.loc[OOS_START:]
            vals.append(pos_oos.diff().abs().fillna(pos_oos.iloc[0] if len(pos_oos) else 0).mean())
        lines.append(f"| {name} | {np.mean(vals):.4f} |")
    bh_turnover = 0.0  # buy-and-hold trades once
    lines.append(f"| buy_hold | {bh_turnover:.4f} |")
    lines.append("")
    lines.append("## Interpretation")
    lines.append("")
    # Auto-generate interpretation based on verdicts
    any_pass = any(v == "PASS" for v in verdicts.values())
    if any_pass:
        passing = ", ".join(k for k, v in verdicts.items() if v == "PASS")
        lines.append(f"**Candidate(s) for further validation:** {passing}. A PASS under this narrow three-ETF, single-holdout protocol is *not* approval to trade — it only means the hypothesis survived a minimal real-data screen and deserves broader walk-forward, cross-asset, and transaction-cost sensitivity checks before any paper trading.")
    else:
        lines.append("**No hypothesis passed the predeclared OOS screen.** All three are REJECTed as stand-alone equal-weight strategies on this universe/holdout. Do not promote to paper trading; consider whether any idea merits a revised hypothesis with its own fresh holdout (not by reusing this OOS).")
    lines.append("")
    lines.append("Common failure modes to check before any follow-up: insufficient diversification (N=3), regime dependence (2019–2024 was mostly a trending bull market with a 2020/2022 drawdown), and the equal-weight assumption itself. The FMZ catalog remains useful only as a source of *other* fixed hypotheses to test under the same protocol, not as evidence of profitability.")
    lines.append("")
    lines.append("## Reproducibility")
    lines.append("")
    lines.append("- Inputs: `data/research/phase3/ohlcv_*.csv` (yfinance `auto_adjust=True` validated OHLCV), `data/research/phase3/backtest_*.csv`, `data/research/phase3/portfolio_*_net.csv`.")
    lines.append("- Rerun: `PYTHONPATH=src .venv/bin/python research/run_phase3.py` (add `--offline` to rerun from cached OHLCV without hitting Yahoo).")
    lines.append("- Determinism: rerunning from the same `data/research/phase3/ohlcv_*.csv` must reproduce identical portfolio numbers; the 12-char SHA256 above fingerprints the inputs.")
    lines.append("- No mock data was used; a download failure exits non-zero per `AGENTS.md`.")
    lines.append("")
    lines.append("## FMZ link")
    lines.append("")
    lines.append("Assessment of the `fmzquant/strategies` clone is in `knowledge/fmz-strategies-assessment.md`. Only fixed idea defaults were taken; no FMZ execution code was copied (no license file was present and several examples contain look-ahead).")
    lines.append("")

    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text("\n".join(lines))
    print(f"\n[report] {REPORT_PATH}")
    # Also print verdict summary to stdout for the session log
    for name, v in verdicts.items():
        print(f"[verdict] {name}: {v}")
    # Persist a machine-readable summary as well
    summary_path = DATA_DIR / "summary.json"
    import json

    summary = {
        "protocol": {
            "symbols": list(SYMBOLS),
            "start": START,
            "end": END,
            "dev_end": DEV_END,
            "oos_start": OOS_START,
            "ptc": PTC,
        },
        "verdicts": verdicts,
        "portfolio_oos": {
            name: _summarize_returns(_slice(strat_portfolio_nets[name], OOS_START, None), name)
            for name in STRATEGIES
        },
        "buy_hold_oos": bh_oos_perf,
    }
    summary_path.write_text(json.dumps(summary, indent=2, default=str))
    print(f"[summary] {summary_path}")


if __name__ == "__main__":
    main()
