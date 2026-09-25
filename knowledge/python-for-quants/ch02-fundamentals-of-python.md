# Chapter 2 — Fundamentals of Python

## Core idea
A thorough, example-driven tour of Python's core language: numbers and
arithmetic, exceptions, the `math` module, precision/rounding, lists,
randomness (Mersenne Twister), tuples/sets/dicts, and functions.

## Numbers, arithmetic, and logic
- **int vs float**: type is inferred — integer math stays int; any float in
  an expression makes the result float. `9/2` differs between Python 2
  (floor) and 3 (true division) — use `9.0/2` or `float()` to force float.
- **Comments**: full-line `#`, suffix comments, and triple-quoted block
  comments.
- **Big integers**: arbitrary precision — `3**219` works exactly
  (`.bit_length()` reports size); floats of the same value lose precision,
  so `3.0**219 == 3**219` is `False`.
- **sys.float_info** reveals float representation limits (max, epsilon
  ≈ 2.2e-16, mantissa digits).
- **Booleans** and `if-elif-else`; comparison and assignment operators;
  operator precedence in arithmetic.

## Imports, exceptions, and modules
- `import module`, `from module import name`, `import module as alias`.
- **Built-in exceptions**: `try/except` structure for error handling —
  catching `TypeError`, `ValueError`, `ZeroDivisionError`, etc.
- `math` module: trig, logs, `sqrt`, constants — and the `fractions` module
  for exact rational arithmetic.

## Rounding and precision
- Float arithmetic is inexact (binary representation) — `0.1 + 0.2` has
  roundoff; use tolerance comparisons or `fractions.Fraction` for exactness.
- `round()`, `%.Nf` formatting, and the `format()` function control display.
- **Near-zero maths**: guarding against tiny denominators/values; `Decimal`
  for decimal-exact financial math.

## Lists
- Construction, indexing (`x[i]`, negative indices), **slicing**
  (`x[a:b]`, `x[::-1]` for reversed), nesting, `range()`, `reversed()`.
- Methods: `append`, `extend`, `insert`, `pop`, `remove`, `index`, `count`,
  `sort` (raises `TypeError` on mixed types), `copy` (breaks shared links).
- Functions: `list()`, `min`, `max`, `len`.
- **Math/statistics with lists**: manual sums/means or the `statistics`
  module; symbolic manipulation via `sympy`.
- **Reference trap**: copying a list copies references — mutating a nested
  list affects copies; use `.copy()`/`deepcopy` for independence.

## Randomness built-in
- `random` module: pseudo-random generation; **seeding** for reproducibility.
- **True randomness**: `os.urandom` (system entropy) vs the deterministic
  PRNG.
- **Mersenne Twister**: Python's PRNG algorithm (MT19937) — long period
  (2^19937 − 1), good statistical quality; the chapter implements it to
  demonstrate its internals (bitwise ops, tempering).
- **Mersenne prime hunt**: computing `2^n − 1` primality as a performance
  demonstration (4+ hours for the 26th on one core).

## Tuples, sets, dicts
- **Tuple**: immutable ordered container — protects data from accidental
  modification; can serve as dict keys.
- **Set**: unique elements; membership tests, unions, intersections.
- **Dict**: key-value mapping — "call your broker" analogy; fast lookup by
  hashable key.

## Functions
- Single-argument and multivariable functions; `return` values;
  `lambda` anonymous functions; default parameters.
- Functions are the unit of reuse — the book builds quant helpers this way.

## Pitfalls
- Python 2 vs 3 division and `print` differences — write Python 3 idioms
  (`print(x)`, true division).
- Float precision for financial amounts — use `Fraction`/`Decimal` where
  exactness matters.
- Shared references on list copies.
- PRNG reproducibility requires explicit seeding.

## Bottom line
The language core, taught with quant-friendly examples (precision, big
numbers, randomness, statistics on lists). It prepares the NumPy chapter,
which is where real quantitative work begins.
