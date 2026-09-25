"""Tests for quantkit.xsec — Phase 8 T1 µ-models lab."""

import unittest

import numpy as np
import pandas as pd

from quantkit.xsec import (
    formation_returns,
    overlapping_weights,
    quantile_assign,
    residual_score,
    wml_weights,
)


def _panel():
    idx = pd.date_range("2020-01-31", periods=20, freq="ME")
    # A: steady +2%/mo, B: flat, C: steady -2%/mo, D: flat with a late spike
    a = 100 * 1.02 ** np.arange(20)
    b = np.full(20, 50.0)
    c = 100 * 0.98 ** np.arange(20)
    d = np.full(20, 30.0)
    d[-2] = 60.0
    d[-1] = 60.0  # +100% realized at second-to-last bar: seen by 12-1, not 12-2
    return pd.DataFrame({"A": a, "B": b, "C": c, "D": d}, index=idx)


class TestFormation(unittest.TestCase):
    def test_hand_value(self):
        p = _panel()
        f = formation_returns(p, 12, 2)
        t = p.index[-1]
        # log(P[t-2]/P[t-12]) for A: 10 months of log(1.02)
        self.assertAlmostEqual(f.loc[t, "A"], 10 * np.log(1.02), places=10)
        self.assertAlmostEqual(f.loc[t, "C"], 10 * np.log(0.98), places=10)
        self.assertAlmostEqual(f.loc[t, "B"], 0.0, places=10)

    def test_skip_month_excludes_recent_spike(self):
        p = _panel()
        f = formation_returns(p, 12, 2)
        # D's +100% happens in the last month (t-1..t); 12-2 must ignore it
        self.assertAlmostEqual(f.loc[p.index[-1], "D"], 0.0, places=10)
        # but a 12-1 window would see it
        f1 = formation_returns(p, 12, 1)
        self.assertGreater(f1.loc[p.index[-1], "D"], 0.5)

    def test_novymarx_split_identity(self):
        p = _panel()
        f12_2 = formation_returns(p, 12, 2)
        f12_7 = formation_returns(p, 12, 7)
        f7_2 = formation_returns(p, 7, 2)
        pd.testing.assert_frame_equal(f12_2, f12_7 + f7_2)

    def test_warmup_nan_and_bad_lags(self):
        p = _panel()
        f = formation_returns(p, 12, 2)
        self.assertTrue(f.iloc[:12].isna().all(axis=None))
        with self.assertRaises(ValueError):
            formation_returns(p, 2, 12)
        with self.assertRaises(ValueError):
            formation_returns(p, 12, 0)
        with self.assertRaises(ValueError):
            formation_returns(pd.DataFrame())


class TestSorts(unittest.TestCase):
    def test_quantile_monotone(self):
        p = _panel()
        f = formation_returns(p, 12, 2).iloc[[-1]]
        q = quantile_assign(f, n=4)
        self.assertEqual(q.iloc[0]["A"], 4)  # winner top bin
        self.assertEqual(q.iloc[0]["C"], 1)  # loser bottom bin

    def test_wml_dollar_neutral(self):
        p = _panel()
        f = formation_returns(p, 12, 2)
        w = wml_weights(f, top=0.25, bottom=0.25)
        row = w.loc[p.index[-1]]
        self.assertAlmostEqual(row.sum(), 0.0, places=12)
        self.assertGreater(row["A"], 0)
        self.assertLess(row["C"], 0)
        self.assertAlmostEqual(abs(row).sum(), 1.0, places=12)

    def test_wml_within_group_neutral(self):
        idx = pd.date_range("2020-01-31", periods=3, freq="ME")
        cols = [f"S{i}" for i in range(10)]
        vals = np.array([[0.5, 0.4, 0.3, 0.2, 0.1, -0.1, -0.2, -0.3, -0.4, -0.5]] * 3)
        scores = pd.DataFrame(vals, index=idx, columns=cols)
        groups = pd.Series(["g1"] * 5 + ["g2"] * 5, index=cols)
        w = wml_weights(scores, top=0.2, bottom=0.2, groups=groups)
        row = w.iloc[-1]
        self.assertAlmostEqual(row.sum(), 0.0, places=12)
        self.assertAlmostEqual(row[cols[:5]].sum(), 0.0, places=12)
        self.assertAlmostEqual(row[cols[5:]].sum(), 0.0, places=12)
        self.assertGreater(row["S0"], 0)   # g1 winner
        self.assertLess(row["S4"], 0)      # g1 loser
        self.assertGreater(row["S5"], 0)   # g2 winner (best of weak group)
        self.assertLess(row["S9"], 0)      # g2 loser

    def test_overlapping(self):
        p = _panel()
        f = formation_returns(p, 12, 2)
        w = wml_weights(f)
        o = overlapping_weights(w, holding=3)
        # decided-at-close: cohort t executes from t+1
        self.assertTrue(o.iloc[:13].eq(0).all(axis=None))
        # equals mean of last 3 decided cohorts
        t = p.index[-1]
        expect = (w.shift(1).loc[t] + w.shift(2).loc[t] + w.shift(3).loc[t]) / 3
        pd.testing.assert_series_equal(
            o.loc[t], expect, check_names=False, check_freq=False
        )

    def test_pit_invariance(self):
        p = _panel()
        f = formation_returns(p, 12, 2)
        w = wml_weights(f)
        # appending a future bar must not change past weights
        p2 = pd.concat([p, p.iloc[[-1]] + 1.0])
        p2.index = pd.date_range(p.index[0], periods=len(p2), freq="ME")
        w2 = wml_weights(formation_returns(p2, 12, 2))
        pd.testing.assert_frame_equal(w, w2.loc[p.index])


class TestResidual(unittest.TestCase):
    def test_identity(self):
        idx = pd.date_range("2020-01-31", periods=6, freq="ME")
        r = pd.DataFrame(np.random.default_rng(0).normal(0, 0.05, (6, 4)), index=idx)
        mu = pd.DataFrame(np.random.default_rng(1).normal(0, 0.01, (6, 4)), index=idx)
        cf = pd.DataFrame(np.random.default_rng(2).normal(0, 0.01, (6, 4)), index=idx)
        pd.testing.assert_frame_equal(residual_score(r, mu, cf), r - mu - cf)


if __name__ == "__main__":
    unittest.main()
