# Ch1 — Python and Algorithmic Trading

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## Why Python won in finance

CPython is an interpreted, high-level language — slow at nested loops,
which naive financial code (option pricing, risk simulation) uses
heavily. It took almost two decades for Python to become a major finance
language, with adoption accelerating ~2011. The fix was **vectorization**
via NumPy (released 2006): delegate looping to compiled C code operating
on homogeneous arrays, eliminating Python-level loops.

## Python vs. pseudo-code

Python's syntax is close enough to mathematical/pseudo-code that the
"pseudo-code step" is often unnecessary. The Euler discretization of GBM:

```
S_T = S_0 · exp((r − 0.5σ²)·T + σ·z·√T)
```

becomes, almost verbatim:

```python
S_T = S_0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * z * np.sqrt(T))
```

## NumPy and vectorization

- **ndarray**: the n-dimensional array class — immutable in size, single
  dtype (homogeneous), enabling specialized fast C code.
- **Vectorization**: operate on the whole array at once instead of looping.
  Simulating 1,000,000 GBM terminal values: pure Python for-loop ~1.15 s
  vs. one vectorized NumPy line ~0.16 s (≈8× faster, and far more
  concise).
- Trade-off: vectorization can have a big memory footprint (8 MB for a
  1M-float array); Numba/Cython alternatives exist when memory matters.
- pandas (the DataFrame class) sits on NumPy and adds labeled, tabular
  data handling — the standard for financial time series (columns, time
  indexing, missing data, rolling ops).

## Algorithmic trading workflow

The book's arc: (1) trading idea/hypothesis; (2) financial data;
(3) backtesting (vectorized for speed, event-based for realism);
(4) machine/deep-learning prediction; (5) real-time data + sockets;
(6) broker APIs (Oanda/FXCM) for deployment; (7) automation, capital
management, cloud deployment, logging/monitoring.

Strategy families covered:
- **Simple moving averages**: buy/sell signals from SMA crossovers
  (e.g. 42-day vs 252-day).
- **Momentum (time-series)**: recent performance persists → long winners,
  short losers.
- **Mean reversion**: prices revert to a mean/trend after deviating too
  far.
- **Machine/deep learning**: predict direction (classification) from
  lagged features.

## Key takeaways

- Vectorization (NumPy) is what made Python viable for quantitative
  finance: concise, fast, C-backed array operations; ~8× speedup on
  typical simulations.
- pandas DataFrames provide the tabular/time-series layer for market data.
- The end-to-end arc: idea → data → backtest → predict → real-time →
  broker → automate; each chapter of the book is one link.
- Watch the memory cost of vectorization and match tool to task (NumPy
  for speed, Numba/Cython for memory-constrained hot loops).
