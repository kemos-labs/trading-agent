#!/usr/bin/env python
"""Pull fresh daily bars (SPY/QQQ/TLT) via quantkit.fresh and stage for research.

- Reads keys at runtime from TERMINAL_ENV (never committed).
- Writes validated canonical CSVs to data/research/fresh/ohlcv_{SYM}.csv.
- Overlap-checks against the SHA-pinned data/research/phase3/ohlcv_{SYM}.csv
  tails and prints a continuity report (last cached date -> first fresh date,
  close agreement on shared dates).
- Runs the three Phase 3 strategies over the EXTENDED window as a diagnostic
  only (does not rewrite phase3 verdicts).

Usage:
    PYTHONPATH=src .venv/bin/python research/pull_fresh.py [--symbols SPY,QQQ,TLT]
        [--start 2024-12-01] [--end 2025-09-25] [--ttl-h 12]

Fresh cache (data/fresh/raw, TTL) is reused automatically — no flag needed
to avoid burning provider budget on repeats.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from quantkit.data_loader import validate_ohlcv
from quantkit.fresh import QuotaLedger, fetch_finnhub_quote, load_terminal_keys, pull_symbol

ROOT = Path(__file__).resolve().parents[1]
FRESH = ROOT / "data" / "research" / "fresh"
PHASE3 = ROOT / "data" / "research" / "phase3"


def overlap_report(sym: str, fresh: pd.DataFrame) -> str:
    base_path = PHASE3 / f"ohlcv_{sym}.csv"
    if not base_path.exists():
        return f"{sym}: no phase3 base to overlap (fresh {len(fresh)} bars {fresh.index[0].date()}->{fresh.index[-1].date()})"
    base = pd.read_csv(base_path, parse_dates=["date"])
    bdates = pd.to_datetime(base["date"])
    shared = fresh.index.normalize().isin(bdates.dt.normalize().values)
    n_shared = int(shared.sum())
    tail_close = float(base["close"].iloc[-1])
    head_close = float(fresh["close"].iloc[0])
    tail_date = bdates.iloc[-1].date()
    head_date = fresh.index[0].date()
    agree = ""
    if n_shared:
        fsub = fresh[shared].copy()
        bsub = base.set_index(bdates.dt.normalize()).reindex(fsub.index.normalize())
        rel = ((fsub["close"].values - bsub["close"].values) / bsub["close"].values)
        agree = f" shared={n_shared} max|rel close diff|={abs(rel).max():.4f}"
    return (f"{sym}: base tail {tail_date} {tail_close:.2f} -> fresh head {head_date} {head_close:.2f}"
            f" ({len(fresh)} bars){agree}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", default="SPY,QQQ,TLT")
    ap.add_argument("--start", default="2024-12-01")
    ap.add_argument("--end", default="2025-09-25")
    ap.add_argument("--ttl-h", type=float, default=12.0)
    args = ap.parse_args()

    keys = load_terminal_keys()
    ledger = QuotaLedger(ROOT / "data" / "fresh" / "quota.json")
    FRESH.mkdir(parents=True, exist_ok=True)
    syms = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]

    for sym in syms:
        try:
            bars, provider = pull_symbol(sym, args.start, args.end, keys, ledger,
                                         cache_dir=ROOT / "data" / "fresh" / "raw",
                                         ttl_h=args.ttl_h)
        except Exception as exc:  # noqa: BLE001 — report per symbol, continue
            print(f"FAIL {sym}: {exc}")
            continue
        validate_ohlcv(bars.reset_index().rename(columns={"index": "date"}))
        out = FRESH / f"ohlcv_{sym}.csv"
        bars.to_csv(out, index_label="date")
        print(f"OK {sym} via {provider}: {len(bars)} bars "
              f"{bars.index[0].date()}->{bars.index[-1].date()} -> {out.name}")
        print("   " + overlap_report(sym, bars))
        # staleness cross-check (1 cheap call per symbol; fail-open: warn only)
        try:
            q = fetch_finnhub_quote(sym, keys, ledger)
            lag = (bars.index[-1].date() - pd.Timestamp(q["time"], unit="s").date()).days
            print(f"   finnhub last {q['last']:.2f} vs fresh close {bars['close'].iloc[-1]:.2f} "
                  f"(bar lag {lag}d)")
        except Exception as exc:  # noqa: BLE001
            print(f"   finnhub cross-check skipped: {exc}")
    print(f"ledger: massive={ledger.used('massive')} finnhub={ledger.used('finnhub')} "
          f"alphavantage={ledger.used('alphavantage')}")


if __name__ == "__main__":
    main()
