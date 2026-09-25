# IV.6 Risk Model Risk

Source: Carol Alexander, *Market Risk Analysis*, Vol. IV (Value at Risk
Models), ch IV.6.

## Core idea

A risk model has three components — (i) the portfolio's risk-factor mapping,
(ii) the multivariate distribution of risk-factor returns, (iii) the
resolution method (analytic/historical/Monte Carlo) — and the choices are
interlinked (i.i.d. normal + linear mapping ⇒ analytic resolution; MC would
only add sampling error). Risk model risk is the accuracy of the model's
forecasts; estimation risk is how parameters are estimated given the model.

**Two error categories**:
1. **Model risk**: which mapping, distribution, resolution method; how the
   three sub-models' assumptions affect forecast accuracy.
2. **Estimation risk**: parameter estimation — includes sampling error
   (choice of data, sample period, EWMA smoothing constant) but also
   *multiple estimation methods consistent with the same model* (equally
   weighted vs EWMA vs orthogonal EWMA covariance under multivariate normal
   i.i.d.).

Sampling error is not the whole story: larger estimation samples improve
in-sample accuracy but not necessarily backtests (out-of-sample); longer
windows make VaR/ETL *less* risk-sensitive. Empirical studies (Alexander &
Sheedy 2008; Berkowitz & O'Brien 2002) show constant-parameter models can't
forecast short-term risk accurately — volatility clustering + heavy-tailed
conditional distributions are required.

## Assessment levels

Portfolio level (simple, no attribution), risk-factor level (allows risk
attribution, adds mapping model risk), asset level (total risk directly, not
practical for large portfolios). The risk-factor mapping itself is a
considerable, often neglected, source of model risk (how sensitivities are
computed, mapping method).

## Backtesting methodology

- **Confidence intervals for VaR**: distribution of the VaR estimator gives
  bounds (e.g., order-statistic intervals for historical VaR).
- **Regulatory backtests**: simple exceedance counts (e.g., the 99% 1-day
  internal-model capital tests) — traffic-light approach.
- **Kupiec (1995) unconditional coverage test**: LR test that the observed
  exceedance rate equals the promised α — chi-squared(1).
- **Christoffersen (1998) conditional coverage test**: tests independence of
  exceedances — captures clustering.
- **Regression-based backtests**: regress realized on forecast to identify
  *why* a model fails (bias, scale, slope).
- **ETL backtesting (McNeil & Frey 2000)**: tests the average shortfall
  beyond VaR using exceedance residuals.
- **Bias statistics** in the normal linear framework; and tests of the whole
  return distribution, not just the tail.

## Key takeaways

- Risk model = mapping + distribution + resolution; estimation choices
  (data, window, EWMA λ) are separate risks.
- Distinguish model risk from estimation risk; sampling error is only part.
- Larger windows are not always better for forecasting — risk sensitivity
  matters.
- Backtest with coverage tests (Kupiec, Christoffersen), regression
  diagnostics, and ETL tests (McNeil-Frey); use VaR confidence intervals.
- Accurate short-horizon risk needs volatility clustering + fat-tailed
  conditional distributions.

Related skills: `skills/var-backtesting` (the practical implementation),
`skills/risk-metrics`, `skills/walk-forward-validation`,
`skills/statistical-significance-testing`.
