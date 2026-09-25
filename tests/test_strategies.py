"""Tests for leakage-safe Phase 3 strategy targets."""

import unittest

import numpy as np
import pandas as pd
from pandas.testing import assert_series_equal

from quantkit.strategies import (
    donchian_breakout_position,
    dual_sma_position,
    vol_targeted_momentum_position,
)


class TestDualSmaPosition(unittest.TestCase):
    def test_warmup_and_long_signal(self):
        close = pd.Series([1.0, 2.0, 3.0, 4.0])
        result = dual_sma_position(close, fast=1, slow=3)
        assert_series_equal(
            result,
            pd.Series([0.0, 0.0, 1.0, 1.0], name="position"),
        )

    def test_long_short_mode(self):
        close = pd.Series([4.0, 3.0, 2.0, 1.0])
        result = dual_sma_position(close, fast=1, slow=3, long_only=False)
        self.assertEqual(result.tolist(), [0.0, 0.0, -1.0, -1.0])

    def test_bad_windows_rejected(self):
        with self.assertRaises(ValueError):
            dual_sma_position(pd.Series([1.0, 2.0]), fast=3, slow=3)


class TestDonchianBreakoutPosition(unittest.TestCase):
    def test_prior_channel_entry_and_exit(self):
        close = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        result = donchian_breakout_position(
            close, entry_window=3, exit_window=2
        )
        self.assertEqual(result.tolist(), [0.0, 0.0, 0.0, 1.0, 1.0, 0.0])

    def test_current_bar_does_not_define_its_own_channel(self):
        close = pd.Series([1.0, 2.0, 3.0, 10.0])
        result = donchian_breakout_position(
            close, entry_window=3, exit_window=2
        )
        self.assertEqual(result.iloc[-1], 1.0)

    def test_bad_windows_rejected(self):
        with self.assertRaises(ValueError):
            donchian_breakout_position(
                pd.Series([1.0, 2.0]), entry_window=10, exit_window=10
            )


class TestVolTargetedMomentumPosition(unittest.TestCase):
    def test_positive_momentum_is_scaled_and_capped(self):
        close = pd.Series(np.linspace(100.0, 120.0, 20))
        returns = close.pct_change()
        result = vol_targeted_momentum_position(
            close,
            returns,
            momentum_lookback=3,
            vol_lookback=3,
            target_vol=0.10,
            max_weight=0.5,
        )
        self.assertTrue((result >= 0.0).all())
        self.assertLessEqual(result.max(), 0.5)
        self.assertTrue((result.iloc[3:] > 0.0).all())

    def test_misaligned_returns_rejected(self):
        close = pd.Series([1.0, 2.0, 3.0])
        returns = pd.Series([0.0, 0.1], index=[0, 1])
        with self.assertRaises(ValueError):
            vol_targeted_momentum_position(close, returns)


class TestPointInTimeInvariance(unittest.TestCase):
    def test_future_price_changes_do_not_change_past_targets(self):
        idx = pd.date_range("2020-01-01", periods=100)
        original = pd.Series(
            100.0 + np.arange(100) + 2.0 * np.sin(np.arange(100)), index=idx
        )
        altered = original.copy()
        altered.iloc[71:] = altered.iloc[71:] * 10.0
        cutoff = idx[70]

        pairs = [
            (
                dual_sma_position(original, fast=5, slow=20),
                dual_sma_position(altered, fast=5, slow=20),
            ),
            (
                donchian_breakout_position(
                    original, entry_window=20, exit_window=10
                ),
                donchian_breakout_position(
                    altered, entry_window=20, exit_window=10
                ),
            ),
            (
                vol_targeted_momentum_position(
                    original,
                    original.pct_change(),
                    momentum_lookback=20,
                    vol_lookback=10,
                ),
                vol_targeted_momentum_position(
                    altered,
                    altered.pct_change(),
                    momentum_lookback=20,
                    vol_lookback=10,
                ),
            ),
        ]
        for left, right in pairs:
            assert_series_equal(left.loc[:cutoff], right.loc[:cutoff])


class TestInputValidation(unittest.TestCase):
    def test_nonpositive_price_rejected(self):
        with self.assertRaises(ValueError):
            dual_sma_position(pd.Series([1.0, 0.0, 2.0]))

    def test_duplicate_index_rejected(self):
        with self.assertRaises(ValueError):
            donchian_breakout_position(
                pd.Series([1.0, 2.0], index=[0, 0]),
                entry_window=2,
                exit_window=1,
            )


if __name__ == "__main__":
    unittest.main()
