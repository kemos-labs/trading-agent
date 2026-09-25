# Ch8 — Serial Correlation (Autocorrelation)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 8.

## Purpose
Identifying the **structure of correlations** between sequential observations lets us (a)
improve forecasts and (b) make simulated series more realistic. A key example: **mean-reverting
pairs trading** shows up as correlation between sequential variables.

## Foundation definitions
- **Expectation** E(x) = μ = mean of x in the population.
- **Variance** = E[(x−μ)²]; always ≥0.
- **Covariance** σ(x,y) = E[(x−μ_x)(y−μ_y)] — how two variables vary linearly together.
  **Sample covariance** for n pairs: Cov(x,y) = (1/(n−1)) Σ(x_i−x̄)(y_i−ȳ) (divide by n−1 to be
  unbiased). R: `cov()`.
  Example: two linearly-increasing noise-perturbed vectors → cov ≈ 681.7. Drawback: covariance
  is *dimensional* (not normalised by spread), so comparison across datasets is hard.
- **Correlation** Cor(x,y) = Cov(x,y)/(sd(x)·sd(y)) — *dimensionless*, constrained to [−1,1].
  R: `cor()`. Example → 0.5797 (moderately strong positive association).

## Time-series-specific: stationarity
- **Mean of a series** μ(t) = E(x_t) — an *ensemble* expectation (over all possible
  realisations), not the sample mean of one history. To estimate from a single series:
  decompose away deterministic trends/seasonality, then assume **stationary in the mean**
  μ(t)=μ, and estimate via sample mean x̄=x̄=Σx_t/n.
- **Stationary in the mean**: μ(t)=μ (constant in time).
- **Variance** σ²(t) = E[(x_t−μ)²]; assume **stationary in the variance** σ²(t)=σ² and estimate
  with sample variance (again /(n−1)).
- **Caveat**: serial correlation con in time-series — sequential observations are *not*
  independent (unlike standard sample estimators). This matters with short data (few
  observations); high-frequency finance often has plentiful data but usually *cannot* assume
  financial series are stationary (addressed later with more sophisticated models).

## Serial correlation (autocorrelation)
- **Second-order stationarity**: correlation between sequential observations depends *only on
  the lag k* (time gap), not on absolute time.
- **Autocovariance** C_k = E[(x_t−μ)(x_{t+k}−μ)] (C_0 = σ² = 1·... always unity at lag 0).
- **Autocorrelation / serial correlation** at lag k:  **ρ_k = C_k / σ²**  (normalised by the
  series variance — valid because stationary in the variance). ρ_0 = 1.
- **Sample autocovariance** c_k = (1/n)Σ_{t=1}^{n-k}(x_t−x̄)(x_{t+k}−x̄); sample autocorrelation
  r_k = c_k/c_0.

## The correlogram (ACF plot) — main tool
Plot of sample autocorrelation vs lag k (R: `acf(w)`).
- Lag 0 always height 1 (reference point); ACF axis is dimensionless.
- Dotted blue bands bound the 5% null region: values outside suggest r_k ≠ 0 at the 5% level.
  Pitfalls: ~5% of lags exceed bands by chance; correlated values cluster (neighbouring lags
  tend to co-exceed). Look for lags with a *reason* (e.g. unexpected seasonality at monthly/
  quarterly/annual lags).

### Worked examples (verifying)
1. `w <- rnorm(100)`: noise → ACF ~ near-zero at all lags (no memory).
2. Increasing linear integer series 1..100: ACF decays nearly linearly — inherent drift looks
   like autocorrelation (misleading; must detrend first).
3. Repeated sequence with period 10: strong peaks at lag 10 & 20; characteristic **negative
   correlation ≈ −0.5** at lag 5 & 15 → classic signature of unremoved **seasonality**.

## Takeaways / pitfalls
- Always consider stationarity (mean & variance) before trusting covariance/ACF.
- Account for non-independence of sequential observations; don't over-read 5% bands.
- A "sawtooth" ACF peaking at seasonal lags plus −0.5 negative side lags flags residual
  seasonal/periodic effects to model away.
- Correlogram validates a fitted model (residual autocorrelation ≈ 0) or tells you to refine.