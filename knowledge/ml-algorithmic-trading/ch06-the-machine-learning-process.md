# Ch06 — The Machine Learning Process

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 6.

## Purpose
The book's conceptual core: how supervised ML generalizes, the bias–variance trade-off, and the disciplined train/validate/test process that keeps financial models honest.

## Learning and generalization
- Supervised learning: find f̂ such that f̂(x) ≈ y on unseen data, given training pairs (x, y).
- **Bias–variance decomposition** of expected error:
  E[error] = irreducible noise + bias² + variance.
  - High bias → underfitting (too simple a model class).
  - High variance → overfitting (too complex / too little data).
  - Financial data: high noise, non-stationarity → variance dominates; regularize aggressively.
- **Curse of dimensionality**: required sample size grows exponentially with features; prefer few, informative, orthogonal features (cf. ch4 factor selection).

## The train/validation/test discipline
- Split once into train / validation (for tuning) / test (final, untouched).
- **Financial twist**: random splits leak temporal dependence — use chronological splits, walk-forward, and purged CV (skills `walk-forward-validation`, `purged-cross-validation`).
- **Preprocessing leakage**: fit scalers/encoders on the *training* split only; apply to validation/test. Standardizing on the full dataset leaks future information.

## Cross-validation
- k-fold CV: average performance over k folds; report mean ± std.
- Time-series CV: expanding or rolling window; test block always after train block.
- Purpose: (1) honest performance estimate, (2) hyperparameter selection — but tuning on the validation folds then quoting their performance double-counts the data.

## Model families in one glance
- Linear (regression, logistic) — interpretable, low variance, high bias.
- Trees/ensembles (RF, boosting) — nonlinear, handle interactions, still tabular-friendly.
- kNN — local constancy assumption, suffers in high dimensions.
- Neural networks — representation learning, high capacity, needs data + regularization.
- Unsupervised (PCA, clustering, autoencoders) — features/risk factors, compression (ch13, ch20).

## Evaluation metrics
- Regression: MSE/RMSE, MAE, R²; in finance: IC and rank-IC for return prediction.
- Classification: accuracy (misleading on imbalanced classes), precision/recall, ROC-AUC, F1.
- **Imbalanced targets** (rare events): use AUC, precision-recall; resample or reweight with care to avoid leakage.

## Key takeaways
- The process — honest splits, leakage-free preprocessing, regularization, and reporting uncertainty — matters far more than the algorithm.
- On noisy financial data, favor simpler models with strong validation discipline over complex ones.
- Never let validation performance leak into model selection and then quote it as out-of-sample.
