# Chapter 4 — Backtesting

## Core idea
Backtesting converts a signal into a simulated equity curve and a set of
performance statistics. The book's canonical pattern: build a `prediction`
(or signal) series, combine it with returns to get a `strategy` return
series, then evaluate.

## The canonical vectorized backtest
```python
df["prediction"] = ...            # model or rule output, in {-1, +1} or continuous
df["strategy"] = df["prediction"].shift(1) * df["returns"]
equity = (1 + df["strategy"]).cumprod()
```
- `shift(1)` on the signal **prevents look-ahead**: today's trade executes on
  yesterday's signal.
- `sign(prediction)` converts classification outputs to long/short positions.
- `cumprod` of `1 + returns` gives the equity curve; log-return
  compounding via `np.exp(returns.cumsum())` is the alternative.

## What the backtest reports
- **Equity curve** and total/annualized return.
- **Sharpe** and **Sortino** ratios (annualized with `sqrt(252)`).
- **Max drawdown**: `max(1 - equity / equity.cummax())`.
- **VaR / cVaR** of strategy returns (see ch5).
- **Beta/alpha** vs a benchmark (e.g., S&P 500).

## Strategy classes in this chapter
- **Moving-average crossover**: `signal = 1 if sma_fast > sma_slow else -1`,
  long when fast MA is above slow MA.
- **Momentum**: position = sign of trailing n-day return.
- **Mean reversion**: position = -sign of deviation from a rolling mean
  (Bollinger-band style).
All are evaluated with the same pipeline, so rankings are apples-to-apples.

## Pitfalls
- **Look-ahead bias**: forgetting the `shift(1)` — the single most common
  backtest error.
- **Overfitting** to the training window; the book's guard is to backtest a
  strategy at most twice and then validate on unseen data (see ch16's
  train/test/validation split).
- Ignoring **transaction costs and spread**; ch16 penalizes each strategy by
  the asset's spread inside the Sharpe computation.
- Annualizing with the wrong factor (252 for daily, 52 for weekly).

## Bottom line
This chapter is the book's operational definition of "does it work": one
vectorized pipeline, one set of metrics. It maps directly onto the
`skills/vectorized-backtesting` skeleton and the risk metrics formalized in
ch5.
