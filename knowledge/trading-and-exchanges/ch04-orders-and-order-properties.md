# Ch04 — Orders and Order Properties

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 4.

## Purpose
The core taxonomy of orders: what order types express, how traders
choose among them, and why the choice is a trade-off among price,
certainty, and cost.

## The fundamental order properties
1. **Action** — buy or sell.
2. **Quantity** — size, including displayed vs. hidden/reserve size.
3. **Price** — limit price (maximum buy / minimum sell) vs. market
   (no limit; any price).
4. **Time conditions** — day, GTC (good-till-canceled), immediate-or-
   cancel (IOC), fill-or-kill (FOK), good-till-time.
5. **Discretion** — marketable vs. not; "not-held" orders let the
   broker/trader decide timing.

## Market vs. limit orders
- **Market orders** guarantee execution but not price; they **demand
   liquidity** (cross the spread, pay it).
- **Limit orders** guarantee price but not execution; they **supply
   liquidity** (rest in the book and are taken by market orders).
- A limit order is a **free option** granted to the market: if prices
  move against the limit trader, their order may execute at an
  unfavorable price; if prices move favorably, it often fails to
  execute ("winner's curse" of limit orders).

## Order-choice logic
- **Impatient traders** (need certainty) use market orders / marketable
  limits. **Patient traders** (cost-sensitive) use limit orders and
  wait.
- Hidden orders (reserve/iceberg) hide size to avoid revealing
  intentions but sacrifice time priority; they are used by large
  traders.
- Stop orders become market orders when a price level is hit — they
  are risk-management tools (stop-losses) and convert into liquidity
  demand at the worst moment (the stop-loss cascade).

## Key takeaways
- The market/limit distinction is the single most important concept in
  microstructure: **execution certainty trades off against price**.
- Limit order traders are systematically at an information disadvantage
  (they are picked off when news arrives), which is why spreads exist.
- Order type selection should follow from the trader's patience and
  information: informed traders prefer market orders (execute before
  the information leaks); uninformed patient traders provide liquidity
  via limit orders and earn the spread.
