# Ch11 — Order Anticipators

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 11.

## Purpose
Traders who trade *in front of* other traders' order flow: who they
are, how they detect orders, and whether they help or hurt markets.

## Who anticipators are
- **Front-runners** (classic): detect a large client order and trade
  ahead of it to profit from the anticipated price move.
- **Preferenced-dealer traders**: dealers who observe preferenced
  order flow and trade on its information.
- **Program-trade anticipators**: detect index-arbitrage program
  baskets and trade the underlying before they hit.
- **Crossing-network monitors**: watch for large crosses and trade in
  the underlying.
- Modern variants: order-flow prediction from the tape, ECN book
  monitoring, and co-located tick-data analysis (HFT anticipates
  institutional order flow).

## How they detect orders
- Observing **quote/order activity** in their own venue (dealer seeing
  its own order flow), **broker connections** (leaks, paid order-flow
  data), and **tape patterns** (repeated prints, odd sizes, timed
  sweeps).
- The more *visible and predictable* large order flow is, the more
  anticipators will trade against it.

## Do they help or hurt?
- **Hurt**: they add transaction costs to the orders they front-run,
  making large institutional orders more expensive and discouraging
  them — a tax on the people who need liquidity most.
- **Help**: anticipators can accelerate price adjustment — they often
  front-run *informed* order flow, moving prices toward value sooner;
  they also add depth while waiting.
- Net assessment depends on who they trade against: front-running
  uninformed flow is pure cost; front-running informed flow partly
  substitutes for price discovery.

## Key takeaways
- Anticipation is a **tax on order size**: the larger and more
  predictable your order, the more you pay.
- Defenses: hide size (icebergs, dark pools, algorithmic slicing),
  randomize timing, trade when others are least attentive, and use
  venues with tighter information controls.
- When reading the tape, distinguishing anticipators from informed
  traders matters: both move prices, but anticipators move them *before*
  the order, informing prices about order flow, not about value.
