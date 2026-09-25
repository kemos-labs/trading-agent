# Chapter I.6 — Introduction to Portfolio Theory

## Core idea
Optimal capital allocation: utility theory (how investors express risk
preferences), Markowitz portfolio selection (diversification, minimum
variance, the efficient frontier), the CAPM, and risk-adjusted performance
measures (Sharpe, Sortino, omega, kappa indices).

## Utility theory (Von Neumann-Morgenstern)
- A utility function U(W) assigns a number to wealth outcomes; investors
  rank allocations by expected utility:
  `E[U(P)] = Σ p_i·U(W_i)`.
- **Axioms**: transitivity, independence, certainty equivalence, stochastic
  dominance — sufficient to prove the existence of a utility function.
- **Risk attitude** from the first/second derivatives: concave U = risk
  averse; convex = risk loving; linear = risk neutral.
- **Coefficients**: absolute and relative risk aversion; risk tolerance =
  reciprocal (interpreted as the max bet on a double-or-half gamble).
- **Exponential utility** is tractable: maximizing expected utility is
  equivalent to a mean–variance criterion; extends to higher moments
  (aversion to negative skewness, positive excess kurtosis).
- How to determine an investor's risk tolerance in practice (I.6.2.3).

## Markowitz portfolio selection (1959)
- Diversification: combine risky assets so that portfolio variance
  `w'Σw` falls below the weighted average of individual variances.
- **Minimum variance portfolio**: minimize w'Σw subject to sum(w)=1 (and
  possibly constraints: no short sales, caps like "≤10% US equities").
- **Efficient frontier**: the trade-off between risk and return — highest
  expected return for each risk level; constrained frontiers with many
  constraints.
- Solved via the calculus of I.1 (differentiate the quadratic variance
  function) with Lagrange multipliers/constraints.

## CAPM (Treynor, Sharpe, Lintner)
- The **market portfolio** all rational investors hold; the **capital
  market line**.
- **CAPM**: expected return of an asset = risk-free rate + beta × market
  risk premium; beta = systematic risk.
- Tests of the CAPM; extensions (multifactor models).

## Risk-adjusted performance measures
- **Sharpe ratio**: excess return per unit of total volatility.
- **Sortino ratio**: second-order kappa index with threshold = risk-free
  rate — downside-only risk.
- **Omega statistic** (Keating-Shadwick): ratio of expected return above a
  threshold to expected return below it.
- **Kappa indices**: based on **lower partial moments**
  `LPM_n(τ) = E[max(0, τ - X)^n]`; K1 = omega − 1; higher-order kappas
  are more sensitive to skewness/kurtosis and suit more risk-averse
  investors.
- Caveat: risk-adjusted measures *order* investments but are not preference
  orderings — only a utility function says which is best for a given
  investor.

## Bottom line
The portfolio-theory capstone: utility → Markowitz allocation → CAPM →
performance measures. It operationalizes I.1's calculus and I.2's matrix
algebra. Cross-refs: `skills/portfolio-optimization`, `skills/risk-metrics`
(Sharpe/Sortino/VaR), and the MPT material in
`knowledge/python-for-finance/ch13`.
