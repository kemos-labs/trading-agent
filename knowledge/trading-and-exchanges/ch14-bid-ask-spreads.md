# Ch14 — Bid/Ask Spreads

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 14.

## Purpose
The quantitative heart of the book: what determines the spread, how to
estimate its components, and why it varies across stocks and time.

## Spread decomposition
The quoted half-spread must cover three expected costs:
1. **Order-processing cost** (a) — a fixed operational cost per share;
   relatively constant.
2. **Inventory-holding cost** — proportional to the dealer's risk: for
   volatility σ and trade size Q, the risk is roughly
   `σ·√t · Q` over holding period t; a risk-averse dealer prices it
   into the half-spread.
3. **Adverse-selection cost** — the expected loss to informed flow:
   if the probability of an informed trade is π and the informational
   value is δ, the cost is roughly `π·δ`.

## The Glosten–Milgrom logic
- The spread exists **even with zero processing costs and zero
  inventory risk** — purely because liquidity suppliers cannot
  distinguish informed from uninformed flow.
- The market-maker's bid is the expected value *conditional on the
  seller being informed*; the ask is value conditional on the buyer
  being informed. The spread is the information gap.
- Quote updates are Bayesian: after a buy, the dealer raises the
  posterior on good news (and the ask); after a sell, lowers it. This
  is the mechanism of price discovery through the spread.

## What widens/narrows spreads
- **Wider**: higher volatility, more informed trading (small caps,
  news periods), larger trade sizes, fewer competitors, wider ticks,
  lower volume, higher inventory risk.
- **Narrower**: more liquidity providers, competition, smaller tick
  sizes, higher volume, less information asymmetry, market makers'
  obligations.

## Empirical measurement
- **Quoted spread** = ask − bid; **effective spread** = 2·|trade price
  − midpoint| (what traders actually pay); **realized spread** =
  effective spread minus the post-trade price move (the component
  retained after paying the informed).
- `effective = realized + price impact` — the standard decomposition
  estimated from trade and quote data.

## Key takeaways
- The spread is an **information tax**, not just a fee: its
  adverse-selection component is the market's estimate of how much
  your flow knows.
- Realized spread (not quoted) is what liquidity providers actually
  earn; the gap between effective and realized is the cost of informed
  trading.
- When designing execution, the effective spread is the immediate cost
  of a market order; patient strategies can earn the spread by
  supplying liquidity instead of demanding it.
