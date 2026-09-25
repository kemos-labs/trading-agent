import unittest
import math
import numpy as np
import pandas as pd
from quantkit.portfolio import hrp_weights, risk_parity_weights, max_sharpe_weights, min_variance_weights, equal_weight

class TestPortfolio(unittest.TestCase):
    def setUp(self):
        # 3 assets cov
        self.cov=pd.DataFrame([[0.04,0.01,0.005],[0.01,0.09,0.02],[0.005,0.02,0.16]], index=["A","B","C"], columns=["A","B","C"])
        self.expected=pd.Series([0.08,0.12,0.05], index=["A","B","C"])
    def test_equal(self):
        w=equal_weight(3)
        self.assertAlmostEqual(w.sum(),1)
    def test_hrp(self):
        w=hrp_weights(self.cov)
        self.assertAlmostEqual(w.sum(),1, places=6)
        self.assertTrue((w>=0).all())
        self.assertEqual(list(w.index), ["A","B","C"])
    def test_risk_parity(self):
        w=risk_parity_weights(self.cov)
        self.assertAlmostEqual(w.sum(),1, places=6)
        self.assertTrue((w>0).all())
    def test_max_sharpe(self):
        w=max_sharpe_weights(self.expected, self.cov)
        self.assertAlmostEqual(w.sum(),1, places=6)
        self.assertTrue((w>=0).all())
    def test_min_var(self):
        w=min_variance_weights(self.cov)
        self.assertAlmostEqual(w.sum(),1, places=6)
        self.assertTrue((w>=0).all())

if __name__=="__main__":
    unittest.main()

class TestEstimationDiscipline(unittest.TestCase):
    def test_flam_diagonal(self):
        from quantkit.portfolio import fundamental_law_ir
        # IR = sqrt(.02^2/.04 + .03^2/.09) = sqrt(.02) = IC*sqrt(N), IC=.1
        ir = fundamental_law_ir(np.array([0.02, 0.03]), np.diag([0.04, 0.09]))
        self.assertAlmostEqual(ir, math.sqrt(0.02), places=12)
        self.assertAlmostEqual(ir, 0.1 * math.sqrt(2), places=12)
    def test_tc_unconstrained_is_one(self):
        from quantkit.portfolio import transfer_coefficient
        S = np.diag([0.04, 0.09]); a = np.array([0.02, 0.03])
        wstar = np.linalg.solve(S, a)
        self.assertAlmostEqual(transfer_coefficient(a, wstar, S), 1.0, places=12)
        # constrained (long-only clip of a short leg) must lose transfer
        wcon = np.array([0.25, 0.0])
        self.assertLess(transfer_coefficient(a, wcon, S), 1.0)
    def test_lw_bounds_and_pd(self):
        from quantkit.portfolio import ledoit_wolf_shrinkage
        rng = np.random.default_rng(3)
        R = pd.DataFrame(rng.normal(0, 0.01, (10, 8)))  # N > T: sample cov singular
        Ss, delta = ledoit_wolf_shrinkage(R)
        self.assertGreaterEqual(delta, 0.0); self.assertLessEqual(delta, 1.0)
        self.assertGreater(np.linalg.eigvalsh(Ss.values).min(), 0.0)
    def test_bs_shrinkage_direction(self):
        from quantkit.portfolio import bayes_stein_means
        rng = np.random.default_rng(5)
        R = pd.DataFrame(rng.normal([0.01, 0.05, -0.02], 0.05, (60, 3)))
        mu = bayes_stein_means(R)
        ybar = R.mean()
        # shrunk means lie between sample means and grand mean
        y0 = ybar.mean()
        for c in R.columns:
            lo, hi = (ybar[c], y0) if ybar[c] <= y0 else (y0, ybar[c])
            self.assertGreaterEqual(mu[c], min(lo, hi) - 1e-12)
            self.assertLessEqual(mu[c], max(lo, hi) + 1e-12)
    def test_combine_1n(self):
        from quantkit.portfolio import combine_with_1n
        w = pd.Series([0.5, 0.3, 0.2])
        pd.testing.assert_series_equal(combine_with_1n(w, 0.0),
            pd.Series([1/3]*3).rename("combined_1n"), check_names=False)
        pd.testing.assert_series_equal(combine_with_1n(w, 1.0), w.rename("combined_1n"),
            check_names=False, check_freq=False)
        with self.assertRaises(ValueError):
            combine_with_1n(w, 1.5)
