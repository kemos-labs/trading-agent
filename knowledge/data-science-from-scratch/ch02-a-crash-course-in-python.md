# Ch02 — A Crash Course in Python

**Source:** Grus, *Data Science from Scratch*, Chapter 2.

## Purpose
A fast tour of Python 3 for readers new to the language — the subset needed
for the rest of the book. Nothing algorithmically deep; it sets up the
language idioms the later chapters rely on.

## Core language pieces used throughout the book
- **Basics**: `None`, booleans (`True`/`False`), `and`/`or`/`not`, `is` vs
  `==` (identity vs equality), `if`/`elif`/`else`, `for`/`while`, `range`.
- **Lists**: indexing (incl. negative), slicing `lst[1:4]` / `lst[:2]` /
  `lst[::2]`, `in`, `append`, `extend`, list comprehensions
  `[x**2 for x in xs if x > 0]`, `sorted` with `key=`.
- **Tuples**: immutable, unpacking `a, b = (1, 2)`; the book uses tuples
  heavily for (key, value) pairs.
- **Dictionaries**: `d[k] = v`, `d.get(k, default)`, `d.items()`, `d.keys()`,
  dict comprehensions.
- **Sets**: `set`, membership tests `x in s`, union/intersection.
- **Control flow**: `break`/`continue`, `enumerate` (index + value), `zip`
  (pair up iterables — the book uses `zip(xs, ys)` constantly to pair inputs
  with outputs).
- **Functions**: `def`, default args, `lambda` (small anonymous functions,
  used as `key=` sort functions), docstrings.
- **`in` / `not in`** semantics, `Counter` from `collections` for tallying.

## Typing (the book's signature style)
- The book uses **type annotations** (`def add(x: int, y: int) -> int`) and
  `from typing import ...` (`List`, `Dict`, `Tuple`, `Callable`, `Iterator`,
  `NamedTuple`, `Optional`).
- **`NamedTuple`** is the book's main way to define small data records with
  readable fields, e.g. `class Rating(NamedTuple): user_id, movie_id, rating`.
- This makes the code self-documenting and lets each example state its data
  shape explicitly.

## Idioms that appear everywhere later
```python
from collections import Counter, defaultdict
Counter(labels).most_common(1)[0]      # majority vote (ch12)
defaultdict(list)                      # group-by collector (ch22, ch25)
sorted(pairs, key=lambda p: p[-1], reverse=True)  # sort by score
random.seed(0)                         # reproducible experiments
tqdm.trange(...)                       # progress bar in training loops
```

## Key takeaways
- The single most important idioms for the book: **list comprehensions,
  `zip`, `sorted(..., key=)`, `Counter`, `defaultdict`, and NamedTuple**.
- `is` vs `==`: `is` checks identity (only for singletons like `None`);
  `==` checks value.
- Randomness is always seeded for reproducibility (`random.seed(...)`).
- Reading this chapter is optional for experienced Python devs; skip to
  ch3+ and come back only if a later snippet confuses you.

## Notes
- Purely a language tutorial; no formulas or data-science content.
- The style choice (from-scratch, typed, seeded) is itself a lesson: code
  for clarity and reproducibility.
