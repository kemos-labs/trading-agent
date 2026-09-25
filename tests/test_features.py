import unittest
import numpy as np
import pandas as pd
from quantkit.features import fractional_diff, get_weights, cusum_filter, triple_barrier_labels, plug_in_entropy

class TestFFD(unittest.TestCase):
    def test_weights_sum(self):
        w = get_weights(0.5, 5)
        self.assertEqual(len(w),5)
        self.assertAlmostEqual(w[-1],1.0)
    def test_fractional_diff_flat(self):
        s=pd.Series([1,1,1,1,1.0], index=pd.date_range("2024-01-01", periods=5))
        out=fractional_diff(s, d=0.5)
        # constant series should be small near zero after diff
        self.assertTrue(np.allclose(out.dropna().values, 0, atol=0.5))
    def test_cusum(self):
        s=pd.Series([100,101,102,103,104,103,102,101], index=pd.bdate_range("2024-01-01", periods=8))
        ev=cusum_filter(s, threshold=0.5)
        self.assertTrue(len(ev)>=1)
    def test_triple_barrier(self):
        close=pd.Series([100,101,102,103,104,105], index=pd.bdate_range("2024-01-01", periods=6))
        events=pd.DatetimeIndex([close.index[0], close.index[2]])
        df=triple_barrier_labels(close, events, pt_sl=(0.01,0.01), vertical_barrier=3)
        self.assertEqual(len(df),2)
        self.assertTrue(set(df["bin"]).issubset({-1,0,1}))
    def test_entropy(self):
        s=pd.Series(np.random.randn(100))
        e=plug_in_entropy(s, bins=10)
        self.assertTrue(0 < e < 4)

if __name__=="__main__":
    unittest.main()
