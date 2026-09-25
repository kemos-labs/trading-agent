# Ch07 — Data Cleaning and Preparation

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 7.

## Purpose
The cleaning toolkit: missing data, duplicates, transformations,
**string/vectorized string manipulation**, and categorical data — the
"80% of analyst time" work.

## Missing data (NA)
- Representation: `NaN` (float sentinel), `NaT` (datetime), `None`
  treated as NA; `pd.NA` for extension types.
- Detect: `isna()`/`notna()` (on Series/DataFrame/index); summaries
  exclude NA by default.
- Filter: `dropna()` — `how='all'` (rows all-NA), `thresh=n` (keep rows
  with ≥ n non-NA), `axis='columns'` for columns.
- Fill: `fillna(value)` (constant, dict per column), `method='ffill'/'bfill'`
  (forward/backward fill), interpolation; `limit` caps how far ffill goes.
- Decide drop vs fill based on *why* data is missing (systematic vs
  random) — analysis of missingness itself is informative.

## Duplicates
- `duplicated()` marks rows (keep='first'/'last'/False); `drop_duplicates()`
  removes them; check on key columns `subset=[...]` rather than whole rows.
- Confirm duplicates are true repeats before deleting (ch9
  learning-data-science lesson).

## Transformations
- `map` (Series element-wise via dict/function — the dict.get pass-through
  trick for partial mappings), `apply`/`applymap`.
- Replace values: `df.replace(a, b)` / dict form.
- Rename axes: `df.rename(index=..., columns=...)`.
- **Binning**: `pd.cut(x, bins, labels=...)` (equal-width), `pd.qcut`
  (equal-frequency/quantile) — returns categorical; pair with
  `value_counts()`/`groupby` for bucket analysis.
- **Dummies**: `pd.get_dummies(df, columns=[...])` one-hot encodes
  categoricals (drop first for collinearity if modeling).
- Vectorized functions: `np.where`, `np.select` for multi-condition
  transforms.

## String manipulation (vectorized `.str`)
- `.str` accessor: `.lower()`, `.upper()`, `.strip()`, `.replace(a,b)`
  (regex=False for literal), `.split()`, `.contains(pat)`, `.startswith/endswith`,
  `.extract(pat)` (regex groups → columns), `.findall`, `.len()`, `.cat`,
  `.join`, `.get`, `.slice`.
- `str.contains(regex)` for pattern filtering; `str.extract` for pulling
  structured pieces out (log lines, identifiers).
- Missing values propagate (result NaN where input NA).

## Categorical data
- `pd.Categorical(values, categories=[...], ordered=True)` — fixed
  category set with order (ordinal). Benefits: memory efficiency,
  semantics, consistent categories for modeling.
- `astype('category')` converts; `cat.codes`, `cat.categories`;
  reorder with `cat.reorder_categories`.

## Key takeaways
- NA handling is a *decision*, not a default: know the missingness
  mechanism before dropping or filling.
- Vectorize strings via `.str` — never loop over string columns.
- cut/qcut + dummies + rename/map form the standard feature-prep
  pipeline before modeling (ch12).
- Cleaning transforms feed the data-pipelines skill (fit-on-train-only
  discipline applies to every statistic you compute here).

## Notes
- Ch8 covers combining datasets (merge/concat) — the other half of
  wrangling; ch13 shows cleaning at scale in real examples.
