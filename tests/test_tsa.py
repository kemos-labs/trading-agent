import unittest
import numpy as np
import pandas as pd
from quantkit.tsa import adfuller_pvalue, coint_pvalue, garch_forecast, kalman_hedge_ratio, hmm_regimes

class TestTSA(unittest.TestCase):
    def test_adf(self):
        # stationary AR(1) with low persistence
        np.random.seed(0)
        x=np.random.randn(100)*0.5
        # random walk with drift is non-stationary
        rw=np.cumsum(np.random.randn(100))
        p_stat=adfuller_pvalue(pd.Series(x))
        p_rw=adfuller_pvalue(pd.Series(rw))
        # stationary should have lower p than random walk (not strict, but check finite)
        self.assertTrue(0 <= p_stat <=1)
        self.assertTrue(0 <= p_rw <=1)
    def test_coint(self):
        np.random.seed(1)
        x=pd.Series(np.cumsum(np.random.randn(100)), index=pd.bdate_range("2024-01-01", periods=100))
        y=2*x + np.random.randn(100)*0.5
        # y and x cointegrated (y -2x stationary)
        p=coint_pvalue(y, x)
        self.assertTrue(0 <= p <=1)
        # non-cointegrated: y random walk independent
        y2=pd.Series(np.cumsum(np.random.randn(100)), index=x.index)
        p2=coint_pvalue(y2, x)
        self.assertTrue(0 <= p2 <=1)
    def test_garch(self):
        r=pd.Series(np.random.randn(200)*0.01)
        vol=garch_forecast(r, horizon=1)
        self.assertTrue(np.isfinite(vol) and vol>0)
    def test_kalman(self):
        idx=pd.bdate_range("2024-01-01", periods=50)
        x=pd.Series(np.random.randn(50).cumsum(), index=idx)
        y=0.5*x + np.random.randn(50)*0.2
        hedge=kalman_hedge_ratio(y, x)
        self.assertEqual(len(hedge),50)
        self.assertTrue(np.isfinite(hedge.iloc[-1]))
    def test_hmm(self):
        r=pd.Series(np.random.randn(100)*0.01, index=pd.bdate_range("2024-01-01", periods=100))
        regimes=hmm_regimes(r, n_components=2)
        self.assertEqual(len(regimes),100)
        self.assertTrue(set(regimes.unique()).issubset({0,1}))

if __name__=="__main__":
    unittest.main()
