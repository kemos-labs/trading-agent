# Ch11 — Random Forests: A Deep-Dive

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 11.

## Purpose
Decision trees and their random-forest ensemble: how they work, why bagging reduces variance, and how to use trees on financial data — including feature importance and the leakage pitfalls unique to tree models.

## Decision trees
- Recursive partitioning: split nodes to minimize impurity (Gini for classification, MSE for regression); each leaf predicts the local mean/majority.
- **Strengths**: nonlinear, handle interactions, no feature scaling, interpretable.
- **Weaknesses**: high variance (small data changes → very different trees), overfit easily, extrapolate poorly beyond training range.

## Bagging → random forests
- **Bootstrap aggregating**: train many trees on bootstrap samples, average predictions → variance reduction.
- **Random feature subsampling** at each split decorrelates trees further (mtry ≈ √p for classification, p/3 for regression).
- Out-of-bag (OOB) score: each sample is predicted by trees that never saw it — a free, leakage-free validation set.

## Tuning the forest
- Key hyperparameters: `n_estimators` (plateaus; more is safer), `max_depth`/`min_samples_leaf` (depth control = variance control), `max_features`, `max_samples` (bootstrap size).
- Tune on validation with time-series CV (ch6); prefer shallower, high-sample trees on noisy financial data.

## Feature importance
- **MDI (impurity-based)**: total impurity decrease attributable to each feature across splits — biased toward high-cardinality/continuous features.
- **MDA (permutation importance)**: shuffle a feature and measure validation-score drop — more honest; requires a proper validation split.
- Trees enable interaction detection: feature importance by pair (product) can surface conditional effects ML thrives on.

## Using forests for trading
- Predict returns/direction from alpha factors (ch4) and lagged features; evaluate via IC and quantile spreads rather than accuracy.
- Forests beat linear models when interactions matter (e.g., value works only for small caps); they handle tabular factor panels well and are far cheaper than deep nets.

## Critical leakage pitfalls
- **Temporal leakage**: random CV splits leak future into training — use chronological splits (skills `walk-forward-validation`, `purged-cross-validation`).
- **Label overlap**: multi-horizon labels overlap in time; purge/embargo validation folds.
- **Scaler/feature leakage**: features computed with full-sample statistics leak; compute rolling/windowed features point-in-time.
- **OOB ≠ backtest**: OOB error still assumes iid samples; a walk-forward backtest is the true test.

## Key takeaways
- Random forests are a top-tier default for tabular financial prediction: robust, nonlinear, and with built-in OOB validation.
- Hyperparameter discipline and feature-leakage awareness decide success more than architecture.
- Interpret importance honestly (permutation-based) and validate with time-series splits.
