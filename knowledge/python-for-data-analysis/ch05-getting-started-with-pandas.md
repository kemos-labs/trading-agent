# Ch05 — Getting Started with pandas

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 5.

## Purpose
The pandas core: **Series** and **DataFrame**, index/label-based data
alignment, and the essential functionality (reindex, drop, indexing,
sorting, rank, apply) that everything else builds on.

## Series
- 1-D labeled array: values + **index** (labels). Default RangeIndex;
  can be strings/datetimes. `pd.Series(data, index=[...])`.
- Acts like a fixed-length ordered dict: `s['a']`, `'a' in s`,
  `s.to_dict()`; from a dict, missing index labels become **NaN**.
- **Index alignment in arithmetic**: `s1 + s2` aligns on labels
  automatically; labels missing from either side → NaN. This is pandas'
  defining behavior vs NumPy.
- Missing data: NaN (float) / NaT (datetime); detect with `isna`/`notna`.

## DataFrame
- 2-D labeled table: rows + columns, both with labels; columns can be
  mixed dtypes. Built from dict of Series/arrays, list of dicts, or 2-D
  ndarray + `columns`/`index`.
- Column access `df['col']` / attribute `df.col`; returns Series.
  Column assignment: `df['new'] = ...`; deleting: `del df['col']` /
  `df.drop(columns=...)`.
- Row selection: `df.loc[labels]` (by label) vs `df.iloc[positions]`
  (by integer). **loc ranges are inclusive, iloc exclusive** — the
  classic bug.
- `df[df['col'] > 0]` Boolean-row filtering; `df.head()/tail()`,
  `df.info()`, `df.describe()`.

## Essential functionality
- **reindex**: conform to a new index — missing labels get NaN (or
  fill/ffill via `method`). Reorder/insert rows or columns.
- **drop**: remove rows (`index=[...]`) or columns (`columns=[...]` /
  `axis=1`) — returns new object.
- **sort**: `sort_values(by=...)`, `sort_index()`; `rank()` for
  ties-aware ranks.
- **apply**: row/column-wise function application
  (`df.apply(f, axis='columns')`); `applymap` element-wise;
  Series `map` for element-wise transforms. Prefer vectorized methods
  (`sum`, `mean`) over apply when possible.
- **fillna/dropna**: NA handling (full treatment in ch7).
- `value_counts()`, `unique()`, `isin()` for categorical work.

## Key takeaways
- **Alignment by index** is pandas' superpower and the source of silent
  NaN surprises — check indexes before/after arithmetic and merges.
- loc (labels, inclusive) vs iloc (positions, exclusive) vs `[]` (labels
  when index is non-integer) — pick deliberately.
- Most operations return new objects (immutable-by-default style); assign
  results to variables or chain.
- pandas ≈ NumPy idioms + labels + alignment; stay vectorized.

## Notes
- Ch7–8 deepen cleaning and joins; ch10 covers groupby; ch11 time series.
- The baby-names / tips examples carry through later chapters.
