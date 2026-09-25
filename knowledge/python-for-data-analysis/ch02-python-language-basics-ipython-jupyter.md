# Ch02 — Python Language Basics, IPython, and Jupyter Notebooks

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 2.

## Purpose
Orientation for the Python language and the interactive environments
(IPython, Jupyter) used throughout the book. Not a full Python tutorial —
just enough to follow along.

## The interpreter & running code
- `python` runs scripts; IPython adds a richer interactive shell with
  numbered `In [n]:` prompts, pretty-printing of objects, tab completion,
  and magic commands.
- `%run file.py` executes a script in the IPython process so its objects
  stay available.
- Jupyter notebooks: cell-based documents mixing code, markdown, and
  output; one cell at a time. Plots render inline with `%matplotlib
  inline`.

## Key IPython magics for data work
- `%timeit` / `%time`: benchmark code.
- `%run`, `%load`, `%paste`, `%who` (list variables), `%magic` help.
- History navigation: `Ctrl-P/Ctrl-R`.
- `?` / `??` after an object shows its docstring/source; `obj?` works on
  functions, methods, attributes.

## Language basics worth internalizing
- **Dynamic typing + duck typing**: objects carry types; variables are
  just names. `a = 5` then `a = 'x'` is fine.
- **Indentation defines blocks**; no braces. Consistency matters (4 spaces
  conventional).
- **Everything is an object**: functions are first-class, can be passed
  and assigned.
- **Import conventions** used throughout: `import numpy as np`,
  `import pandas as pd`, `import matplotlib.pyplot as plt`.
- **Scoping**: functions can access globals read-only; assignments create
  locals. Avoid mutating globals inside functions.
- `is` vs `==`: identity vs equality (relevant for None checks: `x is
  None`).
- **Exceptions**: `try/except/else/finally`; catching `Exception` broadly
  is discouraged — catch specific types.

## Key takeaways
- Interactive iteration (IPython/Jupyter) is the default workflow for
  analysis: explore → refine → formalize into a script.
- The ecosystem idiom is concise array/code idioms, not verbose
  engineering patterns.
- Master the magics and object introspection (`?`) — they replace
  guesswork.

## Notes
- Chapter deliberately skips classes/OOP, pointing to Python Cookbook /
  Fluent Python for deeper language work.
- We already have the deep language/content equivalent in our
  hands-on-ml and learning-data-science notes; this chapter is the setup
  for the pandas-heavy chapters 4–13.
