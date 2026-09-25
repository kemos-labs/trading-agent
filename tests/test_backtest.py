"""Tests for quantkit.backtest (stdlib unittest — no pytest in venv).

Run from the project root:
    .venv/bin/python -m unittest discover -s tests -v
"""

from __future__ import annotations

import math
import sys
import unittest
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np
import pandas as pd

from quantkit import backtest as bt


def _close(prices, dates):
    return pd.Series(prices, index=pd.to_datetime(dates), dtype=float)


def _returns(prices, dates):
    return _close(prices, dates).pct_change()


# ---------------------------------------------------------------------------
# Tier 1 — vectorized backtest
# ---------------------------------------------------------------------------

class TestVectorizedBacktest(unittest.TestCase):
    def test_no_lookahead_shift(self):
        # Returns: +10%, -9.09% (100 -> 110 -> 100)
        r = _returns([100.0, 110.0, 100.0], ["2026-01-01", "2026-01-02", "2026-01-03"])
        # Signal flips to LONG at bar 1's close: bar 2 must earn the +10%.
        pos = _close([0.0, 1.0, 1.0], r.index)
        out = bt.vectorized_backtest(r, pos)
        self.assertEqual(out["exposure"].iloc[0], 0.0)
        self.assertEqual(out["exposure"].iloc[1], 0.0)  # decided at bar 0 -> flat bar 1
        self.assertEqual(out["exposure"].iloc[2], 1.0)  # decided at bar 1 -> long bar 2
        # Bar 2's return is -1/11 (100 <- 110); that is what the long earns.
        self.assertAlmostEqual(out["gross"].iloc[2], -1.0 / 11.0, places=9)

    def test_equity_compounding(self):
        r = _returns([100.0, 110.0, 121.0], ["2026-01-01", "2026-01-02", "2026-01-03"])
        pos = _close([1.0, 1.0, 1.0], r.index)
        out = bt.vectorized_backtest(r, pos)
        self.assertAlmostEqual(out["equity"].iloc[-1], 1.21, places=9)

    def test_proportional_costs(self):
        r = _returns([100.0, 110.0, 121.0], ["2026-01-01", "2026-01-02", "2026-01-03"])
        pos = _close([1.0, 1.0, 1.0], r.index)
        out = bt.vectorized_backtest(r, pos, ptc=0.001)
        # Entering the position (0 -> 1) at bar 0's close costs 0.1%.
        self.assertAlmostEqual(out["costs"].iloc[0], 0.001, places=10)
        # Equity = (1 - 0.001) * (1 + 0.10) * (1 + 0.10)
        self.assertAlmostEqual(out["equity"].iloc[-1], 0.999 * 1.21, places=9)

    def test_flat_cost_per_change(self):
        r = _returns([100.0, 100.0, 100.0, 100.0], ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"])
        pos = _close([1.0, 1.0, 0.0, 0.0], r.index)
        out = bt.vectorized_backtest(r, pos, ffc=0.005)
        # Two changes: entering 0 -> 1 at bar 0, exiting 1 -> 0 at bar 2.
        self.assertAlmostEqual(out["costs"].sum(), 0.01, places=10)
        self.assertAlmostEqual(out["costs"].iloc[0], 0.005, places=10)
        self.assertAlmostEqual(out["costs"].iloc[2], 0.005, places=10)

    def test_nan_target_treated_flat_with_warning(self):
        r = _returns([100.0, 110.0, 121.0], ["2026-01-01", "2026-01-02", "2026-01-03"])
        pos = _close([np.nan, 1.0, 1.0], r.index)
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            out = bt.vectorized_backtest(r, pos)
        self.assertTrue(any("NaN" in str(x.message) for x in w))
        self.assertEqual(out["exposure"].iloc[1], 0.0)  # NaN -> flat, not long

    def test_index_mismatch_raises(self):
        r = _returns([100.0, 110.0], ["2026-01-01", "2026-01-02"])
        pos = _close([1.0, 1.0], ["2026-01-02", "2026-01-03"])
        with self.assertRaises(ValueError):
            bt.vectorized_backtest(r, pos)


# ---------------------------------------------------------------------------
# Performance measurement
# ---------------------------------------------------------------------------

class TestPerformance(unittest.TestCase):
    def test_max_drawdown_known(self):
        # 10% up, 20% down, 10% up: peak 1.10, trough 0.88 -> -20%.
        r = _returns([100.0, 110.0, 88.0, 96.8], ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"])
        self.assertAlmostEqual(bt.max_drawdown(r), -0.2, places=9)

    def test_max_drawdown_never_negative(self):
        r = _returns([100.0, 110.0, 121.0], ["2026-01-01", "2026-01-02", "2026-01-03"])
        self.assertEqual(bt.max_drawdown(r), 0.0)

    def test_drawdown_duration(self):
        # Peak 1.10; bars 2 and 3 underwater (0.88, then 0.968 < 1.10).
        r = _returns([100.0, 110.0, 88.0, 96.8], ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"])
        self.assertEqual(bt.drawdown_duration(r), 2)

    def test_drawdown_duration_zero_when_never_underwater(self):
        r = _returns([100.0, 110.0, 121.0], ["2026-01-01", "2026-01-02", "2026-01-03"])
        self.assertEqual(bt.drawdown_duration(r), 0)

    def test_annualized_sharpe_known(self):
        # Annualized vol 20% -> per-day sigma = 0.2/sqrt(252); mean 0 with rf 0 -> 0.
        rng = np.random.default_rng(42)
        r = pd.Series(rng.normal(0.0, 0.2 / math.sqrt(252), 500))
        # SR estimate noise ~ sqrt(252/n): allow 3 standard errors.
        self.assertLess(abs(bt.annualized_sharpe(r)), 3 * math.sqrt(252 / len(r)))
        # Annualized vol 10%, daily mean 0.0002 -> SR ≈ 0.0002/0.1*sqrt(252) ≈ 0.0317
        r2 = pd.Series(rng.normal(0.0002, 0.1 / math.sqrt(252), 5000))
        # SR estimate noise ~ sqrt(252/n): allow 3 standard errors.
        self.assertLess(
            abs(bt.annualized_sharpe(r2) - 0.0002 / 0.1 * math.sqrt(252)),
            3 * math.sqrt(252 / len(r2)),
        )

    def test_annualized_sharpe_zero_std(self):
        r = _close([0.01, 0.01, 0.01], ["2026-01-01", "2026-01-02", "2026-01-03"])
        self.assertEqual(bt.annualized_sharpe(r), 0.0)

    def test_annualized_return(self):
        # 100 -> 121 over 2 days = 10%/day => annualized (1.21)^(252/2) - 1
        r = _returns([100.0, 110.0, 121.0], ["2026-01-01", "2026-01-02", "2026-01-03"])
        expected = 1.21 ** 126 - 1.0
        # Huge magnitudes: compare relatively.
        self.assertAlmostEqual(bt.annualized_return(r) / expected, 1.0, places=6)

    def test_mar_ratio(self):
        # Positive growth with a real drawdown: MAR = CAGR / |maxDD|.
        r = _returns(
            [100.0, 110.0, 99.0, 108.9, 119.79],
            ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05"],
        )
        dd = bt.max_drawdown(r)
        self.assertAlmostEqual(bt.mar_ratio(r), bt.annualized_return(r) / abs(dd), places=9)
        self.assertGreater(bt.mar_ratio(r), 0.0)

    def test_performance_summary_keys(self):
        r = _returns([100.0, 110.0, 88.0, 96.8], ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04"])
        s = bt.performance_summary(r)
        for key in ("total_return", "cagr", "ann_vol", "sharpe", "max_drawdown", "dd_duration", "mar"):
            self.assertIn(key, s)
        self.assertAlmostEqual(s["max_drawdown"], -0.2, places=9)


# ---------------------------------------------------------------------------
# Tier 2 — bar-by-bar engine
# ---------------------------------------------------------------------------

class TestBacktestEngine(unittest.TestCase):
    def _prices(self):
        return _close([100.0, 110.0, 99.0, 108.9, 119.79], ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05"])

    def _returns(self):
        return self._prices().pct_change()

    def test_buy_and_hold(self):
        r = self._returns()
        engine = bt.BacktestEngine(capital=1000.0)
        out = engine.run(r, strategy=lambda state: 1.0)
        # Always fully long: equity compounds with the full return series.
        self.assertAlmostEqual(out["equity"].iloc[-1], 1000.0 * 119.79 / 100.0, places=6)
        # Bar 0 is warm-up (flat); from bar 1 on, fully long.
        self.assertTrue((out["exposure"].iloc[1:] == 1.0).all())

    def test_lag_one_signal(self):
        # Go long at bar 1's close (after seeing bar 1's return): the
        # +10% of bar 1 must NOT be earned; the -10% of bar 2 IS earned.
        r = self._returns()
        engine = bt.BacktestEngine(capital=1000.0)
        out = engine.run(
            r, strategy=lambda state: 1.0 if state.bar >= 1 else 0.0
        )
        self.assertEqual(out["exposure"].iloc[0], 0.0)
        self.assertEqual(out["exposure"].iloc[1], 0.0)
        self.assertEqual(out["exposure"].iloc[2], 1.0)
        self.assertAlmostEqual(out["equity"].iloc[1], 1000.0, places=6)
        self.assertAlmostEqual(out["equity"].iloc[2], 1000.0 * 99.0 / 110.0, places=6)

    def test_proportional_cost(self):
        r = self._returns()
        engine = bt.BacktestEngine(capital=1000.0, ptc=0.001)
        out = engine.run(r, strategy=lambda state: 1.0)
        # One trade 0 -> 1 at bar 0: cost 0.1% of capital, charged in cash
        # at order time, so the remaining 999 compounds with the asset.
        self.assertEqual(len(engine.trades), 1)
        self.assertAlmostEqual(engine.trades[0]["cost"], 1.0, places=9)
        self.assertAlmostEqual(out["equity"].iloc[-1], 999.0 * 1.1979, places=6)

    def test_flat_cost_per_trade(self):
        r = self._returns()
        engine = bt.BacktestEngine(capital=1000.0, ffc=5.0)
        out = engine.run(
            r, strategy=lambda state: 1.0 if state.bar % 2 == 0 else 0.0
        )
        # Changes: 0->1 (bar 0), 1->0 (bar 1), 0->1 (bar 2), 1->0 (bar 3) = 4 trades.
        self.assertEqual(len(engine.trades), 4)
        self.assertAlmostEqual(out["cost"].sum(), 20.0, places=9)

    def test_exposure_clamped(self):
        r = self._returns()
        engine = bt.BacktestEngine(capital=1000.0, max_exposure=0.5)
        out = engine.run(r, strategy=lambda state: 2.0)
        # Bar 0 is warm-up (flat); from bar 1 on, exposure is clamped to 0.5.
        self.assertAlmostEqual(out["exposure"].max(), 0.5, places=9)
        self.assertAlmostEqual(out["exposure"].min(), 0.0, places=9)  # warm-up bar
        self.assertTrue((out["exposure"].iloc[1:] == 0.5).all())

    def test_stop_loss_halts(self):
        r = self._returns()  # 10%, -10%, +10%, +10%
        engine = bt.BacktestEngine(capital=1000.0, stop_loss=0.05)
        out = engine.run(r, strategy=lambda state: 1.0)
        self.assertTrue(engine.stopped)
        self.assertEqual(engine.stop_bar, 2)  # equity 990 <= 1000*0.95 at bar 2
        self.assertEqual(out["exposure"].iloc[3], 0.0)
        self.assertAlmostEqual(out["equity"].iloc[-1], 990.0, places=6)

    def test_state_has_realized_history_only(self):
        r = self._returns()
        seen = []
        engine = bt.BacktestEngine(capital=1000.0)

        def strat(state):
            seen.append((state.bar, len(state.returns)))
            return 0.0

        engine.run(r, strat)
        self.assertEqual(seen, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)])  # noqa: E501

    def test_prices_passed_through(self):
        r = self._returns()
        engine = bt.BacktestEngine(capital=1000.0)
        out = engine.run(r, strategy=lambda state: 1.0 if state.prices[-1] > 105 else 0.0, prices=self._prices())
        # Price > 105 first seen at bar 1's close (110) -> long from bar 2.
        # Bar 3's close (99) is <= 105, so bar 3 stays long only because the
        # decision at its close (108.9 > 105) keeps it long for bar 4.
        self.assertEqual(out["exposure"].iloc[1], 0.0)
        self.assertEqual(out["exposure"].iloc[2], 1.0)

    def test_empty_returns_raises(self):
        with self.assertRaises(ValueError):
            bt.BacktestEngine().run(pd.Series(dtype=float), lambda state: 0.0)

    def test_bad_constructor_args_raise(self):
        with self.assertRaises(ValueError):
            bt.BacktestEngine(capital=0)
        with self.assertRaises(ValueError):
            bt.BacktestEngine(ptc=-1.0)
        with self.assertRaises(ValueError):
            bt.BacktestEngine(max_exposure=0)
        with self.assertRaises(ValueError):
            bt.BacktestEngine(stop_loss=1.5)


if __name__ == "__main__":
    unittest.main()