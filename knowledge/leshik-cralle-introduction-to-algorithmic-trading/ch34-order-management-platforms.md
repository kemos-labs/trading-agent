# Chapter 34 — Order Management Platforms & Order Execution Systems

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Definitions (functionally the same)

OMP, OES, and other acronyms overlap; the trend is to merge them by
evolutionary survival. A trader cares what it *does*, not the name.

## OMP features

- Ticker info, real-time bid/ask, Time & Sales (streaming transactions),
  selectable order types (the authors use only **Market and Limit**
  orders).
- Show waiting orders, part-fills with prices, average trade price;
  live trades with open P&L and closed trades with P&L; written to a
  downloadable log for archive.

## Execution system (bare bones)

- Finds best routing for an order. The authors find little value in
  special routing for their small (1,000–2,500-share) trades — they
  often specify routing (often to an **ECN**, Electronic
  Communications Network) when placing the order.
- ECN: Buy/Sell orders matched automatically at your limit price;
  marking "ECN only" restricts liquidity, which is a non-issue at the
  authors' trade sizes.

## Key takeaways

1. OMP = info + order entry + P&L + downloadable log; only Market/Limit
   orders needed for the ALPHA ALGO method.
2. ECN routing suffices for small trades; smart routing adds little
   value at 1k–2.5k shares.
