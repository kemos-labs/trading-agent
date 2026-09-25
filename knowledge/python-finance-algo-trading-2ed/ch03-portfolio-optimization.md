# Chapter 3 — Portfolio Optimization

## Core idea
Before and alongside strategy development, the book introduces **portfolio
construction** as the second layer of the pipeline: once you have strategy
returns, decide *how much capital* to allocate to each. Two approaches are
covered: static (optimize once on the whole history) and dynamic
(re-optimize with a rolling window).

## Mean-variance optimization (Markowitz)
- Given a set of assets with expected returns `mu` and covariance matrix
  `Sigma`, find weights `w` that minimize variance for a target return, or
  maximize the Sharpe ratio.
- Objective (max Sharpe):
  ```
  maximize  w'·mu / sqrt(w'·Sigma·w)
  subject to sum(w) = 1,  w >= 0 (long-only) or unconstrained
  ```
- Implementation via scipy.optimize (e.g., `SLSQP` or `minimize` with
  constraints) or the closed-form tangency-portfolio weights.
- The **efficient frontier** is the set of portfolios that dominate all
  others in risk/return space.

## Sharpe / Sortino criteria
Used both to rank single strategies and to pick the "best" portfolio:
- **Sharpe ratio** = `(mean_return - rf) / std(returns)`, annualized by
  `sqrt(252)` for daily data.
- **Sortino ratio** = `(mean_return - rf) / downside_deviation`, where
  downside deviation uses only negative returns. Preferable when returns are
  asymmetric (the norm in trading strategies).

## Dynamic vs static
- **Static allocation**: compute optimal weights once; simple but fragile to
  regime changes and overfit to one period.
- **Dynamic allocation**: re-estimate `mu` and `Sigma` on a rolling window and
  rebalance periodically (e.g., monthly). More robust, more transaction costs.

## Pitfalls
- Mean-variance is hypersensitive to the input estimate of `mu`; small errors
  produce wild weight changes. The book's practical answer is to keep
  re-estimating and rebalancing (dynamic) rather than trusting one static
  solution.
- Daily-return covariance is noisy; use enough history and consider shrinkage.
- Fees on rebalancing can erase the diversification benefit — include
  transaction costs in the objective.

## Bottom line
Portfolio optimization is the *allocation layer* sitting on top of strategy
returns. The metrics defined here (Sharpe, Sortino) are the recurring
evaluation yardsticks for every strategy in the book. This complements the
Kelly-style sizing ideas in `skills/kelly-position-sizing` (allocation under
uncertainty) and `knowledge/python-algorithmic-trading/ch10`.
