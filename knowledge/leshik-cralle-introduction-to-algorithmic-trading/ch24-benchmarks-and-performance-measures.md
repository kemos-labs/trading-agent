# Chapter 24 — Benchmarks and Performance Measures

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## The toolkit

- **VIX**: indicator of implied volatility from S&P 500 options; high
  readings coincide with fear/uncertainty, low with calm (may portend a
  rise). Best interpreted at *extremes*.
- **Beta (β)**: relative volatility vs. a benchmark (S&P 500), from a
  linear regression of daily returns (usual lookback ~1 year; short
  lookbacks give a "beta series" for trend analysis). β = 1 ⇒ parallel;
  β = 2.2 ⇒ 4.4% move for a 2% index move. Portfolio use: diversify
  stock-specific risk toward β ≈ 1; typical range 0.5–4.
- **Alpha (α)**: risk/volatility-discounted performance — the stock
  return when the benchmark return is 0. `α = RET_stock − β·RET_bench`.
  Example: β=2 stock returns 12% while benchmark returns 5% ⇒ α =
  12% − 10% = **2%**. (The book uses "ALPHA" generically for
  profit-targeted algos.)
- **Sharpe ratio**: (return − risk-free)/σ(returns); for short-holding
  ALPHA ALGOS simplified to average return window / σ of their sum
  (risk-free dropped for short periods). Caveat: very sensitive to
  trade frequency (per Irene Aldridge's article).
- **bp/sec and bp/trade** (the authors' favorites): bp/sec = absolute
  cumulative profitability of an algo in *time*; bp/trade shows the
  intra-trade profile (e.g., 150s trade averaging 1 bp/s may have
  peaked at 30 bp/s and stalled at 0). Excel templates can show a
  real-time running cumulative bp return per trade.

## Key takeaways

1. Alpha = stock return beyond β·benchmark; beta from regression with
  lookback-sensitive results (risk quantification is "quite complex and
  possibly not even achievable").
2. Sharpe is frequency-sensitive; for intraday work use bp/sec
  (profitability per unit of time at risk).
