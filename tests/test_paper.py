import tempfile
import unittest
from pathlib import Path

import pandas as pd

from quantkit.paper import PaperTrader, PaperState, STRATEGY_MAP


def _write_store(symbol, dates, closes, store_dir):
    idx = pd.to_datetime(dates)
    df = pd.DataFrame(
        {
            "open": closes,
            "high": [c+1 for c in closes],
            "low": [c-1 for c in closes],
            "close": closes,
            "volume": [1_000_000]*len(closes),
        },
        index=idx,
    )
    df.index.name = "date"
    p = Path(store_dir) / f"{symbol}_1d.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(p)
    return df


class TestPaperState(unittest.TestCase):
    def test_roundtrip(self):
        ps = PaperState(capital=100, ptc=0.001, positions={}, equity=100, peak=100)
        j = ps.to_json()
        self.assertEqual(PaperState.from_json(j).capital, 100)


class TestPaperTrader(unittest.TestCase):
    def test_unknown_strategy_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                PaperTrader(symbols=("SPY",), strategies=("nope",), store_dir=d, state_path=Path(d)/"state.json", journal_path=Path(d)/"j.csv")

    def test_missing_store_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            tr = PaperTrader(symbols=("SPY",), strategies=("dual_sma_9_45",), store_dir=d, state_path=Path(d)/"state.json", journal_path=Path(d)/"j.csv", capital=1000)
            with self.assertRaises(RuntimeError):
                tr.step()

    def test_step_computes_target_and_cost_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d) / "live"
            # enough bars for SMA 9/45 warmup + signal: 50 bars upward trend -> SMA fast > slow
            dates = pd.bdate_range("2024-01-01", periods=50).strftime("%Y-%m-%d").tolist()
            closes = [100 + i*0.5 for i in range(50)]
            _write_store("SPY", dates, closes, store)
            tr = PaperTrader(symbols=("SPY",), strategies=("dual_sma_9_45",), store_dir=store, state_path=Path(d)/"state.json", journal_path=Path(d)/"j.csv", capital=10000, ptc=0.001)
            out = tr.step(dry_run=False)
            self.assertEqual(len(out), 1)
            self.assertEqual(out.iloc[0]["target"], 1.0)
            self.assertGreater(out.iloc[0]["cost"], 0)  # entry cost
            self.assertIn("paper_only", out.iloc[0]["note"])
            # equity reduced by cost per leg
            self.assertAlmostEqual(tr.equity(), 10000 - out.iloc[0]["cost"], places=6)
            # second step same bar -> no new rows
            out2 = tr.step(dry_run=False)
            self.assertEqual(len(out2), 0)
            # journal has exactly one data row + header
            lines = Path(d, "j.csv").read_text().strip().splitlines()
            self.assertEqual(len(lines), 2)  # header + 1

    def test_dry_run_does_not_persist_state(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d) / "live"
            dates = pd.bdate_range("2024-01-01", periods=50).strftime("%Y-%m-%d").tolist()
            closes = [100 + i*0.5 for i in range(50)]
            _write_store("SPY", dates, closes, store)
            state_path = Path(d)/"state.json"
            j_path = Path(d)/"j.csv"
            tr = PaperTrader(symbols=("SPY",), strategies=("dual_sma_9_45",), store_dir=store, state_path=state_path, journal_path=j_path, capital=10000)
            tr.step(dry_run=True)
            # state file should not exist after dry_run (no persist)
            self.assertFalse(state_path.exists())
            # second dry_run still produces a row (not deduped via state)
            tr2 = PaperTrader(symbols=("SPY",), strategies=("dual_sma_9_45",), store_dir=store, state_path=state_path, journal_path=j_path, capital=10000)
            out2 = tr2.step(dry_run=True)
            self.assertEqual(len(out2), 1)

    def test_vol_mom_generates_scaled_target(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d)/"live"
            # need 252 + 60 bars for vol_mom to generate non-zero weight; create 300 bars uptrend
            dates = pd.bdate_range("2022-01-01", periods=300).strftime("%Y-%m-%d").tolist()
            # steady uptrend with some noise
            closes = [100 + i*0.2 + (i%5)*0.1 for i in range(300)]
            _write_store("QQQ", dates, closes, store)
            tr = PaperTrader(symbols=("QQQ",), strategies=("vol_mom_252_60_10pct",), store_dir=store, state_path=Path(d)/"state.json", journal_path=Path(d)/"j.csv", capital=10000)
            out = tr.step()
            self.assertEqual(len(out), 1)
            target = float(out.iloc[0]["target"])
            # vol-targeted long should be 0 < target <= 1.5
            self.assertGreater(target, 0)
            self.assertLessEqual(target, 1.5)

    def test_paper_only_note(self):
        with tempfile.TemporaryDirectory() as d:
            store = Path(d)/"live"
            dates = pd.bdate_range("2024-01-01", periods=50).strftime("%Y-%m-%d").tolist()
            closes = [100 + i for i in range(50)]
            _write_store("SPY", dates, closes, store)
            tr = PaperTrader(symbols=("SPY",), strategies=("dual_sma_9_45",), store_dir=store, state_path=Path(d)/"state.json", journal_path=Path(d)/"j.csv")
            out = tr.step()
            self.assertIn("paper_only", out.iloc[0]["note"])
            self.assertIn("execution next bar", out.iloc[0]["note"])


if __name__ == "__main__":
    unittest.main()
