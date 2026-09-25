# Ch04 — NumPy Basics: Arrays and Vectorized Computation

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 4.

## Purpose
NumPy's `ndarray`: fast array-oriented computing that pandas is built on.
Vectorization (no Python loops) is the performance core of the ecosystem.

## Why NumPy is fast
- Data stored in one contiguous memory block; C algorithms run over it
  without per-element type checking.
- Vectorized ops on whole arrays: `arr * 2` on 1M elements ≈ 70× faster
  than the list comprehension. 10–100× faster than pure Python, less
  memory.

## ndarray fundamentals
- Homogeneous typed container; attributes `shape` (tuple per dim), `dtype`
  (`float64`, `int64`, `bool`, etc.), `ndim`.
- Creation: `np.array(seq)`, `np.zeros`, `np.ones`, `np.empty` (uninit —
  don't assume zeros), `np.arange`, `np.linspace`, `np.full`, `np.random`.
- dtypes: specify with `dtype=np.float32`; mixed lists → common type
  (`int`+`float` → float).
- **Views vs copies**: slicing returns a *view* sharing memory — mutating
  a slice mutates the base array (`arr[2:5]` then modify). Use
  `arr.copy()` to detach. This is the #1 NumPy surprise.

## Operations
- Vectorized arithmetic elementwise: `+ - * /`, comparisons → Boolean
  arrays, `np.exp/log/sqrt/abs`, ufuncs (`np.add`, `np.maximum`).
- Boolean indexing / fancy indexing: `arr[arr > 5]`, `arr[[0, 2, 4]]`,
  assignment via masks. Boolean masks and fancy indexes return copies.
- **Broadcasting**: align arrays with different shapes by stretching
  dimensions (e.g. `arr` (4,3) + `row` (3,)). Rules: trailing dims must
  match or be 1. Shape `(3,1)` + `(3,)` → `(3,3)`.
- Transpose `.T`, reshape (may return view/copy), `np.where(cond, a, b)`
  for conditional vectorized logic, `np.unique`, `np.in1d`.
- `np.sort` (returns copy) vs `arr.sort()` (in-place).
- Linear algebra: `np.dot`/`@`, `np.linalg.inv/solve/qr/eig`.
- Random: `np.random.standard_normal`, `seed`/`default_rng` for
  reproducibility.

## Aggregations & set ops
- `arr.sum()`, `.mean()`, `.std()`, `.min()`, `.max()`, `.cumsum()`,
  `.cumprod()` — with `axis=0/1` for row/column directions (axis =
  dimension being *collapsed*).
- `np.unique(arr, return_counts=True)`, `np.in1d`, intersect/union/diff.

## Key takeaways
- Think in arrays, not loops: every loop over array elements is a
  candidate for a vectorized expression.
- Watch views vs copies; when in doubt, `.copy()`.
- Broadcasting + Boolean masks + `np.where` cover most conditional logic.
- pandas sits on top; `df.to_numpy()` is the handoff point (ch12).

## Notes
- Advanced NumPy (memory-mapping, C/F-order, performance tips) is in
  Appendix A; basics here are enough for the rest of the book.
- Overlaps with Grus ch4 (linear algebra) and hands-on-ml ch2 — this is
  the canonical reference.
