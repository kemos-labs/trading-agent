# Ch13 — Dealers

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 13.

## Purpose
The dealer's business: quoting two-sided markets, managing inventory,
and the three costs that determine the spread they charge.

## The dealer's problem
- A dealer quotes a **bid** (buy) and **ask** (sell) and stands ready
  to trade either side at any time. Order flow is a **random walk of
  buys and sells**; the dealer's inventory bounces around a target.
- The dealer profits from the **spread** — buying at the bid, selling
  at the ask — but bears three costs that the spread must cover.

## The three costs (from Ch14)
1. **Order-processing costs**: the operational cost of handling the
   trade (labor, systems, clearing) — roughly a constant per trade.
2. **Inventory-holding costs**: the risk of holding a position that
   moves against you while you wait for offsetting flow. More risk
   (higher volatility, larger positions, longer holding) → wider
   spreads.
3. **Adverse-selection costs**: expected losses from trading with
   informed traders before prices adjust. The more informed the flow,
   the wider the spread.

## Inventory management
- Dealers **shade quotes** to manage inventory: long inventory → quote
  lower bid/ask (discourage buys, encourage sells); short → quote
  higher.
- They also trade with other dealers / hedge to rebalance, and they
  time their trading to avoid moving prices against themselves.
- **Inventory risk** is the reason dealers are willing to accept
  "toxic" order flow at a price: every fill is a bet on mean
  reversion.

## Key takeaways
- The spread is a **price for three services**: processing, inventory
  insurance, and information insurance. Shrink any cost and spreads
  narrow.
- A dealer's quotes encode their belief about the *probability of
  informed flow* — watching quote shading reveals how "toxic" the
  market currently thinks your flow is.
- Market-making is a risk business: the dealer who always quotes is
  short volatility, and in fast markets the losses to informed flow
  dwarf the spread income.
