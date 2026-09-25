# Ch11 — Data Visualization

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 11.

## Purpose
The theory and practice of encoding data visually, using Plotly
(`plotly.express`): marks, channels, encodings, and the pitfalls that
produce misleading charts.

## Grammar of graphics (via plotly.express)
- **Marks**: the graphical objects — points (scatter), lines (line/trend),
  bars (bar), areas (box, histogram, density).
- **Channels**: how features map to visual properties — x/y position,
  color, size, shape, pattern.
- **Encoding choice is a design decision**: position is the most accurate
  channel, then length, angle, area, color intensity, shape.

## Plot types and when
- Scatter: two numeric features; add `color`/`size` for third/fourth
  dimensions.
- Line: ordered/numeric x (time series, trends).
- Histogram/density: single distribution; `nbins` controls smoothness.
- Box: distribution + outliers, by category.
- Bar: categorical counts or means.
- Faceting (`facet_col`/`facet_row`): small multiples per category.
- Choropleth/maps for geospatial (used with xarray/NetCDF in ch14).

## Pitfalls
- **Overplotting**: many overlapping points hide density — fix with
  transparency (alpha), jittering, or hexagonal/2D histograms.
- **Truncated axes**: exaggerate differences — prefer zero-based or
  clearly-marked breaks.
- **Color misuse**: rainbow palettes and bad contrast mislead; use
  perceptually-ordered scales; remember color-blind viewers.
- Pie/3D/area charts: hard to read lengths; bar charts are usually better.
- Don't encode continuous data with discrete colors (or vice versa).

## Key takeaways
- Every chart answers a question: choose the plot that makes the answer
  legible, not the prettiest one.
- Interactive plotly gives hover/tooltips and zoom for free — great for
  exploration, but export static figures for communication.
- Visualization and EDA (ch10) are the same activity: plots reveal what
  summaries hide.

## Notes
- The book uses `plotly.express` throughout; the grammar-of-graphics
  concepts transfer to matplotlib/seaborn/ggplot.
- Title/axis-label/source discipline: a chart without labels is an opinion
  without evidence.
