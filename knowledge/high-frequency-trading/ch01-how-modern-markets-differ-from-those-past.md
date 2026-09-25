# Ch01 — How Modern Markets Differ from Those Past

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 1.

## Purpose
Documents the 50-year structural transformation of securities markets —
from manual, broker-centric 1970s trading to today's technology-enabled,
democratized markets — and defines what HFT is (and is not).

## The 1970s vs. today
- **1970s**: discretionary asset managers, manual market makers,
  manual arbitrageurs, retail flow; a single not-for-profit exchange per
  asset class; high transaction costs and low turnover; errors from
  verbal orders; specialists with preferential access; brokers earned
  outsized commissions (Buttonwood agreement capped the minimum
  commission at 0.25% of volume).
- **Today**: quantitative managers, automated market makers and
  arbitrageurs, ATS/dark pools, algorithmic execution. Falling hardware
  costs (driven largely by video-gaming demand) made
  technology-enabled trading cost-effective; error rates collapsed and
  commissions fell ~100× ($70/trade in 1997 → ~$0.70 today).
- The power shift: customers now generate their own research and even
  build their own execution algos; brokers' role narrowed to best-
  execution facilitation.

## HFT vs. related terms
- **Electronic trading**: orders transmitted electronically (obsolete
  term — everything is electronic now).
- **Algorithmic trading**: automating execution once buy/sell decisions
  are made elsewhere (slicing, routing, timing).
- **Systematic trading**: computer-driven decisions, any horizon — may
  or may not be high frequency.
- **HFT**: systematic + algorithmic trading with **positions held one
  day or less, usually flat overnight**. HFT makes the full decision
  chain: signal generation, portfolio allocation, and execution.
  Equities are the most algorithmically executed asset class (>50% of
  volume).

## HFT's four strategy classes
1. **Arbitrage** (stat-arb, latency arbitrage) — trade price
   deviations from equilibrium.
2. **Directional event-based trading** — trade predictable short-term
   moves around news.
3. **Automated market making** — provide liquidity, earn the spread.
4. **Liquidity detection** — infer and exploit others' order flow.

## Key takeaways
- HFT is "algorithmic trading of positions with short holding periods"
  — the distinguishing feature is holding time, not technology per se.
- The democratization of access (anyone can quote) and plummeting
  transaction costs are the two durable market improvements of the era.
- Under Dodd-Frank, banks' prop HFT survived inside the market-making
  function as "prehedging" — run on client, not bank, capital.
