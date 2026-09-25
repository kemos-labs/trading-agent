# Chapter 7 — Data Visualization

## Core idea
Visualization for finance with **matplotlib** (static) and **plotly +
Cufflinks** (interactive). Matplotlib is the benchmark; plotly brings D3.js
interactivity and candlestick charts.

## matplotlib essentials
```python
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('seaborn')
mpl.rcParams['font.family'] = 'serif'
```
- `plt.plot(x, y)` — the fundamental 2-D plot; pass an ndarray directly and
  the index becomes x.
- Method chaining: `plt.plot(y.cumsum())` plots the cumulative sum.
- Customization: axis labels, grid, legends, multiple subplots
  (`plt.subplots(nrows, ncols)`), twin axes (`secondary_y` / `twinx`).
- 3-D plots via matplotlib for surfaces relevant to finance.
- **Fixed seed** (`np.random.seed(1000)`) for reproducible example plots.

## plotly + Cufflinks (interactive)
- D3.js-based interactive charts: zoom, hover, embeddable in web apps.
- Cufflinks binds plotly to pandas: `df.iplot(...)` and the
  `QuantFigure`/`qf` API for financial plots (candlesticks, OHLC).
- Useful for dashboards and technical stock analysis.

## Finance visualization patterns
- Price series + overlays (moving averages) — ch8.
- Return distributions: histograms of random draws, KDE.
- Scatter/correlation plots (S&P 500 vs VIX) — ch8.
- Strategy equity vs benchmark — ch15.

## Pitfalls
- Don't pass too-large/complex arrays to matplotlib.
- Static PNGs vs interactive: choose by audience (report vs dashboard).
- Date axes: convert `datetime64` → Python `datetime` for clean x-ticks;
  `fig.autofmt_xdate()` for readable date labels.

## Which tool when
- **matplotlib**: any static figure for papers/reports; full control over
  layout, axes, and annotation; the safe default.
- **plotly/Cufflinks**: interactive exploration, dashboards, web embedding;
  zoomable time series and candlesticks.
- **pandas built-in plotting** (`df.plot()`): quick one-liners directly on
  DataFrames, fine for inspection.
- The book's convention (imports, style, serif font, `%matplotlib inline`)
  is reused in every later chapter, so keeping the same setup makes code
  portable across notebooks.

## Bottom line
The plotting layer. Matplotlib covers all static analytics; plotly/Cufflinks
add interactivity for monitoring and client-facing visuals. Cross-ref:
`knowledge/python-for-finance/ch08` (time-series visualization in pandas).
