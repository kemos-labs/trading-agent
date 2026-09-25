"""Validation lab — purged CV, CPCV, PSR/DSR.

Implements the discipline distilled in ``skills/purged-cross-validation``
(López de Prado, AFML Ch.7, Ch.11–14) and ``skills/backtesting-framework``:

- **PurgedKFold**: purge training labels overlapping the test span and
  embargo post-test bars (trailing-window leakage).
- **CPCV**: combinatorial splits → many OOS paths → empirical Sharpe
  distribution (honest range, not one lucky path).
- **PSR / DSR**: many-trial-aware Sharpe significance.

All are vectorized/numpy except the unavoidable per-split purging loop.
Fail-closed on bad embargo / non-finite Sharpe.
"""

from __future__ import annotations

import itertools
import math
import warnings
from dataclasses import dataclass

import numpy as np
import pandas as pd
from scipy.stats import norm

__all__ = ["CPCV", "PurgedKFold", "deflated_sharpe", "probabilistic_sharpe_ratio"]


def _coerce_t1(t1: pd.Series, index: pd.Index) -> pd.Series:
    """Coerce t1 to a Series aligned with index; if None, use index itself (no overlap span)."""
    if t1 is None:
        # No horizon — label ends at its own timestamp (no overlap beyond point)
        return pd.Series(index, index=index)
    t1 = pd.Series(t1)
    # Align; if t1 index is not the same as X index, try to reindex
    if not t1.index.equals(index):
        # If t1 is positional (RangeIndex) and X is DatetimeIndex, map positionally
        if len(t1) == len(index):
            t1.index = index
        else:
            t1 = t1.reindex(index)
    return t1


@dataclass
class PurgedKFold:
    """Purged K-Fold with embargo.

    Splits T rows chronologically into N groups (contiguous). For each
    fold, the test set is one group; the training set is the other N-1
    groups after purging overlaps and embargoing post-test bars.

    Parameters
    ----------
    n_splits : int
        Number of groups / folds (N). Must be >=2.
    t1 : pd.Series | None
        Label horizon end timestamps, indexed like the rows to be split.
        If None, labels have zero span (purge reduces to no-op beyond
        embargo).
    embargo : float | int
        Bars to embargo after each test block. If 0 < embargo < 1,
        interpreted as fraction of total rows (e.g., 0.01 = 1%). If
        integer >=1, absolute bars. 0 disables embargo (but purge still
        applies).

    Notes
    -----
    - Purging rule: drop a training row i if its label span
      ``[index[i], t1[i]]`` overlaps the test span
      ``[test_start, test_end_t1]`` (any shared bar). For point labels
      (t1 == index), this is simply ``test_start <= t1[i] <= test_end``.
    - Embargo: drop training rows whose *start* timestamp is within
      ``embargo_bars`` after ``test_end_t1``. Walk-forward (train before
      test) would need no embargo, but any CV with test between train
      needs it for trailing-window features.
    """

    n_splits: int = 5
    t1: pd.Series | None = None
    embargo: float | int = 0

    def __post_init__(self):
        if self.n_splits < 2:
            raise ValueError("n_splits must be >=2")
        if isinstance(self.embargo, float) and not 0 <= self.embargo < 1:
            # allow 0 < embargo <1 as fraction; 0 is ok
            if self.embargo != 0:
                raise ValueError("embargo float must be in [0,1)")
        if isinstance(self.embargo, int) and self.embargo < 0:
            raise ValueError("embargo must be >=0")

    def _embargo_bars(self, n_total: int) -> int:
        if isinstance(self.embargo, float) and 0 < self.embargo < 1:
            return int(math.ceil(n_total * self.embargo))
        return int(self.embargo)

    def split(self, X: pd.DataFrame | pd.Series | np.ndarray, y=None, groups=None):
        """Yield (train_idx, test_idx) as numpy integer arrays, purged + embargoed."""
        # Determine length and index
        if isinstance(X, (pd.DataFrame, pd.Series)):
            n = len(X)
            idx = X.index
        else:
            n = len(X)  # type: ignore[arg-type]
            idx = pd.RangeIndex(n)
        if n < self.n_splits:
            raise ValueError("n_splits cannot exceed number of samples")

        t1 = _coerce_t1(self.t1, idx)
        # Ensure t1 is comparable with idx (both datetime or both int)
        # For positional t1 that is integer, keep as is.

        # Chronological groups
        indices = np.arange(n)
        # Use array_split for roughly equal groups; keeps order
        groups_list = np.array_split(indices, self.n_splits)
        embargo_bars = self._embargo_bars(n)

        for test_idx in groups_list:
            test_pos = test_idx
            # test span in terms of label horizon
            # test_start = idx[test_pos[0]], test_end_t1 = max t1 over test
            try:
                test_start_idx_val = idx[test_pos[0]]
                test_t1_vals = t1.iloc[test_pos] if isinstance(t1, pd.Series) else t1[test_pos]  # type: ignore
                test_end_t1 = test_t1_vals.max()
            except Exception:
                # fallback to positional
                test_start_idx_val = test_pos[0]
                test_end_t1 = max(t1.iloc[i] if isinstance(t1, pd.Series) else t1[i] for i in test_pos)  # type: ignore

            train_idx = np.concatenate([g for g in groups_list if not np.array_equal(g, test_idx)])
            if len(train_idx) == 0:
                yield train_idx, test_idx
                continue

            # Purging: drop train rows where label overlaps test span
            # For each train i, overlap if t1[i] >= test_start and idx[i] <= test_end_t1
            # Simplified for point labels: t1[i] in [test_start, test_end_t1]
            # Use vectorized check
            keep_mask = np.ones(len(train_idx), dtype=bool)
            for j, tr_pos in enumerate(train_idx):
                # For train row tr_pos, get its t1
                tr_t1 = t1.iloc[tr_pos] if isinstance(t1, pd.Series) else t1[tr_pos]  # type: ignore
                tr_start = idx[tr_pos] if not isinstance(idx, pd.RangeIndex) else tr_pos
                # Overlap condition: intervals [tr_start, tr_t1] and [test_start, test_end_t1] intersect
                # Handle both datetime and int comparison
                try:
                    overlaps = (tr_start <= test_end_t1) and (tr_t1 >= test_start_idx_val)
                except TypeError:
                    # fallback to positional ints
                    overlaps = (tr_pos <= max(test_pos)) and (tr_pos >= min(test_pos))
                if overlaps:
                    # But be careful: for point labels, a train before test_start with t1 < test_start is fine
                    # The above already captures; we keep only non-overlapping
                    keep_mask[j] = False
            purged_train = train_idx[keep_mask]

            # Embargo: drop train rows whose start is within embargo_bars after test_end_t1
            if embargo_bars > 0 and len(purged_train):
                # Find test_end position as max test_pos (for RangeIndex) or timestamp
                test_end_pos = int(np.max(test_pos))
                # Embargo applies to train rows that start soon after test_end
                # For simplicity, embargo the next `embargo_bars` *positions* after test_end
                embargo_mask = np.ones(len(purged_train), dtype=bool)
                for j, tr_pos in enumerate(purged_train):
                    if tr_pos > test_end_pos and tr_pos <= test_end_pos + embargo_bars:
                        embargo_mask[j] = False
                    # For datetime index, also check timestamp proximity if t1 is datetime
                    # If idx is DatetimeIndex, check if idx[tr_pos] <= test_end_t1 + embargo in time units?
                    # We keep positional embargo as it is the common 1% rule in AFML.
                purged_train = purged_train[embargo_mask]

            yield purged_train, test_idx

    def get_n_splits(self, X=None, y=None, groups=None) -> int:
        return self.n_splits


class CPCV:
    """Combinatorial Purged Cross-Validation.

    Splits T rows into N chronological groups and evaluates every
    combination of k test groups (N choose k splits). For each split,
    training groups are purged + embargoed as in PurgedKFold.

    Parameters
    ----------
    n_groups : int
        Number of chronological groups (N). N=6, k=2 → 15 splits.
    k : int
        Number of groups per test set. Keep k ≤ N/2 so train fraction
        θ = 1 − k/N ≥ 0.5.
    t1 : pd.Series | None
        Label horizon (see PurgedKFold).
    embargo : float | int
        Same semantics as PurgedKFold.
    """

    def __init__(self, n_groups: int = 6, k: int = 2, t1: pd.Series | None = None, embargo: float | int = 0):
        if n_groups < 2:
            raise ValueError("n_groups must be >=2")
        if not 1 <= k <= n_groups:
            raise ValueError("k must be in [1, n_groups]")
        if k > n_groups // 2:
            warnings.warn(f"k={k} > N/2={n_groups//2}: train fraction < 0.5; consider smaller k")
        self.n_groups = n_groups
        self.k = k
        self.t1 = t1
        self.embargo = embargo

    def split(self, X: pd.DataFrame | pd.Series | np.ndarray, y=None, groups=None):
        if isinstance(X, (pd.DataFrame, pd.Series)):
            n = len(X)
            idx = X.index
        else:
            n = len(X)  # type: ignore[arg-type]
            idx = pd.RangeIndex(n)
        if n < self.n_groups:
            raise ValueError("n_groups cannot exceed number of samples")
        indices = np.arange(n)
        groups_list = np.array_split(indices, self.n_groups)
        combos = list(itertools.combinations(range(self.n_groups), self.k))
        # Reuse purging logic via PurgedKFold helper per split
        # For each combo, test = union of k groups, train = rest purged
        t1 = _coerce_t1(self.t1, idx)
        embargo_bars = PurgedKFold(n_splits=self.n_groups, t1=self.t1, embargo=self.embargo)._embargo_bars(n)
        for combo in combos:
            test_idx = np.concatenate([groups_list[i] for i in combo])
            test_idx_sorted = np.sort(test_idx)
            # For purging, treat test span as union of its groups' spans
            # Compute test_end_t1 as max t1 over test_idx
            test_t1_vals = t1.iloc[test_idx_sorted] if isinstance(t1, pd.Series) else t1[test_idx_sorted]  # type: ignore
            test_end_t1 = test_t1_vals.max()
            test_start_val = idx[test_idx_sorted[0]] if not isinstance(idx, pd.RangeIndex) else test_idx_sorted[0]
            train_idx = np.concatenate([groups_list[i] for i in range(self.n_groups) if i not in combo])
            # Purge
            keep_mask = np.ones(len(train_idx), dtype=bool)
            for j, tr_pos in enumerate(train_idx):
                tr_t1 = t1.iloc[tr_pos] if isinstance(t1, pd.Series) else t1[tr_pos]  # type: ignore
                tr_start = idx[tr_pos] if not isinstance(idx, pd.RangeIndex) else tr_pos
                try:
                    overlaps = (tr_start <= test_end_t1) and (tr_t1 >= test_start_val)
                except TypeError:
                    overlaps = (tr_pos <= np.max(test_idx_sorted)) and (tr_pos >= np.min(test_idx_sorted))
                if overlaps:
                    keep_mask[j] = False
            purged_train = train_idx[keep_mask]
            if embargo_bars > 0 and len(purged_train):
                test_end_pos = int(np.max(test_idx_sorted))
                embargo_mask = np.ones(len(purged_train), dtype=bool)
                for j, tr_pos in enumerate(purged_train):
                    if tr_pos > test_end_pos and tr_pos <= test_end_pos + embargo_bars:
                        embargo_mask[j] = False
                purged_train = purged_train[embargo_mask]
            yield purged_train, test_idx_sorted

    def get_n_splits(self, X=None, y=None, groups=None) -> int:
        # N choose k
        return math.comb(self.n_groups, self.k)


def probabilistic_sharpe_ratio(
    sharpe: float, sharpe_benchmark: float, n_obs: int, skew: float, kurt: float
) -> float:
    """PSR = P[ true SR > SR* | observed SR̂ ] (Bailey & López de Prado, 2012).

    PSR = Φ[ (SR̂ − SR*)·√(T−1) / √(1 − γ₃·SR̂ + ((γ₄−1)/4)·SR̂²) ]

    Parameters
    ----------
    sharpe : float
        Observed Sharpe SR̂ (annualized or not — use same as benchmark).
    sharpe_benchmark : float
        Benchmark SR* to beat.
    n_obs : int
        Number of return observations T.
    skew : float
        Sample skewness γ₃ of returns.
    kurt : float
        Sample kurtosis γ₄ (Pearson, i.e., normal = 3, not excess).

    Returns
    -------
    float
        Probability in [0,1]; >0.95 suggests skill at 5% significance.
    """
    if n_obs < 2:
        raise ValueError("n_obs must be >=2")
    if not np.isfinite(sharpe) or not np.isfinite(sharpe_benchmark):
        return 0.0
    # Standard error of Sharpe with non-normal correction (Mertens)
    denom = math.sqrt(1 - skew * sharpe + ((kurt - 1) / 4) * sharpe * sharpe)
    if denom <= 0 or not math.isfinite(denom):
        return 0.0
    z = (sharpe - sharpe_benchmark) * math.sqrt(n_obs - 1) / denom
    return float(norm.cdf(z))


def deflated_sharpe(
    sharpe: float, n_obs: int, skew: float, kurt: float, n_trials: int
) -> float:
    """DSR — PSR with benchmark SR* endogenized for N trials (multiple testing).

    SR* = √V[SR̂] · [ (1−γ)·Φ⁻¹(1−1/N) + γ·Φ⁻¹(1−1/(N·e)) ],
    where γ = Euler–Mascheroni ≈0.5772 and V[SR̂] is the variance of SR̂
    under the null (approx).

    With ~20 trials at 5% significance, false positives are expected —
    DSR corrects for that.
    """
    if n_trials < 1:
        raise ValueError("n_trials must be >=1")
    if n_trials == 1:
        return probabilistic_sharpe_ratio(sharpe, 0.0, n_obs, skew, kurt)
    # Variance of Sharpe under null (approx; Bailey et al. 2014)
    # Use same denom as PSR but at SR=0 → 1
    # More accurate: V = (1 + 0.5*SR^2) / (T-1) but we use the skew/kurt corrected denom
    # For SR* we need an estimate of V[SR̂] — use the PSR denominator at observed SR as plug-in
    # Standard error of Sharpe
    var = (1 - skew * sharpe + ((kurt - 1) / 4) * sharpe * sharpe) / (n_obs - 1)
    if var <= 0 or not math.isfinite(var):
        return 0.0
    sd = math.sqrt(var)
    gamma = 0.5772156649015328606
    # Expected max of N i.i.d. Gaussian
    # Approximate as in AFML Ch.14: SR* ≈ sd * [ (1-γ)*inv(1-1/N) + γ*inv(1-1/(N*e)) ]
    try:
        inv1 = norm.ppf(1 - 1 / n_trials)
        inv2 = norm.ppf(1 - 1 / (n_trials * math.e))
    except Exception:
        return 0.0
    sr_star = sd * ((1 - gamma) * inv1 + gamma * inv2)
    return probabilistic_sharpe_ratio(sharpe, sr_star, n_obs, skew, kurt)
