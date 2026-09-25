# Chapter 8 — Financial Time Series

## Core idea
Financial data is time-indexed data; pandas is the tool built for it
(originally developed at AQR). This chapter covers the full toolkit: import,
summary stats, changes, resampling, rolling statistics, correlation, and
high-frequency (tick) data.

## Data import & basics
```python
data = pd.read_csv('tr_eikon_eod_data.csv', index_col=0, parse_dates=True)
```
- `index_col=0, parse_dates=True` turns the first column into a DatetimeIndex.
- **Summary stats**: `.info()`, `.head()`, `.describe()` — reveals NaN
  patterns (holidays, missing series).
- **Changes over time**: `pct_change()` (returns), `diff()` (absolute
  changes).
- **Resampling**: `data.resample('M').last()` / `'W'` / `'B'` — aggregate
  daily data to weekly/monthly/business-frequency.

## Rolling statistics
```python
data['SMA1'] = data['AAPL.O'].rolling(42).mean()   # simple moving average
data['ROLL_STD'] = data['AAPL.O'].rolling(252).std()  # rolling vol
```
- Rolling windows (fixed-length) underpin SMA strategies, rolling
  volatility, and rolling betas.
- Rolling correlation: `data['.SPX'].rolling(252).corr(data['.VIX'])`.

## Correlation analysis (S&P 500 vs VIX case study)
- The empirical **negative correlation** between the S&P 500 index and the
  VIX volatility index — rolling correlation drifts but stays mostly
  negative — a stylized fact used in hedging and regime logic.

## High-frequency (tick) data
- Tick data needs time-of-day handling: resample ticks into OHLC bars
  (`resample` + `ohlc`), handle irregular timestamps, and aggregate
  volume/time-weighted bars.
- pandas handles large tick sets, but memory/performance push toward
  PyTables/HDF5 (ch9) for storage.

## Pitfalls
- Missing data is common (holidays, stale quotes): decide between `dropna`,
  `ffill`, or NaN-aware math per use case.
- `pct_change()` first value is NaN.
- Rolling windows need enough history — early rows are NaN; drop or pad
  before backtesting.
- Resampling to business vs calendar frequency changes what each bucket
  contains — know which you need (e.g., `'B'` skips weekends).

## The Eikon dataset used in the book
A CSV of end-of-day data for AAPL, MSFT, INTC, AMZN, GS, SPY, .SPX, .VIX,
EUR=, XAU=, GDX, GLD (2010–2018). It recurs across the book: `.dropna()`
handles series that started later; the S&P/VIX pair illustrates the
negative-correlation stylized fact; SPY/GLD/GDX give equity/gold/gold-miner
comparisons for strategy work.

## Bottom line
The time-series toolkit that all strategy work uses: rolling means/vols,
resampling, correlation. SMA-based signals from this chapter feed the
backtesting chapter (ch15). Cross-refs: `skills/vectorized-backtesting`,
`knowledge/python-finance-algo-trading-2ed/ch02`.
