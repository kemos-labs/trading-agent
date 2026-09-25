# Chapter 18 — Simulation of Financial Models

## Core idea
Building the simulation component of the DX library: random number
generation with **variance reduction**, a generic simulation class, and
three workhorse stochastic processes — **GBM**, **jump diffusion**, and
**square-root diffusion** (CIR).

## Random number generation with variance reduction
```python
def sn_random_numbers(shape, antithetic=True, moment_matching=True):
    ran = np.random.standard_normal(shape)
    if antithetic:                       # pair z with -z
        ran = np.concatenate((ran, -ran), axis=2)
    if moment_matching:                  # exact mean 0, std 1
        ran = ran - ran.mean()
        ran = ran / ran.std()
    return ran
```
- **Antithetic variates**: halve variance by using mirrored draws — reduces
  the number of paths needed for the same precision.
- **Moment matching**: force sample mean=0, std=1 — removes sampling noise in
  the first two moments.

## Generic simulation class
A base class holds common structure (paths, date grid, discount curve) from
which specific process classes inherit — the OOP pattern from ch6.

## The three processes
- **Geometric Brownian Motion** (Black-Scholes-Merton):
  ```
  S_t = S_0 * exp((r - 0.5*sigma^2)*t + sigma*W_t)
  ```
  Log-normal prices, normal log-returns. Still the benchmark, despite
  empirical evidence against it.
- **Jump diffusion** (Merton 1976): GBM + log-normal jumps via Poisson
  arrivals — explains why short-term OTM options appear priced for larger
  moves than GBM implies.
- **Square-root diffusion** (Cox-Ingersoll-Ross): mean-reverting and
  strictly positive —
  ```
  dr = kappa*(theta - r)*dt + sigma*sqrt(r)*dW
  ```
  Used for interest rates and volatility.

## Why three processes
Different instruments need different dynamics: GBM for equities (baseline),
jump diffusion when tail jumps matter, CIR for mean-reverting positive
quantities (rates, vol).

## Pitfalls
- GBM's `-0.5*sigma^2` drift correction is essential in the Euler step —
  omitting it biases simulated prices.
- Jump diffusion needs the Poisson intensity calibration; rare large jumps
  are hard to estimate.
- CIR can go negative in naive Euler discretization when the Feller
  condition is violated — use exact/reflecting schemes.

## Bottom line
The simulation layer of DX: variance-reduced normals + three process classes.
These feed every valuation in ch19–21. Cross-refs:
`skills/correlated-scenario-simulation` (Cholesky for multi-asset),
`knowledge/python-for-finance/ch12` (stochastics primer).
