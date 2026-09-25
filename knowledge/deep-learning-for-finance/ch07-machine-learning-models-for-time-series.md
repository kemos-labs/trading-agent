# Ch07 — Machine Learning Models for Time Series

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 7.

## Purpose
Introduces classic ML models applied to financial time series —
linear regression, k-nearest neighbors, random forests, support vector
regression, and boosting — plus the accuracy metrics used to judge
them, and the train/test discipline required to trust results.

## The setup
- Features: lagged returns, indicators, and other derived quantities;
  target: future direction (classification) or future return
  (regression).
- **Train/test split is non-negotiable**: fit only on training data,
  evaluate on held-out data. For time series use sequential splits
  (no shuffling — shuffling leaks the future into the past) or
  walk-forward validation.

## Models
- **Linear regression / logistic regression**: baseline; assumes
  linear relationships and no multicollinearity. Simple, interpretable,
  rarely the winner but always the reference point.
- **k-Nearest Neighbors (kNN)**: classifies/predicts by averaging the
  k most similar historical observations (similarity = distance in
  feature space). No training phase, but sensitive to feature scaling
  and curse of dimensionality.
- **Random Forest**: ensemble of decision trees trained on bootstrap
  samples with random feature subsets; averages predictions to cut
  variance. Robust to nonlinearity, gives feature importances, hard to
  overfit badly — a strong default.
- **Support Vector Regression (SVR)**: fits a tube of width ε around
  the data and minimizes error outside it; good in high dimensions,
  sensitive to kernel choice and scaling.
- **Boosting (e.g., AdaBoost, XGBoost)**: trains weak learners
  sequentially, each focusing on the previous ones' errors. Powerful,
  but the most overfit-prone — use strong regularization and early
  stopping.

## Accuracy metrics
- **Classification**: accuracy, precision, recall, F1, and the
  confusion matrix. For rare events (most trading signals), accuracy is
  misleading — precision/recall matter more.
- **Regression**: MSE (penalizes large errors), RMSE, MAE, and R²
  (share of variance explained; can be negative out-of-sample).
- For direction forecasting, also measure **hit rate** (fraction of
  correct directions) — but a high hit rate with skewed payoff sizes
  can still lose money.

## Key takeaways
- Start with a linear baseline, then random forest, then boosting —
  match model complexity to data size; small datasets punish
  over-flexible models.
- Time-series evaluation must respect time order: no shuffling, no
  leakage of future information into features (e.g., normalizing with
  full-sample statistics).
- Accuracy alone never validates a strategy — the metric must align
  with the trading objective (direction, magnitude, cost).
