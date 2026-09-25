# Chapter 3 — Algos Defined and Explained

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Definitions & key concepts

- **Algorithm**: a deterministic, step-by-step plan — inputs in, outputs
  out; same inputs ⇒ same results. Basic algos are deterministic; the
  book's are Excel-function-language formulas embedded in templates that
  recompute on each incoming tick and "trigger" when a calculation
  parameter attains a BUY/SELL condition (order placement deliberately
  manual to teach the process).
- **Parameters**: values (usually trader-set) the algo uses; sometimes
  *adaptive* (computed by the algo from inputs). Parameter setting is
  the most crucial — and hardest — step for profitability: skill +
  experience + trial and error.
- **Protective stop loss on every trade**: an *adaptive* algo computed
  right after fill; essential component (the authors' LC Adaptive
  Capital Protection Stop, ch. 25).
- **Electronic pit** metaphor: thousands of traders viewing identical
  real-time data; feed fields: ticker symbol, timestamp, volume, trade
  price.

## Architecture of the book's system

Real-time feed → Excel template (embedded algo formulas) → trigger
condition appears on the spreadsheet → trader manually places the order
via the OMS. Future possibility: fully automated order placement.

## Key takeaways

1. Algo = deterministic function of (data, parameters); parameters are
   where the edge (or loss) comes from.
2. Stops are non-negotiable, and should be adaptive to recent volatility
   rather than fixed percentages.
3. Start with manual execution to build understanding before automating.
