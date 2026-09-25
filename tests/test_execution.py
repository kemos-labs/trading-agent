import unittest
import numpy as np
import pandas as pd
from quantkit.execution import quoted_spread, effective_spread, roll_spread, variance_ratio, kyle_lambda, amihud_illiquidity

class TestExecution(unittest.TestCase):
    def test_spreads(self):
        idx=pd.bdate_range("2024-01-01", periods=5)
        bid=pd.Series([99,99.5,100,100.5,101], index=idx)
        ask=pd.Series([100,100.5,101,101.5,102], index=idx)
        qs=quoted_spread(bid, ask)
        self.assertTrue((qs==1).all())
        price=pd.Series([99.6,100,100.8,101,101.6], index=idx)
        es=effective_spread(price, bid, ask)
        self.assertTrue((es>=0).all())
    def test_roll(self):
        # mean-reverting price changes -> negative autocov -> positive spread
        dp=pd.Series([1,-1,1,-1,1,-1,1,-1], dtype=float)
        spread=roll_spread(dp)
        self.assertTrue(np.isfinite(spread) and spread>0)
        # trending -> cov positive -> nan
        dp2=pd.Series([1,1,1,1,1], dtype=float)
        self.assertTrue(np.isnan(roll_spread(dp2)))
    def test_variance_ratio(self):
        r=pd.Series(np.random.randn(100)*0.01)
        vr=variance_ratio(r, k=2)
        self.assertTrue(np.isfinite(vr) and vr>0)
    def test_kyle_amihud(self):
        dp=pd.Series(np.random.randn(20)*0.5)
        sv=pd.Series(np.random.randn(20)*1000)
        lam=kyle_lambda(dp, sv)
        self.assertTrue(np.isfinite(lam) or np.isnan(lam))
        r=pd.Series(np.random.randn(20)*0.01)
        dv=pd.Series(np.random.uniform(1e6,5e6,20))
        ill=amihud_illiquidity(r, dv)
        self.assertTrue(np.isfinite(ill) and ill>0)

if __name__=="__main__":
    unittest.main()

class TestAlmgrenImpact(unittest.TestCase):
    def test_hand_values(self):
        from quantkit.execution import almgren_impact
        # X=1e6, V=1e7, T=0.1, sigma=0.02, Theta=1e9:
        # I = .314*.02*.1*100^.25 = .314*.02*.1*3.16227766 = .00019859...
        # J = I/2 + .142*.02*|1e6/(1e7*.1)|^.6 = I/2 + .00284
        perm, real = almgren_impact(1e6, 1e7, 0.1, 0.02, 1e9)
        self.assertAlmostEqual(perm, 0.314*0.02*0.1*(100**0.25), places=12)
        self.assertAlmostEqual(real, perm/2 + 0.142*0.02*1.0**0.6, places=12)
    def test_sign_and_schedule(self):
        from quantkit.execution import almgren_impact
        p_buy = almgren_impact(1e6, 1e7, 0.1, 0.02, 1e9)
        p_sell = almgren_impact(-1e6, 1e7, 0.1, 0.02, 1e9)
        self.assertAlmostEqual(p_sell[0], -p_buy[0], places=12)
        self.assertAlmostEqual(p_sell[1], -p_buy[1], places=12)
        # permanent impact is schedule-free: same X/V, different T -> same I
        p_slow = almgren_impact(1e6, 1e7, 0.4, 0.02, 1e9)
        self.assertAlmostEqual(p_slow[0], p_buy[0], places=12)
        # slower execution -> smaller temporary piece
        self.assertLess(abs(p_slow[1]), abs(p_buy[1]))
    def test_fail_closed(self):
        from quantkit.execution import almgren_impact
        with self.assertRaises(ValueError):
            almgren_impact(1e6, 0, 0.1, 0.02, 1e9)
        with self.assertRaises(ValueError):
            almgren_impact(0, 1e7, 0.1, 0.02, 1e9)
