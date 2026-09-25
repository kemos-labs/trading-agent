"""Paper demo — offline replay of Phase 3 PASS legs.

Run as: PYTHONPATH=src .venv/bin/python notebooks/paper_demo.py
Or open as notebook: jupyter notebook notebooks/paper_demo.ipynb
"""
import pandas as pd
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"src"))
from quantkit.live import load_store
from quantkit.paper import PaperTrader

# Offline seed already done by research/paper_trade.py --offline, but demo can also load directly
store_dir = Path("data/live")
if not (store_dir/"SPY_1d.csv").exists():
    print("No live store yet. Run: PYTHONPATH=src .venv/bin/python research/paper_trade.py --offline")
else:
    for sym in ("SPY","QQQ","TLT"):
        df = load_store(sym, store_dir)
        print(sym, len(df), df.index.min().date(), df.index.max().date(), f"close={df['close'].iloc[-1]:.2f}")

    tr = PaperTrader(symbols=("SPY","QQQ","TLT"), strategies=("dual_sma_9_45","vol_mom_252_60_10pct"), store_dir=store_dir, state_path="data/paper/demo_state.json", journal_path="data/paper/demo_journal.csv")
    out = tr.step(dry_run=True)
    print("\nPaper step (dry_run):")
    print(out.to_string(index=False) if not out.empty else "(no new bar)")
