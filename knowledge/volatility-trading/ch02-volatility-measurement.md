# Ch2 — Volatility Measurement

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## What we measure

Volatility is the standard deviation of (log) returns. Which estimator you
use matters enormously: close-to-close is noisy and slow; range-based
estimators use more of the information in the price path and are far more
efficient.

## Estimators

- **Close-to-close (classic)**: σ = std(ln(S_t / S_{t-1})). Uses only daily
  closes; discards intraday information; unbiased but high variance.
- **Parkinson (high/low)**: σ² = (1/(4 ln 2)) · E[ln(H/L)²]. Uses only the
  daily range; ~5× more efficient than close-to-close (less variance for the
  same sample).
- **Garman-Klass**: σ² = ½(ln(H/L))² − (2 ln 2 − 1)(ln(C/O))². Combines
  range and open/close; more efficient still, but assumes continuous
  sampling (ignores opening jumps → biases estimates down for stocks with
  overnight gaps).
- **Rogers-Satchell**: valid when there is a drift; handles nonzero mean.

Efficiency order (variance reduction vs. close-to-close): Parkinson ≈ 5×,
Garman-Klass ≈ 7.4×, Rogers-Satchell similar. All range estimators share the
jump/overnight-gap problem — the day's open gaps from the prior close, which
the intraday range misses.

## Practical issues

- **Annualization**: σ_annual = σ_daily · √252 (iid assumption). Wrong when
  vol is autocorrelated or when returns are fat-tailed; √t scaling
  overstates long-horizon vol for mean-reverting vol.
- **Volatility of volatility (vol-of-vol)**: how much the vol estimate
  itself moves; critical for option traders because it drives how wrong a
  static forecast can be and the width of confidence bands.
- **Estimation error**: with n observations, the standard error of a vol
  estimate is roughly σ/(√(2n)) — huge for small samples; ranges help but
  don't cure it.
- **Realized vs. implied**: realized vol is what happened (estimated
  historically or intraday from high-frequency data); implied is the
  market's forecast embedded in option prices. The spread between them is
  the trade.
- **Sampling frequency**: higher frequency → less noise but microstructure
  effects (bid-ask bounce) add spurious variance; 30-min to 1-day sampling
  is a common sweet spot.

## Key takeaways

- Measurement error in vol is the biggest practical enemy; prefer
  range-based estimators (Parkinson/Garman-Klass) over close-to-close.
- Watch for overnight-gap bias in range estimators (use adjusted data or a
  correction).
- A vol estimate without a confidence interval is not an estimate — know
  the standard error and how many observations back it up.
- Volatility is a measurable, forecastable quantity; that measurability is
  the foundation of volatility trading.
