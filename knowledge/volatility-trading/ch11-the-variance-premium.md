# Ch11 — The Variance Premium

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## The premium

Index-implied volatility (from option prices) has a persistent tendency to
be **higher than subsequently realized volatility** — the variance risk
premium (VRP). Selling index vol (short straddles/strangles, variance
swaps) earns a positive average return for bearing the risk of vol
spikes. It is one of the most robust, documented premia in finance, but it
is a *risk* premium: you get paid for taking crash/vol-spike risk, and the
payoff is negatively skewed.

## Why it exists

- **Demand for crash insurance**: portfolio managers systematically buy OTM
  index puts → pushes index IV up, especially the put skew. Sellers
  (insurance writers) demand compensation.
- **Behavioral**: overreaction to recent vol and to tail events keeps IV
  rich; recency bias means IV is slow to decline after crises.
- **Structural**: many institutions must own protection (cannot sell it),
  creating one-sided demand.
- **Stochastic vol / jumps**: the risk-neutral measure overweights
  high-volatility states; the premium compensates for bearing
  volatility-of-volatility.

## Measuring and harvesting

- **Measure**: compare model-free implied variance (VIX²-style construction
  from the option strip) against subsequent realized variance
  (sum of squared returns). The average gap (in vol points) over history is
  the premium.
- **Harvesting vehicles**: short index straddles/strangles, variance swaps,
  short VIX futures (in contango). All express the same bet; variance
  swaps isolate pure variance exposure (no path dependence), options add
  gamma/skew effects.
- **Skew decomposition**: the OTM-put portion of the VRP is bigger than the
  ATM portion — selling the put skew is where most of the premium lives,
  but it's also where the tail risk concentrates.
- **Timing**: the premium is not constant — it widens after crashes (IV
  spikes) and narrows/occasionally inverts in calm rich markets. Entry
  after vol spikes (selling rich IV) has historically been the better
  risk-adjusted entry than constant harvesting.

## Risks

- **Fat left tail**: a single crash can give back years of premium
  harvesting (e.g. short-VIX blowups). Position size, stop rules, and
  hedging matter more than the edge's existence.
- **Regime changes**: the premium can persist for decades then compress;
  strategy decay is real.
- The premium is *not* a free lunch: it's selling insurance.

## Key takeaways

- Index IV > realized vol persistently: the variance risk premium.
- Rooted in crash-insurance demand, behavioral overreaction, and vol-of-vol
  compensation; it lives disproportionately in the put skew.
- Harvest via short index vol/variance; size for the fat left tail; entry
  after vol spikes historically better than steady harvesting.
- It is a risk premium — selling insurance, not a free lunch.
