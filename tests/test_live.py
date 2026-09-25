import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import pandas as pd

from quantkit.live import detect_gaps, load_store, store_path, update_store


def _make_frame(dates, closes=None):
    """Helper: valid OHLCV frame from date strings."""
    idx = pd.to_datetime(dates)
    n = len(idx)
    closes = closes or [100 + i for i in range(n)]
    return pd.DataFrame(
        {
            "open": closes,
            "high": [c + 1 for c in closes],
            "low": [c - 1 for c in closes],
            "close": closes,
            "volume": [1_000_000] * n,
        },
        index=idx,
    )


class TestLiveStore(unittest.TestCase):
    def test_store_path_upper(self):
        self.assertEqual(store_path("spy", "/tmp/x").name, "SPY_1d.csv")
        with self.assertRaises(ValueError):
            store_path("", "/tmp/x")

    def test_load_store_missing_returns_none(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertIsNone(load_store("SPY", d))

    def test_update_store_creates_and_appends(self):
        with tempfile.TemporaryDirectory() as d:
            def fetcher(symbol, lookback_days=10, interval="1d", auto_adjust=True):
                return _make_frame(["2024-01-02", "2024-01-03", "2024-01-04"])

            df = update_store("SPY", store_dir=d, fetcher=fetcher)
            self.assertEqual(len(df), 3)
            self.assertTrue(Path(d, "SPY_1d.csv").exists())

            # second fetch overlaps + one new bar
            def fetcher2(symbol, lookback_days=10, interval="1d", auto_adjust=True):
                return _make_frame(["2024-01-03", "2024-01-04", "2024-01-05"], [102, 103, 104])

            df2 = update_store("SPY", store_dir=d, fetcher=fetcher2)
            self.assertEqual(len(df2), 4)
            self.assertIn(pd.Timestamp("2024-01-05"), df2.index)
            # last write wins for duplicate date
            self.assertEqual(df2.loc["2024-01-05", "close"], 104)

    def test_update_store_validates_and_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            # first valid
            def good(symbol, lookback_days=10, interval="1d", auto_adjust=True):
                return _make_frame(["2024-01-02", "2024-01-03"])

            update_store("SPY", store_dir=d, fetcher=good)

            # second fetch with only invalid bars (negative prices -> <2 rows after cleaning)
            def bad(symbol, lookback_days=10, interval="1d", auto_adjust=True):
                idx = pd.to_datetime(["2024-01-04", "2024-01-05"])
                return pd.DataFrame(
                    {"open": [-1, -2], "high": [-1, -2], "low": [-2, -3], "close": [-1, -2], "volume": [100, 100]},
                    index=idx,
                )

            with self.assertRaises(ValueError):
                update_store("SPY", store_dir=d, fetcher=bad)

    def test_detect_gaps(self):
        df = _make_frame(["2024-01-02", "2024-01-03", "2024-01-05"])  # skip Jan 4 (Thu)
        gaps = detect_gaps(df)
        # Jan 4 is a business day missing
        self.assertIn(pd.Timestamp("2024-01-04"), gaps)

        # weekends not flagged (B freq)
        df2 = _make_frame(["2024-01-05", "2024-01-08"])  # Fri -> Mon, weekend skipped
        self.assertEqual(detect_gaps(df2), [])

        self.assertEqual(detect_gaps(df.iloc[:1]), [])

    def test_fetcher_exception_propagates(self):
        with tempfile.TemporaryDirectory() as d:
            def boom(symbol, lookback_days=10, interval="1d", auto_adjust=True):
                raise RuntimeError("yahoo down")

            with self.assertRaises(RuntimeError):
                update_store("SPY", store_dir=d, fetcher=boom)


if __name__ == "__main__":
    unittest.main()
