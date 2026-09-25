# Correlated Scenario Simulation (Cholesky)

## name
Generating correlated random paths with the Cholesky decomposition for
Monte Carlo and scenario analysis of multi-asset portfolios.

## description
A vectorized recipe for simulating realistic multi-asset price paths:
decompose a target covariance (or correlation) matrix with Cholesky,
mix independent standard normals through the lower-triangular factor,
and exponentiate to lognormal prices. This produces paths whose
cross-asset correlations and per-asset volatilities match the inputs —
the engine behind option-book scenario grids, portfolio stress tests,
and Monte Carlo pricing. Built on the insight in Taleb's Module A
(two-asset correlated random walk) and generalized to n assets.

## when to use it
- You need Monte Carlo paths for several correlated assets (options,
  portfolios, factor models) rather than independent ones.
- You want a scenario grid for an option book: perturb spot (and vol)
  coherently across assets, respecting their correlation structure.
- You are stress-testing a portfolio and want realistic joint moves
  (correlation breakdown in crises means: re-run with higher ρ).
- You need to sanity-check whether a covariance matrix is valid
  (positive definite) before using it in optimization or simulation.

## the method
Given volatilities σᵢ and a correlation matrix R (or a covariance matrix Σ):
1. **Build Σ**: Σ[i][j] = σᵢ·σⱼ·R[i][j] (covariance = vol × vol × corr).
   Check it is positive definite (all eigenvalues > 0) — otherwise the
   inputs are not arbitrage-free.
2. **Cholesky factorize**: find lower-triangular A with A·Aᵀ = Σ.
   For n = 2: a₁₁ = √Σ₁₁; a₂₁ = Σ₂₁/a₁₁; a₂₂ = √(Σ₂₂ − a₂₁²).
   In numpy: `A = np.linalg.cholesky(Σ)`.
3. **Generate independent standard normals** Z (shape steps × n):
   `Z = rng.standard_normal((n_steps, n_assets))`.
4. **Mix**: correlated innovations U = Z @ A.T — each column now has
   the right variance and the right cross-correlations.
5. **Simulate lognormal paths** (driftless GBM, step dt, vol σᵢ):
   S_{t+1} = S_t · exp(−½·σᵢ²·dt + σᵢ·√dt·U_t). Vectorized across
   assets and steps; the −½σ²dt drift term keeps the expected price
   constant (martingale).

```python
import numpy as np
from numpy.linalg import cholesky

def correlated_paths(sigma, corr, n_steps, n_paths=1, seed=0,
                     dt=1/252, s0=None):
    n = len(sigma)
    Sigma = np.outer(sigma, sigma) * corr      # covariance matrix
    A = cholesky(Sigma)                        # lower-triangular factor
    rng = np.random.default_rng(seed)
    Z = rng.standard_normal((n_paths, n_steps, n))
    U = Z @ A.T                                # correlated innovations
    drift = -0.5 * np.array(sigma)**2 * dt
    rets = drift + np.array(sigma) * np.sqrt(dt) * U
    if s0 is None:
        s0 = np.ones(n)
    return s0 * np.exp(np.cumsum(rets, axis=1))  # (paths, steps, assets)
```

## known pitfalls
- **Cholesky fails (LinAlgError) on non-positive-definite input**: the
  correlation matrix has an inconsistent triangle (e.g., ρ_AB = 0.9,
  ρ_AC = 0.9, ρ_BC = −0.5). Fix by shrinking the matrix toward the
  identity or using the nearest PSD projection (e.g., `Higham`'s
  algorithm) before factorizing.
- **Use covariances, not raw correlations, for the factor**: `np.outer(vol, vol) * corr` is the standard construction; feeding a
  correlation matrix alone loses the per-asset scale.
- **Correlations are unstable** (Taleb's core warning): a constant-ρ
  simulation understates crisis risk. Re-run scenarios with elevated ρ
  and fat-tailed innovations (Student-t) for stress testing.
- **Lognormal drift**: forget the −½σ²dt term and simulated prices
  drift upward with volatility — a silent bias in long simulations.
- **Same seed for correlated assets**: generate one Z matrix and mix it
  (as above); do NOT draw independent normals per asset, or the
  correlation target is ignored.

## source
Nassim N. Taleb, *Dynamic Hedging* (Wiley, 1997), Module A (Brownian
motion on a spreadsheet, two-asset correlated walk + Cholesky);
consistent with standard Monte Carlo practice for multi-asset
option/portfolio risk.
