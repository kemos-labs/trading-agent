# Chapter 12 — Ensemble Methods

## Core idea
Ensembles combine many weak learners into one strong predictor. The book
covers decision trees as the base model and the classic ensembles: Random
Forest and gradient boosting (XGBoost).

## Decision trees
- Recursive partitioning: split on the feature+threshold that best reduces
  impurity (Gini/entropy for classification, MSE for regression).
- `max_depth` and `min_samples_split` control complexity — deep trees
  overfit, shallow trees underfit. The book uses `max_depth=6`.
- Trees are nonparametric: they capture interactions automatically, need no
  feature scaling, and give **feature importance** (a rare transparency win
  for ML trading).

## Random Forest
- **Bagging + feature randomness**: train many trees on bootstrap samples,
  each considering a random feature subset; average (regression) or vote
  (classification).
- Reduces variance vs a single tree; robust to noise; hard to overfit as
  badly as a single deep tree.

## Gradient boosting (XGBoost)
- **Sequential** additive model: each new tree fits the *residuals* of the
  current ensemble, shrinking the loss step by step.
- Powerful, but needs careful regularization (`learning_rate`, `max_depth`,
  `n_estimators`, `subsample`) — it overfits easily on noisy financial data.
- In ch16, a decision-tree regressor (boosting's base class) is one of the
  three diverse learners screened across 150 assets.

## Pitfalls
- Trees on **imbalanced/trending** data can latch onto trivial splits —
  evaluate by strategy P&L, not accuracy.
- Boosting + noisy returns = overfit magnet; use early stopping and modest
  depth.
- No extrapolation: trees can't predict outside the training range of the
  target — relevant for return-regression targets with fat tails.

## Practical settings (book's defaults)
- Decision tree: `max_depth=6` — shallow enough to stay robust on 3–5k rows
  of daily data.
- Random forest: hundreds of trees, each on a bootstrap sample with random
  feature subsets; `n_estimators` up, `max_depth` modest.
- Boosting: small learning rate (0.01–0.1), early stopping on a validation
  loss, `subsample < 1` for stochasticity.
- Always report **feature importance** — trees give a transparency
  governance auditors and discretionary traders can actually use.

## When to prefer which
- Linear regression: baseline, interpretable, fails on interactions.
- SVR: nonlinear boundary, good on small clean feature sets.
- Single tree: fast, transparent, moderate accuracy.
- Random forest: the default robust choice for noisy financial data.
- XGBoost: highest ceiling, highest overfitting risk — reserve for larger
  datasets with careful validation (the ch16 three-way split).

## Bottom line
Ensembles are the strongest practical non-deep learners in the book's stack
(linear → SVM → trees/ensembles → DNN/RNN). The knowledge base's
`knowledge/halls-moore.../ch18-tree-based-methods.md` covers the theory;
this chapter is the scikit-learn/XGBoost application inside the standard
feature→fit→sign-trade→backtest skeleton.
