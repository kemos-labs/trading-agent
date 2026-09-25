"""Tests for quantkit.sizing (stdlib unittest — no pytest in venv).

Run from the project root:
    .venv/bin/python -m unittest discover -s tests -v
"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import pandas as pd

from quantkit import sizing as sz


class TestKelly(unittest.TestCase):
    def test_continuous_kelly_known(self):
        # mean 0.02, var 0.0001 (ddof=1) -> f* = m/var = 200
        r = pd.Series([0.01, 0.02, 0.03])
        self.assertAlmostEqual(sz.kelly_fraction(r), 200.0, places=6)

    def test_fractional_kelly(self):
        r = pd.Series([0.01, 0.02, 0.03])
        self.assertAlmostEqual(sz.kelly_fraction(r, fraction=0.5), 100.0, places=6)

    def test_zero_variance_returns_zero(self):
        self.assertEqual(sz.kelly_fraction(pd.Series([0.01, 0.01, 0.01])), 0.0)

    def test_negative_mean_returns_negative(self):
        r = pd.Series([-0.01, -0.02, -0.03])  # mean -0.02, var 0.0001
        self.assertAlmostEqual(sz.kelly_fraction(r), -200.0, places=6)

    def test_too_few_observations(self):
        self.assertEqual(sz.kelly_fraction(pd.Series([0.01])), 0.0)

    def test_discrete_kelly_known(self):
        # p=0.6, b=1 -> f = p - q/b = 0.6 - 0.4 = 0.2
        self.assertAlmostEqual(sz.discrete_kelly(0.6, 1.0), 0.2, places=10)
        # fair coin with double-your-money odds has no edge
        self.assertAlmostEqual(sz.discrete_kelly(0.5, 1.0), 0.0, places=10)

    def test_discrete_kelly_negative_is_a_loss(self):
        # p=0.4, b=0.5 -> f = 0.4 - 0.6/0.5 = -0.8 (no bet)
        self.assertAlmostEqual(sz.discrete_kelly(0.4, 0.5), -0.8, places=10)

    def test_discrete_kelly_validates(self):
        with self.assertRaises(ValueError):
            sz.discrete_kelly(0.0, 1.0)
        with self.assertRaises(ValueError):
            sz.discrete_kelly(0.5, 0.0)


class TestVolTargetWeight(unittest.TestCase):
    def test_weight_matches_rolling_vol(self):
        # Alternating +/-1%: rolling std ~= 0.01*sqrt(60/59); weight = target/annvol.
        idx = pd.date_range("2026-01-01", periods=100)
        r = pd.Series([0.01 if i % 2 == 0 else -0.01 for i in range(100)], index=idx)
        w = sz.vol_target_weight(r, 0.10)
        window = r.iloc[-60:]
        expected = 0.10 / (window.std(ddof=1) * math.sqrt(252))
        self.assertAlmostEqual(w.iloc[-1], expected, places=8)
        # Sanity: ~0.625 for +/-1% daily vol and a 10% target
        self.assertAlmostEqual(w.iloc[-1], 0.625, places=1)

    def test_warmup_is_zero(self):
        idx = pd.date_range("2026-01-01", periods=100)
        r = pd.Series(0.01, index=idx)
        w = sz.vol_target_weight(r, 0.10, lookback=60)
        self.assertTrue((w.iloc[:59] == 0.0).all())
        self.assertFalse((w.iloc[59:] == 0.0).all())

    def test_leverage_cap(self):
        idx = pd.date_range("2026-01-01", periods=70)
        r = pd.Series(0.001, index=idx)  # tiny vol -> huge weight, must clip
        w = sz.vol_target_weight(r, 0.20, lookback=60, max_weight=3.0)
        self.assertLessEqual(w.max(), 3.0)

    def test_nan_returns_give_zero_weight(self):
        idx = pd.date_range("2026-01-01", periods=70)
        vals = [0.01] * 35 + [np.nan] * 35
        w = sz.vol_target_weight(pd.Series(vals, index=idx), 0.10, lookback=30)
        self.assertTrue((w.iloc[35:] == 0.0).all())


class TestCarverPipeline(unittest.TestCase):
    def test_cash_vol_target(self):
        # Simple test case from the skill: $1M capital, 20% target -> daily $12,500.
        self.assertAlmostEqual(sz.cash_vol_target(1_000_000, 0.20), 12500.0, places=6)

    def test_cash_vol_target_252_convention(self):
        self.assertAlmostEqual(
            sz.cash_vol_target(1_000_000, 0.20, periods=252),
            1_000_000 * 0.20 / math.sqrt(252),
            places=6,
        )

    def test_instrument_value_volatility(self):
        # 2% daily price vol on a $100 block -> $2/day/block.
        self.assertAlmostEqual(sz.instrument_value_volatility(0.02, 100.0), 2.0, places=10)

    def test_instrument_value_volatility_fx(self):
        self.assertAlmostEqual(
            sz.instrument_value_volatility(0.02, 100.0, fx=1.2), 2.4, places=10
        )

    def test_volatility_scalar(self):
        self.assertAlmostEqual(sz.volatility_scalar(12500.0, 2.0), 6250.0, places=10)

    def test_subsystem_position(self):
        scalar = 6250.0
        self.assertAlmostEqual(sz.subsystem_position(scalar, 10.0), 6250.0, places=10)
        self.assertAlmostEqual(sz.subsystem_position(scalar, 15.0), 9375.0, places=10)
        # Forecast beyond the cap clips at +-20 -> 2x the +10 position.
        self.assertAlmostEqual(sz.subsystem_position(scalar, 25.0), 12500.0, places=10)
        self.assertAlmostEqual(sz.subsystem_position(scalar, -30.0), -12500.0, places=10)

    def test_carver_position_end_to_end(self):
        # $1M, 20% target, 2% vol, $100 block, forecast +10 -> 6,250 blocks.
        pos = sz.carver_position(1_000_000, 0.20, 0.02, 100.0, 10.0)
        self.assertAlmostEqual(pos, 6250.0, places=6)

    def test_carver_position_scales_with_inputs(self):
        base = sz.carver_position(1_000_000, 0.20, 0.02, 100.0, 10.0)
        double_target = sz.carver_position(1_000_000, 0.40, 0.02, 100.0, 10.0)
        half_vol = sz.carver_position(1_000_000, 0.20, 0.01, 100.0, 10.0)
        self.assertAlmostEqual(double_target, 2 * base, places=6)
        self.assertAlmostEqual(half_vol, 2 * base, places=6)

    def test_round_blocks_only_at_the_end(self):
        # 1% target on $1M -> budget $6,250; 3% vol -> scalar 2083.333... blocks.
        pos = sz.carver_position(1_000_000, 0.10, 0.03, 100.0, 10.0)
        self.assertAlmostEqual(pos, 6250.0 / 3.0, places=6)
        self.assertEqual(sz.carver_position(1_000_000, 0.10, 0.03, 100.0, 10.0, round_blocks=True), 2083)

    def test_low_vol_instrument_raises(self):
        # Zero instrument vol -> infinite leverage -> fail closed.
        with self.assertRaises(ValueError):
            sz.volatility_scalar(12500.0, 0.0)


if __name__ == "__main__":
    unittest.main()