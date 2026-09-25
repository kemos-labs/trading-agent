# Chapter 15 — Trading Strategies

## Core idea
Vectorized backtesting of algorithmic strategies, plus ML/DL approaches to
directional prediction. The canonical pipeline: signal → `Position` →
strategy returns → performance stats.

## The vectorized backtest skeleton
```python
data['SMA1'] = data['AAPL.O'].rolling(42).mean()
data['SMA2'] = data['AAPL.O'].rolling(252).mean()
data['Position'] = np.where(data['SMA1'] > data['SMA2'], 1, -1)  # long/short
data['Strategy'] = data['Position'].shift(1) * data['Returns']   # no look-ahead
data['Market'] = data['Returns']
data['Outperformance'] = (data['Strategy'] - data['Market']).cumsum()
```
- `np.where(cond, a, b)` builds positions from conditions.
- **`shift(1)` is the no-look-ahead discipline**: today's position trades
  tomorrow's return.
- Performance: cumulative returns, Sharpe, vs-benchmark outperformance.

## Strategies covered
- **Simple moving averages** (SMA crossover) — the canonical example.
- **Random walk hypothesis test**: regress prices on `lag_1..lag_5`
  (`data['lag_k'] = data[symbol].shift(k)`) — R² near zero supports the RWH;
  OLS with lagged prices as a (weak) predictor.
- **Linear OLS regression strategy**: predict next price/return from lags;
  trade the sign.
- **Clustering (unsupervised)**: cluster days by features (e.g., returns
  patterns); trade based on cluster labels.
- **Frequency approach**: simple frequentist odds — compare conditional
  distributions of returns after events.
- **Classification (ML)**: logistic/SVM/kNN etc. on lagged features to
  predict direction; strategy = sign of predicted probability.
- **Deep neural networks**: Keras-based MLP on lagged features → direction
  probabilities.

## Parameter optimization & overfitting
- Brute-force grid over SMA windows (e.g., `SMA1` 30–60, `SMA2` 120–260):
  `results.sort_values('OUT', ascending=False)` finds "optimal" params —
  but the book warns this **overfits** the sample.
- Proper discipline: optimize in-sample, validate out-of-sample; expect
  performance to decay OOS.

## Pitfalls
- Forgetting `shift(1)` → look-ahead bias inflates results.
- Optimizing parameters on the full sample → data snooping; always reserve
  an out-of-sample period.
- High turnover strategies ignore costs — net of costs results differ.

## Bottom line
The strategy chapter that turns signals into backtests. Its skeleton
(`Position.shift(1) * Returns`) is codified in `skills/vectorized-backtesting`;
the overfitting warning is reinforced by `skills/walk-forward-validation`.
