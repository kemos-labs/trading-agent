# Ch19 — Liquidity

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 19.

## Purpose
A formal treatment of liquidity: its four dimensions, how to measure
each, and how liquidity providers earn their compensation.

## The four dimensions
1. **Width** — the bid/ask spread: the cost of trading a small
   quantity immediately.
2. **Depth** — the size available at the quoted prices (and beyond);
   how much you can trade before price moves.
3. **Immediacy** — how quickly an order executes; for some orders,
   waiting is the price.
4. **Resiliency** — how fast prices revert after a temporary order
   imbalance (the speed of recovery after impact).

## Measurement toolkit
- **Quoted spread** and **effective spread** (2·|price − mid|);
  effective spread is what a marketable order actually pays.
- **Depth**: displayed sizes at best bid/ask; order-book depth curves.
- **Impact**: price change per unit of traded volume — e.g. the
  **Amihud measure** `|r|/volume`, or slope of a market-impact
  regression.
- **Turnover and volume**: activity proxies for liquidity availability.
- **Bid/ask bounce**: the transitory volatility from trades crossing
  the spread — a *cost*, not information.

## Who provides liquidity
- **Dealers** (quote-driven), **limit order traders** (order-driven),
  **block positioners** (upstairs), and increasingly **automated
  market makers**.
- Compensation: the spread, minus adverse selection (the realized
  spread is the true payment), plus any maker rebates.
- Liquidity is **episodic**: it evaporates when uncertainty spikes —
  suppliers withdraw, spreads widen, depth thins, resiliency drops,
  exactly when demand peaks.

## Key takeaways
- Liquidity is not one number: **width, depth, immediacy, and
  resiliency** must all be measured to understand a market's cost
  profile.
- For a trader, the question is *which dimension am I buying?* —
  paying the spread buys immediacy; resting in the book sells it.
- Liquidity risk (the inability to transact at reasonable cost when
  you need to) is a distinct risk factor and should be priced and
  stress-tested like any other.
