# Purged K-Fold CV, Embargo, and Combinatorial Purged CV (CPCV)

## Name
purged-cross-validation

## Description
Backtest and validate ML strategies when labels overlap in time
(triple-barrier/meta-labeling outcomes): purge overlapping training
labels, embargo post-test observations, and build multiple
out-of-sample paths with Combinatorial Purged Cross-Validation (CPCV)
to get a distribution of performance instead of one historical path.
Use whenever financial labels are path-dependent or overlapping.

## When to use it
- Labels span intervals (triple-barrier t1 objects) or features are
  serially correlated — plain k-fold leaks information.
- You want to report backtest performance honestly (distribution of
  Sharpe, not one lucky path).
- Hyper-parameter tuning must not overfit to leakage (GridSearchCV with
  a purged CV generator).
- Many strategy variants were tried — you need multiple-testing-aware
  significance (deflated Sharpe).

## The method

### 1. Purge overlapping training labels
Two labels i (train) and j (test) leak when their spans
[t_i0, t_i1] and [t_j0, t_j1] overlap. Drop i from the training set
if any of:
- t_i0 ≤ t_j0 ≤ t_i1
- t_j0 ≤ t_i0 ≤ t_j1
- t_i0 ≤ t_j1 ≤ t_i1 (and vice versa) — any shared return bar.
Implement with label `t1` (vertical-barrier/end timestamps) vs test
set spans. If the test set is contiguous, one `testTimes` series spans
it.

### 2. Embargo after each test block
For features with trailing windows, overlap persists beyond label
spans. Drop training observations for a short period (e.g., 1% of the
sample) *after* each test set. Not needed in walk-forward (train
predates test), needed in any CV where test blocks sit between train
blocks.

### 3. Use PurgedKFold for tuning
Pass a custom `PurgedKFold` (not sklearn's plain KFold) to
GridSearchCV/RandomizedSearchCV; feed uniqueness `sample_weight`
(ch4-style) via `fit_params` (sklearn Pipelines don't take
sample_weight in fit — subclass or use fit_params).

### 4. CPCV: many OOS paths
- Split T observations chronologically into N groups.
- For k test groups per split, evaluate **every combination** of
  N−k train / k test groups (purge + embargo each split).
- Concatenate forecasts into φ[N,k] backtest paths; compute one
  Sharpe per path → empirical Sharpe distribution.
- φ grows with N and k→N/2 (train fraction θ = 1 − k/N; keep k ≤ N/2).
- Report mean/median Sharpe, % of paths with negative Sharpe — the
  honest range of what live trading may deliver.

### 5. Significance: PSR and DSR
- Probabilistic Sharpe Ratio (PSR): probability true SR > benchmark
  SR*, adjusting for skew γ₃ and kurtosis γ₄:
  PSR = Φ[ (SR̂ − SR*)·√(T−1) /
        √(1 − γ₃·SR̂ + ((γ₄−1)/4)·SR̂²) ]
- Deflated Sharpe Ratio (DSR): same but SR* endogenized for N trials:
  SR* = √(V[SR̂])·[(1−γ)·Φ⁻¹(1 − 1/N) + γ·Φ⁻¹(1 − 1/(N·e))],
  γ = Euler–Mascheroni ≈ 0.5772. Many trials → higher bar.

## Code sketch (purged split)

```python
def purged_split(train_idx, test_idx, t1_train, t1_test, embargo=0):
    # t1_*: label end timestamps indexed like the rows
    test_start, test_end = t1_test.min(), t1_test.max()
    # drop train rows whose label span overlaps the test span
    keep = ~((t1_train >= test_start) & (t1_train <= test_end))
    # (also check train label start <= test_end; use both bounds in practice)
    train_idx = train_idx[keep]
    # embargo: drop train rows immediately after test_end
    if embargo:
        after = train_idx[train_idx.index > test_end]
        n = int(len(after) * embargo)
        train_idx = train_idx.drop(after.sort_index().index[:n])
    return train_idx, test_idx
```

## Known pitfalls
- Plain k-fold on overlapping labels inflates scores — especially with
  irrelevant features (leakage creates false discoveries).
- Purging only label overlaps but not embargoing trailing-window
  features.
- Quoting the best of many trials' Sharpe without deflating it —
  with ~20 trials at 5% significance, false positives are expected.
- CPCV with too-small N: few paths; k close to N/2 halves training
  data — balance path count against train fraction.

## Source
López de Prado, *Advances in Financial Machine Learning* (Wiley, 2018),
ch7, ch11–14.
