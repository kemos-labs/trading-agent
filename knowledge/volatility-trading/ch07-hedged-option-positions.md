# Ch7 — Hedged Option Positions

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## Distribution of hedged P&L

A delta-hedged option position has a P&L distribution, not a fixed
outcome. Understanding it requires more than the mean (½Γ(σ_r²−σ_i²)S²):

- **Skewness**: short-vol (short gamma) positions are positively skewed in
  the *daily* P&L but have a negatively skewed tail over the trade's life
  (rare large losses from vol spikes); long-vol is the mirror.
- **Kurtosis**: hedged P&L is fat-tailed; the "smooth theta" of a short
  straddle hides tail risk that only shows in the distribution's extreme
  quantiles.
- **Volatility dependency**: if realized vol is itself volatile, hedged P&L
  has wider dispersion — you can predict vol correctly and still lose on a
  single trade; the edge only shows statistically over many trades.

## Path dependency

Hedged positions are highly path-dependent: the same realized vol achieved
via a smooth grind vs. violent swings produces different P&L because of
when rebalancing occurs (and because gamma is a function of spot).

- Hedging once a week vs. once a day produces different cost and risk
  profiles: more frequent hedging captures gamma better but pays more
  spread.
- Terminal stock price matters beyond realized vol — the final delta hedge
  and the option's remaining time value interact (this is why the "P&L =
  gamma capture" identity is approximate).

## Position-level concepts

- **Long options**: pay theta, collect gamma (realized > implied makes
  money). Positive vega.
- **Short options**: collect theta, pay gamma (need realized < implied).
  Negative vega; selling vol earns the premium but inherits tail risk.
- The **bleed** (theta) vs. **gamma capture** trade-off is the whole game;
  sizing and hedging frequency tune the balance.
- Aggregation across underlyings: hedging a book of many stocks with index
  products shifts risk from individual-name to market/correlation risk —
  cheaper but riskier; use hedging bands per name plus index-level risk
  tracking.

## Practical guidance

- Model the *distribution* of hedged P&L, not just its expected value:
  simulate the hedge path (bootstrap realized vol, rebalance at your policy)
  and look at quantiles.
- Account for vol-of-vol: the dispersion of the trade's outcome scales with
  how wrong the vol forecast can be.
- Choose hedge frequency/bands based on cost vs. risk trade-off measured on
  your actual execution costs, not theory.

## Key takeaways

- Delta-hedged P&L has skew and fat tails; short-vol harvests theta but
  sells a tail.
- Path-dependence means realized vol alone doesn't determine the outcome.
- Simulate the hedge path to see the real distribution; set hedging policy
  from measured costs and risk tolerance.
