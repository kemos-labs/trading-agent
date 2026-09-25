# IV.4 Monte Carlo VaR

Source: Carol Alexander, *Market Risk Analysis*, Vol. IV (Value at Risk
Models), ch IV.4.

## Core idea

Monte Carlo (MC) is the flexible method of "last resort" when analytic
solutions don't exist. Two equally important design aspects: the **sampling
algorithm** and the **behavioral model** of risk-factor returns. The chapter
argues the model selection is the hard part — sampling error is easier to
control than model risk. Both sources must be controlled.

## Sampling techniques

- **Pseudo-random numbers**: linear congruential generators
  `x_{i+1} ≡ c·x_i mod(m)` with prime modulus; better generators (e.g.,
  Mersenne Twister) have long periods. Seed controls reproducibility.
- **Quasi Monte Carlo**: low-discrepancy sequences (Sobol, Halton) cover the
  unit hypercube with far fewer points than pseudo-random — dimension
  reduction makes them effective.
- **Variance reduction**: antithetic sampling (negate each draw), stratified
  sampling (partition the unit interval). Control variates also mentioned
  (Glasserman 2004 is the classic reference).
- **Structured MC**: transform uniforms → draws from the parametric
  multivariate distribution via the inverse CDF / Cholesky of the covariance.
- **Multi-step MC**: simulate day-by-day so conditional distributions evolve —
  necessary for volatility clustering (GARCH), mean reversion, and any
  dynamic model.

## Behavioral models for risk-factor returns

- **Static (i.i.d.) models**: only the multivariate unconditional
  distribution matters — normal, Student-t, normal mixture. Sample once.
- **Dynamic models**: conditional distributions evolve over time — EWMA and
  GARCH (univariate → multivariate) capture volatility clustering; mean
  reversion for rates/vol.
- **Dependence**: multivariate normal/Student-t via covariance (Cholesky), or
  **copulas** for more general dependence than correlation.
- Non-linear regression can embed richer relationships in bivariate
  simulation.

## Estimating MC VaR and ETL

For a linear portfolio mapped to risk factors:
1. Draw S scenarios of h-day risk-factor returns from the model.
2. Apply the linear mapping (weights/PV01 vector) to get S portfolio returns.
3. VaR = α-quantile of simulated P&L (negative); ETL = average of losses
   beyond VaR.

Examples show:
- **Copula-based credit-spread VaR** for cash-flow portfolios;
- **PCA-based interest-rate VaR**: simulate on 3 principal components instead
  of 60 rates — big efficiency gains from dimension reduction;
- **Normal mixture** stock portfolios for scenario analysis;
- **Multivariate GARCH + conditional Student-t** currency portfolios: VaR
  estimates shift significantly with non-normality and volatility/correlation
  clustering even over 10-day horizons.

## Key takeaways

- MC VaR = sample the risk-factor model, map, take the quantile; model
  selection dominates accuracy.
- Use low-discrepancy sequences and variance reduction (antithetic,
  stratified) to cut simulation error.
- Use multi-step simulation for dynamic models (GARCH, mean reversion).
- Copulas generalize dependence beyond correlation.
- PCA on risk factors cuts dimension massively (60 rates → 3 PCs).

Related skills: `skills/monte-carlo-option-pricing` (sampling/variance
reduction), `skills/correlated-scenario-simulation`, `skills/risk-metrics`,
`skills/var-backtesting`.
