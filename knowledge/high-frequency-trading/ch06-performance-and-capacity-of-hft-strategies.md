# Ch06 — Performance and Capacity of HFT Strategies

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 6.

## Purpose
How to measure HFT strategy performance (the three P's), evaluate
capacity, and understand alpha decay.

## Principles: the three P's
- **Precision**: statistical exactitude to separate winners from
  losers; **Productivity**: standardized, scalable metrics;
  **Performance**: real-time monitoring at tick frequency.
- All require the least-processed data — tick data is the most
  informative.

## Basic performance measures
- **Return**: simple `R = P_t1/P_t0 − 1` or log `r = ln P_t1 − ln P_t0`
  (nearly identical at high frequency).
- **Volatility**: standard deviation of returns; weighted deviation
  (later obs weighted more, `w_i > w_{i+1}`); OHLC-based estimates;
  high−low range; average squared returns (GARCH-friendly).
- **Drawdown**: max peak-to-trough loss between high-water marks;
  the basis of hedge-fund performance fees.
- **Win ratio**: fraction of profitable trading periods.
- **Sharpe ratio**: with HFT, the risk-free rate is often omitted —
  positions aren't held overnight, so the HFT Sharpe is
  `E[R]/σ[R]` and is **invariant to leverage** (both numerator and
  denominator scale by L) — a crucial property for sizing.
- VaR and modified VaR (accounting for fat tails); Sortino and other
  downside variants give comparable strategy rankings (Eling &
  Schuhmacher 2007: Sharpe is adequate).

## Performance attribution
- Factor structure: strategy return regressed on systematic factors
  `R_it = α_i + Σ b_ik·F_kt + u_it`; α is genuine added value. If β is
  high and α low, just buy the benchmark — it's cheaper and more
  liquid. Fung–Hsieh eight global factor groups (equities, bonds,
  cash, gold, dollar index) serve as benchmarks.

## Capacity
- HFT capacity is **not** limited only by market impact: limit-order
  strategies also face **probability of execution** and **transparent
  costs**. Market-order-only capacity = best-bid/ask depth, but most
  HFT uses limit orders.
- Capacity measured via the efficient frontier of cost vs. size; alpha
  decays as capacity grows and as competitors copy the strategy.

## Key takeaways
- Because the HFT Sharpe ratio ignores the risk-free rate and scales
  with leverage, HFT strategies can sustain far higher leverage than
  their Sharpe implies — the binding constraint is drawdown, not
  Sharpe.
- Attribution tells you if you're paying for alpha or beta; a
  benchmark-dependent strategy is worth replacing by the benchmark.
