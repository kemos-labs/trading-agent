# Chapter 24 — Volatility Skews

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## What a skew is

In a Black-Scholes world all strikes of one expiry share one volatility;
in reality implied volatility varies across strikes (FTSE 100 June 2012
example). The market is pricing the model's weaknesses + hedging
demand. Shape names: skew (monotonic), smile (U), smirk.

**Three canonical skews** (driven by who hedges):
- **Investment skew** (stocks/indexes): longs dominate; they *buy*
  OTM protective puts (low strikes) and *sell* OTM covered calls (high
  strikes) → low-strike IV inflated — "skew to the downside". Also
  consistent with markets getting more volatile when falling (higher
  vega ATM + vol-up when price-down ⇒ the 95 put gains on both counts,
  the 105 call on neither).
- **Demand/commodity skew** (ag, energy): end users dominate; buy
  calls at high strikes, sell puts at low → high strikes inflated.
- **Balanced skew** (FX): both sides hedge → symmetric about spot
  (need not be flat).

## Modeling the skew

- Fit a polynomial to IV(strike): `y = a + bx + cx² + dx³ + …`.
  **Sticky-strike** (fixed per strike) vs. **floating skew** (shift the
  whole curve with spot/IV). Better axes: moneyness X/S, then ln(X/S),
  then standard deviations from ATM:
  `z = ln(X/S)/(σ√t)` → *sticky-delta* skew (comparable across
  expiries). y-axis: IV − ATM IV, or better IV/(ATM IV) (scales when
  vol doubles).
- **Skewness** (tilt, coefficient b) and **kurtosis** (curvature, c ≥ 0
  for all listed markets) are inputs with sensitivities: ATM is the
  pivot (both ≈ 0 there); raising skewness raises high-strike vol,
  lowers low-strike (high strikes +, low strikes −); raising kurtosis
  raises both wings (+ for all non-ATM). Most skew-sensitive: ±25-delta
  options (benchmark: 25Δ put IV − 25Δ call IV); most kurtosis-
  sensitive: ±5 delta.
- **Skewed Greeks**: with a floating skew, an OTM put's delta is
  adjusted — spot +1 (value −0.20 by delta) + skew shift (+0.5 vol ×
  vega 0.10 = +0.05) → *adjusted delta* −15. Skew complicates all risk
  measures; a pragmatic split: skew model for values, flat model for
  Greeks (or engineer proper sensitivities for big books).
- Combine term structure × skew = the **volatility surface**.

## Volatility shifts & real-world deltas

- Demand-skew markets: spot up ⇒ IV up (positive relation); investment-
  skew markets: spot up ⇒ IV down (inverse). So an "delta-neutral" ATM
  straddle in an index is really **delta negative** (wants falling
  market → higher vol); in a commodity, delta positive.

## Skew & kurtosis strategies

- **Skew view**: buy low strikes/sell high strikes (or reverse) using
  ±25Δ options; delta-hedge with the underlying = a **risk reversal**
  (+10 Jun 95 puts (−25Δ), −10 Jun 105 calls (+25Δ), +5 underlying).
  Prefer legs of equal *vega* to isolate the slope from level moves.
- **Kurtosis view**: kurtosis up → buy strangles (both wings); down →
  sell strangles. Neutralize vega with ATM straddles (ATM is kurtosis-
  neutral); 2 strangles : 1 straddle = **dragonfly**.
- **Cross-month skew trades**: buy put calendars / sell call calendars
  when skews are mispriced relative to each other (put calendars
  capture skew *and* cheap June vol; avoid call calendars where the two
  effects cancel). Same for strangles across months (pick equal-vega
  strangles → pure kurtosis).

## Implied distributions (butterfly decoding)

All 5-point butterflies over all strikes sum to exactly the strike
spacing (5.00) at expiry → in a risk-neutral world, **P(spot = strike
at expiry) = butterfly price / spacing**. Refine with finer strikes
(0.10 → near-continuous). Skew-implied distribution (FTSE example) vs.
lognormal: *more small-up, more big-down, fewer mid-down, fewer big-up*
— typical of indexes; wheat's is closer to lognormal. Compare your own
probability view with the market-implied distribution to find trades.

## Key takeaways

1. The skew is the market's honest statement about the model's flaws
   and hedging demand — treat it as a model *input*, not noise.
2. Trade skew with risk reversals (vega-matched, delta-hedged); trade
   kurtosis with strangles vs. ATM straddles (dragonflies).
3. Butterfly prices let you extract the market's implied terminal
   distribution and spot disagreements.
