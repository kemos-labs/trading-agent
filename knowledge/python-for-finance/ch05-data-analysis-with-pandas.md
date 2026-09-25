# Chapter 5 — Data Analysis with pandas

## Core idea
pandas adds labeled, indexed data on top of NumPy: the **DataFrame**
(2-D tabular) and **Series** (1-D). Financial analysis in the book runs
almost entirely through pandas.

## The DataFrame
- Built from lists, dicts, or ndarrays with `columns` labels and an `index`:
  ```python
  df = pd.DataFrame([10, 20, 30], columns=['numbers'], index=['a','b','c'])
  ```
- **Selection**: `.loc['label']` (label-based), `.iloc[1:3]` (position-based),
  `.loc[['a','d']]` for multiple rows.
- **Vectorized ops**: `df.sum()`, `df.apply(lambda x: x**2)`, `df ** 2` —
  column-wise operations with broadcasting.
- **Columns** can be added/assigned; index and columns are `Index` objects
  with labels.

## The Series
A DataFrame with one column — index + values. The natural container for a
single time series (prices, returns).

## GroupBy
- Group rows by one or more keys: `df.groupby('col').mean()` etc. — the
  split-apply-combine pattern for aggregations.

## Complex selection
- Boolean conditions: `df[df['col'] > threshold]` — vectorized filtering.

## Combining data
- **concat**: stack DataFrames along rows/columns.
- **join/merge**: combine on keys/indices (SQL-like) — essential for joining
  price series from different sources.

## Performance
- pandas is often as fast as raw NumPy for typical operations; but `apply`
  with Python functions is slow — prefer vectorized/NumPy expressions.
- Choosing the right operation (e.g., `rolling().mean()` vs manual loops)
  matters.

## Pitfalls
- **Index alignment**: operations align on index automatically — misaligned
  indices silently produce NaN (a common finance gotcha).
- `.loc` vs `.iloc` confusion (labels vs positions).
- Chained assignment warnings: modify via `.loc`/`.iloc` on the object, not
  through chained indexing.

## Typical finance workflow with pandas
1. `pd.read_csv(..., index_col=0, parse_dates=True)` — indexed time series.
2. Derive columns: `df['returns'] = df['close'].pct_change()`, rolling
   means/stds, lagged columns via `.shift(k)`.
3. Filter rows with boolean conditions; group by year/month for aggregates.
4. Join instruments on the DatetimeIndex to build a multi-asset frame.
5. Plot with pandas/matplotlib; export with `to_csv`/`to_hdf`.

## Bottom line
pandas is the analysis layer: read data, derive columns, select/filter,
group, combine. Everything in ch8+ (time series, backtesting, valuation)
assumes fluency here. Cross-refs:
`knowledge/python-finance-algo-trading-2ed/ch02` (canonical df shape).
