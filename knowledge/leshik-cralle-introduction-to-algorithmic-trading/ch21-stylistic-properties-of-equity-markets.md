# Chapter 21 — Stylistic Properties of Equity Markets

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Stylized empirical facts (affecting ALPHA ALGO design)

- **Volatility clustering**: a turbulent day is usually followed by
  another turbulent day (tranquil sessions often cluster even more);
  volatility is higher after down-market days; events cluster at
  moderate (multi-day) timescales. Regime switching between ~2–3
  distinct states (high/low), with no hint of duration or trigger.
- **Non-Gaussianity at high frequency**: returns at ≤1-minute sampling
  are not normal and have monotonically increasingly *fat tails* as
  sampling frequency increases; Gaussianity reappears at longer
  timescales. Kurtosis: leptokurtic at ≤60s; approaches Gaussian (~3)
  at >5-session intervals. Magnitudes vary by stock.
- **Autocorrelation**: stock-specific, wanes after ~180–300 seconds,
  insignificant at sampling >600s (when microstructure isn't engaged).
  *Most ALPHA ALGO triggering relies on this short-window
  autocorrelation as part of pattern recognition* — the essence of their
  edge.
- **Scaling laws**: absolute/mean-squared returns relate to the time
  interval by a power law of the sampling frequency.
- **Asymmetry**: drawdowns are significantly larger and faster than
  upward movements; price-trajectory smoothness varies per stock and
  over time.
- **Bellwether lead**: sector bellwethers have predictive power — other
  stocks in the sector react with a finite delay (information
  diffusion), though the data is too variable to assign a stable "time
  constant". Applied via topology (Vandewalle's market-topology.com) to
  the General Pawn algo.
- **Law of Large Numbers**: sampling distributions of 30+ samples from
  non-Gaussian data become Gaussian.
- Returns exhibit **mean reversion** (RETURNS workbook: tick window
  interval + lookback size are the two built-in timing parameters).

## Key takeaways

1. Microstructure-level autocorrelation (seconds) and mean reversion
   are the exploitable features at the measured timescale; fat tails
   and asymmetric drawdowns dictate tiny per-trade risk.
2. Volatility clustering ⇒ parameterize stops/triggers to the current
   regime rather than a fixed scale.
3. Sector bellwether lags give cross-sectional signal (information
   diffusion timing).
