# Ch06 — Ensemble Methods

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 6.

## Purpose
Explains what makes bagging and boosting work, the bias-variance-noise
decomposition, and why in finance bagging is generally preferable to
boosting.

## Three sources of error
- **Bias**: unrealistic assumptions → underfitting.
- **Variance**: sensitivity to small training-set changes → overfitting
  (modeling noise as signal).
- **Noise**: irreducible error (measurement, unpredictable variation).
- MSE = bias² + variance + noise; ensembles attack bias and/or
  variance.

## Bagging (bootstrap aggregation)
- Sample N training sets *with replacement*, fit N independent
  estimators in parallel, average (regression) or majority-vote
  (classification) the predictions.
- Reduces **variance**: the bagged variance is
  φ̄² = (1/N)·σ̄² + (N−1)/N·ρ̄·σ̄² — effective only when the
  average correlation between estimators ρ̄ is low. Low correlation is
  the whole point: more diverse learners → lower bagged variance.
- Implication: on financial data, use **sequential bootstrap** (ch4)
  and `max_samples = average uniqueness` so redundant overlapping
  observations aren't oversampled — maximizing diversity.
- Known sklearn bug: out-of-bag accuracy breaks when labels aren't
  sequentially ordered integers (workaround: rename labels).
- Bagging also enables **scalability**: chunk the data into
  bootstrapped samples, fit an SVM per chunk in parallel — handles
  datasets too large for one SVM fit.

## Boosting (e.g., AdaBoost)
- Fit estimators *sequentially*; re-weight observations so
  misclassified ones get more weight each round; discard weak
  estimators below the accuracy threshold; final prediction is a
  *weighted* average weighted by each estimator's accuracy.
- Reduces **both variance and bias** — but correcting bias comes at the
  cost of more overfitting risk.

## Bagging vs. boosting in finance
- Boosting addresses underfitting; bagging addresses overfitting.
- Finance's low signal-to-noise ratio makes overfitting the dominant
  risk → **bagging is generally preferable to boosting** in finance.
- Bagging parallelizes; boosting is inherently sequential.

## Key takeaways
- Ensemble value depends on member diversity (low ρ̄) — with correlated
  members, ensembles do little.
- On financial data, combine bagging with uniqueness-aware sampling;
  prefer bagging over boosting unless underfitting is clearly the
  problem.
- Use ensembles for scalability: many small models in parallel beat one
  giant model.
