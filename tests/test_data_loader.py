"""Tests for quantkit.data_loader (stdlib unittest — no pytest in venv).

Run from the project root:
    .venv/bin/python -m unittest discover -s tests -v
"""

from __future__ import annotations

import math
import sys
import tempfile
import unittest
import unittest.mock
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import pandas as pd

from quantkit import data_loader as dl


def _close(prices, dates):
    return pd.Series(prices, index=pd.to_datetime(dates), dtype=float)


class TestNormalizeColumns(unittest.TestCase):
    def test_mixed_case_csv_headers(self):
        df = pd.DataFrame(
            {
                "Date": ["2026-01-02", "2026-01-05"],
                "Open": [100.0, 101.0],
                "High": [102.0, 103.0],
                "Low": [99.0, 100.0],
                "Close": [101.5, 102.5],
                "Volume": [1000, 2000],
            }
        )
        out = dl.normalize_columns(df)
        self.assertEqual(list(out.columns), ["open", "high", "low", "close", "volume"])
        self.assertIsInstance(out.index, pd.DatetimeIndex)

    def test_yfinance_multindex_single_ticker(self):
        idx = pd.to_datetime(["2026-01-02", "2026-01-05"])
        cols = pd.MultiIndex.from_product(
            [["Close", "High", "Low", "Open", "Volume"], ["AAPL"]]
        )
        df = pd.DataFrame(
            np.array(
                [[101.5, 102.0, 99.0, 100.0, 1000],
                 [102.5, 103.0, 100.0, 101.0, 2000]],
                dtype=float,
            ),
            index=idx,
            columns=cols,
        )
        out = dl.normalize_columns(df)
        self.assertEqual(list(out.columns), ["open", "high", "low", "close", "volume"])
        self.assertEqual(out.loc[idx[0], "close"], 101.5)

    def test_multiticker_raises(self):
        cols = pd.MultiIndex.from_tuples(
            [("Close", "AAPL"), ("Close", "MSFT"), ("Open", "AAPL"), ("Open", "MSFT")]
        )
        df = pd.DataFrame([[1.0, 2.0, 1.0, 2.0]], columns=cols)
        with self.assertRaises(ValueError):
            dl.normalize_columns(df)

    def test_missing_columns_raises(self):
        df = pd.DataFrame({"Open": [1.0], "Close": [2.0]})
        with self.assertRaises(ValueError):
            dl.normalize_columns(df)


class TestValidateOhlcv(unittest.TestCase):
    def _frame(self, **overrides):
        base = {
            "open": [100.0, 101.0, 102.0],
            "high": [102.0, 103.0, 104.0],
            "low": [99.0, 100.0, 101.0],
            "close": [101.0, 102.0, 103.0],
            "volume": [100, 200, 300],
        }
        base.update(overrides)
        return pd.DataFrame(base, index=pd.to_datetime(["2026-01-02", "2026-01-05", "2026-01-06"]))

    def test_clean_passes_through(self):
        df = self._frame()
        out = dl.validate_ohlcv(df)
        self.assertEqual(len(out), 3)

    def test_non_positive_price_dropped(self):
        df = self._frame(open=[100.0, 0.0, 102.0])
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            out = dl.validate_ohlcv(df)
        self.assertEqual(len(out), 2)
        self.assertTrue(any("non-positive" in str(x.message) for x in w))

    def test_high_below_low_dropped(self):
        df = self._frame(high=[102.0, 99.0, 104.0], low=[99.0, 100.0, 101.0])
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            out = dl.validate_ohlcv(df)
        self.assertEqual(len(out), 2)
        self.assertTrue(any("high < low" in str(x.message) for x in w))

    def test_duplicate_timestamps_dropped(self):
        df = self._frame()
        df = pd.concat([df, df.iloc[[0]]])
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            out = dl.validate_ohlcv(df)
        self.assertEqual(len(out), 3)
        self.assertTrue(any("duplicate" in str(x.message) for x in w))

    def test_too_few_rows_raises(self):
        df = self._frame().iloc[[0]]
        with self.assertRaises(ValueError):
            dl.validate_ohlcv(df)


class TestLoadCsv(unittest.TestCase):
    def test_round_trip(self):
        csv_text = (
            "Date,Open,High,Low,Close,Volume\n"
            "2026-01-02,100.0,102.0,99.0,101.5,1000\n"
            "2026-01-05,101.0,103.0,100.0,102.5,2000\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "ohlcv.csv"
            p.write_text(csv_text)
            out = dl.load_csv(p)
        self.assertEqual(list(out.columns), list(dl.OHLCV))
        self.assertEqual(len(out), 2)
        self.assertEqual(out.loc["2026-01-05", "close"], 102.5)
        self.assertTrue(out.index.is_monotonic_increasing)

    def test_missing_date_column_raises(self):
        csv_text = "Open,Close\n100.0,101.0\n"
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "no_date.csv"
            p.write_text(csv_text)
            with self.assertRaises(ValueError):
                dl.load_csv(p)


class TestAdjustPrices(unittest.TestCase):
    def test_two_for_one_split_continuity(self):
        close = _close([100.0, 100.0, 50.0, 50.0], ["2026-01-02", "2026-01-05", "2026-01-06", "2026-01-07"])
        events = pd.DataFrame({"ex_date": [pd.Timestamp("2026-01-06")], "split_ratio": [2.0], "dividend": [0.0]})
        out = dl.adjust_prices(close, events)
        np.testing.assert_allclose(out.values, [50.0, 50.0, 50.0, 50.0])

    def test_dividend_factor(self):
        # $5 dividend, prior close $100 → pre-history × 0.95
        close = _close([100.0, 100.0], ["2026-01-05", "2026-01-06"])
        events = pd.DataFrame({"ex_date": [pd.Timestamp("2026-01-06")], "split_ratio": [np.nan], "dividend": [5.0]})
        out = dl.adjust_prices(close, events)
        np.testing.assert_allclose(out.values, [95.0, 100.0])

    def test_compound_factors(self):
        # two 2:1 splits → pre-history × 1/4
        close = _close([100.0, 100.0, 50.0, 25.0], ["2026-01-02", "2026-01-05", "2026-01-06", "2026-01-07"])
        events = pd.DataFrame(
            {
                "ex_date": [pd.Timestamp("2026-01-06"), pd.Timestamp("2026-01-07")],
                "split_ratio": [2.0, 2.0],
                "dividend": [0.0, 0.0],
            }
        )
        out = dl.adjust_prices(close, events)
        np.testing.assert_allclose(out.values, [25.0, 25.0, 25.0, 25.0])

    def test_returns_invariant_across_split(self):
        # Raw return 100 → 50 is -50%; adjusted must be 0%.
        close = _close([100.0, 50.0], ["2026-01-05", "2026-01-06"])
        events = pd.DataFrame({"ex_date": [pd.Timestamp("2026-01-06")], "split_ratio": [2.0], "dividend": [0.0]})
        adj = dl.adjust_prices(close, events)
        r = dl.compute_returns(adj)
        self.assertAlmostEqual(float(r.iloc[-1]), 0.0, places=9)

    def test_no_events_returns_copy(self):
        close = _close([100.0, 101.0], ["2026-01-05", "2026-01-06"])
        out = dl.adjust_prices(close)
        pd.testing.assert_series_equal(out, close)


class TestComputeReturns(unittest.TestCase):
    def test_log_returns(self):
        close = _close([100.0, 110.0, 99.0], ["2026-01-05", "2026-01-06", "2026-01-07"])
        out = dl.compute_returns(close)
        self.assertTrue(np.isnan(out.iloc[0]))
        self.assertAlmostEqual(out.iloc[1], math.log(1.1), places=10)
        self.assertAlmostEqual(out.iloc[2], math.log(99.0 / 110.0), places=10)

    def test_simple_returns(self):
        close = _close([100.0, 110.0], ["2026-01-05", "2026-01-06"])
        out = dl.compute_returns(close, log=False)
        self.assertAlmostEqual(out.iloc[-1], 0.1, places=10)

    def test_zero_price_does_not_produce_inf(self):
        close = _close([100.0, 0.0, 100.0], ["2026-01-05", "2026-01-06", "2026-01-07"])
        out = dl.compute_returns(close)
        self.assertTrue(np.isnan(out.iloc[1]))
        self.assertTrue(np.isnan(out.iloc[2]))


class TestToBars(unittest.TestCase):
    def test_ohlcv_aggregation(self):
        idx = pd.to_datetime(
            ["2026-01-02 09:30", "2026-01-02 09:31", "2026-01-02 09:32"]
        )
        df = pd.DataFrame(
            {
                "open": [100.0, 101.0, 102.0],
                "high": [101.0, 102.0, 103.0],
                "low": [99.0, 100.0, 101.0],
                "close": [100.5, 101.5, 102.5],
                "volume": [100, 200, 300],
            },
            index=idx,
        )
        out = dl.to_bars(df, "1D")
        self.assertEqual(len(out), 1)
        bar = out.iloc[0]
        self.assertEqual(bar["open"], 100.0)
        self.assertEqual(bar["high"], 103.0)
        self.assertEqual(bar["low"], 99.0)
        self.assertEqual(bar["close"], 102.5)
        self.assertEqual(bar["volume"], 600)


class TestFlagOutliers(unittest.TestCase):
    def test_spike_flagged(self):
        r = _close([0.01] * 20 + [0.5], [f"2026-01-{d:02d}" for d in range(1, 22)])
        out = dl.flag_outliers(r, z=4.0)
        self.assertFalse(out.iloc[:-1].any())
        self.assertTrue(out.iloc[-1])

    def test_nan_never_flagged(self):
        r = _close([np.nan, 0.01, 0.02], ["2026-01-01", "2026-01-02", "2026-01-03"])
        out = dl.flag_outliers(r)
        self.assertFalse(out.iloc[0])
        self.assertFalse(out.any())

    def test_rolling_window(self):
        idx = pd.date_range("2026-01-01", periods=50)
        r = pd.Series([0.01] * 50, index=idx)
        out = dl.flag_outliers(r, window=10)
        self.assertFalse(out.any())


class TestLoadYfinance(unittest.TestCase):
    def test_fail_closed_on_empty(self):
        empty = pd.DataFrame()
        with unittest.mock.patch("yfinance.download", return_value=empty):
            with self.assertRaises(RuntimeError):
                dl.load_yfinance("XXXX")

    def test_fail_closed_when_import_missing(self):
        with unittest.mock.patch.dict(sys.modules, {"yfinance": None}):
            with self.assertRaises(RuntimeError):
                dl.load_yfinance("XXXX")

    def test_live_download(self):
        """Real network check; skipped when the sandbox is offline."""
        try:
            df = dl.load_yfinance("AAPL", start="2026-06-01", end="2026-07-01")
        except RuntimeError as exc:
            self.skipTest(f"offline or feed error: {exc}")
        self.assertEqual(list(df.columns), list(dl.OHLCV))
        self.assertGreater(len(df), 20)
        self.assertTrue((df["high"] >= df["low"]).all())


if __name__ == "__main__":
    unittest.main()
