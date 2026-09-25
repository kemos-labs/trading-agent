# Ch08 — Statistical Arbitrage Strategies

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 8.

## Purpose
Stat-arb (value-motivated) strategies: detecting statistically
persistent relationships with economic roots, and trading deviations
from them. The key discipline: relationships must have *fundamental*
foundations, not spurious data-mining correlations (the "Spaghetti
Principle" — if you throw data at statistics, something sticks, but it
falls apart in production).

## The pairs-trading recipe (formula core)
1. **Universe**: only instruments liquid at the trading frequency
   (e.g., trade at least hourly).
2. **Spread**: `ΔS_{ij,t} = S_{i,t} − S_{j,t}` over T observations
   (≥30 minimum per CLT; 500 daily obs ≈ 2 years preferred).
3. **Selection**: pick pairs with the most stable relationship —
   e.g., minimize Σ(ΔS)² (Gatev–Goetzmann–Rouwenhorst) or use
   cointegration tests.
4. **Statistics**: mean `E[ΔS]` and std `σ[ΔS]` of the spread.
5. **Trigger**: if `ΔS > E + 2σ` → sell i, buy j; if `ΔS < E − 2σ` →
   buy i, sell j (Bollinger-style bands on the spread).
6. **Exit**: close when the spread reverts to a target gain; stop-loss
   if it widens against you. Use rolling/weighted estimates to adapt
   to changing conditions.

## Strategy catalog by asset class
- **Equities**: pairs, dual-class shares, market-neutral pairs,
  liquidity arbitrage, large→small information spillovers.
- **FX**: **triangular arbitrage** — synthetic cross vs. market:
  `EUR/CAD_synth = EUR/USD × USD/CAD`; buy the cheaper leg, sell the
  synthetic, reverse on convergence. Requires simultaneous sampling
  (1-second delays destroy the signal) and spread costs ≤ the gap.
  **UIP arbitrage**: `(1+i_t) = (1+i*_t)·E[S_{t+1}]/S_t`; estimate in
  regression form `ln S_{t+1} − ln S_t = α + β(ln(1+i) − ln(1+i*)) + ε`
  and trade statistical deviations; works best 4–9 pm ET (Chaboud–
  Wright).
- **Indices/ETFs**: index composition arbitrage — sell the
  index-mimicking portfolio and buy the index (or vice versa) when
  they diverge beyond costs; cointegration-based (Alexander 1999).
- **Options**: pairs with different expirations/strikes on the same
  underlying (volatility curve arbitrage).
- **Cross-asset**: futures basis trading (futures vs. underlying;
  cost-of-carry), futures/ETF arbitrage.

## Trader-type mapping (per Harris)
Value-motivated → stat-arb; informed → directional (aggressive,
market orders); liquidity traders → market making (limit orders).

## Key takeaways
- The 2σ band on a spread is the workhorse trigger; the edge is in the
  *stability* of the relationship, not the band.
- Every arbitrage must clear transaction costs (two spreads minimum
  for triangular arb) and must be timed coherently (simultaneous
  quotes).
- Economic grounding separates durable relationships from sunspot-style
  spurious ones.
