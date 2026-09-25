# Chapter 19 — Derivatives Valuation

## Core idea
Monte Carlo valuation classes for European and American exercise, built on
the simulation classes (ch18). American options are handled with the
**Least-Squares Monte Carlo (LSM)** algorithm — the benchmark method.

## Generic valuation class
`valuation_class(name, underlying, mar_env, payoff_func)`:
- `payoff_func` is a **Python string** evaluated on the simulated grid, e.g.
  `'np.maximum(maturity_value - 100, 0)'` — payoffs are code, not hardcoded.
- Methods: `present_value()` (price), `delta()` and `vega()` (numerical
  Greeks via finite differences — bump the underlying/vol and re-price).

## European exercise
- Simulate `S_T` paths under Q; value = `exp(-r*T) * mean(payoff(S_T))`.
- Closed-form checks: GBM European call vs Black-Scholes formula — used to
  validate the MC implementation.
- Greeks numerically: `delta = (V(S0+h) - V(S0-h)) / (2h)`.

## American exercise — LSM (Longstaff-Schwartz)
- American options can be exercised any time; value = max(payoff now,
  continuation value).
- **LSM idea**: regress continuation value on basis functions of the current
  underlying (polynomials) using *in-the-money* paths — the fitted regression
  is the conditional expectation `E[V(t+1) | S(t)]`.
- Backward induction on the simulated grid:
  1. Terminal payoff from the final time step.
  2. At each earlier step, regress discounted future values on `S(t)`.
  3. Exercise where `payoff_now > fitted_continuation`, else hold.
- Produces both the price and (via the exercise rule) an approximate optimal
  stopping strategy.

## Greeks for risk management
- delta/vega from the valuation classes feed hedging and risk reporting —
  valuation and risk management share one codebase.

## Pitfalls
- LSM regression must use only in-the-money paths and a suitable basis
  (low-order polynomials) — wrong basis biases the price.
- MC converges slowly (~1/sqrt(N)); use variance reduction (ch18) and enough
  paths; compare to closed forms (BS) where available.
- Numerical Greeks need re-pricing; small bumps + MC noise → noisy Greeks;
  use common random numbers.

## Bottom line
The valuation engine: MC European pricing and LSM for American — with
payoffs-as-strings and numeric Greeks. This is the knowledge base's first
full MC-valuation treatment beyond the binomial tree
(`skills/binomial-tree-pricing`). Cross-refs:
`knowledge/stochastic-calculus-finance/ch20/ch25` (exotics, American
theory).
