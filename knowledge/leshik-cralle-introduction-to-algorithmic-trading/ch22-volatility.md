# Chapter 22 — Volatility

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Measurement

- **Realized volatility** = estimates from intraday squared returns at
  short sampling intervals (~5 min is common usage; the authors use
  shorter, tick-valued intervals ≈60s or less).
- Classical: standard deviation of returns,
  `σ = √( Σ(r_i − μ)² / (P−1) )` over P periods (sample σ).
- Also used: σ of raw prices; and the **high–low "range-based"
  (extreme-value) method** with very short lookbacks (200–500 ticks,
  vs. usual daily usage).
- **Preferred metric: intraday %Range averaged over 200T** — comparable
  across stocks. Generate a time series of it to see volatility change
  over time, from one-session intraday (100T lookbacks) up to ~20
  sessions; also EOD time-series tracking of volatility (± "volatility
  of the volatility").

## Behavior

- **Volatility clustering**: short periods of increased amplitude bunch
  together (10T window chart); a high-clustering day is often followed
  by another, and tranquil periods follow tranquil periods.

## Key takeaways

1. Realized vol from short-interval squared returns; %Range(200T)
   normalized is the authors' cross-stock comparable.
2. Clustering ⇒ regime awareness in parameterizing stops and triggers.
