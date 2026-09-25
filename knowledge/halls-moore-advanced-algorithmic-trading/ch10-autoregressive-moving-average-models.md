# Ch10 — Autoregressive Moving Average Models (AR, MA, ARMA)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 10.

## Motivation & roadmap
AR, MA and ARMA are linear models to capture serial correlation beyond the random walk.
Downside: they are *not* conditionally heteroskedastic (don't model volatility clustering),
which motivates the later **ARCH/GARCH** family. They underlie **ARIMA**. The book later builds
an ARIMA+GARCH trading strategy.

## New model-selection tools
- **Strict stationarity**: the joint distribution of (x_i,…,x_j) is time-invariant; mean and
  variance constant, autocovariance depends only on |t−s|.
- **AIC = −2 log(L) + 2k** (k = number of parameters). Minimise AIC; penalises overfitting
  (more parameters → higher AIC, better fit → lower −2logL).
- **BIC** — like AIC but *more stringent* penalty for parameter count.
- **Ljung-Box test** — tests whether the *whole set* of autocorrelations up to lag h differ from
  zero (series white-noise / i.i.d.), not each lag individually:
  H0: i.i.d.; Ha: serial correlation. Stat: Q = n(n+2)Σ ρ̂²_k/(n−k). Reject H0 if it exceeds
  the χ²_{α,h} critical value. P-value > 0.05 ⇒ residuals look like white noise ⇒ good fit.

## AR(p) — Autoregressive of order p
**x_t = α1 x_{t−1} + … + αp x_{t−p} + w_t** (w = white noise; αp≠0). BSO form:
**θ_p(B) x_t = w_t**, θ = (1−α1B−α2B²−…−αpB^p).
- **Random walk = AR(1) with α=1.**
- Prediction: x̂_t = Σ α_i x_{t−i}; can make n-step forecasts.
- **Stationarity**: solve characteristic equation θ_p(B)=0; stationary iff *all* roots have
  |root|>1. (AR(1) root B=1/α: α=1→recurring unit root (non-stationary); α chosen <1 stationary.)
- Mean 0; covariances given recursively by **Yule-Walker equations**.
- R `ar()` auto-selects order + MLE coefficients; check 95% CI contains true α.

### Simulated verification
- AR(1): true α=0.6 → recovered order 1, α̂=0.523 (within CI; slightly low).
- AR(1): α=−0.6 → α̂=−0.597 (excellent).
- AR(2): α=(0.666,−0.333) → order 2, α̂=(0.696,−0.395) ≈ recover.

### Real data
- **AMZN**: fit differenced daily log prices → AR(2), α̂=(−0.0278,−0.0687). CI: α2 excludes 0,
  α1 includes 0 → caution; residual autocorrelation at k=2. AR doesn't handle volatility
  clustering.
- **S&P500** (^GSPC): ACF shows many peaks incl. k=1, long-memory. Fitting AR yields **AR(22)**
  (22 params!) — clear sign of high complexity → AR insufficient (vol clustering + long memory).

## MA(q) — Moving Average of order q
Linear combination of past *white-noise shocks*: **x_t = w_t + β1 w_{t−1} + … + βq w_{t−q}**
(BSO: x_t = φ_q(B) w_t). Sees only the *last q* shocks (vs AR taking all prior, decaying).
- Mean 0; Autocorrelation **ρ_k = 0 for k > q** — so the number of significant consecutive ACF
  lags ≈ q. Very useful for model order identification.

### Simulation
- MA(1) β=0.6 → significant peak k=1, rest ~0 → fit β̂=0.602 ✓;
  β=−0.6 → β̂=−0.730 (underestimate), negative k=1 peak.
- MA(3) β=(0.6,0.4,0.3) → three significant peaks; β̂=(0.544,0.345,0.298) ✓ (CIs contain true).

### Real data (R `arima` with order c(0,0,q); note arima estimates an intercept unless you
remove the mean)
- **AMZN**: MA(1) residuals have peaks at lags 2,11,18 (poor). MA(2)/MA(3) capture short-lag
  correlation well but leave 12,16,19,27 peaks → MA insufficient, long-memory/vol-clustering.
- **S&P500**: MA(1) leaves peaks at k∈{5,10,14,15,16,18,20,21}; MA(3) still leaves long lags.
  Reject MA models.

## ARMA(p,q) — Autoregressive Moving Average
Combines AR (momentum/mean-reversion-like autoregressive behaviour, own past) + MA
("shocks", e.g. surprise news = BP oil-spill type events): **x_t = … α past values + … β past
noise + w_t**. BSO: θ(B)x_t = φ(B)w_t. Setting q=0 → AR(p).
- **Parsimonious**: often needs fewer params than AR or MA alone; polynomials share factors.
- Still linear; does NOT handle volatility clustering.

### Simulation & model selection
- ARMA(1,1) α=0.5, β=−0.5 → recovered; wide CIs (short series).
- ARMA(2,2) α=(0.5,−0.25), β=(0.5,−0.3) → the *CRITICAL lesson*: CIs for the MA coefficients
  (β) do NOT include the true values even for simulated known-params data → fitting risk; for
  trading we only need predictive power "reasonably exceeds chance" above transaction costs.
- **Order selection procedure**: loop p,q (0..4), fit ARIMA(p,0,q), keep lowest AIC;
  simulate ARMA(3,2) → procedure recovers p=3,q=2, residuals ≈ white noise, Ljung-Box p>0.05.

### Real data
S&P500 log-returns: best ARMA still leaves significant residual ACF peaks at higher lags;
Ljung-Box p<0.05 → residuals NOT white → additional autocorrelation (esp. 2007–08 vol
clustering). Conclusion: **ARMA never fits log-equity-returns well** — you need ARIMA + GARCH
(next chapters).

## Key takeaways
- p,lags absent in ACF after q ⇒ MA order q; decaying ACF pattern helps infer FAR.
- Always validate how a model fails (simulate-then-fit) before trusting on real data.
- Model selection = minimise AIC/BIC, then Ljung-Box the residuals to confirm white noise.