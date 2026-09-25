# Ch08 — Data Wrangling: Join, Combine, and Reshape

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 8.

## Purpose
The combining/rearranging half of wrangling: **hierarchical indexing
(MultiIndex)**, `merge`/`join` for keyed combines, `concat` for stacking,
and reshape via `stack`/`unstack`/`pivot`/`melt`.

## Hierarchical indexing (MultiIndex)
- Multiple index levels on an axis: `pd.MultiIndex.from_arrays`,
  `from_tuples`, `from_product`.
- Partial selection: `data['b']`, `data.loc[:, 2]` (inner level),
  `data.loc[['b','d']]`.
- `unstack()` → pivot inner level to columns; `stack()` → back to rows.
  Pair with `sort_index(level=...)` and `swaplevel`.
- Levels can be named (`index.names`) and reordered; `.nlevels`.

## Combining: merge/join
- `pd.merge(left, right, how='inner'|'outer'|'left'|'right', on=[keys])`
  — SQL-style joins on columns.
- Keys: `on` (shared), `left_on`/`right_on` (different names),
  `left_index`/`right_index` (join on row indexes; MultiIndex joins =
  multi-key).
- **Duplicate keys multiply rows** (many-to-many explosion) — always
  sanity-check row counts after a join.
- `validate='one_to_one'` etc. catches unexpected key cardinality.
- Suffixes for overlapping columns: `suffixes=('_l','_r')`.
- `indicator=True` adds a `_merge` column ('left_only'/'right_only'/'both').
- `df.join(other, on=key)` is the index-friendly shortcut; `concat` for
  stacking.

## Combining: concat
- `pd.concat([df1, df2], axis=0)` stacks rows (default), `axis=1` stacks
  columns side-by-side; `ignore_index=True` to reset labels; `keys=...`
  adds a hierarchical level tagging source frames; `join='inner'/'outer'`
  controls alignment of columns.

## Reshaping
- `stack()`/`unstack()`: rotate between long and wide forms via the index
  (tidy-data mechanics).
- `pivot(index, columns, values)`: spread a column's values into column
  headers (requires unique index or use `pivot_table` with aggfunc).
- `pivot_table(values, index, columns, aggfunc='mean')`: group-based
  reshape with aggregation — the workhorse for reports.
- `melt(id_vars, value_vars)`: wide → long (each measured column becomes
  a row pair); the inverse of pivot.
- Long vs wide choice follows the task: plotting/modeling often wants
  long; reporting wants wide.

## Key takeaways
- Merge by keys, concat by position: pick the right tool; both can
  silently duplicate rows.
- MultiIndex + unstack/stack is the generic reshape engine; pivot_table
  and melt are the ergonomic wrappers.
- Check row/column counts before and after every combine — alignment
  surprises are silent.
- Ties to learning-data-science ch9 (tidy data) and our data-pipelines
  skill (leak-safe combining).

## Notes
- Ch10's groupby uses these reshaping tools constantly; ch13 applies
  merge/concat/pivot to real datasets.
