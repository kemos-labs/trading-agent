#!/usr/bin/env python
"""Paper-trading CLI — live yfinance polling + offline replay.

- Online: poll Yahoo for 1d bars (via quantkit.live.update_store), then
  step the paper trader (cost/lag disciplined, paper_only).
- Offline: copy cached Phase-3 bars into the live store and step
  without network (deterministic replay for tests/docs).

Never places real orders. State in data/paper/state.json, journal in
data/paper/journal.csv (append-only). Exit 2 on feed failure (fail-closed).
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

import pandas as pd

# allow PYTHONPATH=src or direct
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from quantkit.live import update_store
from quantkit.paper import PaperTrader


def _parse_args():
    p = argparse.ArgumentParser(description="Paper-trading runner (paper-only)")
    p.add_argument("--symbols", nargs="+", default=["SPY", "QQQ", "TLT"], help="symbols")
    p.add_argument("--strategies", nargs="+", default=["dual_sma_9_45", "vol_mom_252_60_10pct"], help="strategy keys from paper.STRATEGY_MAP")
    p.add_argument("--store-dir", default="data/live", help="live store dir")
    p.add_argument("--journal", default="data/paper/journal.csv")
    p.add_argument("--state", default="data/paper/state.json")
    p.add_argument("--capital", type=float, default=1_000_000)
    p.add_argument("--ptc", type=float, default=0.001, help="proportional cost per unit turnover")
    p.add_argument("--lookback-days", type=int, default=10)
    p.add_argument("--offline", action="store_true", help="replay from data/research/phase3 caches without network")
    p.add_argument("--offline-src", default="data/research/phase3", help="offline cache dir")
    p.add_argument("--dry-run", action="store_true", help="compute and journal with dry_run note, but do not persist state")
    p.add_argument("--reset-state", action="store_true", help="delete state.json before stepping (fresh start)")
    p.add_argument("--impact-on", action="store_true", help="add Almgren impact layer on top of flat ptc (requires --outstanding)")
    p.add_argument("--horizon-days", type=float, default=1.0, help="execution horizon in trading days (volume time T)")
    p.add_argument("--outstanding", type=float, default=None, help="shares outstanding per symbol (required with --impact-on)")
    return p.parse_args()


def _offline_seed(symbols, offline_src: Path, store_dir: Path):
    offline_src = Path(offline_src)
    store_dir.mkdir(parents=True, exist_ok=True)
    for sym in symbols:
        src = offline_src / f"ohlcv_{sym}.csv"
        if not src.exists():
            print(f"[fatal] offline cache missing {src} (run research/run_phase3.py first)", file=sys.stderr)
            sys.exit(2)
        dst = store_dir / f"{sym}_1d.csv"
        # copy cache to live store (overwrite for deterministic replay)
        shutil.copyfile(src, dst)
        print(f"[offline] seeded {sym} {src} -> {dst} ({dst.stat().st_size} bytes)")


def main():
    args = _parse_args()
    store_dir = Path(args.store_dir)
    offline_src = Path(args.offline_src)

    if args.reset_state:
        p = Path(args.state)
        if p.exists():
            p.unlink()
            print(f"[reset] removed {p}")

    if args.offline:
        _offline_seed(args.symbols, offline_src, store_dir)
    else:
        # online poll — fail-closed per symbol
        for sym in args.symbols:
            try:
                df = update_store(sym, store_dir=store_dir, lookback_days=args.lookback_days)
                print(f"[live] {sym}: {len(df)} bars {df.index.min().date()} -> {df.index.max().date()} {store_dir}/{sym}_1d.csv")
            except Exception as exc:
                print(f"[fatal] live fetch failed for {sym}: {exc}", file=sys.stderr)
                print("Use --offline to replay cached Phase-3 bars.", file=sys.stderr)
                sys.exit(2)

    if args.impact_on and args.outstanding is None:
        print("[fatal] --impact-on requires --outstanding (shares outstanding per symbol)", file=sys.stderr)
        sys.exit(2)

    trader = PaperTrader(
        capital=args.capital,
        ptc=args.ptc,
        symbols=args.symbols,
        strategies=args.strategies,
        store_dir=store_dir,
        state_path=args.state,
        journal_path=args.journal,
        impact_on=args.impact_on,
        horizon_days=args.horizon_days,
        outstanding=args.outstanding,
    )
    out = trader.step(dry_run=args.dry_run)
    if out.empty:
        print("[paper] no new bar to process (already up-to-date for this bar_date)")
    else:
        print(f"[paper] step — {len(out)} leg(s) {'(dry_run)' if args.dry_run else ''}")
        # compact table
        print(out.to_string(index=False))
        print(f"[paper] equity {trader.equity():,.2f} peak {trader.state.peak:,.2f} journal {args.journal} state {args.state}")
        if args.dry_run:
            print("[paper] dry_run — state not persisted (journal appended with note)")

    # Also show gap warning if recent (last 10 business days) — older are holidays
    for sym in args.symbols:
        store = store_dir / f"{sym}_1d.csv"
        if store.exists():
            df = pd.read_csv(store, index_col=0, parse_dates=True)
            if len(df) > 1:
                recent_cut = df.index.max().normalize() - pd.Timedelta(days=14)
                bdays = pd.bdate_range(max(df.index.min(), recent_cut), df.index.max())
                missing = bdays.difference(df.index.normalize())
                if len(missing):
                    print(f"[warn] {sym} {len(missing)} recent missing business day(s): {', '.join(d.strftime('%Y-%m-%d') for d in missing[:5])}")


if __name__ == "__main__":
    main()
