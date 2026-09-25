# Portfolio Optimization (Mean-Variance)

## name
Mean-variance portfolio optimization (Markowitz): construct the efficient
frontier and optimal portfolios — max-Sharpe, min-variance, and target-return
solutions — with scipy/cvxpy, plus estimation and robustness guardrails.

## description
Solve the classic Markowitz problem: choose asset weights `w` to maximize
expected return for a given risk (or minimize risk for a target return),
using the expected-return vector `mu` and covariance matrix `Sigma`. Includes
the efficient frontier sweep, the max-Sharpe and global-min-variance
portfolios, long-only constraints, and the estimation-error caveats that make
naive mean-variance fragile in practice. Use this whenever capital must be
allocated across assets or strategies (pairing with Kelly-style sizing).

## when to use it
- Allocating capital across assets or across trading strategies (a strategy
  portfolio) to maximize risk-adjusted return.
- Drawing the efficient frontier to visualize the risk/return trade-off and
  choose a point by risk appetite.
- Risk budgeting: computing which assets drive portfolio variance (see
  risk contributions in `skills/risk-metrics`).
- Dynamic allocation: re-optimizing on a rolling window as `mu`/`Sigma`
  drift (the practical answer to estimation error).
- Benchmarking a portfolio against the frontier (is it efficient?).

## the method

### 1. Inputs
- `mu`: mean returns (annualized), shape (n,).
- `Sigma`: covariance matrix (annualized), shape (n, n).
- `rf`: risk-free rate for the Sharpe objective.
- Estimate from a long, stationary window; prefer shrinkage or factor models
  for `Sigma` when n is large relative to history.

### 2. Objectives
```python
import numpy as np
from scipy.optimize import minimize

def port_stats(w, mu, Sigma):
    ret = w @ mu
    vol = np.sqrt(w @ Sigma @ w)
    return ret, vol

# Max Sharpe (equivalently min variance at the frontier point)
def neg_sharpe(w, mu, Sigma, rf):
    ret, vol = port_stats(w, mu, Sigma)
    return -(ret - rf) / vol

# Global minimum variance
def min_variance(w, Sigma):
    return w @ Sigma @ w

n = len(mu)
long_only = True                # set False for long-short (negative weights)
cons = [{"type": "eq", "fun": lambda w: np.sum(w) - 1}]   # sum(w) = 1
bnds = [(0, 1)] * n if long_only else None                 # w >= 0 optional
res = minimize(neg_sharpe, np.ones(n)/n, args=(mu, Sigma, rf),
               method="SLSQP", bounds=bnds, constraints=cons)
w_sharpe = res.x
```

### 3. The efficient frontier sweep
1. Compute the global-min-variance portfolio (minimize variance).
2. Compute the max-return (max-Sharpe or corner) portfolio.
3. Sweep target returns between them; for each target, minimize variance
   subject to `w'mu = target` and `sum(w) = 1`.
4. Plot the (vol, return) pairs — the upper edge is the efficient frontier.

### 4. cvxpy (convex, cleaner for larger problems)
```python
import cvxpy as cp
w = cp.Variable(n)
risk = cp.quad_form(w, Sigma)
prob = cp.Problem(cp.Minimize(risk),
                  [cp.sum(w) == 1, w >= 0, mu @ w >= target_ret])
prob.solve()
```

## known pitfalls
- **Estimation error dominates**: mean-variance is hypersensitive to `mu` —
  tiny input errors produce wild weight swings. Mitigate with long windows,
  shrinkage, Black-Litterman-style priors, or dynamic re-optimization.
- **Frontier in-sample ≠ out-of-sample**: the optimized portfolio
  systematically disappoints OOS; validate on held-out data
  (`skills/walk-forward-validation`).
- **Long-only vs long-short**: constraints change the solution dramatically;
  state them explicitly.
- **Correlations drift** across regimes; fixed `Sigma` over-weights recently
  volatile assets. Re-estimate on rolling windows or regime-conditional
  matrices (`skills/hmm-regime-detection`).
- **Fees kill rebalancing**: high-turnover re-optimization erodes returns —
  include transaction costs or trade less often.
- Local optima: use SLSQP with multiple starts, or cvxpy (guaranteed global
  for convex objectives).

## source
Van Der Post, *Pythonic Quant* (Reactive Publishing), ch6 (risk management
and portfolio optimization); Hilpisch, *Python for Finance*, 2nd ed., ch13
(Markowitz MPT, efficient frontier) — knowledge notes
`knowledge/pythonic-quant/ch06-risk-management-and-portfolio-optimization.md`
and `knowledge/python-for-finance/ch13-statistics.md`.
Complementary: `skills/risk-metrics` (risk contributions, VaR/cVaR),
`skills/kelly-position-sizing` (growth-optimal sizing), `skills/parametric-var`.
