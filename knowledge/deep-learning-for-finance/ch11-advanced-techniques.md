# Ch11 — Advanced Techniques

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 11.

## Purpose
Covers the advanced tools that take a model from prototype to
deployable strategy: genetic algorithms for feature selection and
hyperparameter search, systematic hyperparameter optimization, and
backtesting with walk-forward validation.

## Genetic algorithms
- Inspired by evolution: a **population** of candidate solutions
  (e.g., sets of features, network architectures, indicator
  parameters), each scored by a **fitness function**.
- **Selection** keeps the fittest; **crossover** combines pairs of
  solutions; **mutation** randomly perturbs them. Repeat over
  generations — the population converges toward good solutions.
- Uses in trading: selecting which of dozens of indicators to feed a
  model, optimizing indicator parameters (e.g., SMA/RSI windows),
  and architecture search. Fitness must be out-of-sample performance
  (e.g., Sharpe) — never in-sample.
- Pitfalls: fitness is noisy (financial data), so the "best" solution
  is often the luckiest; early stopping and multiple seeds help.

## Hyperparameter optimization
- **Grid search**: try all combinations of a few discrete parameter
  values — exhaustive but explodes combinatorially.
- **Random search**: sample parameters from distributions; often finds
  good settings far more cheaply than grid search because most
  hyperparameters matter little.
- **Bayesian optimization**: builds a probabilistic model of the
  objective (e.g., Gaussian process) and proposes the next point to
  maximize expected improvement — sample-efficient for expensive
  evaluations.
- **Validation loop**: each configuration is scored via
  cross-validation or walk-forward; the outer evaluation uses a final
  untouched test set so the search itself doesn't leak into results.

## Backtesting with walk-forward validation
- **Walk-forward**: repeatedly train on a rolling window and test on
  the next out-of-sample block, simulating how the strategy would have
  been updated through time. More realistic than one static
  train/test split.
- **Realism checklist**: include transaction costs, slippage, and
  market impact; avoid look-ahead bias (using data not available at
  decision time); account for data snooping (many trials → some will
  look good by chance — the multiple-testing problem).
- Reported performance should be the *walk-forward* out-of-sample
  equity curve, not the best in-sample configuration.

## Key takeaways
- Optimization searches find good configurations only when the scoring
  metric is out-of-sample and cost-adjusted; otherwise they overfit to
  noise.
- Prefer random search or Bayesian optimization over grid search;
  cap the number of trials and beware multiple-testing bias.
- Walk-forward backtesting is the closest honest approximation of live
  trading available before going live — build the cost and leakage
  checks into it from the start.
