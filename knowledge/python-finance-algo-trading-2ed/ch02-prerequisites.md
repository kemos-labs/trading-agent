# Chapter 2 — Prerequisites

## Core idea
Before any strategy work, the book sets up the Python toolchain and the core
data-handling skills: NumPy for fast numerical arrays, pandas for tabular
time-series data, Matplotlib for plotting, and the `yfinance` API for
historical price data.

## Key tools and patterns
- **Anaconda / Jupyter**: the development environment used throughout.
- **yfinance** data pull:
  ```python
  import yfinance as yf
  df = yf.download("AAPL", start="2010-01-01", end="2022-01-01")
  ```
- **Returns** (the universal strategy ingredient):
  ```python
  df["returns"] = df["close"].pct_change().dropna()
  ```
- **pandas basics**: `.iloc` slicing, `.shift(lag)` for lagged features,
  `np.where(cond, a, b)` for vectorized signal construction.
- The book emphasizes **vectorization** — avoid Python loops; use NumPy/pandas
  array operations for speed.

## Trading relevance
- `pct_change()` returns are used as the target and as the return series every
  strategy trades.
- Lagged returns (`shift`) become the raw material for features in the ML
  chapters (ch9–14).
- Data hygiene matters: `dropna()` after `pct_change`, and consistent index
  alignment when combining series.

## Pitfalls
- `pct_change()` produces a NaN in the first row — must be dropped or handled
  with `fillna(0)` before backtesting.
- Yahoo data can have gaps (holidays, suspensions); forward-fill only when
  the semantics allow it.
- Never standardize before splitting into train/test (leakage) — a rule the
  book revisits in the ML chapters.

## The canonical dataframe shape
Almost every chapter produces or consumes the same object:

```python
df = yf.download("AAPL", start=..., end=...)          # OHLCV frame
close = df["Close"]
df["returns"] = close.pct_change().dropna()          # tradable series
df["feature"] = df["returns"].shift(k)               # lagged inputs
```

From here, strategies add `prediction` and `strategy` columns and the
backtest helper reduces them to metrics. Once you can produce this shape
from any source (Yahoo, a broker API, HDF5), every chapter's code runs
unchanged.

## The backtest helper signature
```python
def backtest_dynamic_portfolio(strategy_returns, ...):
    # returns equity curve + Sharpe/Sortino/VaR/cVaR/drawdown
```
This function is reused from ch4 onward and is the project's single source
of truth for "did it work?".

## Bottom line
A setup chapter, but it fixes the canonical data frame shape used everywhere
later: an indexed `df` with `close`/`returns` columns, plus a features/target
pipeline. This is the same entry-point pattern as
`knowledge/python-algorithmic-trading/ch03`, and the helper-function
reuse philosophy (one backtest function for all strategies) is the project's
key engineering habit.
