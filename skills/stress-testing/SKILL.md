# Stress Testing and Scenario Analysis

## name
Formal scenario analysis and stress testing for market risk: the single-case
vs distribution-scenario taxonomy, scenario VaR and ETL, stressed covariance
matrices (with positive semi-definiteness), PCA-focused stress scenarios,
liquidity-adjusted VaR, and sensitivity analysis to identify risk drivers.

## description
Quantify portfolio losses under extreme-but-credible market conditions by
replacing historical beliefs with explicit scenario beliefs. The key
principle: express scenarios as probability distributions, not vague "worst
case" language (a worst-case loss is mathematically meaningless). Apply
single-case scenarios for point estimates and distribution scenarios for
scenario VaR/ETL with probabilities; stress covariance matrices (higher
volatilities/correlations) across all three VaR resolution methods. Use when
history is insufficient for tail risk — crises are by definition events with
no historical precedent.

## when to use it
- Stress testing a portfolio whose risk is dominated by tail events (options
  books, credit spread books, illiquid markets) where historical VaR is
  systematically underestimating risk.
- Supplementing VaR reports for governance: regulators and boards expect
  stress scenarios alongside VaR numbers.
- When little or no historical data exists (unlisted stocks, junk bonds,
  operational risk) — hypothetical scenarios are the only option.
- Evaluating a portfolio's sensitivity to specific market moves (parallel
  yield shift, equity crash, vol spike) and to *small* moves in major factors
  that non-linear (option) profiles make dangerous.

## the method

### 1. Classify the scenario
Two dimensions: type of change x data source.
- **Single case** — one vector of risk-factor returns (e.g., 100bp parallel
  shift). Loss via the mapping; NO probability. Use for point "what ifs".
- **Distribution** — a full multivariate distribution of factor returns
  (e.g., yields ~ N(mean=100bp, sd=50bp) with correlations). Probabilities
  attach to loss levels; this is the coherent framework.
- **Historical** vs **hypothetical**: past data vs analyst/management views.

### 2. Sensitivity analysis first
Map the portfolio's loss as a function of each risk factor to identify the
main risk drivers before choosing scenarios:

```python
import numpy as np

def sensitivity_grid(mapping_fn, factor_base, factor_ranges, n=20):
    """Loss profile across one-factor shocks (keep others at base)."""
    grid = {}
    for name, (lo, hi) in factor_ranges.items():
        shocks = np.linspace(lo, hi, n)
        losses = [mapping_fn({**factor_base, name: s}) for s in shocks]
        grid[name] = (shocks, losses)
    return grid  # inspect curvature; a small move may cause the largest loss
```

### 3. Stressed covariance matrix
Build a stress covariance matrix with elevated volatilities and correlations,
apply in all three VaR methods:

```python
def stress_covariance(Sigma, vol_mult, corr_mult):
    """Scale volatilities and correlations of a covariance matrix."""
    vol = np.sqrt(np.diag(Sigma)) + 1e-12            # guard vs zero-vol series
    D = np.diag(vol)
    C = np.linalg.inv(D) @ Sigma @ np.linalg.inv(D)   # recover correlations
    # scale only the OFF-diagonals so the diagonal stays 1 (still a corr matrix)
    C_stress = C.copy()
    idx = ~np.eye(C.shape[0], dtype=bool)
    C_stress[idx] = np.clip(C[idx] * corr_mult, -1, 1)
    # nearest-PSD fix if the scaling broke definiteness:
    vals, vecs = np.linalg.eigh(C_stress)
    vals = np.clip(vals, 0, None)                     # zero negative eigenvalues
    C_psd = vecs @ np.diag(vals) @ vecs.T
    # re-normalize to unit diagonal so (vol*vol_mult)^2 is preserved exactly
    d = np.sqrt(np.diag(C_psd)) + 1e-12
    C_norm = C_psd / np.outer(d, d)
    D_stress = np.diag(vol * vol_mult)
    return D_stress @ C_norm @ D_stress
```

- Stressed VaR/ETL = recompute VaR (parametric, historical, or Monte Carlo)
  with the stressed matrix.
- **Keep the matrix positive semi-definite** — eigenvalue clipping is the
  standard fix after arbitrary correlation/vol adjustments.

### 4. Scenario VaR / ETL
For a distribution scenario, plug the scenario distribution into the risk
model and compute the quantile (scenario VaR) and the average loss beyond it
(scenario ETL) — identical machinery to VaR estimation, just with the
scenario distribution instead of historical data. Distinguish from Bayesian
VaR (which updates a prior with data) — scenario VaR uses the scenario
distribution directly.

### 5. PCA-focused stress
Decompose the covariance (or stressed covariance) into principal components
and stress the dominant ones (shift/tilt/curvature for yield curves) — fewer,
more interpretable, more likely scenarios; the portfolio's PC exposures come
from the eigenvector loadings.

### 6. Liquidity-adjusted VaR
Add a liquidity premium to the risk-horizon P&L. Distinguish exogenous
liquidity (market-wide, add to the factor distribution) from endogenous
liquidity (position-size-dependent, model the cost of unwinding size).

## known pitfalls
- **"Worst case" is meaningless** — always attach probabilities via
  distribution scenarios; a single-case loss is a point estimate, not a risk
  metric.
- **Stress adjustments can break positive semi-definiteness** — arbitrary
  correlation/vol scaling then clipping demands a PSD fix (eigenvalue
  clipping) before use in Cholesky/portfolio variance.
- **Small moves matter for options** — non-linear profiles can lose more on
  a small move in a major factor; sensitivity grids catch this where large
  uniform shocks miss it.
- **History is not enough** — a stress test built only from historical
  scenarios misses the unprecedented (Russian default 1998, 2007-08 crunch).
- **Volatility clustering**: for multi-day holdings, stress VaR is
  materially higher when you include clustered vol (GARCH-style) dynamics —
  plain scalar vol shocks understate multi-day risk.

## source
Alexander, *Market Risk Analysis*, Vol. IV (Value at Risk Models), ch IV.7
(scenario analysis and stress testing). Knowledge note:
`knowledge/market-risk-analysis-vol4/ch-iv7-scenario-analysis-and-stress-testing.md`.
Complementary: `skills/risk-metrics`, `skills/parametric-var`,
`skills/correlated-scenario-simulation` (Cholesky engine),
`skills/var-backtesting`.
