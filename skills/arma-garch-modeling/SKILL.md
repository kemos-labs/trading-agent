# ARMA/GARCH Modeling for Return Forecasting

## name
ARMA/GARCH time-series modeling for financial returns

## description
Fit an ARMA model to the conditional mean of a (differenced) return series and
a GARCH model to its conditional variance, then use the combined model to
forecast next-period return direction or volatility.

## when to use it
- Modelling daily/intraday asset returns that show serial dependence in the
  mean (autocorrelation) and volatility clustering (heteroskedasticity).
- Generating a rolling next-day return-direction signal for a systematic
  strategy, or forecasting variance for risk/sizing.
- ARMA alone never fits log-equity returns well — you need ARIMA (differencing)
  plus GARCH for the variance.

## method / formula / code

**Model definitions:**
- AR(p): x_t = c + Σᵢφᵢx_{t−i} + ε_t
- MA(q): x_t = c + ε_t + Σᵢθᵢε_{t−i}
- ARMA(p,q): both terms; **ARIMA(p,d,q)** applies d differences first.
- **GARCH(1,1)**: σ²_t = α₀ + α₁·ε²_{t−1} + β₁·σ²_{t−1}, with α₁, β₁ ≥ 0 and
  **α₁ + β₁ < 1** (stationarity).

**Order selection:** grid-search p,q ∈ {0..5} (skip p=q=0), pick min
**AIC** (or BIC); check residuals with the **Ljung-Box** test (no remaining
autocorrelation). Detect ARCH effects by looking at the **ACF of squared
residuals** — significant lags ⇒ need GARCH.

**Rolling signal-generation loop (per day d, window k):**
1. Take last k differenced log returns.
2. Fit ARMA(p,q) for all p,q; keep min-AIC order (wrap fits in tryCatch to
   skip non-converging combos).
3. Fit ARIMA-mean + GARCH(1,1) (e.g. `rugarch::ugarchspec` with
   `variance.model=list(garchOrder=c(1,1))`,
   `mean.model=list(armaOrder=c(p,q))`, skewed-error distribution; use a
   `hybrid` solver for convergence).
4. Predict next-day return; sign = trading direction (short if negative,
   long if positive; hold if unchanged).
5. If GARCH fails to converge, fall back to a default signal — flag it.

**CRITICAL:** predictions labelled with today's date must be **shifted one
day forward** before use in a backtest, otherwise you introduce look-ahead
bias (the prediction uses data including the day it's applied to).

## known pitfalls
- **Look-ahead bias** from mis-aligned forecast dates — always shift forecasts.
- Anachronism: ARMA/ARCH models postdate pre-1970 data; results on old series
  are not live-tradeable evidence.
- Backtests on an index, not a tradeable instrument (use futures/ETF).
- Non-converging GARCH fits must be handled (skip/fallback), not silently
  dropped.
- Strategy performance is regime-dependent: strong in crash/high-serial-
  correlation periods, poor in stochastic-trend markets.

## source book
Halls-Moore, *Advanced Algorithmic Trading*, ch10–ch11 (ARMA; ARIMA+GARCH)
and ch26 (ARIMA+GARCH trading strategy on the S&P500).
