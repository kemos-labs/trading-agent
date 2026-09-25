# Ch06 — Order-Driven Markets

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 6.

## Purpose
The mechanics of limit order book markets: how orders are stored,
prioritized, and matched, plus the pricing rules that govern
executions.

## The limit order book
- The book stores resting limit orders at each price level, with
  **buy-side (bid) and sell-side (ask) queues**.
- **Marketable orders** (market orders or marketable limits) execute
  immediately against the best opposite-side book prices; non-
  marketable orders join the queue.
- The **spread** is the gap between the best bid and best ask; **depth**
  is the quantity available at each level.

## Priority rules
- **Price priority**: better-priced orders always execute first.
- **Time priority**: within a price, earlier orders execute first —
  this rewards liquidity suppliers who are willing to wait.
- Alternatives: **size pro-rata** (futures markets allocate by size),
  **size priority** (larger orders first). Time priority is friendliest
  to small patient liquidity suppliers.
- **Crossing**: when a buy and sell meet, the trade price follows
  pricing rules — typically the *prevailing quote* (midpoint or the
  resting limit price), or a **uniform price** in call auctions.

## Pricing rules
- **Derivative pricing** (market orders execute at the resting limit
  price): liquidity-demanding traders pay the spread.
- **Midpoint pricing** (crossing networks): both sides save half the
  spread but face execution uncertainty.
- **Discriminatory vs. uniform**: continuous books are discriminatory
  (each order pays its own price); call auctions can be uniform (all
  trades at the clearing price), which improves fairness and
  incentivizes aggressive orders.

## Key takeaways
- Order-driven markets make **liquidity supply competitive**: anyone
  can post a limit order, and time priority rewards early suppliers.
- The book is a public record of liquidity demand/supply — reading it
  (depth, queue imbalance) is a primary signal for short-horizon
  traders.
- Call auctions concentrate liquidity: the same orders that would trade
  at several prices in continuous trading clear at one price,
  minimizing spread cost and maximizing volume at the open/close.
