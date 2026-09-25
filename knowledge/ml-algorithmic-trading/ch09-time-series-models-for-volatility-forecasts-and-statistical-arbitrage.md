# Ch09 — Time-Series Models: Volatility Forecasts and Statistical Arbitrage

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 9.

## Purpose
Classical time-series machinery applied to markets: ARMA/ARIMA for levels, GARCH for volatility, and cointegration/VAR for statistical arbitrage — the statistical foundations beneath ML models.

## Stationarity first
- A series is stationary if its mean/variance are constant over time; most price series are I(1) — work with returns/differences.
- **Tests**: ADF / KPSS for unit roots; check autocorrelation (ACF) and partial autocorrelation (PACF) to identify AR/MA orders (see `arma-garch-modeling`).

## ARMA / ARIMA
- AR(p): y_t = c + Σφᵢy_{t−i} + ε_t
- MA(q): y_t = c + ε_t + Σθᵢε_{t−i}
- ARIMA(p,d,q): ARMA on d-differenced data. Model selection: AIC/BIC; residuals should be white noise.
- **Limitation**: constant-variance assumption fails for financial returns — volatility clusters.

## GARCH for volatility
- Return: r_t = μ + σ_t·z_t, z_t ~ iid(0,1)
- Variance: σ²_t = ω + α·ε²_{t−1} + β·σ²_{t−1}
- α measures reaction to new shocks, β persistence; α+β < 1 for stationarity; α+β near 1 → volatility is highly persistent (long memory).
- Extensions: GJR/EGARCH for asymmetry (leverage effect), GARCH-M. Use GARCH forecasts for vol-targeting and option-implied comparisons.

## Cointegration and pairs trading
- Two I(1) series are cointegrated if a linear combination is stationary: y_t − β·x_t ~ I(0) (see `cointegration-testing`).
- **Engle-Granger**: regress y on x, test residual stationarity (ADF).
- **Pairs strategy**: when the spread z_t = y_t − βx_t deviates beyond a threshold (e.g., ±1.5–2σ of its z-score), go long the cheap leg / short the rich leg, exit on reversion; positions sized by spread volatility.
- **VAR** for multivariate systems: models each series as a linear function of lagged values of all series; captures cross-dependencies (e.g., sentiment ↔ industrial production).

## Applying ML to time series
- ML models (trees, RNNs) are nonlinear alternatives to ARMA/VAR; they still need stationarity (transform to returns) and lag-based feature matrices (windows).
- Compare ML forecasts against the classical baselines — beating a well-tuned ARMA/GARCH is the real test of added value.

## Key takeaways
- Stationarity, ACF/PACF order selection, and residual diagnostics are non-negotiable foundations.
- GARCH models the conditional variance that linear return models ignore — crucial for risk and vol-targeting.
- Cointegration gives the cleanest statistical-arbitrage framework: mean-reverting spreads on a stationary combination.
