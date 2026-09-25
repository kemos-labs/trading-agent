# Chapter 8 — ARMA Models

## Core idea
The Autoregressive Moving Average (ARMA) model describes a stationary time
series as a function of its own past values (AR part) and past errors (MA
part). For financial returns, ARMA captures short-term serial dependence.

## Model form
```
ARMA(p, q):  y_t = c + φ1·y_{t-1} + ... + φp·y_{t-p}
                  + ε_t + θ1·ε_{t-1} + ... + θq·ε_{t-q}
```
- `p` = number of autoregressive lags, `q` = number of moving-average lags.
- Requires **stationarity** of `y_t` (see ch7); returns are typically already
  close to stationary, prices are not.
- AR(1) is the simplest case: `y_t = c + φ·y_{t-1} + ε_t` — a mean-reverting
  process when |φ| < 1.

## Workflow
1. Check stationarity (ADF test); difference if needed.
2. Choose `(p, q)` via **ACF/PACF** inspection (ACF decays for AR, cuts off
   for MA at lag q; PACF cuts off at p) or via information criteria (AIC/BIC).
3. Fit with `statsmodels.tsa.arima.model.ARIMA(y, order=(p,0,q))`.
4. Diagnose residuals: they should be white noise (no autocorrelation left).
5. Forecast and trade: use the model's next-step forecast (or its sign) as
   the signal, then apply the ch4 backtest pipeline.

## Trading use
- An AR(1)-type positive coefficient on daily returns implies short-term
  momentum (yesterday's move predicts today's); a negative one implies mean
  reversion. The fitted forecast can be sign-traded.
- Usually the *residuals* or *forecasts* of ARMA are combined with other
  features in the ML chapters rather than traded alone.

## Pitfalls
- ARMA on non-stationary data gives spurious fits — always test first.
- Over-fitting `p,q` on noisy returns; AIC/BIC penalize complexity.
- Financial returns are close to white noise: expect tiny R²; ARMA edges are
  weak and must survive costs (ch6).

## Bottom line
ARMA is the classical linear time-series workhorse. The knowledge base
already covers the full family in `skills/arma-garch-modeling` (ARIMA/GARCH,
stationarity testing, residual diagnostics); this chapter is the practical
statsmodels implementation of the AR/MA part with a trading loop attached.
