# Ch03 — Built-In Data Structures, Functions, and Files

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 3.

## Purpose
The Python built-ins that underpin all data work: tuples, lists, dicts,
sets; function essentials (anonymous/lambda, closures, generators); and
file I/O. pandas/NumPy build on these.

## Data structures
- **Tuple**: fixed-length, immutable sequence `(4, 5, 6)`. Use for
  fixed records; safe as dict keys. Supports unpacking: `a, b, *rest =
  values` (pluck with `*_`); `tup.count(x)`. Cannot be reassigned, but
  mutable objects *inside* can change.
- **List**: variable-length, mutable `[2, 3, 7]`. `append`, `insert`
  (expensive — shifts elements; use `collections.deque` for both ends),
  `pop`, `remove`, `in`, slicing `[::-1]`, `sorted`/`list.sort`,
  `bisect` for insertion in sorted lists.
- **Dict**: hashable key → value. `d.get(k, default)`, `d.update`,
  `setdefault`, `defaultdict` (auto-init), `Counter` (count items),
  dict comprehension, and `sorted(d.items(), key=...)` by value.
- **Set**: unordered unique collection; `&` (intersection), `|` (union),
  `-` (difference), `^` (symmetric diff), subset checks; `frozenset`
  immutable.

## Functions
- Default arguments, keyword args, `*args` / `**kwargs` collection.
- **Lambda**: anonymous single-expression functions — keep simple.
- **Closures**: inner functions capturing outer variables (nonlocal to
  rebind) — used for factory functions.
- **Generators**: functions with `yield` produce values lazily; use
  `list()` to materialize. Generator expressions `(x for x in ...)`.
- `itertools`: `groupby`, `chain`, `product`, `permutations`,
  `combinations`, `accumulate` — avoid hand-rolled loops.
- `functools.partial`, `map`/`filter` (often clearer as comprehensions),
  `sorted` key functions.

## Files
- `open(path, 'r')` returns file object; context manager `with` guarantees
  closing. Modes: `'r'/'w'/'a'/'x'`, `+` for read/write, `'b'` binary.
- Read: `read()`, `readlines()`, iterate `for line in f`, `read(n)`.
- Write: `write()`; check `os.path.exists`; `pathlib.Path` preferred in
  modern code (`.` / `/` operators).
- JSON: `json.loads`/`json.dumps` (with `lines=True` for line-delimited).
- `open(..., encoding='utf-8')` explicit for text; encoding errors raise.

## Key takeaways
- Choose the structure by the operation: dict for lookups, set for
  membership/dedup, list/tuple for order.
- Prefer comprehensions and itertools over loops for readability and
  speed; vectorized numpy/pandas over all three for bulk numeric work.
- `with open(...)` + explicit encoding — the two file habits that prevent
  the classic leaks and mojibake.

## Notes
- This is the "escape hatch" chapter: when pandas isn't the right tool
  (awkward text, custom parsing), these built-ins are the fallback.
- Complements our data-science-from-scratch ch02 note (same material,
  different emphasis).
