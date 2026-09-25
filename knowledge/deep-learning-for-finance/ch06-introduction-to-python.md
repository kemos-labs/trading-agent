# Ch06 — Introduction to Python

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 6.

## Purpose
A crash course in the Python data stack used throughout the book:
core language essentials, NumPy for vectorized math, and pandas for
time-series manipulation. Everything after this chapter is built on
these tools.

## Python essentials
- Data types: int, float, str, bool; containers: list, tuple, dict,
  set. List comprehensions `[expr for x in it if cond]` replace loops
  for most data transforms.
- Control flow with `if/elif/else`, `for`, `while`; functions defined
  with `def`; exceptions via `try/except`.
- Write vectorized code, not loops, over data — it is orders of
  magnitude faster and matches how NumPy/pandas work internally.

## NumPy
- The **ndarray** is a homogeneous n-dimensional array; built via
  `np.array`, `np.arange`, `np.zeros`, `np.linspace`.
- Vectorized ops: `a + b`, `a * 2`, `np.dot`, `np.sqrt` apply
  elementwise without Python loops.
- Key functions: `np.mean`, `np.std`, `np.corrcoef`, `np.random`
  (seeded via `np.random.seed(42)` for reproducibility),
  `np.percentile` for VaR-style tail estimates.
- Shapes and broadcasting: operations align dimensions automatically
  when shapes are compatible — shape mismatches are the classic bug.

## pandas
- **Series** (1-D labeled) and **DataFrame** (2-D labeled table) are
  the workhorses; the index is often a datetime for financial data.
- I/O: `pd.read_csv` loads data; `df.head()`, `df.describe()`,
  `df.info()` for inspection; missing data via `df.isna().sum()` and
  `df.dropna()` / `df.fillna()`.
- Time series: `df.set_index('date')`, `df.resample('D')` for
  frequency conversion, `df['col'].shift(1)` for lagged features,
  `.rolling(n).mean()` for moving averages, `.pct_change()` for
  returns.
- Merging/joining: `pd.concat` and `df.merge` combine datasets by
  axis or key; index alignment is automatic and powerful.

## Key takeaways
- Learn the idiom "no explicit loops over data": every loop has a
  vectorized pandas/NumPy equivalent, and vectorized code is both
  faster and less bug-prone.
- Reproducibility discipline: fix random seeds, keep data-loading and
  preprocessing in functions, and log data shapes at every transform.
- The pipeline (load → clean → feature-engineer → split → model →
  evaluate) is the skeleton of every chapter that follows; master
  pandas rolling/shift/pct_change now and the ML chapters are mostly
  about choosing models.
