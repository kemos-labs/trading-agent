# Ch05 — Statistics

**Source:** Grus, *Data Science from Scratch*, Chapter 5.

## Purpose
Descriptive statistics from scratch: summarising a list of numbers with a
few well-chosen measures.

## Measures of centrality
- **Mean**: `sum(xs) / len(xs)` — sensitive to outliers.
- **Median**: the middle value (or average of the two middles) of the sorted
  list — robust to outliers. Use `sorted` + midpoint indexing.
- **Quantile**: the p-th quantile = the value at position `int(p * len(xs))`
  of the sorted list (e.g. 0.25, 0.75). Quartiles = quantiles at 0.25/0.5/0.75.
- **Mode**: the most common value (`Counter(xs).most_common(1)`). Mean is
  most common, then median, then mode — each robust to different distortions.

## Measures of dispersion
- **Range**: `max - min` — wildly sensitive to outliers.
- **Variance** (population, with n not n−1 in the book's toy code):
  `variance = sum((x - mean)**2 for x in xs) / len(xs)`.
- **Standard deviation**: `sqrt(variance)` — the "typical" deviation from
  the mean.
- **Interquartile range (IQR)**: `quantile(0.75) − quantile(0.25)` — robust
  to outliers.

## Correlation
- **Covariance** between two series:
  `sum((x_i − mean_x) * (y_i − mean_y)) / len(xs)` — tells direction but
  not strength (depends on units/scales).
- **Correlation** — covariance normalised to [−1, 1]:
  `correlation(x, y) = covariance(x, y) / (std(x) * std(y))`.
  - +1 perfect positive, −1 perfect negative, 0 none.
  - Unit-free, so it's the standard "how related" measure.

## Pitfalls (explicitly taught)
- **Correlation ≠ causation** — the classic "num_friends vs time on site"
  example shows correlated variables with no direct causal link.
- **Correlation is sensitive to outliers**: a single extreme point can
  dominate the computation. The book's fix is to recompute after removing
  (or logging) outliers — visualise with scatterplots first.
- **Simpson's paradox** (mentioned): patterns can reverse when data is
  pooled vs split by a hidden grouping variable.
- The mean is dragged by outliers; report median + IQR for skewed data.

## Key takeaways
- "Correlation" in this book is Pearson correlation: standardised
  covariance, always in [−1, 1].
- Inspect *shape* with quantiles before trusting any single number.
- Scatterplots + correlation together beat either alone.

## Notes
- Uses the toy DataSciencester friend data; the same functions (mean,
  variance, std, correlation) are reused by regression chapters to build
  the `total_sum_of_squares` and error metrics.
- The `-p log p` entropy of ch17 is a different information measure, not
  statistical correlation.
