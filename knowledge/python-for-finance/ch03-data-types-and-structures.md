# Chapter 3 — Data Types and Structures

## Core idea
The Python fundamentals that everything else builds on: basic types
(int, float, bool, str) and the core container structures (tuple, list,
dict, set).

## Basic types
- **int**: arbitrarily large — Python uses as many bits as needed
  (`10**100` works; `bit_length()` reports the size).
- **float**: IEEE binary representation — `0.35 + 0.1 == 0.44999999999999996`.
  Never test float equality; use tolerance/`np.allclose`.
- **bool**: `True`/`False`, subclass of int.
- **str**: immutable text; Python 3 uses Unicode throughout.
- Dynamic typing: `type(x)` infers at runtime; "everything is an object"
  (ints have methods too).

## Data structures
- **tuple**: immutable container — use for fixed records; hashable (usable as
  dict keys).
- **list**: mutable, ordered, flexible — the workhorse container; supports
  slicing, appending, comprehensions.
- **dict**: key-value store with fast lookup; keys must be hashable
  (tuples ok, lists not).
- **set**: collection of unique elements; membership tests and set algebra
  (union/intersection/difference).
- **Copy semantics trap**: `m = [v, v, v]` repeats *references* to `v` —
  mutating `v[0]` changes all rows. Use `deepcopy(v)` from the `copy` module
  to build independent rows.

## Python idioms used throughout the book
- List comprehensions: `[gauss(1.5, 2) for _ in range(n)]`.
- `np.where(cond, a, b)` for vectorized conditional selection.
- Iteration over collections and `enumerate`/`zip` patterns.
- Functional touches: `map`, `filter`, `lambda` — used where concise.

## Pitfalls
- Mutable default arguments and shared references cause subtle bugs
  (the `[v]*3` trap).
- `1/4` gives `0.25` in Python 3 (true division); `1//4` floors.
- Floats are inexact — financial math needs decimal care or tolerance-based
  comparison (though most of the book uses floats with NumPy).

## Bottom line
The language primer. For finance, the key takeaways are the reference-copy
trap and float inexactness, plus the comprehension/`np.where` idioms that
recur in every later chapter.
