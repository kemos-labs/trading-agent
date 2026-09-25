# Ch09 — Wrangling Dataframes

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 9.

## Purpose
The cleaning/reshaping toolkit that turns raw tables into **tidy** data
ready for analysis: tidiness, reshaping, string cleaning, and new features.

## Tidy data (the organizing principle)
Each row = one observation, each column = one variable, each cell = one
value. Tidiness is a *layout* choice, separate from cleanliness (correct
values). Many analyses fail because the data aren't tidy (e.g. one column
per category instead of one row).

## Reshaping
- **Long → wide**: `pivot` (or `pivot_table` for aggregation) turns
  category values into column names.
- **Wide → long**: `melt` collapses columns into a `variable`/`value` pair
  (id_vars stay as keys).
- Grouping and `agg` (ch6) pair naturally with reshape to summarize by
  category.

## Cleaning operations
- String fixes: lowercase, strip, replace substrings, split — on pandas via
  `.str` accessor (full treatment in ch13 with regex).
- Type coercion: `pd.to_numeric`, `pd.to_datetime`; handle parse errors
  with `errors='coerce'`.
- Missing values: identify with `isna`, decide drop vs fill based on *why*
  they're missing (MCAR vs systematic).
- Duplicates: `duplicated`/`drop_duplicates` — check whether duplicates are
  true repeats or legitimate repeated measurements.
- Outliers: find via summary stats/plots; decide keep/drop/flag with
  domain knowledge — don't blind-drop.

## Feature engineering
- New columns via `assign`: derived measures, indicators (e.g. presence of
  a word), binned categories.
- One-hot encoding (`pd.get_dummies`) turns categorical features into 0-1
  columns for modeling — drop one level to avoid perfect collinearity
  (ch18's donkey example does this explicitly).

## Key takeaways
- Tidy-first: most wrangling pain is actually a shape problem.
- Every cleaning decision (drop, fill, bin, merge) is a modeling decision —
  document it.
- Check what missing means before choosing drop vs fill; check what
  duplicates mean before deleting.

## Notes
- The chapter runs the restaurant-violations example (later used for regex
  features in ch13) and the air-quality data (later modeled in ch12/ch15).
- `pipe` chains custom functions into pandas pipelines for readability.
