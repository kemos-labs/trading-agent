# Ch4 — Mastering Vectorized Backtesting

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## The vectorized approach

Vectorized backtesting formulates a strategy as array operations on price
and return series — no loops, fast, concise. Suited for simple strategies,
interactive exploration, visualization-first work, and sweeping many
parameter combinations. Limits: can't model incremental data arrival
(look-ahead bias), fixed transaction costs, non-divisible instruments, or
path-dependent state.

**The core pattern (all strategies share it):**

```python
data['returns'] = np.log(data['price'] / data['price'].shift(1))  # log returns
data['position'] = ...                                             # signal: -1/0/+1
data['strategy'] = data['position'].shift(1) * data['returns']     # shift! no look-ahead
data[['returns','strategy']].cumsum().apply(np.exp)                # gross performance
```

The `.shift(1)` on the position is the heart: you can only earn today's
return with yesterday's signal (no look-ahead bias).

## SMA-based strategy

- Signals: `position = 1` when short SMA > long SMA (e.g. 42 vs 252),
  `-1` when short < long, else 0 (or hold via ffill).
- Derive signals vectorized: `np.where(sma_s > sma_l, 1, -1)` then
  `.ffill()` to hold positions between crosses.
- Momentum strategy: `position = np.sign(returns.rolling(window).mean())`
  — sign of the trailing average return (time-series momentum).
- Mean-reversion strategy: distance = price − SMA; `+1` when distance <
  −threshold (buy the dip), `-1` when > +threshold (short the pop),
  `0` on sign change of distance (back to neutral); `.ffill().fillna(0)`.

## Transaction costs

Model proportional costs by adjusting strategy returns:

```python
data['strategy_tc'] = np.where(data['position'].diff() != 0,
                               data['strategy'] - ptc, data['strategy'])
```

Each position change pays the proportional cost `ptc`. Costs radically
change conclusions: with no costs, momentum crushes SMA; with costs, the
trade-frequency difference flips the ranking (SMA trades less). **The
number of trades a strategy triggers is a first-order performance
factor.**

## Performance metrics

- Gross/net cumulative performance: `cumsum().apply(np.exp)` (log
  returns compound).
- Final balance = initial capital × exp(cumulative log return).
- Compare strategy vs. benchmark instrument (the underlying ETF).

## Data snooping and overfitting

White (2000): data snooping = "a given set of data is used more than once
for purposes of inference or model selection." Tuning parameters on the
same data that you evaluate on manufactures good-looking results that
won't generalize. Rules: hold out test data, minimize the number of
specifications tried, and treat any "great" result found by search as
suspect until validated out-of-sample (the book's ML chapter does
train/test splits for this reason).

## Key takeaways

- The vectorized backtest skeleton: returns → position (shifted!) →
  strategy returns → cumulative performance — reuse it for any signal.
- Always shift positions by one bar: yesterday's signal × today's return.
- Model transaction costs via per-trade cost × position changes; they can
  reverse strategy rankings (trade count matters).
- Guard against data snooping: out-of-sample validation, few
  specifications, honest reporting.
