import unittest
import numpy as np
import pandas as pd
from quantkit.risk import historical_var, historical_cvar, parametric_var, stress_covariance, cholesky_scenarios, var_backtest_kupiec, downside_deviation, sortino_ratio, bond_duration_convexity

class TestRisk(unittest.TestCase):
    def test_var_cvar(self):
        r=pd.Series(np.random.randn(100)*0.01)
        self.assertGreater(historical_var(r, 0.05),0)
        self.assertGreaterEqual(historical_cvar(r,0.05), historical_var(r,0.05))
        self.assertGreater(parametric_var(r,0.05),0)
    def test_downside(self):
        r=pd.Series([0.01,-0.02,0.015,-0.01])
        self.assertGreater(downside_deviation(r),0)
        self.assertTrue(np.isfinite(sortino_ratio(r)))
    def test_bond(self):
        cf=pd.Series([5,5,105], index=[1,2,3.0])
        res=bond_duration_convexity(cf, y=0.05, freq=1)
        self.assertIn("macaulay", res)
        self.assertGreater(res["macaulay"],0)
        self.assertGreater(res["pv01"],0)
    def test_stress_psd(self):
        cov=pd.DataFrame([[0.04,0.01],[0.01,0.09]], index=["A","B"], columns=["A","B"])
        stressed=stress_covariance(cov, shock=0.2, psd=True)
        # should be PSD (eigenvalues >=0)
        vals=np.linalg.eigvalsh(stressed.to_numpy())
        self.assertTrue((vals>=-1e-8).all())
    def test_cholesky(self):
        cov=pd.DataFrame([[0.04,0.01],[0.01,0.09]], index=["A","B"], columns=["A","B"])
        scen=cholesky_scenarios(cov, n_scenarios=100, seed=0)
        self.assertEqual(scen.shape, (100,2))
    def test_kupiec(self):
        r=pd.Series(np.random.randn(200)*0.01)
        var=pd.Series([0.02]*200, index=r.index)
        res=var_backtest_kupiec(r, var, alpha=0.05)
        self.assertIn("p_value", res)
        self.assertTrue(0 <= res["p_value"] <=1)

if __name__=="__main__":
    unittest.main()
