# Chapter 11 — Our Nomenclature

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Definitions used throughout the book

- **Ticks**: T = trade (finest resolution); tick data = intraday real-
  time trade data. `nT` = number of ticks (e.g., 30T). Subscripts mark
  position: T₁₀ = the 10th tick; return intervals between T₀…T₁₂ span 13
  ticks.
- **Time**: t = time unit in seconds; `nt` = number of seconds;
  timestamp = exchange-reported execution time (hh:mm:ss).
- **EOD**: end-of-day totals for the whole session.
- **Backtest**: testing an algo against historical tick data over a
  specified lookback.
- **TXN**: transaction(s) — total trades in a stock in a session.
- **Trade price**: S, shown as $ to two decimals. **Return** $RET =
  (S_n − S_0); can be % by dividing by S_0. **Basis points**: 100 bp =
  1%; bpRET = ((S_n − S_0)/S_0) × 10000 (0.01 → 100 bp).
- **Lookback (LB)**: how far back we look for moving averages,
  volatilities, returns, backtests, EMA α constants; chosen to suit the
  calculation.
- **Maxima/minima/ranges**: MAXS, MINS over LB; $R = range = MAXS −
  MINS; %R = (MAXS − MINS)/SAVG.
- Statistics vocabulary: variance, σ, std dev, average, median, mode,
  median standard deviation; math: sigma, log/ln, exponents, first/
  second derivatives.

## Key takeaways

1. A shared, precise vocabulary (tick-based lookbacks, bp returns,
   %Range) is foundational — the authors deliberately standardize
   definitions to avoid ambiguity in formulas and discussions.
