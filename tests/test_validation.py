import unittest
import numpy as np
import pandas as pd
from quantkit.validation import PurgedKFold, CPCV, probabilistic_sharpe_ratio, deflated_sharpe

class TestPurgedKFold(unittest.TestCase):
    def test_purge_overlapping_labels(self):
        # T=10, t1 = idx + 2 (labels span 2 bars), 5 splits, test group 2 should purge train rows whose t1 overlaps
        n=10
        idx=pd.RangeIndex(n)
        t1=pd.Series(np.arange(n)+2, index=idx)  # label ends 2 after start
        X=pd.DataFrame({"a": range(n)}, index=idx)
        kf=PurgedKFold(n_splits=5, t1=t1, embargo=0)
        splits=list(kf.split(X))
        self.assertEqual(len(splits),5)
        # For each split, verify no train t1 overlaps test span
        for train_idx, test_idx in splits:
            if len(train_idx)==0 or len(test_idx)==0:
                continue
            test_start=test_idx.min()
            test_end_t1=t1.iloc[test_idx].max()
            for tr in train_idx:
                # train interval [tr, t1[tr]] should not intersect [test_start, test_end_t1]
                self.assertFalse((tr <= test_end_t1 and t1.iloc[tr] >= test_start), f"overlap {tr} {t1.iloc[tr]} vs test {test_start}-{test_end_t1}")

    def test_embargo_drops_recent_train(self):
        n=20
        idx=pd.RangeIndex(n)
        t1=pd.Series(idx, index=idx)  # point labels
        X=pd.DataFrame({"a": range(n)}, index=idx)
        kf=PurgedKFold(n_splits=5, t1=t1, embargo=2)  # 2 bars
        for train_idx, test_idx in kf.split(X):
            test_end=test_idx.max()
            for tr in train_idx:
                self.assertFalse(test_end < tr <= test_end+2, "embargo failed")

    def test_embargo_fraction(self):
        n=100
        idx=pd.RangeIndex(n)
        t1=pd.Series(idx, index=idx)
        X=pd.DataFrame({"a": range(n)}, index=idx)
        kf=PurgedKFold(n_splits=5, t1=t1, embargo=0.01)  # 1% => 1 bar
        train, test = next(kf.split(X))
        # should have embargo of 1
        test_end=test.max()
        for tr in train:
            self.assertFalse(test_end < tr <= test_end+1)

    def test_get_n_splits(self):
        kf=PurgedKFold(n_splits=3)
        self.assertEqual(kf.get_n_splits(),3)

class TestCPCV(unittest.TestCase):
    def test_n_choose_k(self):
        n=12
        idx=pd.RangeIndex(n)
        t1=pd.Series(idx, index=idx)
        X=pd.DataFrame({"a": range(n)}, index=idx)
        cpcv=CPCV(n_groups=4, k=2, t1=t1, embargo=0)
        splits=list(cpcv.split(X))
        self.assertEqual(len(splits), 6)  # 4 choose 2 =6
        self.assertEqual(cpcv.get_n_splits(),6)
        for train_idx, test_idx in splits:
            self.assertEqual(len(test_idx), 6)  # 2 groups *3 per group
            self.assertTrue(len(train_idx) + len(test_idx) <= n)  # purged may reduce train
            self.assertTrue(len(set(train_idx) & set(test_idx))==0)

    def test_k_too_large_warns(self):
        import warnings
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            CPCV(n_groups=4, k=3)
            self.assertTrue(any(issubclass(x.category, UserWarning) for x in w))

class TestPSRDSR(unittest.TestCase):
    def test_psr_monotonic(self):
        # PSR increases with higher observed Sharpe and more obs
        psr_low=probabilistic_sharpe_ratio(0.5, 0.0, 100, 0, 3)
        psr_high=probabilistic_sharpe_ratio(1.0, 0.0, 100, 0, 3)
        self.assertGreater(psr_high, psr_low)
        self.assertTrue(0 < psr_low < 1)
        # DSR with many trials should be lower than PSR with 1 trial (higher bar)
        dsr1=deflated_sharpe(1.0, 100, 0, 3, n_trials=1)
        dsr20=deflated_sharpe(1.0, 100, 0, 3, n_trials=20)
        self.assertGreater(dsr1, dsr20)

    def test_psr_benchmark(self):
        # If sharpe == benchmark, PSR ~0.5
        psr=probabilistic_sharpe_ratio(0.0, 0.0, 1000, 0, 3)
        self.assertAlmostEqual(psr, 0.5, delta=0.02)

if __name__=="__main__":
    unittest.main()
