# Ch20 — Multiprocessing and Vectorization

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 20.

## Purpose
The computational infrastructure behind the book's methods: replace
loops with vectorized array ops, and split jobs across processors
(multiprocessing) to make heavy ML/backtest workloads tractable.

## Vectorization
- Replace explicit loops with array operations (NumPy) — C/C++
  under the hood. Four benefits: fast iterators, dimensionality
  inferred from the data, no code change for higher dimensions,
  compiled speed.
- Example: the Cartesian product of a parameter grid as vectorized
  array broadcasting instead of nested For-loops; a 100-dimensional
  search needs no new code.

## Single-thread vs. multithreading vs. multiprocessing
- Modern machines: multiple sockets → cores → threads per core.
- Python's **GIL** allows one thread per core to execute Python code —
  multithreading doesn't give parallelism for CPU-bound Python.
- **Multiprocessing** spawns separate processes (separate memory):
  true parallelism, but objects must be passed explicitly.
- Rule of thumb: vectorize first, then multiprocess the vectorized
  units, then distribute across an HPC cluster — three levels of
  parallelism compose.

## Atoms and molecules
- **Atoms** = indivisible tasks; **molecules** = groups of atoms run
  sequentially on one processor by a callback. Parallelize at the
  molecular level.
- **Linear partitions** (`linParts`): split N atoms into N_processors
  contiguous chunks. Poor when tasks have unequal complexity (the
  heavy molecule dominates). Front-load heavy molecules so light ones
  backfill idle CPUs.
- **Two-nested-loops partitions**: triangular task sets (e.g., SADF
  windows, pairwise covariances) — partition rows so each molecule's
  workload is balanced; heavy-row molecules get assigned first.

## The `mpPandasObj` pattern
- The book's workhorse: given a set of atoms (indices), partition into
  molecules, dispatch each to a process via an engine (joblib,
  multiprocessing), collect results in order, concatenate.
- Works over any pandas/vectorized function: apply the parallel
  dispatcher to the *index range* and let the function slice its
  inputs by molecule — clean, hardware-agnostic, testable.

## Key takeaways
- Performance discipline: vectorize → multiprocess → cluster; each
  level multiplies the gain.
- Balance molecule workload (linear for equal tasks, triangular-aware
  for nested loops) or wall-time is set by the heaviest molecule.
- Design functions to take an index "molecule" argument from the
  start — retrofitting parallelism later is far costlier.
