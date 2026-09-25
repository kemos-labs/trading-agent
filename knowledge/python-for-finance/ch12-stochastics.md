# Chapter 12 — Stochastics

## Core idea
Randomness is the raw material of finance: simulation of random variables
and stochastic processes, valuation under risk-neutrality, and risk measures
computed by Monte Carlo. This chapter is the practical simulation primer.

## Random numbers
- `numpy.random` functions: `rand` (uniform [0,1)), `randn` (standard
  normal), `randint`, `choice` (sample from array), `sample`.
- Interval transform via broadcasting: `a + (b - a) * npr.rand(n)`.
- **Seed** (`npr.seed(100)`) for reproducibility.

## Simulation
- **Random variables**: draw many samples, inspect distributions
  (histograms, mean/std).
- **Stochastic processes**: simulate paths of, e.g., geometric Brownian
  motion (GBM):
  ```python
  # S_t = S_0 * exp((r - 0.5*sigma^2)*t + sigma*W_t)
  # Euler step: S[t+1] = S[t] * exp((r - 0.5*sigma^2)*dt + sigma*sqrt(dt)*z)
  ```
  Vectorize across paths: build an `(M+1, I)` array of paths in one shot.
- The book's `gen_paths(S0, r, sigma, T, M, I)` pattern: `M` time steps,
  `I` paths.

## Valuation by simulation
- **European exercise**: average the discounted payoffs:
  `V0 = exp(-r*T) * mean(max(S_T - K, 0))` over simulated paths.
- **American exercise**: needs optimal stopping — solved by the
  Least-Squares Monte Carlo algorithm (ch19).
- **Variance reduction** improves precision: antithetic variates (use `z`
  and `-z`), moment matching (subtract sample mean, divide by sample std —
  exact first two moments), control variates.

## Risk measures
- **Value-at-Risk (VaR)**: quantile of the simulated portfolio value
  distribution at confidence level `alpha`.
- **Credit VaR / CVA**: counterparty-risk measures requiring simulation of
  exposures and default.
- Simulation-based risk naturally captures fat tails and path dependence
  that analytic formulas miss.

## Pitfalls
- Few paths → noisy estimates; use variance reduction or more paths.
- Wrong discretization (e.g., missing the `-0.5*sigma^2` drift term in GBM)
  biases prices — always use the exact log-Euler scheme.
- Seeding is for reproducibility, not correctness — always report path
  counts and seeds.

## Bottom line
The simulation foundation: generate randomness, simulate GBM paths, price by
expectation, compute VaR — all vectorized in NumPy. This feeds ch18
(simulation classes) and ch19–21 (valuation). Cross-refs:
`skills/correlated-scenario-simulation`, `skills/risk-metrics`.
