# Ch6 — Hedging

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## Purpose of hedging

Hedging converts an option position into a volatility trade: it removes the
directional (delta) risk so the P&L depends on realized vs. implied
volatility, not on where the underlying goes. Hedging is not about making
directional profits — it is about managing the volatility trade in the
cheapest possible way.

## Mechanics

- **Delta hedge**: hold Δ shares (or futures) against each option so the
  portfolio is first-order market-neutral. As spot moves, delta changes →
  rebalance. Discrete rebalancing at cost is the real world.
- **Theta–gamma trade-off**: a delta-hedged long option position earns
  theta decay but loses on gamma as it is rebalanced; the expected P&L per
  interval ≈ ½·Γ·(σ_real² − σ_implied²)·S²·dt. You make money when realized
  vol exceeds implied (long), lose when it underperforms.
- **Breakeven vol**: the realized vol at which the hedged long option makes
  zero P&L over its life ≈ the implied vol (approximately, ignoring costs
  and higher-order terms). Transaction costs raise the breakeven for long
  hedgers and lower it for short-vol traders.

## Hedging frequency & cost

- Hedge **less often**: fewer rebalances → lower transaction costs, but more
  gap risk (unhedged moves between rebalances). Optimal frequency balances
  gamma risk vs. cost.
- **Leland adjustment**: to value an option with discrete-cost hedging,
  replace σ with σ_adj ≈ σ·√(1 + A) where A is proportional to the round-trip
  cost per rebalance scaled to the rebalance interval — i.e. costs can be
  modeled as a volatility increase. The same idea gives break-even vol for
  short-vol strategies.
- Use **hedging bands** (rebalance when delta moves by X) or scheduled
  rebalancing; both reduce costs vs. continuous hedging.
- **Aggregation**: hedge net delta across the whole book, not per option —
  offsetting risks inside the book save costs; accept correlation risk in
  exchange for transaction savings (e.g. hedge stock deltas with index
  products). Factor models (BARRA/APT) can quantify cross-hedges.

## Practical notes

- Hedging makes volatility trading **path-dependent**: you can be right on
  vol and lose money because of bad hedge timing or costs. This is a
  feature of the business, not a bug.
- Delta is model-dependent: with skew/surface dynamics, the "right" hedge
  ratio changes; measure how deltas behave under the surface regime.
- Execution quality is the biggest controllable factor — the market-taker
  pays the spread on every hedge.

## Key takeaways

- Hedging converts price risk into volatility exposure; its P&L is
  realized-vs-implied over the position's life.
- Expected hedged P&L ≈ ½Γ(σ_r²−σ_i²)S²; trade costs shift the breakeven.
- Hedge less and aggregate; bands and netting beat continuous per-leg
  hedging.
- Track hedge costs — they are part of the trade's expected value.
