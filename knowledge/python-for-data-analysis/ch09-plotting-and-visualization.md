# Ch09 — Plotting and Visualization

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 9.

## Purpose
The matplotlib API as used for analysis: figures/subplots, styling,
annotations, and the pandas/plotly/seaborn integrations. The chapter's
principle: plot to *see* the data before and during modeling.

## matplotlib core model
- **Figure** (the canvas) contains **Axes** (subplots). Two idioms:
  - `plt.subplots(nrows, ncols)` returns `(fig, axes_array)` — preferred.
  - `fig.add_subplot(2, 2, 1)` for incremental building.
- Use **axis methods** (`ax.plot`, `ax.hist`, `ax.scatter`, `ax.bar`,
  `ax.boxplot`) over pyplot globals — cleaner and explicit.
- Ticks/labels/titles: `ax.set_xticks`, `set_xticklabels(rotation=...)`,
  `set_xlabel`, `set_title`, or batch `ax.set(...)`.
- Legends: pass `label=` per series then `ax.legend()`; `loc='best'`.
- Annotations: `ax.text`, `ax.annotate(text, xy=, xytext=,
  arrowprops=...)` — e.g. marking crisis dates on an S&P plot.
- Limits/zoom: `ax.set_xlim`, `set_ylim`.
- Save: `fig.savefig('out.png', dpi=..., bbox_inches='tight')`;
  `plt.tight_layout()` for subplots.
- In Jupyter: `%matplotlib inline`; all plotting code must be in one cell
  (figures reset between cells).

## pandas integration
- `df.plot()` on Series/DataFrame — quick line/bar/hist/box/scatter
  (`kind='barh'`, `kind='kde'`, etc.); `spx.plot(ax=ax, color='black')`
  targets a specific axis.
- Great for time series and grouped summaries (bar plots by category).

## seaborn & others
- seaborn layers statistical plots on matplotlib (barplots with error
  bars, `sns.barplot(x, y, hue, data=...)`, histograms/density, lmplot).
- plotly for interactive/webtargeted figures (per learning-data-science
  ch11, which covers the grammar-of-graphics view).

## Key takeaways
- Think figure → axes → artist; keep style (color, linestyle, alpha,
  labels) explicit for reproducibility.
- Plot early and often: distribution checks (hist/box), relationships
  (scatter), time structure (line) — the EDA loop.
- One cell per figure in notebooks; set `index_col`/`parse_dates` so time
  axes plot correctly.
- Annotations and limits are what make a chart tell a story (the
  2008–09 crisis plot is the chapter's showcase).

## Notes
- Complements learning-data-science ch10–11 (EDA + plotly) and our
  hands-on-ml notes (TensorBoard for training curves).
- For financial work: candle charts and volume subplots come later via
  mplfinance/plotly — same Axes model.
