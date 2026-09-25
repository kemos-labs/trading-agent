# Ch12 — The VIX

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## What the VIX is

The VIX is the CBOE's model-free implied volatility index for the S&P 500:
an annualized, 30-day, risk-neutral expected volatility derived from a
weighted strip of OTM SPX options. Its construction avoids relying on a
specific pricing model — it synthesizes the variance swap rate.

## Construction

- **Model-free variance**: implied variance ≈ (2/T)·Σ_i (ΔK_i/K_i²)·
  e^(rT)·P(K_i) summed over a range of OTM puts and calls (the variance
  swap fair strike). The VIX = 100·√(implied variance annualized to 30
  days).
- This is the **variance swap rate**, not a historical or ATM vol: it
  embeds the skew (put premiums raise it) and the term structure
  (interpolated to a fixed 30-day maturity).
- Interpretations: market's risk-neutral expectation of 30-day S&P 500 vol;
  also a gauge of fear/insurance cost.

## Properties

- **Contango** (normal state): VIX futures/spot above subsequent realized
  vol → the variance premium is directly tradable via VIX futures (roll
  yield) — this is the "short VIX contango harvest."
- **Mean reversion + spikiness**: VIX is stationary, spikes on crashes,
  decays slowly (clustering + slow mean reversion); it's roughly lognormal
  with fat right tail.
- **Negative correlation with equities**: VIX and SPX returns are strongly
  negatively correlated (leverage effect); VIX acts as a cheap hedge/moment
  of the market.
- **Term structure**: normally upward (backwardation in calm → steep
  contango after calm; steepness collapses/inverts in crises).

## Trading implications

- **VIX futures/ETFs**: long-dated futures converge to expected future spot
  vol; the contango roll is a persistent drag for long positions and income
  for shorts — trade the term structure, not the spot level alone.
- **VIX options**: priced off VIX futures; their vol-of-vol is huge;
  options on VIX let you trade expected *future* vol-of-vol and tail risk
  with defined risk.
- **The VIX as forecast**: compare VIX to your realized-vol forecast over
  30 days — the gap is the trade (see variance premium). VIX reliably
  exceeds subsequent realized vol on average, but is a weak *point*
  forecast; the edge is statistical, not per-event.
- **Skew of VIX options**: heavily right-skewed (crash of the market = spike
  of VIX); pricing VIX options requires modeling the VIX's own dynamics
  (lognormal-ish, fat-tailed).

## Key takeaways

- VIX = model-free 30-day implied variance of the S&P 500, annualized and
  √-scaled; it is the market's variance-swap rate, skew included.
- Persistent contango = the tradable variance premium via futures.
- Mean-reverting, fat right tail, negatively correlated with equities.
- Trade the term structure and the VIX-vs-realized gap, not the spot level.
