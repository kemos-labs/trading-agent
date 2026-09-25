# Ch03 — Market Microstructure, Orders, and Limit Order Books

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 3.

## Purpose
The order-driven market machinery HFT operates in: limit order books,
matching rules, order types, and modern fragmentation across asset
classes.

## Markets and the CLOB
- Most modern exchanges are **centralized limit order books (CLOBs)** —
  double-sided auctions where all limit orders are recorded in a price/
  size table; pioneered in the U.S. in the early 1970s.
- **Liquidity** = cumulative size of limit orders available to meet
  market orders; it is finite and measurable (Demsetz, 1968).
- Books are typically **asymmetric and non-normal** — the standard
  theoretical assumptions don't hold in practice.
- **Dark pools** (e.g., Liquidnet) don't display their books; ~22% of
  U.S. equity volume trades dark (2011). Dark pools appeal to large
  investors who don't want to reveal size; lit venues display the book.

## Matching mechanics
- A market buy order matches the best ask; if larger than the best ask
  queue, it **sweeps** up the book, consuming liquidity and widening
  the spread (slippage for later orders).
- Priority: most exchanges use **price-time priority (FIFO)**; some
  futures use pro-rata. Sweeps create the transient liquidity gaps HFT
  strategies exploit.

## Order types (beyond market/limit)
- **Iceberg/hidden**: display a slice, hide the total (privacy; costs
  more).
- **Stop/trailing stop**: risk control (liquidation triggers).
- **Market-on-close, midpoint match, sweep-to-fill**: speed.
- **Fill-or-kill, good-till-canceled**: time-to-market control.
- Algo-enabled: POV (percentage of volume) etc.

## Fragmentation and regulation
- Equities: **NBBO** rule (2005, Reg NMS) — orders must execute at the
  national best bid/offer or better; exchanges lacking NBBO liquidity
  must route orders onward. SIP aggregates and disseminates quotes.
- Futures: no centralized pricing, but daily margining/mark-to-market.
- FX: fully OTC, no centralized quotes; interdealer networks for
  select participants. Options: many venues, little activity.
- Asset classes differ, so market structure is fragmented by design.

## Key takeaways
- The order book is the HFT battlefield: who is at the touch, queue
  position, and depth behind the best quotes determine what market
  orders can do.
- Rebate structures (maker/taker, normal vs. inverted) segment traders
  by whether they add or remove liquidity (see ch12 for the economics).
- Reg NMS's NBBO routing mandate is why HFT can trade the same name
  across many venues at once.
