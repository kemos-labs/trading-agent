import unittest
import numpy as np
import pandas as pd
from quantkit.execution import quoted_spread, effective_spread, roll_spread, variance_ratio, kyle_lambda, amihud_illiquidity, almgren_impact

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


class TestImpactAlmgren(unittest.TestCase):
    def test_hand_value(self):
        from quantkit.execution import impact_almgren
        # X=1e6, V=1e7, T=0.1, sigma=.02, Theta=1e9, ptc=0:
        # J = I/2 + .142*.02*1^.6 ≈ 38.33 bps
        perm, real = almgren_impact(1e6, 1e7, 0.1, 0.02, 1e9)
        got = impact_almgren(1e6, 1e7, 0.02, 0.1, 1e9, ptc=0.0)
        self.assertAlmostEqual(got, real * 1e4, places=6)
        self.assertAlmostEqual(got, 38.33, places=2)
    def test_flat_floor_additive(self):
        from quantkit.execution import impact_almgren
        # ptc=0.001 (10 bps) is a floor: total = ptc + |J|
        got = impact_almgren(1e6, 1e7, 0.02, 0.1, 1e9, ptc=0.001)
        self.assertGreater(got, 10.0)
        self.assertAlmostEqual(got, 10.0 + 38.33, places=2)
    def test_sign_symmetry(self):
        from quantkit.execution import impact_almgren
        buy = impact_almgren(1e6, 1e7, 0.02, 0.1, 1e9)
        sell = impact_almgren(-1e6, 1e7, 0.02, 0.1, 1e9)
        self.assertAlmostEqual(buy, sell, places=9)
    def test_schedule_monotonic(self):
        from quantkit.execution import impact_almgren
        fast = impact_almgren(1e6, 1e7, 0.02, 0.1, 1e9)
        slow = impact_almgren(1e6, 1e7, 0.02, 0.4, 1e9)
        self.assertLess(slow, fast)
    def test_fail_closed(self):
        from quantkit.execution import impact_almgren
        with self.assertRaises(ValueError):
            impact_almgren(1e6, 0, 0.02, 0.1, 1e9)
        with self.assertRaises(ValueError):
            impact_almgren(1e6, 1e7, 0.0, 0.1, 1e9)
        with self.assertRaises(ValueError):
            impact_almgren(1e6, 1e7, 0.02, 0.0, 1e9)
        with self.assertRaises(ValueError):
            impact_almgren(1e6, 1e7, 0.02, 0.1, 0.0)
        with self.assertRaises(ValueError):
            impact_almgren(0, 1e7, 0.02, 0.1, 1e9)
        # oversize: 30% ADV raises by default, allowed with flag
        with self.assertRaises(ValueError):
            impact_almgren(3e6, 1e7, 0.02, 0.1, 1e9)
        got = impact_almgren(3e6, 1e7, 0.02, 0.1, 1e9, allow_oversize=True)
        self.assertGreater(got, 0.0)


class TestEFMidpoint(unittest.TestCase):
    def test_risk_neutral_even_pace(self):
        from quantkit.execution import ef_midpoint
        x0 = np.array([0.0, 0.0])
        xT = np.array([10.0, -4.0])
        Pi = np.zeros((2, 2))
        T = np.eye(2)  # temporary impact present; lam=0 -> classic even pace
        Omega = np.eye(2)
        mid = ef_midpoint(x0, xT, Pi, T, 0.0, Omega)
        np.testing.assert_allclose(mid, (x0 + xT) / 2, atol=1e-12)
    def test_risk_averse_front_loads(self):
        from quantkit.execution import ef_midpoint
        x0 = np.array([0.0])
        xT = np.array([10.0])
        Pi = np.zeros((1, 1))
        T = np.zeros((1, 1))
        Omega = np.eye(1)
        mid = ef_midpoint(x0, xT, Pi, T, 1.0, Omega)
        # front-loaded: midpoint closer to target than the even pace
        self.assertGreater(float(mid[0]), 5.0)
        self.assertLessEqual(float(mid[0]), 10.0)
    def test_fail_closed(self):
        from quantkit.execution import ef_midpoint
        with self.assertRaises(ValueError):
            ef_midpoint(np.array([0.0]), np.array([1.0]), np.zeros((1, 1)),
                        np.zeros((1, 1)), -1.0, np.eye(1))
