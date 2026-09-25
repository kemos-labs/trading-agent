# Chapter 3 — Understanding Financial Data

## Core idea
The data layer of quantitative finance: types of financial data, sources,
cleaning, and the pandas workflow that turns raw data into analysis.

## Types of financial data
- **Time series**: prices, rates, indicators over time — the foundation for
  trend analysis, forecasting, temporal comparison.
- **Cross-sectional**: many entities at one point in time — comparative
  analysis across securities/sectors; outliers, market breadth.
- **Panel data**: multiple entities over time — the richest structure for
  modeling time-varying effects across entities.
- **Market data**: prices, volumes, trades (equities, fixed income,
  derivatives, FX).
- **Fundamental data**: financial statements and ratios — P/E, EPS,
  debt-to-equity (intrinsic value analysis).
- **Alternative data**: social media sentiment, satellite imagery, credit
  card transactions, web traffic — a source of edge before it hits
  traditional data.
- **Transactional data**: execution times, order sizes, bid-ask spreads —
  the raw material of high-frequency analysis.

## Acquisition, cleaning, preprocessing
- Sources: historical data providers, real-time feeds, alternative data
  vendors.
- Raw data is noisy: **outlier detection, imputation of missing values,
  normalization** before any analysis.

## The pandas workflow
```python
data = pd.read_csv('TechCorp_StockPrices.csv', parse_dates=True, index_col='Date')
data['30_day_MA'] = data['Close'].rolling(window=30).mean()
data['90_day_MA'] = data['Close'].rolling(window=90).mean()
```
- Moving averages smooth short-term fluctuations and reveal trends.
- Visualization (line charts, correlation heatmaps) unearths patterns
  hidden in tables.

## Tools
- pandas (manipulation), NumPy (arrays), Matplotlib/Seaborn (plots).

## Pitfalls
- Missing values and outliers distort every downstream model — clean first.
- Look-ahead: computed columns must only use past data.
- Garbage-in-garbage-out: data quality determines model quality (a theme
  echoed in every ML chapter of the book).

## Bottom line
The data taxonomy (time series/cross-sectional/panel; market/fundamental/
alternative/transactional) is the mental map for choosing the right source
and tool. The rolling-window pandas pattern here is the same skeleton used
in `skills/vectorized-backtesting` and Hilpisch's time-series chapter.
