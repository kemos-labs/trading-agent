# II.3 Classical Models of Volatility and Correlation

Source: Carol Alexander, *Market Risk Analysis*, Vol. II (Practical Financial
Econometrics), ch II.3.

## Core idea

The covariance matrix is the workhorse object for risk: estimating and
forecasting volatility and correlation drives VaR of linear portfolios,
optimal allocations, correlated simulation, multi-asset option pricing, and
hedging. This chapter covers the classical moving-average estimators
(historical, equally weighted, and exponentially weighted EWMA, popularized by
JPMorgan's RiskMetrics) and their pitfalls — chiefly **model risk**: the
"true" variance depends on the model, and different models on the same data
give very different covariance matrices.

## Volatility and the square-root-of-time rule

Volatility = annualized standard deviation of returns (the diffusion
coefficient of the log-price process). If one-period log returns are
stationary i.i.d. with variance sigma^2, the h-period log return (sum of h
one-period returns) has variance `h * sigma^2`, so:

```
sigma_h = sqrt(h) * sigma_1
```

with annualizing factor A (e.g., A = 252 daily, 12 monthly, 52 weekly):

```
annualized mean      = A * mu
annualized variance  = A * sigma^2
annualized stdev     = sqrt(A) * sigma
```

**The rule only holds for i.i.d. returns.** With autocorrelated returns,
volatility scales differently:
- positive serial correlation (momentum) → h-period volatility *greater* than
  sqrt(h) scaling;
- negative serial correlation (mean reversion) → *less* than sqrt(h).

Correlation also breaks down outside the bivariate normal i.i.d. world —
Pearson correlation only captures linear dependence in elliptical
distributions.

## Conditional vs unconditional volatility

- **Unconditional**: constant over the whole sample; estimated by the sample
  variance (equally weighted average of squared deviations).
- **Conditional**: time-varying, dependent on the information set up to t-1.
  Moving-average estimators are conditional estimates — the estimate changes
  as the window moves, even though the model assumes a constant parameter.

## Moving average models

**Equally weighted moving average (historical)**: rolling-window sample
variance/covariance; all observations in the window weighted equally. Simple
but slow to react and drops data abruptly at window edges.

**EWMA (RiskMetrics)**: exponentially weighted, with smoothing constant
lambda (~0.94 daily for RiskMetrics):

```
sigma_t^2 = lambda * sigma_{t-1}^2 + (1 - lambda) * r_{t-1}^2
```

Covariances update analogously. EWMA reacts faster to new information and
needs no window length, but the implied volatility forecast is flat for all
horizons beyond one step (returns are modeled as i.i.d.), and it responds to
noise as much as to signal.

## Pitfalls

- **Model risk**: two defensible models on identical data give materially
  different covariance matrices — report sensitivity.
- **Sampling error**: changing the sample period or the observation frequency
  changes the estimate.
- **Precision**: equally weighted estimators of unconditional parameters are
  imprecise unless the window is long relative to the true persistence.
- Early RiskMetrics versions applied incorrect time-series methodology; the
  corrected version is the EWMA above — a reminder to verify even canonical
  recipes.
- Volatility is *not observable*; every estimate or forecast is
  model-specific (contrast with returns, which are observable ex post).

## Key takeaways

- sqrt-time scaling assumes i.i.d. — verify autocorrelation before
  annualizing.
- EWMA (lambda ≈ 0.94) is the practical default for daily covariance
  matrices; equally weighted windows suit stable, longer-horizon contexts.
- These moving-average models are the baseline that GARCH (ch II.4) improves
  on; GARCH captures volatility clustering the moving averages cannot.

Related skills: `skills/risk-metrics`, `skills/parametric-var`, and ch II.4
(GARCH) notes.
