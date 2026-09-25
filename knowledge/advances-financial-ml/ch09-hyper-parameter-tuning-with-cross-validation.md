# Ch09 — Hyper-Parameter Tuning with Cross-Validation

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 9.

## Purpose
Applies purged k-fold CV (ch7) to hyper-parameter tuning, so the model
selection process itself doesn't overfit to leaked information, and
discusses grid vs. randomized search and scoring choices.

## Why tune with purged CV
- Hyper-parameter tuning is essential (mistuned → overfit → live
  disappointment), but tuning via standard CV inherits ch7's leakage
  problem. Pass the `PurgedKFold` class as the CV generator to
  `GridSearchCV`/`RandomizedSearchCV` so every fitted configuration is
  evaluated on leakage-free folds.
- `clfHyperFit` pattern: purged GridSearchCV + `fit_params` carrying
  `sample_weight` (ch4 uniqueness weights) + optional bagging of the
  tuned estimator.

## Grid vs. randomized search
- **Grid search**: exhaustive over a parameter grid; reasonable first
  approach when the parameter space is small.
- **Randomized search**: sample each parameter from a distribution
  (Bergstra et al.). Two benefits: (1) fixed computational budget
  regardless of dimensionality; (2) irrelevant parameters don't waste
  search time (unlike grid, which is exponential in them). Preferred
  for high-dimensional spaces.

## Scoring choice matters
- For **meta-labeling** problems (rare positives), use `scoring='f1'`:
  a classifier that predicts all-negative achieves high accuracy and
  zero recall — F1 exposes that inflation.
- For standard labeling, `accuracy`/`neg_log_loss` are fine (equally
  interested in both classes); note accuracy is invariant to relabeling
  while F1 is not.

## sklearn friction
- `Pipeline.fit` doesn't accept `sample_weight` directly — use
  `fit_params`; the author ships an enhanced `MyPipeline` subclass
  that forwards it (a reported sklearn bug/limitation).
- Same for other sklearn CV utilities: verify they accept custom CV
  generators and sample weights before trusting their outputs.

## Key takeaways
- Tune hyper-parameters only under purged CV — otherwise you're
  selecting parameters that exploit leakage.
- Use randomized search for anything beyond a small grid; set a budget
  and don't exceed it (more trials = more multiple testing).
- Choose the scoring function to match the business objective: F1 for
  meta-labeling/size decisions, accuracy/log-loss for symmetric
  side-prediction problems.
