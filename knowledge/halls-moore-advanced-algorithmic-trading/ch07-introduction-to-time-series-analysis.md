# Ch7 — Introduction to Time Series Analysis

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 7 (survey/intro).

## What a time series is
A **time series** is a quantity measured sequentially over time. Analysis seeks to (a) infer
what happened in the past and (b) predict the future, assuming some underlying generating
process (a **DTSP** – discrete-time stochastic process). In trading we fit statistical models to
DTSPs to infer relationships / predict prices.

## Common features of series
- **Trends** — consistent directional movement; either *deterministic* (can give a rationale) or
  *stochastic* (random, unlikely to explain). Commodities show trends; CTA funds use trend
  identification.
- **Seasonal Variation** — periodic pattern (business sales, climate, commodities/harvests).
- **Serial Dependence / serial correlation** — observations close in time are correlated;
  **volatility clustering** is one aspect. This is central for financial series.

## Uses in quantitative trading
1. **Forecast future values** → signals.
2. **Simulate series** — once properties are known, simulate scenarios to estimate expected
   trade count, costs, returns, infrastructure needs, and thus risk & profitability.
3. **Infer relationships** between series → filter/enhance signals (e.g. how an FX spread
   varies with bid/ask volume → filter trades during unfavourable periods).
4. **Statistical tests** (classical or Bayesian) → justify behaviour, detect **regime change**.

## Tooling
Use **R** for time-series research (not C++/Python, which lack mature statistical libraries):
R has rich time-series libraries, statistical methods, plotting. Taught problem-solver style.
Data for TS work: R.

## The book's time-series roadmap (each = a later chapter)
- **Serial correlation** — define, visualise, use (correlogram, stationarity checks).
- **Random Walks & White Noise** — two basic models underpinning later linear & conditional
  heteroskedastic models.
- **ARMA family** — autoregressive, moving-average, combined (first attempt at prediction).
- **Differencing/integration → ARIMA** — make non-stationary stationary; then conditional
  heteroskedastic models (vol clustering), e.g. **GARCH**.
- **Cointegration** — (mean-reverting pairs from *Successful Algorithmic Trading*) formalised
  for pairs trading.
- **State space models / Kalman filter + Hidden Markov Models** — handle rapidly-varying
  parameters (e.g. the slope β of a mean-reverting pair); major uses of Bayesian inference.

## Positioning / strategy
- Retail traders applying *advanced* (not just entry-level) methods to capacity-constrained
  strategies, plus robust portfolio management and brokerage connection, can achieve long-term
  profitability (funds above ~$1–2M don't bother) — a rationale for retail sophistication.
- Later chapters combine time-series with Bayesian testing/selection and optimised R/Python to
  build non-linear, non-stationary systematic strategies.

## Notes
- Pure survey chapter — no formulas. Carry-over concept to remember: identifying trends,
  seasonality, correlation; then simulate, forecast, and *infer relationships* to filter
  signals; detect regime change.