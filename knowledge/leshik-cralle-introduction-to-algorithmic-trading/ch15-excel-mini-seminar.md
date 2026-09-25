# Chapter 15 — Excel Mini Seminar

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Setup philosophy

- Excel chosen for its universal spreadsheet + rich, microcode-optimized
  function language (fast execution). Book uses Excel 2003 (64K rows;
  2007's 1M rows not needed; one row per transaction).
- **One Excel instance per traded stock** — safe, redundant, fast
  overall; costs CPU/RAM/SSD. Keep files <20–30MB (the authors admit to
  125MB+ — not recommended).
- Work left-to-right, top-down (matches Excel's recalc order); split an
  algo across columns for transparency, compact later.

## Essentials

- Cell refs: letter column + number row (e.g., A1). Ranges (A1:B200).
- Formulas start with `=`. Operators: `+ − * / ^`. **Relative
  addressing** adjusts refs when copied (crucial for copy-down);
  `$A$1` locks (absolute/mixed).
- `'` before `=` displays a formula as text (notes/markers).
- **IF/Boolean logic** (Boole's algebra, 1850s): `=IF(A1=10,1,"")`;
  AND/OR/NOT (capitals), truth tables, chaining/nesting with
  parentheses. Used to build trigger conditions.
- Key functions: STDEV (σ), SUM, AVERAGE, MEDIAN (sorts first), MAX,
  MIN, SLOPE (linear regression slope = rate of change), CORREL.

## Key takeaways

1. The book's algo = Excel function code over tick data columns, using
   relative addressing for series computation and IF/Boolean logic for
   triggers.
2. Operational rules: one instance per stock, small files, frequent
   saves/backups, transparent column-wise decomposition.
