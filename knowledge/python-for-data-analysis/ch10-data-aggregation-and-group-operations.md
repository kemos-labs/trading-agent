# Ch10 — Data Aggregation and Group Operations

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 10.

## Purpose
The **split-apply-combine** paradigm (Wickham) via `groupby`: aggregate,
transform, apply arbitrary functions, pivot tables, and bucket/quantile
analysis — the engine of summary statistics and feature engineering.

## groupby mechanics
- `df.groupby(keys)` splits on keys (column names, arrays, dict/Series
  mapping, or functions on the index); the GroupBy object computes lazily.
- `.mean()/.sum()/.count()/.size()/.std()/.describe()` aggregate each
  group. Missing keys dropped by default (`dropna=False` to keep).
- Non-numeric "nuisance" columns are auto-excluded from numeric
  aggregations.
- `as_index=False` returns flat (range) index instead of grouped index.

## Aggregation (`agg`)
- Multiple functions: `df.groupby(k).agg(['min','max','mean'])`;
  per-column dict: `grouped.agg({'tip': np.max, 'size': 'sum'})`; nested
  lists → hierarchical columns.
- String shortcuts ('mean', 'sum', 'size') or callables.

## Transform
- `grouped.transform(func)` broadcasts the per-group result back to the
  original index — e.g. normalize within group:
  `df['x'] / grouped['x'].transform('sum')`, or z-score per group.
- Distinguished from agg: transform returns same-length result; agg
  collapses.

## apply (general split-apply-combine)
- `grouped.apply(fn)` — the escape hatch: any function taking a DataFrame
  piece and returning a DataFrame/Series/scalar; results are concat'd with
  group labels. E.g. `top(df, n=5)` per group; pass extra args after fn.
- `group_keys=False` suppresses the group-key level in the result.
- Warning: apply can be slow and surprising (index behavior); prefer
  built-in agg/transform when they suffice.

## Pivot tables & cross-tabs
- `df.pivot_table(values, index=..., columns=..., aggfunc='mean')` — a
  grouped reshape with aggregation (margins=True for row/col totals).
- `pd.crosstab(index, columns)` counts combinations (with
  `normalize=True` for proportions).

## Bucket/quantile analysis
- `pd.cut(x, bins)` (equal width) / `pd.qcut(x, q)` (quantile) to slice
  into bins, then `groupby(bins).mean()` etc. — classic for "effect by
  size/vol bucket" analysis (think: strategy returns by volatility
  regime).
- `groupby(...)['col'].quantile([0.25, 0.5, 0.75])`.

## Key takeaways
- split-apply-combine is the mental model for all grouped work; choose
  agg (collapse) vs transform (broadcast) vs apply (arbitrary) by what
  you need back.
- groupby + agg/transform + pivot_table covers ~90% of summary and
  feature-engineering needs — vectorized and fast.
- Time-based grouping is resampling — ch11 (groupby with freq rules).

## Notes
- The tips dataset runs through the chapter; the same patterns appear in
  ch13's FEC/MovieLens examples.
- Directly reusable for strategy stats: returns by day/regime/symbol via
  groupby; our arma-garch/hmm skills produce the grouping keys.
