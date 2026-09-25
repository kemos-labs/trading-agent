# Chapter 4 — Time Series Analysis

## Core idea
Financial time series have temporal structure — trends, seasonality,
volatility clustering, non-stationarity — and pandas provides the tools
(datetime indexing, resampling, rolling statistics) to analyze them.

## Characteristics of financial time series
- **Trend**: long-term direction (up/down/stationary).
- **Seasonality**: periodic fluctuations (quarterly earnings effects).
- **Decomposition**: trend + seasonality + residual — the basis of ARIMA
  and variations.
- **Volatility clustering**: large changes follow large changes — motivates
  GARCH over constant-volatility models; crucial for derivatives pricing.
- **Non-stationarity**: mean/variance change over time — differencing and
  transformations restore stationarity before model fitting.
- **Cointegration**: non-stationary series that move together long-term —
  the basis of pairs trading (see `skills/cointegration-testing`).
- **High-frequency data**: millisecond granularity, market microstructure,
  and **microstructure noise** (observed vs true prices) that needs
  filtering.

## Datetime indexing in pandas
- `DatetimeIndex`: slicing (`data['2021-03']`), aggregation, resampling.
- Build via `pd.to_datetime()`, direct assignment, or `parse_dates=True` in
  `read_csv`.

## Resampling and frequency conversion
```python
monthly = daily.resample('M').mean()    # downsample
quarterly_rev = daily_sales.resample('Q').sum()
```
- **Downsampling**: reduce frequency, aggregate (mean/sum/last).
- **Upsampling**: increase frequency, fill via interpolation or
  forward-fill.
- Frequency conversion aligns datasets of different granularities for
  comparison.

## Rolling and expanding statistics
```python
df['MA'] = df['Close'].rolling(window=30).mean()
df['RollStd'] = df['Close'].rolling(30).std()
df['CumReturn'] = df['Close'].pct_change().expanding().sum()
```
- Rolling windows: moving averages, rolling vol, rolling beta.
- Expanding windows: cumulative statistics (running returns).

## Time zones
- Markets span time zones; pandas supports tz-aware indexing and conversion
  for cross-market alignment.

## Pitfalls
- Fitting stationary-only models (OLS/ARMA) on non-stationary prices gives
  spurious regressions — difference first.
- Resampling with the wrong aggregation (mean vs last) changes semantics.
- Forward-fill invents data — use it only where semantics allow.

## Bottom line
The time-series toolkit: decomposition, stationarity/cointegration,
resampling, rolling stats. These map directly onto the knowledge base's
`skills/arma-garch-modeling` (ARIMA/GARCH) and
`skills/cointegration-testing` skills, and the rolling window patterns used
in every backtest.
