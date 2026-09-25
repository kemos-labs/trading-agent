# Chapter 6 — Advanced Backtesting

## Core idea
Simple backtests (ch4) assume you can always trade at the close and ignore
frictions. This chapter makes backtesting more realistic: transaction costs,
spread, slippage, and the distinction between what a signal *says* and what
the market *gives*.

## Realism upgrades
- **Spread costs**: every round trip pays the bid-ask spread. For FX, the
  spread is typically 0.01–0.07% depending on the pair. Penalize strategy
  returns by the spread on each trade.
- **Transaction costs**: proportional fees (e.g., `0.1%` per side) and fixed
  fees per trade. Applied on position *changes*, not on the whole position:
  ```python
  cost = ptc * abs(position.diff()).fillna(0)
  strategy_net = strategy_gross - cost
  ```
- **Signal → position realism**: signals computed on today's close can only
  be traded at the *next* bar (the `shift(1)` discipline from ch4).
- **Multiple strategies / portfolio backtest**: backtest each strategy
  separately, then combine with portfolio weights (ch3) to get a
  portfolio-level equity curve and risk metrics (ch5).

## The lesson
- **Trade frequency vs costs can reverse rankings**: a high-turnover strategy
  with a great gross Sharpe can be worse than a low-turnover one once spread
  and fees are applied. The book's repeated warning: always judge net of
  costs.
- **Robustness over peak performance**: prefer a strategy that degrades
  gracefully across parameter choices to one that peaks at a single
  overfit point (ties into the "backtest twice max" rule in ch16/17).

## Pitfalls
- Applying costs to the full position instead of position *changes*
  double-charges.
- Ignoring the open/close execution point — assume fills at the signal bar's
  close or next open, never intra-bar.
- `position.diff()` charges a phantom cost on the very first position change
  from 0 — acceptable (that's the entry), but be aware it counts the initial
  entry cost.

## Bottom line
The bridge from toy backtests to believable ones. Combined with the
`skills/vectorized-backtesting` skeleton, the cost model here is the part
most often omitted and most often responsible for live-vs-backtest drift.
