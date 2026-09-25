# Ch6 — Building Classes for Event-Based Backtesting

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## Why event-based?

Vectorized backtesting's shortcomings:
- **Look-ahead bias**: works on the complete dataset; real trading receives
  data incrementally.
- **Simplification**: can't model fixed costs, fixed amounts per trade, or
  non-divisible instruments (shares are integers).
- **Non-recursiveness**: can't track path-dependent state (running P&L,
  trailing stops).

Event-based backtesting fixes these: an **event** = arrival of new data
(a bar — 1-minute or 1-day). Benefits: incremental processing like live
trading, complete freedom in modeling event-triggered processes, easy
path-dependent state, OOP reusability, and elements that transfer directly
to live implementation.

## The base class (BacktestBase)

Responsibilities: retrieve/prepare EOD data (CSV → DataFrame, log
returns); helpers (plot, print state, get bar info); **place market
orders**; **close out** any open position at the end.

Key state: `initial_amount` (constant), `amount` (running balance), `units`
(shares held), `position` (0/−1/+1), `trades`, plus `ftc` (fixed cost per
trade) and `ptc` (proportional cost per trade).

Order logic (market orders):
```
buy: cost = units·price + ftc + ptc·units·price   → amount −= cost, units += …
sell: proceeds = units·price − ftc − ptc·units·price → amount += proceeds, units = 0
```
(`place_buy_order`/`place_sell_order` update balance/units/trades;
`close_out` sells remaining units at the last bar.)

## Long-only and long-short subclasses

- `BacktestLongOnly`: `go_long(bar, units|amount)` — buy with units or all
  available cash (`amount='all'`); strategies (SMA crossover, momentum,
  mean reversion) implemented as methods that place orders per bar.
- `BacktestLongShort`: adds `go_short`; entering the opposite direction
  first closes the current position (buy-to-cover/sell-to-close), then
  opens the new one. `go_long` checks `if self.position == -1: close`
  before buying; `go_short` mirrors it.

## Results and the costs lesson

SMA (42/252), momentum (60d), mean reversion (SMA=50, thr=5) on the same
data, no costs: momentum dominates ($136,716 vs ~$56,000). With fixed
$10/trade + 1% proportional: momentum collapses to $38,074, SMA $51,960,
mean-reversion $15,375 — mean reversion (most trades) is crushed. **There
is a "third side" of performance beyond hit ratio and timing: trade
frequency vs transaction costs.** Fewer-trade strategies win net of costs;
this is the case for low-cost passive (ETF) investing.

## Key takeaways

- Event-based = incremental, realistic, path-capable, reusable — the
  honest upgrade from vectorized backtesting.
- Base-class design: data prep, order placement with fixed + proportional
  costs, position tracking, close-out — the skeleton any backtester needs.
- Long-short = close-then-open on direction flip; keep `amount`/`units`/
  `position` consistent across order methods.
- Net-of-cost rankings reverse naive ones: trade count × cost is a
  first-order performance driver.
