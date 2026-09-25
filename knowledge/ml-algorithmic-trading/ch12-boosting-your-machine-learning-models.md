# Ch12 — Boosting Your Machine Learning Models

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 12.

## Purpose
Gradient boosting — the sequential ensemble method that dominates tabular ML competitions — applied to return/direction prediction, with hyperparameter discipline and early stopping to avoid overfitting.

## Boosting vs. bagging
- **Bagging** (RF): parallel, variance reduction by averaging.
- **Boosting**: sequential — each new tree fits the *residuals/errors* of the ensemble so far (gradient descent in function space). Reduces bias; must control capacity or it overfits.

## Gradient boosting mechanics
- Start with a constant model; each iteration m fits a weak learner (shallow tree) to the negative gradient of the loss w.r.t. current predictions (residuals for MSE), scaled by learning rate η, added to the ensemble:
  F_m(x) = F_{m−1}(x) + η·h_m(x)
- **Learning rate (η)**: small η (0.01–0.1) + more trees = better generalization; large η overfits fast.
- **Tree capacity**: shallow trees (depth 3–6) as weak learners; `min_child_weight`, `max_depth`, `subsample` (row), `colsample` (feature) all fight overfitting.
- **Early stopping**: monitor validation loss; stop when it degrades — the single most important overfitting control.

## XGBoost specifics
- Additive training with a regularized objective (L1+L2 on leaf weights), Newton boosting (second-order gradients), built-in missing-value handling, and weighted quantile sketching for splits.
- `max_depth`, `eta` (learning rate), `subsample`, `colsample_bytree`, `min_child_weight`, `lambda`/`alpha` (regularization).
- n_estimators + early_stopping_rounds pattern: train many trees with early stopping on a validation set.

## Practical patterns for finance
- Same leakage discipline as RF (ch11): chronological splits, point-in-time features, purge/embargo (skills `walk-forward-validation`, `purged-cross-validation`).
- Evaluate with IC/quintile spreads; boosting is a natural fit for factor panels with interactions.
- Watch for **slow drift**: boosted models memorize; retrain on rolling windows and monitor performance decay.
- Feature importance: use permutation/validation-based (like RF MDA) rather than raw gain where possible.

## When boosting beats alternatives
- Tabular, medium-to-large n, nonlinear interactions, and mixed feature types — boosting (XGBoost/LightGBM/CatBoost) is usually the strongest practical choice before deep learning.
- On very noisy financial targets, cap capacity (shallow trees, low η) and lean on early stopping.

## Key takeaways
- Boosting is gradient descent on functions: learning rate + tree capacity + early stopping are the dials that separate genius from overfit.
- It's the default winner for tabular financial prediction; pair it with honest time-series validation.
- Ensemble diversity (bagging + boosting) can be combined (e.g., XGBoost with subsampling) for further stability.
