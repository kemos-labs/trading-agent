# IV.2 Parametric Linear VaR Models

Source: Carol Alexander, *Market Risk Analysis*, Vol. IV (Value at Risk
Models), ch IV.2.

## Core idea

Analytic VaR/ETL formulas for portfolios whose value is a **linear** function
of risk factors (cash, futures, forwards, bonds, loans, swaps, equities, FX,
commodities mapped as cash flows). All co-dependencies are captured by
correlations in an h-day covariance matrix; the matrix drives the model.
Applies to any portfolio that can be mapped linearly — it fails for options
and option-like payoffs (non-linear P&L). Moving-average covariance estimates
(equally weighted or EWMA) are used because the i.i.d. assumption implies the
h-day covariance = h × 1-day covariance (square-root-of-time).

**GARCH cannot be used here**: GARCH returns are not i.i.d., so the h-day
return distribution is unknown (only moments); quasi-analytic moment-based
extensions exist (Alexander et al.), otherwise Monte Carlo resolution.

## Normal linear VaR

Portfolio-level (no mapping): i.i.d. normal returns →
`VaR_α = Phi^-1(1-α) * sigma_h - mu_h`. With autocorrelated returns the
1-day formula is unchanged; only the h-day scaling changes (adjust for the
autocorrelation structure).

With risk-factor mapping (systematic VaR):

```
VaR = Phi^-1(1-α) * sqrt(w' * Sigma_h * w)     (in value terms, PV01/weights w)
```

- Interest-rate portfolios: cash flows mapped to zero-coupon vertices with
  PV01 sensitivities; risk factors = LIBOR curve + credit-spread term
  structures per rating; disaggregate total VaR into LIBOR VaR and credit
  spread VaR.
- PCA reduces factor dimension: UK bond portfolio with 60 rates → 3 PCs.
- Stock portfolios: beta-mapped to indices; decompose into systematic VaR
  and specific (residual) VaR.
- International portfolios: disaggregate into equity, FX, and interest-rate
  VaR components; compute stand-alone and marginal VaRs; normal linear VaR is
  sub-additive so component VaRs aggregate to ≤ sum.
- Commodities: constant-maturity futures as risk factors (trading-desk case
  study).

## Other analytic models

- **Student-t linear VaR**: analytic with the t-quantile and degrees-of-
  freedom parameter — heavier tails than normal.
- **Normal mixture and Student-t mixture linear VaR**: weighted sums of
  components, each with its own covariance matrix; capture skew and excess
  kurtosis. The iTraxx Europe 5-year credit-spread case study (highly skewed,
  fat-tailed daily changes) shows the mixture model fits best.
- These i.i.d. formulas can be extended to autocorrelated returns; volatility
  clustering requires Monte Carlo.

## EWMA / RiskMetrics

EWMA covariance (λ ≈ 0.94 daily) in the parametric linear framework is the
RiskMetrics™ methodology (JPMorgan, 1990s). Advantages: responsive to recent
volatility; limitations: implied flat forecasts beyond one step, sensitive to
noise.

## ETL formulas

Analytic ETL exists for each parametric model:
- Normal linear ETL: `ETL = sigma * phi(Phi^-1(alpha))/alpha - mu`
  (phi = standard normal density) — the average loss beyond VaR.
- Student-t, normal mixture, t-mixture versions derived similarly.

## Key takeaways

- Parametric linear VaR is analytic for linear portfolios; covariance matrix
  + sensitivities are the model.
- Use PCA for factor reduction (60 rates → 3 PCs); credit spreads add rating-
  specific factors.
- Student-t and mixture models handle fat tails/skew analytically.
- GARCH dynamics need Monte Carlo, not the analytic framework.
- ETL is a simple function of the same model: for normal,
  ETL = σ·φ(Φ⁻¹(α))/α − μ.

Related skills: `skills/parametric-var`, `skills/risk-metrics`,
`knowledge/market-risk-analysis-vol2/ch-ii3` (covariance estimation),
`ch-ii2` (PCA).
