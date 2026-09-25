# Monte Carlo Option Pricing

## name
Monte Carlo valuation of derivatives with variance reduction: European
options by discounted payoff expectation, American options by
Least-Squares Monte Carlo (Longstaff-Schwartz), and the three standard
underlying processes (GBM, jump diffusion, square-root diffusion).

## description
Price European and American options by simulating the underlying under the
risk-neutral measure and averaging discounted payoffs. Includes the
vectorized GBM/jump/CIR path generators, antithetic variates and moment
matching (variance reduction), and the LSM backward-induction regression
for American early exercise. Use this when closed forms (Black-Scholes,
binomial tree) are unavailable or the payoff is path-dependent, multi-
asset, or needs an exercise decision — and when simulation noise must be
controlled.

## when to use it
- Pricing European options with arbitrary (possibly exotic) payoffs that
  have no closed form.
- Pricing American/Bermudan options where early exercise matters — the
  binomial tree works, but LSM handles high dimensions and path-dependent
  state naturally.
- Multi-asset options needing correlated simulations (pair with
  `skills/correlated-scenario-simulation` for the Cholesky step).
- Computing Greeks (delta, vega) by finite differences of re-priced values.
- Valuing whole books / computing VaR of portfolios (Hilpisch's DX library,
  ch18–21).
- Cross-checking Black-Scholes or binomial-tree prices on European options
  (all three should agree within MC noise).

## the method

### 1. Simulate the underlying (vectorized, all paths at once)
Standard log-Euler schemes on an `(M+1, I)` grid (M steps, I paths). The
`-0.5*sigma**2` drift term is essential.

```python
import numpy as np

def sim_gbm(S0, r, sigma, T, M, I, seed=1000):
    np.random.seed(seed)
    dt = T / M
    z = np.random.standard_normal((M, I))
    # S[t+1] = S[t] * exp((r - 0.5*sigma^2)*dt + sigma*sqrt(dt)*z)
    steps = np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z)
    S = np.empty((M + 1, I)); S[0] = S0
    S[1:] = S0 * np.cumprod(steps, axis=0)
    return S

def sim_jump_diffusion(S0, r, sigma, lamb, mu, delta, T, M, I, seed=1000):
    # GBM + Poisson jump process: dS/S = (r - lamb*(exp(mu+0.5 delta^2)-1)) dt
    #                                + sigma dW + (exp(J)-1) dN
    np.random.seed(seed)
    dt = T / M
    z = np.random.standard_normal((M, I))
    jumps = np.random.poisson(lamb * dt, (M, I))
    jump_amp = np.exp(np.random.normal(mu, delta, (M, I))) - 1.0
    drift = (r - 0.5 * sigma**2 - lamb * (np.exp(mu + 0.5 * delta**2) - 1)) * dt
    steps = np.exp(drift + sigma * np.sqrt(dt) * z + np.log1p(jump_amp * jumps))
    S = np.empty((M + 1, I)); S[0] = S0
    S[1:] = S0 * np.cumprod(steps, axis=0)
    return S

def sim_sqrt_diffusion(r0, kappa, theta, sigma, T, M, I, seed=1000):
    # CIR: dr = kappa*(theta - r) dt + sigma*sqrt(r) dW  (mean-reverting, positive)
    np.random.seed(seed)
    dt = T / M
    r = np.empty((M + 1, I)); r[0] = r0
    for t in range(M):
        r[t+1] = np.maximum(
            r[t] + kappa * (theta - r[t]) * dt
            + sigma * np.sqrt(np.maximum(r[t], 0)) * np.sqrt(dt)
            * np.random.standard_normal(I), 0.0)
    return r
```

### 2. Variance reduction
```python
def sn_random_numbers(shape, antithetic=True, moment_matching=True):
    ran = np.random.standard_normal(shape)
    if antithetic:                                  # pair z with -z
        ran = np.concatenate((ran, -ran), axis=2)
    if moment_matching:                             # force mean 0, std 1
        ran = ran - ran.mean()
        ran = ran / ran.std()
    return ran
```
- **Antithetic variates**: mirrored draws halve the variance of the mean
  estimate (same precision with ~half the paths).
- **Moment matching**: rescale draws to exact sample mean 0 and std 1,
  removing first-two-moment sampling noise.
- Use a fixed seed so results are reproducible, and always report path
  count + seed.

### 3. European valuation
```python
def mc_european(S, K, r, T, payoff='call'):
    ST = S[-1]
    if payoff == 'call': pay = np.maximum(ST - K, 0)
    else:                pay = np.maximum(K - ST, 0)
    return np.exp(-r * T) * pay.mean()
```

### 4. American valuation — Least-Squares Monte Carlo (LSM)
Work backward from maturity. At each step, estimate the continuation value
by **regressing discounted future option values on basis functions of the
current underlying**, using only in-the-money paths:

```python
def ls_american(S, K, r, T, payoff='put'):
    M, I = S.shape[0] - 1, S.shape[1]
    dt = T / M
    if payoff == 'put': V = np.maximum(K - S[-1], 0)
    else:               V = np.maximum(S[-1] - K, 0)
    for t in range(M - 1, 0, -1):
        itm = (S[t] > K) if payoff == 'call' else (S[t] < K)
        if itm.sum() < 2:                       # too few paths to regress
            V = np.exp(-r * dt) * V
            continue
        X = S[t][itm]
        Y = np.exp(-r * dt) * V[itm]
        # polynomial basis fit (degree 2-3 typically)
        A = np.vstack([X**0, X, X**2]).T
        beta, *_ = np.linalg.lstsq(A, Y, rcond=None)
        cont = A @ beta                          # fitted continuation value
        exer = np.maximum(K - X, 0) if payoff == 'put' else np.maximum(X - K, 0)
        V[itm] = np.where(exer > cont, exer, Y)
        V[~itm] = np.exp(-r * dt) * V[~itm]
    return np.exp(-r * dt) * V.mean()
```

### 5. Greeks (finite differences)
Re-price with bumped inputs using the same random numbers (common random
numbers reduce noise):
```python
delta = (V(S0 + h) - V(S0 - h)) / (2 * h)   # h ~ 0.01 * S0
vega  = (V(sigma + h) - V(sigma - h)) / (2 * h)
```

## known pitfalls
- **Missing the `-0.5*sigma**2` term** biases GBM prices — always use the
  exact log-Euler drift.
- **MC noise**: error ~ 1/sqrt(N); use variance reduction + common random
  numbers before increasing N blindly.
- **LSM regression**: use only in-the-money paths and low-degree polynomial
  basis; too few paths (< a few hundred) makes the regression unstable.
- **CIR going negative** in Euler discretization breaks `sqrt(r)` — clamp
  with `np.maximum(r, 0)` or use an exact scheme; also respect the Feller
  condition (`2*kappa*theta > sigma**2`) for positivity in expectation.
- **Discounted vs undiscounted paths**: discount the payoff (or the
  continuation values) correctly — mixing undiscounted values breaks LSM.
- Seeding: `np.random.seed` is process-global — reset it per function or
  pass a generator to keep runs reproducible and independent.

## source
Hilpisch, *Python for Finance*, 2nd ed., ch12 (stochastics), ch18
(simulation of financial models), ch19 (derivatives valuation: European MC
+ LSM), ch20 (portfolios), ch21 (market-based calibration).
Knowledge notes: `knowledge/python-for-finance/ch12` through `ch21`.
Complementary: `skills/binomial-tree-pricing` (discrete alternative),
`skills/correlated-scenario-simulation` (multi-asset Cholesky),
`skills/risk-metrics` (VaR from simulated values).
