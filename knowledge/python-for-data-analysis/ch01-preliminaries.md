# Ch01 — Preliminaries

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 1.

## Purpose
Sets the book's scope: the Python programming you need for data
manipulation, processing, cleaning, and analysis — with the pandas/NumPy
ecosystem as the centerpiece. Deliberately not a statistics or ML text;
it's the wrangling foundation those books assume.

## What "data" means here
Structured data in common forms:
- **Tabular**: spreadsheets, relational tables, delimited text — each
  column may have a different type.
- **Multidimensional arrays** (matrices).
- **Multiple related tables** keyed by columns (primary/foreign keys).
- **Time series**, evenly or unevenly spaced.
Most real datasets can be coerced into one of these forms; if not, you can
extract features (e.g. news articles → word-frequency table).

## Why Python
- Rich, mature scientific stack (NumPy, pandas, matplotlib, scikit-learn,
  statsmodels) with an active community.
- General-purpose language (unlike R/MATLAB/SAS): the same code does data
  prep, analysis, and software engineering.
- Fast to iterate for interactive analytics.

## The book's core message
- "Data manipulation"/"wrangling"/"munging" is the emphasis: reshaping,
  cleaning, and combining data — often 50–80% of an analyst's time.
- Workflow: load with pandas → clean/transform (ch7–8) → explore/plot
  (ch9) → aggregate (ch10) → time series (ch11) → hand off to modeling
  libraries (ch12).
- Data in memory vs on disk: tools assume datasets that fit on a personal
  computer; HDF5/Parquet handle bigger arrays.

## Key takeaways
- The pandas/NumPy split: NumPy = homogeneous numeric arrays; pandas =
  heterogeneous tabular data with labels. Know which tool each job wants.
- Real-world messy data is the norm; the whole book is about getting it
  into shape quickly and correctly.
- Version context (3rd ed.): Python 3.10, pandas 1.4, NumPy 1.23 — API
  details evolve, so verify against installed versions.

## Notes
- The book's examples come with data in a GitHub repo — reproducible
  practice is the point.
- Noted as prerequisite prep for the deeper ML texts (Géron, Grus, etc.),
  which we already have in /knowledge/.
