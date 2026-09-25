# Ch06 — Working with Dataframes Using pandas

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 6.

## Purpose
Dataframes: the workhorse representation of tabular data in Python, via
`pandas`. This chapter covers the core manipulation vocabulary used
throughout the book.

## Mental model
- A **DataFrame** is a table: rows = records, columns = features. Both rows
  and columns have **labels**; rows are ordered and have an **index** (the
  index is labels, not data).
- A **Series** is a single column.
- Columns are typed (same type within a column); a statistical "type"
  (nominal/ordinal/numeric, ch10) is distinct from the storage dtype.

## Core operations
- **Slicing** (subset rows/cols):
  - `.loc[label]` — by row/column *label* (inclusive ranges).
  - `.iloc[pos]` — by integer *position* (exclusive end).
- **Filtering**: Boolean Series mask — `df[df['sex'] == 'F']`. Combine with
  `&`, `|`, `~`.
- **Sorting**: `df.sort_values('col')`.
- **Grouping**: `df.groupby('col')['other'].mean()` — split-apply-combine:
  split by key, apply function to each group, combine results. `agg` for
  multiple functions; `value_counts()` for counts.
- **Joining**: `df1.merge(df2, on='key')` combines tables on matching
  columns; kinds = inner/left/right/outer. Watch for key name collisions
  and duplicate keys (cartesian blow-up).

## Pipeline style
- Chain operations with method calls for readable pipelines.
- `assign` adds columns; `drop` removes; `rename` relabels.
- Missing values: `isna()/dropna()/fillna()`.

## Key takeaways
- `.loc` labels vs `.iloc` positions is the #1 source of pandas bugs —
  `.loc` ranges are inclusive, `.iloc` are exclusive.
- groupby + agg is the workhorse for EDA ("compare means by category").
- Merge is where silent row multiplication happens — always sanity-check
  row counts after a join.
- Same operations in SQL (ch7) replicate the chapter's analysis for
  comparison.

## Notes
- The baby-names dataset (SSA) runs through the chapter; note its
  documented limitations (only binary sex, coverage after 1937, 100% of
  card applications).
- pandas is favored for exploration/modeling; SQL (ch7) is favored for
  large data on disk.
