# Chapter 13 — Statistics

## Core idea
Statistical methods for finance: **normality tests** (returns aren't
Gaussian), **portfolio optimization** (Markowitz), **Bayesian statistics**
(parameter distributions, not point estimates), and a first look at
**machine learning** classification.

## Normality tests
- Portfolio theory, CAPM, EMH, and Black-Scholes all assume normal returns.
- Test GBM-simulated and real returns:
  - **Jarque-Bera** (skewness + kurtosis) — `scs.jarque_bera`.
  - **Shapiro-Wilk** — powerful normality test.
  - **QQ plots** vs the normal.
- Real financial returns show **fat tails and negative skew** — normality is
  rejected; this motivates simulation-based risk (ch12) and ML.

## Portfolio optimization (Markowitz / MPT)
- With normal returns, optimal allocation depends only on mean, variance,
  covariance: maximize Sharpe
  `(w'mu - rf) / sqrt(w'Sigma w)` subject to `sum(w)=1`.
- scipy `minimize` with constraints; visualize the efficient frontier.
- The mean-variance approach is the classic application of ch11's convex
  optimization.

## Bayesian statistics
- Treat parameters as random: prior + data → posterior.
- Linear regression with **distributions for coefficients** instead of point
  estimates — uncertainty quantification.
- Implemented via sampling (e.g., PyMC-style) or conjugate priors for simple
  cases; the book demonstrates Bayesian updating of a normal mean.
- Cross-ref: `skills/bayesian-updating` in the knowledge base.

## Machine learning (classification preview)
- Supervised classification on features to predict direction (up/down).
- Train/test split, features like lagged returns, accuracy and confusion
  metrics — the setup that ch15's strategy chapter operationalizes fully.

## Pitfalls
- Testing many portfolios in-sample → overfit; use out-of-sample validation.
- Normality tests on small samples lack power.
- Bayesian posterior depends on the prior — report and justify it.

## Working checks
- Always pair a normality test with a QQ plot — the statistic alone hides
  where the tails deviate (usually heavier left tail in returns).
- For MPT, confirm `sum(w) == 1` and, if long-only, `w >= 0`; sensitivity to
  the mean estimate is huge, so report the frontier, not one point.
- Bayesian results should be shown as posterior distributions (credible
  intervals), not just posterior means — the width encodes uncertainty.
- ML baselines: compare classification accuracy against always-predicting-
  the-majority-class; directional accuracy near 50% means no edge.

## Bottom line
The statistical foundation: normality testing (usually rejected), MPT
optimization, Bayesian inference, and the ML teaser. Cross-refs:
`skills/bayesian-updating`, `skills/risk-metrics`, and
`knowledge/python-finance-algo-trading-2ed/ch03` (portfolio optimization).
