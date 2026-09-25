# Ch04 — High-Frequency Data

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 4.

## Purpose
What tick data is, how it differs from low-frequency data, and the
sampling problems that make it hard to work with.

## What tick data is
- **Level I**: best bid/ask price and size + last trade price/size.
- **Level II**: all order book changes — arrivals and cancellations at
  every price.
- Each tick: timestamp, security identifier, quote/trade indicator,
  prices, sizes; timestamps now reach microseconds.

## The four properties of HF data
1. **Voluminous**: one day of tick data ≈ 30 years of daily data —
   big sample sizes, but heavy to handle.
2. **Bid-ask bounce**: quotes/trades alternate between bid and ask,
   injecting a jump process into returns — the naive use of
   transaction prices overstates short-horizon volatility.
3. **Not normal/lognormal**: tick returns are fat-tailed; models
   assuming lognormality (e.g., standard option pricing on raw tick
   data) fail. Midquotes are better behaved than trade prices.
4. **Irregularly spaced in time**: quotes arrive at random intervals;
   naive clock-time aggregation (last-tick carried forward) creates
   sparse, zero-heavy return distributions.

## Sampling methodology
- **Last-tick (closing) sampling**: use the last quote before the
  sample time — simple, but assumes prices are constant between
  quotes.
- **Linear time-weighted interpolation** (Dacorogna et al., 2001):
  interpolate between the surrounding quotes:
  `q̂_t = q_last + (q_next − q_last)·(t − t_last)/(t_next − t_last)`.
  Produces more continuous, less sparse distributions; interpolated
  midquotes are the standard research choice.
- **Volume/duration clocks**: sample per unit of volume or per
  duration instead of per clock interval (basis of VPIN, ch13).
- **Duration models**: inter-trade times carry information (short
  durations often precede moves); modeled with Poisson processes.

## Trade classification
- Most HF data lack buy/sell identifiers; direction is inferred
  (price relative to prevailing quote / tick rule) — see the
  spread-decomposition skill for Lee–Ready classification.

## Key takeaways
- Never feed raw transaction prices into models that assume
  continuous, normally distributed prices — the bounce and fat tails
  will corrupt the estimates.
- Choose the sampling clock deliberately: clock-time for calendar
  studies, volume-time for liquidity studies, duration for event
  detection.
- Interpolation beats last-tick carry-forward for building regular
  series from tick data.
