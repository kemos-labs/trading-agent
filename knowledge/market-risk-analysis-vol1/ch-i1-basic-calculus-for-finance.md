# Chapter I.1 — Basic Calculus for Finance

## Core idea
The functions and calculus tools used across finance: exponential/log
functions, differentiation and integration, functions of several variables,
Taylor expansions, and the return mathematics of portfolios. Derivatives
are "sensitivities" in finance (duration, convexity, delta, gamma).

## Functions in finance
- **Exponential**: discounting forward prices to present value; the futures
  price is exponential in the interest rate.
- **Natural log**: inverse of exp; computes continuously compounded returns.
- **Nonlinear functions**: bond price vs yield (convex); option price vs
  underlying and volatility.
- **Bond basics**: periodic coupons, redemption at par; yield-to-maturity =
  the discount rate making NPV of cash flows equal the price.

## Differentiation
- **Sensitivities**: first derivative = modified duration (bond price yield
  sensitivity, % of price); second derivative = convexity.
- **Options**: hedge ratios come from first/second partial derivatives of
  the option price; market makers hedge to make a risk-free portfolio.
- **No-arbitrage**: all risk-free investments earn the same (risk-free)
  return; option pricing derives a PDE satisfied by the price, solved
  analytically in special cases (Black-Scholes-Merton).

## Integration
- Inverse of differentiation; connects probability distributions (CDF) with
  density functions (PDF): differentiating the distribution gives the
  density, integrating the density gives the distribution.

## Functions of several variables
- Partial derivatives; stationary points; constrained optimization (e.g.,
  no short sales, ≥30% US equities); total derivatives.
- The investor's problem: choose weights to optimize an objective subject to
  constraints — solved with differentiation.

## Taylor expansion
- Approximate a nonlinear differentiable function with its first few
  derivatives: duration–convexity for bonds; delta–gamma for options
  portfolios; simplifies BSM adjustments and SDE derivations.

## Returns and P&L
- **Portfolio weights**: proportions of capital; positive = long, negative =
  short.
- Constant-holdings vs continuously rebalanced portfolios; under constant
  weights the portfolio return is the weighted sum of asset returns — the
  foundation of portfolio theory.
- **Discrete vs continuous returns**: percentage vs log returns; GBM in
  continuous time; discrete/continuous compounding; period log returns.
- **Sources of returns**: price change, dividends, interest, FX.

## Risk
- Risk = uncertainty about an expected value; risk-averse investors maximize
  return for minimum risk.
- Portfolio variance is a **quadratic function of weights** — minimizing it
  (subject to constraints) gives the minimum-variance portfolio.

## Bottom line
The calculus toolkit: sensitivities, Taylor approximations, constrained
optimization, and return definitions. This is the mathematical foundation
for everything in the volume — linear algebra (I.2), statistics (I.3),
regression (I.4), numerics (I.5), and portfolio theory (I.6).
