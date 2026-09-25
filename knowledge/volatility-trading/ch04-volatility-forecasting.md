# Ch4 — Volatility Forecasting

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## Why forecast

The core trade is: forecast future realized volatility, compare with implied
volatility, and trade the divergence. The forecast is only as good as the
method; naive historical vol is a weak forecast because vol is clustered
(persistence) yet mean-reverting.

## Models

- **EWMA (exponentially weighted moving average)**: σ²_t = λ σ²_{t-1} +
  (1−λ) r²_t. Simple, adapts to clustering; λ ≈ 0.94 (RiskMetrics) for daily
  data. Single parameter; ignores mean reversion.
- **GARCH(1,1)**: σ²_t = ω + α ε²_{t-1} + β σ²_{t-1}, with ω = γ·V (long-run
  variance V, persistence weight γ). Captures both clustering (α) and
  mean reversion toward V (γ). Unconditional vol = √(ω/(1−α−β)).
- **Regime-switching / Markov models**: vol flips between high and low
  states (e.g. HMM); forecasts condition on the current regime. Useful when
  vol behavior is bimodal (crisis vs. calm).
- **Realized-vol models**: sum intraday squared returns; for short horizons
  (days–weeks) realized vol from 5–30-min returns is an excellent forecast
  of future realized vol.
- **Implied volatility** is itself a forecast: model-free IV (VIX-style
  construction) is a decent, forward-looking, risk-neutral forecast that
  generally beats historical models at 1-month horizons but has a premium
  embedded (see the variance premium).

## Practical points

- **Forecast horizon must match the option's life** (and roughly its
  maturity weighting for a position): 1-day forecasts don't directly price
  3-month options; forecast over the horizon and vol-of-vol matters.
- **Overfitting**: with enough parameters you can fit anything; out-of-sample
  testing and parameter parsimony are essential. GARCH(1,1) is preferred
  over richer variants unless data clearly support them.
- **Vol of vol**: report forecast uncertainty; a point forecast without a
  band is not actionable for sizing.
- Forecast evaluation: use RMSE/MSE of variance forecasts, or trading
  metrics (Sharpe of the vol-trade) rather than in-sample fit.

## Key takeaways

- Forecast volatility over the option's horizon, not just tomorrow.
- GARCH(1,1)/EWMA capture clustering; mean reversion requires the long-run
  anchor (ω term); regime models capture bimodal behavior.
- Implied vol is a competitor forecast with a premium; the exploitable
  signal is forecast-vs-implied divergence that you can explain.
- Always validate out-of-sample; the market's edge is in forecast accuracy
  over the position's life.
