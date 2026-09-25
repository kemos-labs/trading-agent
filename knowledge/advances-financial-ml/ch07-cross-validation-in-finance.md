# Ch07 — Cross-Validation in Finance

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 7.

## Purpose
Shows why standard k-fold CV fails on financial data (non-IID
observations → leakage) and introduces **purged k-fold CV with
embargo** as the fix.

## Why k-fold CV fails in finance
- Standard CV assumes IID draws. Financial labels are formed on
  *overlapping* intervals (ch3/ch4): when a training observation and a
  test observation share overlapping label spans, information leaks —
  the model is effectively tested on data it saw during training.
- Two failure causes: (1) leakage from overlapping/non-IID data;
  (2) multiple testing and selection bias (test set reused during
  development; covered in ch11–13).
- With serially correlated features X_t ≈ X_{t+1} and overlapping
  labels Y_t ≈ Y_{t+1}, leakage inflates performance especially with
  *irrelevant* features — false discoveries.
- Defensive measures: purge overlaps; avoid overfitting the classifier
  (early stopping, bagging with `max_samples = average uniqueness`,
  sequential bootstrap).

## The solution: purging
- **Purging**: remove from the *training* set any observation i whose
  label span overlaps the testing set — if Y_i is a function of
  information used to determine a test label Y_j, drop i from training.
- Three sufficient overlap conditions on label spans [t_i0, t_i1] vs
  [t_j0, t_j1]; implement by comparing label `t1` objects across sets.
- Effect: after purging, performance improves with more splits k only
  because the model recalibrates more often — beyond k* it flatlines,
  confirming the backtest isn't profiting from leaks.

## The solution: embargo
- **Embargo**: additionally drop training observations *after* every
  test set for a brief period (e.g., 1% of observations). Needed when
  serial correlation persists beyond label spans (e.g., features
  depending on a trailing window). Purging alone can't always prevent
  leakage from overlapping features.
- Practical note: sklearn's CV classes have quirks/bugs for financial
  data — implement `PurgedKFold` yourself.

## Key takeaways
- Never use stock k-fold CV on labeled financial series — overlapping
  labels guarantee leakage and inflated scores.
- Always purge by label overlap and embargo after each test block;
  then tune hyperparameters via the purged CV generator.
- A sign of a clean CV: performance gains from more folds stop past
  some k*, rather than rising monotonically from leakage.
