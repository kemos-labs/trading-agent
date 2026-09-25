# Ch15 — Block Traders

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 15.

## Purpose
How large institutional orders (blocks) are traded: the search
problem, the upstairs market, and why block execution differs
structurally from retail execution.

## The block trader's problem
- A block (typically ≥10,000 shares) is far larger than displayed
  depth. A naive market order would move the price several times the
  spread — a **market-impact cost** far exceeding commissions.
- The core difficulty is **search**: finding counterparties willing to
  absorb size at a reasonable price without leaking the order's
  existence.

## The upstairs market
- Large orders are worked by **block positioners** (dealer-brokers)
  who search their client network for natural counterparties —
  matching buyers and sellers **before** exposing the order to the
  floor/electronic market.
- If the block cannot be crossed, the positioner may **take the other
  side** (risk capital) and unwind gradually — earning the discount
  for providing immediacy to a large order.
- Upstairs trading is **opaque by design**: pre-trade information
  control is the block trader's most valuable asset; leaks destroy
  the positioner's economics.

## Price discovery for blocks
- Blocks trade at a **discount/premium relative to the small-order
  market** — the "block discount" compensates the liquidity supplier
  for search and risk.
- The positioner's bid depends on: expected cost of unwinding
  (volatility, market depth), probability the seller is informed, and
  competition from other positioners.
- **Worked orders** (algorithmic slicing): executing a large order as
  many small orders over time to minimize impact — the modern
  successor to the block search.

## Key takeaways
- Large orders face **three distinct costs**: spread, market impact
  (price pressure), and opportunity cost (delay); block trading is the
  art of trading them off.
- Information control is worth money: the marginal dollar of impact
  cost avoided by hiding the order exceeds most visible fees.
- The choice between a block trade (pay for immediacy, reveal intent
  to a positioner) and an algorithm (pay in time, hide intent) depends
  on urgency and on how informed the flow is believed to be.
