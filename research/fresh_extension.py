#!/usr/bin/env python
"""Extended-window diagnostic — fixed Phase 3 rules on spliced fresh data.

Splices SHA-pinned base (data/research/phase3) with fresh pulls
(data/research/fresh) via median-ratio rescale on shared December-2024
dates, then runs the FIXED Phase 3 strategy lambdas (same params, 10 bps,
next-bar) over the full 2010→2026 window. Reports the genuinely
out-of-sample 2025-2026 leg the frozen rules never saw.

Diagnostic only: never rewrites phase3 verdicts or SHAs.
Writes knowledge/strategy-research/fresh-extension-2026-09-25.md.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from quantkit.backtest import performance_summary, vectorized_backtest
from quantkit.data_loader import compute_returns
from quantkit.strategies import (
    donchian_breakout_position,
    dual_sma_position,
    vol_targeted_momentum_position,
)

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data" / "research" / "phase3"
FRESH = ROOT / "data" / "research" / "fresh"
SYMBOLS = ("SPY", "QQQ", "TLT")
PTC = 0.001
FRESH_START = "2025-01-01"

STRATEGIES = {
    "dual_sma_9_45": lambda close, rets: dual_sma_position(close, fast=9, slow=45),
    "donchian_50_20": lambda close, rets: donchian_breakout_position(close, entry_window=50, exit_window=20),
    "vol_mom_252_60_10pct": lambda close, rets: vol_targeted_momentum_position(
        close, rets, momentum_lookback=252, vol_lookback=60, target_vol=0.10, max_weight=1.5),
}


def splice(sym: str) -> tuple[pd.DataFrame, float]:
    b = pd.read_csv(BASE / f"ohlcv_{sym}.csv", parse_dates=["date"])
    f = pd.read_csv(FRESH / f"ohlcv_{sym}.csv", parse_dates=["date"])
    b = b.set_index(b.date.dt.normalize()).sort_index()
    f = f.set_index(f.date.dt.normalize()).sort_index()
    shared = b.index.intersection(f.index)
    if len(shared) < 5:
        raise SystemExit(f"{sym}: only {len(shared)} shared dates, cannot anchor splice")
    ratio = float((f.loc[shared, "close"] / b.loc[shared, "close"]).median())
    b_scaled = b.copy()
    for c in ["open", "high", "low", "close"]:
        b_scaled[c] = b_scaled[c] * ratio
    seam = b_scaled.loc[b_scaled.index < f.index[0]]
    full = pd.concat([seam, f])
    full = full[~full.index.duplicated(keep="last")].sort_index()
    return full, ratio


def main() -> None:
    frames = {}
    lines = ["# Fresh extension diagnostic — 2026-09-25", "",
             "Fixed Phase 3 rules (same params, 10 bps, next-bar) on spliced base+fresh.",
             "Diagnostic only — phase3 verdicts/SHAs untouched.", "",
             "| sym | anchor ratio | base bars | fresh bars | full range |",
             "|---|---|---|---|---|"]
    for sym in SYMBOLS:
        full, ratio = splice(sym)
        frames[sym] = full
        lines.append(f"| {sym} | {ratio:.5f} | {(full.index < f'{FRESH_START}').sum()} | "
                     f"{(full.index >= FRESH_START).sum()} | {full.index[0].date()} → {full.index[-1].date()} |")
    idx = frames[SYMBOLS[0]].index
    for sym in SYMBOLS[1:]:
        idx = idx.intersection(frames[sym].index)
    lines += ["", f"Common bars: {len(idx)} ({idx[0].date()} → {idx[-1].date()})", "",
              "| strategy | window | total | CAGR | Sharpe | MaxDD |",
              "|---|---|---|---|---|---|"]
    for name, fn in list(STRATEGIES.items()) + [("buy_hold", None)]:
        nets = {}
        for sym in SYMBOLS:
            close = frames[sym].loc[idx, "close"]
            rets = compute_returns(close, log=False)
            pos = pd.Series(1.0, index=idx) if fn is None else fn(close, rets)
            nets[sym] = vectorized_backtest(rets, pos, ptc=PTC, ffc=0.0)["net"]
        port = pd.concat(nets, axis=1).mean(axis=1)
        for label, sl in [("full", slice(None)), ("2025+", slice(FRESH_START, None))]:
            s = performance_summary(port.loc[sl], periods_per_year=252)
            lines.append(f"| {name} | {label} | {s['total_return']:.2%} | {s['cagr']:.2%} | "
                         f"{s['sharpe']:.2f} | {s['max_drawdown']:.2%} |")
    out = ROOT / "knowledge" / "strategy-research" / "fresh-extension-2026-09-25.md"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
