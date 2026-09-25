# Chapter 4 — Numerical Computing with NumPy

## Core idea
NumPy's `ndarray` — a homogeneous, multidimensional array — is the workhorse
of numerical finance. Its power is **vectorization**: operations run on
compiled C-level loops, not Python loops.

## Key concepts
- **ndarray**: regular n-dimensional array of one dtype; supports vector
  (1-D), matrix (2-D), and higher-dimensional structures.
- **Structured (record) arrays**: 2-D arrays with named columns — the
  proto-DataFrame for tabular data.
- **Vectorization**: replace Python loops with array expressions;
  `np.random.random(n).mean()` beats a Python loop by ~10x.
- **Memory layout**: contiguous C-order arrays are fastest; copying/striding
  affects performance (relevant for large simulations).

## Essential operations
```python
import numpy as np
a = np.array([0.5, 0.75, 1.0])        # from list
m = np.random.standard_normal((5, 5)) # 2-D random draws
a[1], m[1][0]                          # indexing
a * 2, a + a                           # broadcasting elementwise
a.cumsum(), a.mean(), a.std()          # reductions
np.allclose(a, b)                      # tolerance-based float comparison
```
- Broadcasting: `a * 2` scales every element; `npr.rand(10) * (b - a) + a`
  transforms draws to any interval.
- Slicing returns *views* in NumPy (unlike Python lists) — mutations affect
  the original; use `.copy()` when independence is needed.

## Pitfalls
- **Lists-of-lists are reference-based**: `m = [v, v, v]` then mutating `v`
  changes all rows — use `deepcopy` (or better, build from a single ndarray).
- Mixing dtypes forces upcasting or errors; ndarray expects homogeneity.
- Vectorized ops trade memory for speed (a 10M-float array is 80 MB) — fine
  for mid-data (GB-scale), the sweet spot the book targets.

## Working with financial data
- Store OHLCV as an `(n, m)` ndarray or structured array with named fields
  (`price`, `volume`, `date`).
- Compute returns with `np.diff`/`pct_change`-style arithmetic on arrays.
- `np.argmax`/`np.argmin` locate peaks and troughs; `np.where` builds
  signals; `cumsum`/`cumprod` build equity-like series.
- Seed the RNG (`np.random.seed(1000)`) before any simulation so results
  are reproducible across runs.

## Bottom line
NumPy is the foundation layer: every later chapter (pandas, stochastics,
simulation, valuation) operates on ndarrays or pandas structures built on
them. The vectorization discipline established here is the book's core
performance doctrine, revisited in ch10 (Performance Python).
