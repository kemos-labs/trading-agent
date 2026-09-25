# Chapter 23 — Returns: Theory

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Findings

- The **absolute size of returns is a function of the measurement
  frequency**; lookback lengths range from "boxcar" to EOD. A stock
  with 30,000 transactions can be studied with, e.g., lookback 1,000
  and returns at 200T.
- The definitive generating-function formulation of returns remains
  debated — the task's complexity is enormous; charts of return-length
  effects (CD file RETURNS) are the practical route to understanding.
- From the return-window analyses one can *guess*: how long to hold a
  trade, what the "perfect" return might be, and the probabilities —
  but an **optimum holding time cannot be derived a priori**; it must
  be inferred from recent data, and it **fluctuates in synch with the
  stock's current volatility**. Stocks in the same cluster appear to
  have similar optimum holding times.
- Charts use 200T-spaced vertical gridlines to gauge what a particular
  holding time would produce.

## Key takeaways

1. Return magnitude is scale-dependent (power-law-ish with sampling
   frequency); no a-priori optimal holding time — infer it from recent
   data, per cluster.
2. Optimum holding time co-moves with the stock's volatility regime.
