# Ch11 — ARIMA and GARCH (conditional heteroskedasticity)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 11.

## ARIMA(p,d,q) — Autoregressive Integrated Moving Average
Purpose: reduce a **non-stationary** series to **stationary** via $d$-fold **differencing**
(∇^d x_t = (1−B)^d x_t). Definition: {x_t} is ARIMA(p,d,q) if ∇^d x_t follows an ARMA(p,q)
process. The random walk (ARMA on first differences of a cumulated white-noise series) is a
special case. Used because most financial price series are non-stationary (stochastic trends /
volatility clustering); repeated differencing (d>1) can handle non-linear trends. (SARIMA and
ARCH/GARCH handle seasonality & conditional heteroskedasticity.)

### Simulated verification
ARIMA(1,1,1) α=0.6, β=−0.5 → recovered; residuals ≈ white noise; Ljung-Box p>0.05 (good fit).

### Real data (R: `arima`, `forecast` package)
- **AMZN** (daily log-returns): grid-search p,d,q by AIC → ARIMA(4,0,4) (d=0 because already
  differenced). Residuals ≈ white noise (two peaks at k=15,21 within sampling variation),
  Ljung-Box p>0.05. ✓
- **S&P500**: truncating the data to start at **2013** (excluding volatile 2007–08) yields
  ARIMA(2,0,1), residual Ljung-Box p>0.05 → *false* good fit. **Critical caveat**: slicing out
  high-volatility windows makes a CH series "look stationary". Regime/period handling is
  crucial ("regime detection") — a recurring theme in quant finance.
- Forecasting: `forecast()` gives point forecasts + 95%/99% error bands; basis of the first
  trading-strategy chapter later.

## Conditional heteroskedasticity (CH) — motivation
Volatility matters because: options pricing (**Black-Scholes** uses σ), **VaR** calculation,
and volatility is now a *tradeable* security (e.g. VIX).
- **Heteroskedasticity**: variance varies across subsets of a series (e.g. rises with trend /
  seasonality).
- **Conditional**: serially-correlated variance (e.g. correlated sell-off cascade from portfolio
  insurance / automated risk sells amplifying downturns).
- **Detection trap**: a CH series' correlogram can look like white noise (mean/variance in the
  *levels* look constant) even while the series is clearly non-stationary in variance — so
  volatility clustering is hard to see in the plain ACF.

## ARCH(p) — Autoregressive Conditional Heteroskedastic
Model the *variance* autoregressively: ε_t = σ_t w_t where **σ_t² = α0 + α1 ε_{t−1}² + … +
= αp ε_{t−p}²** (w = DWN zero-mean unit-variance). Squaring shows Var(ε_t) is a linear AR(p)
process on the squared past residuals.
- **Only ever apply ARCH to series whose residuals already look like DWN** (i.e. after a good
  ARMA/ARIMA fit removes first-order serial correlation) — you detect ARCH *from the
  correlogram of the squared residuals*.
- ARCH(1) vs AR(1): same form except the noise term is the sole source in AR; in ARCH the
  *variance* (not level) is the AR process.

## GARCH(p,q) — Generalised ARCH
Adds a moving-average (and prior-variance) component:
**σ_t² = α0 + α1 ε_{t−1}² + … + Σ_{j=1}^q β_j σ_{t−j}²**. GARCH = "ARMA-equivalent of ARCH".
- **GARCH(1,1)**: σ_t² = α0 + α1 ε²_{t−1} + β1 σ²_{t−1}, three params (α0, α1, β1).
- **Stability requires α1 + β1 < 1** (else series becomes unstable/explosive).

### Simulated verification
GARCH(1,1) α0=0.2, α1=0.5, β1=0.3 (10k samples):
- Correlogram of ε: white-noise-like (levels don't reveal CH).
- Correlogram of ε²: clear decay of successive lags → CH present.
- Fit with tseries `garch()` + `confint()` → true params within CIs. ✓

## Predicting CH: detection recipe
1. Fit ARIMA to a differenced series; check residuals ≈ DWN.
2. Plot **ACF of the squared residuals**: serial correlation here ⇒ CH present.
3. Fit **GARCH** to the residual series; verify residual & squared-residual correlograms ≈ DWN.
   (i.e. GARCH "explains" the CH/serial correlation in the squared residuals.)

## Applied to FTSE100 (index)
- Differenced daily log-close; grid search → **ARIMA(4,0,4)** (fits, d=0 expected since already
  differenced).
- Residual correlogram ≈ DWN; but **squared-residual correlogram shows serial correlation** ⇒ CH
  present (peaks especially around 2008–09).
- Fit GARCH to residuals → residual & squared-residual correlograms both ≈ DWN ⇒ the ARIMA +
  GARCH combination explains both level serial correlation and volatility clustering.

## Takeaways
- Use ARIMA for the *mean/level structure* + GARCH for the *variance structure*; combine to
  forecast returns with more realistic (conditionally heteroskedastic) variance.
- Beware sample-window selection (regime effects) that can falsely "improve" stationarity.
- Always check squared residuals, not just residuals, for CH serial correlation.
- Stability bound α1+β1<1 is a hard validity constraint on GARCH.