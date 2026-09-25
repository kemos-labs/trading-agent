# Chapter 10 — Performance Python

## Core idea
The "Python is slow" prejudice is wrong when you use the right tools. This
chapter benchmarks four approaches to speed up financial algorithms:
**vectorization**, **dynamic compiling (Numba)**, **static compiling
(Cython)**, and **multiprocessing**.

## The loop benchmark
Task: average `n=10,000,000` random numbers.
- Pure Python loop: ~1.3 s.
- NumPy vectorized: ~128 ms — **~10x speedup** (at higher memory cost).
- Numba JIT on the loop (`@njit`): near-C speed, often another 10x.
- Cython with static types: comparable to Numba.
- `multiprocessing.Pool` parallelizes across cores for embarassingly
  parallel tasks.

## Speedup toolbox
- **Vectorization first**: replace loops with array ops (already used since
  ch4).
- **Numba**: `from numba import njit; @njit def f(...)` — LLVM JIT-compiles
  pure Python (with supported types) to machine code.
- **Cython**: hybrid Python/C language; add static type declarations
  (`cdef double`) and compile to C.
- **multiprocessing**: `from multiprocessing import Pool` — map a function
  over inputs across processes (bypasses the GIL for CPU work).

## Case studies
- **Fibonacci**: naive recursion vs memoization vs compiled variants —
  algorithmic improvement beats micro-optimization.
- **Binomial trees** (ch10's worked example): vectorizing the CRR tree
  backward induction across all nodes (NumPy) vs Python loops gives large
  speedups — pricing arrays, not single nodes.
- **Monte Carlo simulation**: vectorized path generation (all paths at once)
  is dramatically faster than looping paths; variance reduction helps too
  (see ch12).
- **Recursive EWMA**: several implementations compared — a pure-Python
  recursion is slow; a closed-form vectorized update
  (`ewma = lambda*ewma_prev + (1-lambda)*r`) is fast; Numba/Cython get
  close to the vectorized version.

## Pitfalls
- Vectorization costs memory (n×m arrays); for huge problems use
  chunking/multiprocessing.
- Numba has a type-support subset; not every Python construct compiles.
- Multiprocessing needs picklable functions and has IPC overhead — worth it
  only for CPU-bound, chunkable work.
- Profile first (`%timeit`); don't optimize what isn't slow.

## Bottom line
The performance doctrine: vectorize, then JIT/compile hot loops, parallelize
embarrassingly parallel work, and always measure. This is the practical
backbone for the simulation-heavy valuation chapters (ch12, ch18–21).
