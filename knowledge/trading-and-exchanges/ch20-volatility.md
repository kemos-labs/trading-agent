# Ch20 — Volatility

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 20.

## Purpose
What volatility is, its two components (fundamental vs. transitory),
what causes each, and how to measure them separately.

## The two components
1. **Fundamental volatility** — price changes caused by new
   information about value. Permanent: subsequent price changes are
   unrelated to them. The *good* volatility: it is price discovery.
2. **Transitory volatility** — price changes caused by order-flow
   imbalances and liquidity demand (uninformed trading, bluffs,
   anticipator activity, bid/ask bounce). Reverting: prices bounce
   back when the imbalance clears. The *costly* volatility: it is
   liquidity friction, not information.

## What causes each
- Fundamental: news, earnings, macro surprises — anything that changes
  the expected cash flows or discount rates.
- Transitory: large uninformed orders hitting thin books, stop-loss
  cascades, margin calls, manipulation, and the **bid/ask bounce**
  itself (trades alternating between bid and ask create
  mean-reverting quote noise).
- Both rise together in crashes: bad news (fundamental) plus panicked
  liquidity demand (transitory).

## Measuring them
- **Variance ratio tests**: if price changes are purely fundamental
  (random walk), the variance of k-period returns ≈ k·variance of
  1-period returns. Transitory volatility makes short-horizon variance
  *too high* relative to long-horizon variance → variance ratio < 1.
- **Bid/ask bounce correction**: signed trade decomposition isolates
  the bounce component.
- **Roll's estimator**: autocovariance-based spread estimator
  `spread = 2·√(−cov(Δp_t, Δp_{t−1}))`.
- Realized volatility at multiple horizons separates persistent
  (fundamental) from reversionary (transitory) components.

## Key takeaways
- Don't treat all volatility as risk: **fundamental volatility is the
  information you trade on; transitory volatility is the cost you
  pay**. Strategies differ fundamentally in which they harvest.
- High-frequency mean reversion strategies monetize transitory
  volatility; they are short the other side's liquidity needs.
- Variance-ratio analysis of your instruments reveals how much of the
  observed volatility is friction — and therefore how much a
  liquidity-supplying strategy might earn.
