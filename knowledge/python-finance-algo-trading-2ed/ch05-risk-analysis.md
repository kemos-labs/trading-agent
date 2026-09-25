# Chapter 5 — Risk Analysis

## Core idea
After a backtest shows returns, this chapter formalizes *how bad it can get*.
The book's risk layer reports four statistics for every strategy: drawdown,
VaR, cVaR, and risk contributions.

## Key metrics
- **Max drawdown**: largest peak-to-trough equity decline.
  ```python
  dd = 1 - equity / equity.cummax()
  max_dd = dd.max()
  ```
- **Value at Risk (VaR)**: the loss level exceeded with probability `alpha`
  (e.g., 95%): `VaR(95%) = -quantile(returns, 0.05)`.
- **Conditional VaR (cVaR / Expected Shortfall)**: average loss *beyond* VaR:
  ```python
  cVaR = -returns[returns <= -VaR].mean()
  ```
  Captures tail severity that VaR ignores.
- **VaR/cVaR ratio**: a diagnostic — a ratio near 1 means losses cluster at
  the VaR threshold (thin tail); a large ratio means a heavy tail where the
  worst losses exceed VaR substantially.
- **Risk contribution**: how much each asset/strategy contributes to portfolio
  variance: `RC_i = w_i * (Sigma·w)_i / (w'·Sigma·w)`, summing to 1.

## Why VaR/cVaR together
VaR alone is blind to what happens past the quantile; two strategies can have
identical VaR but very different worst-case losses. cVaR + the VaR/cVaR ratio
expose tail behavior — essential for strategies with fat-tailed returns.

## Pitfalls
- VaR is not sub-additive for non-elliptical distributions; cVaR is coherent.
- Historical VaR depends on the sample; a single bad day can move it sharply.
- Reporting only annualized Sharpe hides all of this — always pair return
  metrics with risk metrics (the book's report card does exactly this:
  Beta/Alpha/Sharpe/Sortino on one side, VaR/cVaR/drawdown on the other).

## Bottom line
This chapter standardizes the "risk half" of every strategy report card used
in the book (see the ch14 RNN example reporting Sharpe 1.04 *alongside*
drawdown 44% and cVaR 66%). It is the natural seed for a future
`risk-metrics` skill covering drawdown, VaR, cVaR, and risk contributions.
