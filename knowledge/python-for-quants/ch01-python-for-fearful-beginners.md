# Chapter 1 — Python for Fearful Beginners

## Core idea
The on-ramp chapter: why a quant should learn Python, how to install it,
and how to work with it — with the book's signature conversational,
example-driven style.

## The book's philosophy
- Written for **quantitative analysts** in finance, algorithmic trading, and
  risk management — assumes maths/statistics background, not programming.
- **Copy-and-run is the beginner's instinct**: read code, run it, modify it —
  learning happens by alteration.
- Reading advice from the author's mentor: re-read anything you don't
  understand until you do.
- The trilogy goal: turn quantitative problems into Python code,
  "efficiently, exhaustively, and effortlessly."
- Margin tips throughout: alternative syntax (e.g., `g = lambda x: x**2`),
  code idioms, and quick-reference `Code 0.0` blocks showing function
  usage with examples.

## Conventions used in the book
- Plain code (no `>>>`) = script; `>>>` = interactive-mode commands; output
  shown beneath.
- Marginal labels mark new functions/commands for quick reference.
- `%`-formatting for output: `print("You have $%.2f" % wallet)`.

## Installing Python
- Official python.org distribution (vanilla).
- **Anaconda (recommended)**: bundles Python + NumPy + SciPy + pandas +
  matplotlib + Jupyter — the scientific stack out of the box, plus `conda`
  for package/environment management. This is what the book uses
  (Anaconda Python 3.5 at time of writing).

## Using Python
- **Interactive mode** (REPL): quick experiments.
- **.py scripts**: saved programs run with the interpreter.
- **IDEs**: PyCharm, PyDev in Eclipse, Spyder (scientific IDE), Rodeo —
  each with code completion, debugging, and variable inspection; Spyder
  suits quantitative work.

## Bottom line
A motivational + setup chapter. The key practical takeaways: use Anaconda
for the scientific stack, learn by running/modifying code, and adopt the
book's script/interactive conventions. Nothing here is finance-specific —
it primes the reader for the fundamentals in ch2 and NumPy in ch3.
