# Vectorized Backtesting

## name
Vectorized (array-based) backtesting of signal-based trading strategies:
returns → shifted position → strategy returns → cumulative performance,
with transaction-cost modeling.

## description
A fast, loop-free pandas/NumPy skeleton for backtesting any signal that
produces a target position (-1/0/+1). Covers the no-look-ahead shift
discipline, log-return compounding, proportional + fixed transaction
costs, and performance comparison against a benchmark. The standard first
pass for simple strategies (SMA, momentum, mean reversion, ML
direction predictions) before moving to event-based backtesting.

## when to use it
- You have a signal (indicator, ML prediction, factor) and need its P&L
  quickly, without building a full event-based engine.
- You are sweeping many parameter combinations and need speed (vectorized
  runs in milliseconds).
- You need to sanity-check whether a strategy has any edge *before*
  investing in a realistic event-based backtester.
- Teaching/auditing the basic discipline: yesterday's signal × today's
  return (no look-ahead).

## the method

### 1. Build returns and position
```python
import numpy as np
import pandas as pd

data = pd.read_csv('prices.csv', index_col=0, parse_dates=True)
data['returns'] = np.log(data['price'] / data['price'].shift(1))

# Example signal: SMA crossover (short > long => long)
sma_s = data['price'].rolling(42).mean()
sma_l = data['price'].rolling(252).mean()
data['position'] = 0.0                          # warm-up region: flat
# NaN > NaN is False in np.where → sets -1; guard with valid mask
valid = sma_s.notna() & sma_l.notna()
data.loc[valid, 'position'] = np.where(sma_s[valid] > sma_l[valid], 1, -1)
```

### 2. The no-look-ahead shift (the critical step)
```python
data['strategy'] = data['position'].shift(1) * data['returns']
```
You can only earn TODAY's return with YESTERDAY's position. Skipping the
shift is look-ahead bias and manufactures fake performance.

### 3. Cumulative performance
```python
data['cum_strategy'] = data['strategy'].cumsum().apply(np.exp)
data['cum_benchmark'] = data['returns'].cumsum().apply(np.exp)
```
(log-return compounding; subtract the strategy's mean or scale to
notional as needed). Compare final cumulative values vs. the benchmark.

### 4. Transaction costs
Subtract a per-trade cost whenever the position changes:
```python
ptc = 0.001  # proportional cost per trade (e.g. 0.1%)
data['strategy_net'] = np.where(data['position'].diff() != 0,
                                data['strategy'] - ptc, data['strategy'])
```
Also support a fixed fee per trade (ftc) if required; net performance is
the only honest number.

### 5. Longer positions (holding between signals)
For crossover systems that should hold rather than flip each bar, use
`.ffill()` on the position (and `fillna(0)` for warm-up) instead of
re-signaling every bar — otherwise you churn trades and pay phantom costs.

## known pitfalls
- **Missing the shift(1)**: the classic bug — without it results are
  look-ahead and inflated. Always verify `position.shift(1)`.
- **Signal churn**: re-signaling every bar without ffill creates massive
  phantom turnover; costs (which are real) then expose it. Trade count ×
  cost can reverse strategy rankings entirely.
- **Costs omitted**: a strategy that looks great gross can be net-negative;
  model proportional (and fixed) costs before drawing conclusions.
- **Data snooping / overfitting**: tuning parameters on the same data you
  evaluate on is dishonest; use a train/test split or walk-forward
  validation (see `walk-forward-validation`) and report the out-of-sample
  number.
- **Vectorization limits**: fixed costs, non-divisible units, and
  path-dependent state (stops, running P&L) need an event-based backtester
  (Hilpisch ch6) — know when to graduate.
- **Warm-up NaN**: rolling windows leave NaNs; `np.where` on NaN
  comparisons yields −1 (False), so initialize positions to 0 and set
  them only where the signals are valid, rather than relying on fillna.

## source
Hilpisch, *Python for Algorithmic Trading* (O'Reilly, 2021), ch4
(vectorized backtesting: SMA, momentum, mean reversion, transaction
costs, data snooping) and ch5 (ML prediction backtests).
