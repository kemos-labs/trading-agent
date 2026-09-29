import unittest
import numpy as np
import pandas as pd
from quantkit.factors import winsorize, zscore, neutralize, information_coefficient, quantile_spread

class TestWinsorize(unittest.TestCase):
    def test_clip(self):
        s=pd.Series([1,2,3,100], index=list("abcd"))
        w=winsorize(s, limits=(0.25,0.75))
        # clipped at 25% and 75% quantiles
        self.assertLessEqual(w.max(), s.quantile(0.75))
        self.assertGreaterEqual(w.min(), s.quantile(0.25))

class TestZscore(unittest.TestCase):
    def test_zero_std(self):
        s=pd.Series([5,5,5])
        z=zscore(s)
        self.assertTrue((z==0).all())
    def test_standard(self):
        s=pd.Series([1,2,3])
        z=zscore(s)
        self.assertAlmostEqual(z.mean(), 0, places=6)
        self.assertAlmostEqual(z.std(ddof=1), 1, places=6)

class TestNeutralize(unittest.TestCase):
    def test_residual(self):
        factor=pd.Series([1,2,3,4], index=[0,1,2,3])
        exposures=pd.Series([1,1,1,1], index=[0,1,2,3])  # constant exposure -> residual should be demeaned
        resid=neutralize(factor, exposures)
        # residual sum should be 0 if exposures includes constant? Actually X=1, beta=mean, resid = factor - mean
        self.assertAlmostEqual(resid.mean(), 0, places=6)

class TestIC(unittest.TestCase):
    def test_perfect_ic(self):
        # 3 periods, 5 assets each, factor perfectly predicts fwd_return
        periods=pd.date_range("2024-01-01", periods=3, freq="B")
        assets=[f"A{i}" for i in range(5)]
        idx=pd.MultiIndex.from_product([periods, assets], names=["period","asset"])
        # factor = forward return (perfect)
        fwd=pd.Series(np.tile([1,2,3,4,5],3), index=idx)
        factor=fwd.copy()
        res=information_coefficient(factor, fwd)
        self.assertEqual(res["n_periods"],3)
        self.assertAlmostEqual(res["mean"],1.0, places=6)
        self.assertEqual(res["hit_rate"],1.0)
        # t_stat is inf when std=0 for perfect IC, or 0 if we return 0 — just check hit_rate/mean
        self.assertTrue(res["t_stat"]==0.0 or res["t_stat"]>10)
    def test_no_signal(self):
        rng = np.random.default_rng(42)  # seeded: 5-asset IC is high-variance
        periods=pd.date_range("2024-01-01", periods=4, freq="B")
        assets=[f"A{i}" for i in range(5)]
        idx=pd.MultiIndex.from_product([periods, assets], names=["period","asset"])
        factor=pd.Series(rng.standard_normal(len(idx)), index=idx)
        fwd=pd.Series(rng.standard_normal(len(idx)), index=idx)
        res=information_coefficient(factor, fwd)
        self.assertEqual(res["n_periods"],4)
        # mean IC near 0, t-stat small
        self.assertLess(abs(res["mean"]), 0.5)

class TestQuantileSpread(unittest.TestCase):
    def test_monotonic(self):
        periods=pd.date_range("2024-01-01", periods=10, freq="B")
        assets=[f"A{i}" for i in range(10)]
        idx=pd.MultiIndex.from_product([periods, assets], names=["period","asset"])
        # factor rank predicts fwd return monotonically
        # Create factor = 0..9 per period, fwd = factor *0.01 + noise
        factor_vals=[]
        fwd_vals=[]
        for p in periods:
            for a_i in range(10):
                factor_vals.append(a_i)
                fwd_vals.append(a_i*0.01 + np.random.randn()*0.001)
        factor=pd.Series(factor_vals, index=idx)
        fwd=pd.Series(fwd_vals, index=idx)
        qs=quantile_spread(factor, fwd, n_quantiles=5)
        self.assertEqual(len(qs),5)
        # mean fwd should be monotonic increasing with quantile
        means=qs["mean_fwd_return"].values
        self.assertTrue(all(means[i] <= means[i+1] for i in range(len(means)-1)))

if __name__=="__main__":
    unittest.main()

class TestPureFactorReturns(unittest.TestCase):
    def _case(self):
        idx = ["a", "b", "c", "d"]
        rets = pd.Series([0.10, 0.06, 0.04, 0.00], index=idx)
        ind = pd.Series(["tech", "tech", "bank", "bank"], index=idx)
        cty = pd.Series(["us", "eu", "us", "eu"], index=idx)
        return rets, ind, cty
    def test_hand_values_ew(self):
        from quantkit.factors import pure_factor_returns
        rets, ind, cty = self._case()
        out = pure_factor_returns(rets, ind, cty)
        self.assertAlmostEqual(out["alpha"], 0.05, places=12)  # EW market
        self.assertAlmostEqual(out["industry"]["tech"], 0.03, places=10)
        self.assertAlmostEqual(out["industry"]["bank"], -0.03, places=10)
        self.assertAlmostEqual(out["country"]["us"], 0.02, places=10)
        self.assertAlmostEqual(out["country"]["eu"], -0.02, places=10)
    def test_constraints_and_reconstruction(self):
        from quantkit.factors import pure_factor_returns
        rng = np.random.default_rng(7)
        n = 60
        rets = pd.Series(rng.normal(0.01, 0.05, n))
        ind = pd.Series(rng.choice(["i1", "i2", "i3"], n))
        cty = pd.Series(rng.choice(["c1", "c2"], n))
        w = pd.Series(rng.uniform(1, 10, n))
        out = pure_factor_returns(rets, ind, cty, w)
        W = pd.Series(w.values, index=ind.values).groupby(level=0).sum()
        V = pd.Series(w.values, index=cty.values).groupby(level=0).sum()
        self.assertAlmostEqual(float((W * out["industry"]).sum()), 0.0, places=10)
        self.assertAlmostEqual(float((V * out["country"]).sum()), 0.0, places=10)
        self.assertAlmostEqual(out["alpha"], float((w * rets).sum() / w.sum()), places=10)
        fitted = out["alpha"] + ind.map(out["industry"]).values + cty.map(out["country"]).values
        np.testing.assert_allclose(fitted + out["resid"].values, rets.values, atol=1e-10)
    def test_fail_closed(self):
        from quantkit.factors import pure_factor_returns
        rets, ind, cty = self._case()
        with self.assertRaises(ValueError):
            pure_factor_returns(rets, ind, pd.Series(["us"] * 4, index=rets.index))
