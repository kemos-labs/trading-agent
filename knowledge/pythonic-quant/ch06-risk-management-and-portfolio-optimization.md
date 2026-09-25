# Chapter 6 — Risk Management and Portfolio Optimization

## Core idea
The twin pillars of quantitative finance: measuring risk (types, VaR/CVaR,
Monte Carlo) and constructing optimal portfolios (Markowitz MPT, the
Efficient Frontier) — with Python's NumPy, pandas, SciPy, and cvxpy.

## Types of financial risk
- **Market risk** (systematic): losses from market-wide factors — rates,
  FX, geopolitics; measured with VaR/CVaR, Monte Carlo simulation.
- **Credit risk**: counterparty default; modeled with ML default-probability
  prediction.
- **Liquidity risk**: inability to sell without moving price; analyzed via
  market depth, volumes, bid-ask spreads.
- **Operational risk**: failed processes/systems, cyberattacks, fraud;
  anomaly detection in transactions, neural nets on failure patterns.
- **Systemic risk**: modeled via network analysis (NetworkX) — how
  disruptions propagate through interconnected institutions.

## Risk measurement
- **VaR / CVaR**: quantile-based loss forecasts from historical/simulated
  data.
- **Monte Carlo simulation**: simulate market movements with volatility and
  correlations to map the distribution of portfolio outcomes.
- Cross-ref: `skills/risk-metrics`, `skills/parametric-var`,
  `skills/monte-carlo-option-pricing`.

## Portfolio optimization (Markowitz MPT)
- Goal: maximum return for a given risk — the **Efficient Frontier**.
- Tooling: scipy `minimize` for constrained optimization; **cvxpy** for
  convex optimization.
- Define portfolio return and risk as functions of weights `w`, solve for
  the frontier, visualize with Matplotlib/Seaborn.

## Machine learning in risk
- Predictive risk modeling: default prediction, market-movement forecasting
  with scikit-learn/TensorFlow — proactive rather than reactive risk.
- **Dynamic portfolio optimization**: re-optimize as market conditions and
  alternative data arrive.

## Pitfalls
- Optimization is hypersensitive to input estimates (mean/covariance) —
  small errors, wild weights.
- VaR is not sub-additive; pair with CVaR.
- Overfitting an optimizer to historical data — validate out-of-sample.

## The optimization setup (sketch)
- Expected portfolio return: `mu_p = w'·mu`; variance:
  `sig_p^2 = w'·Sigma·w`, with `sum(w) = 1` (and `w >= 0` long-only).
- Maximize Sharpe `(mu_p - rf)/sig_p` or minimize variance for a target
  return — both convex problems for `cvxpy` or `scipy.optimize.minimize`.
- The frontier is traced by sweeping the target return and recording each
  optimal (risk, return) pair.

## Bottom line
Risk taxonomy + MPT in one chapter. It consolidates the knowledge base's
risk toolkit: `skills/risk-metrics` (VaR/cVaR/drawdown), `parametric-var`,
and the MPT material in `knowledge/python-for-finance/ch13`.
