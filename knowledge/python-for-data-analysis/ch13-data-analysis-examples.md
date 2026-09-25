# Ch13 — Data Analysis Examples

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 13.

## Purpose
Five end-to-end analyses applying every tool from the book: Bitly
(JSON+counting), MovieLens (merge/groupby), US Baby Names (aggregate/
pivot), USDA (cleaning/normalizing), and 2012 FEC donations (groupby/
pivot/plots). A template for "load messy data → wrangle → explore →
summarize → present".

## 13.1 Bitly 1.USA.gov data (JSON, counting)
- Line-delimited JSON: `json.loads` per line → list of dicts → 
  `pd.DataFrame(records)`.
- Missing fields: guard with `if 'tz' in rec`; missing values show as
  NaN; `frame.info()` reveals per-column null counts/dtypes.
- Counting: pure Python (defaultdict/Counter) vs pandas
  (`value_counts()`) — pandas wins for brevity and speed.
- Clean unknown/empty categories; group by OS (Windows vs other) via
  `'a'` user-agent sniffing; `value_counts(normalize=True)` for shares;
  groupby + `transform('sum')` to normalize within group before plotting
  (seaborn barplot with hue).
- Lesson: start small (sample the file), count, then refine.

## 13.2 MovieLens 1M (joins + pivot)
- `read_table(sep='::', names=[...], engine='python')` for non-CSV
  delimited files; merge users/ratings/movies on ids.
- `pivot_table('rating', index='title', columns='gender',
  aggfunc='mean')` → gender-difference matrix; sort by diff column for
  "movies women like more than men".
- Active viewers: `groupby('title').size()` filter by count threshold
  (only titles with ≥ N ratings) before trusting means — small-sample
  bias guard.
- Lesson: joins + pivot_table + size-filtering is the canonical
  recommendation-style summary.

## 13.3 US Baby Names 1880–2010
- Read many per-year CSVs: `pd.concat([...])` with `keys`/ignore_index;
  or glob + list comprehension.
- `groupby(['year','sex']).sum()` → total births; `pivot(year, sex)`
  → wide for plotting; normalize per year/sex for share-of-name analysis.
- Find top names per year: groupby('year').apply(top_n) or sort +
  nlargest.
- Name "fads": filter by name, plot share over time (boy/girl curves);
  use `nunique()` on year to measure persistence (e.g. names used in
  every year vs fads).
- Lesson: concat many files → groupby/agg → pivot → plot is the whole
  loop; ranking within groups via apply.

## 13.4 USDA food database (cleaning/normalizing)
- Wide, messy records (nutrient fields); use `.str` vectorized string
  ops, `str.split`/`str.extract` to parse free-text columns; convert
  dtypes with `to_numeric(errors='coerce')`.
- Normalize by unit; `groupby(['category']).apply` for summaries;
  `value_counts` for distributions.
- Lesson: free-text → structured features via vectorized string methods
  (ties to our learning-data-science ch13 regex/tf-idf notes).

## 13.5 2012 FEC donations (groupby + pivot + plots)
- `map` with a dict to add derived categories (candidate → party);
  `occ_mapping.get(x, x)` pass-through trick for partial mappings.
- Filter: positive contributions only; subset to main candidates with
  `isin`.
- `pivot_table('contb_receipt_amt', index='occupation',
  columns='party', aggfunc='sum')` → party-by-occupation totals; filter
  rows by total (> $2M); `plot(kind='barh')`.
- `groupby('cand_nm').apply(get_top_amounts, key, n)` → top employers/
  occupations per candidate; `nlargest`.
- Lesson: value_counts cleanup → mapping → pivot_table → horizontal bar
  chart answers "who gives to whom".

## Key takeaways
- The five examples are the same pipeline in different clothes: load
  (right parser) → clean (missing/dupes/dtypes/strings) → combine
  (merge/concat) → summarize (groupby/pivot) → plot → interpret.
- Small-sample filtering (min count) before comparing means; normalize
  before comparing shares.
- dict.get pass-through + `.str` parsing + pivot_table are the highest-
  leverage, most-reused patterns.

## Notes
- This is the practical capstone to ch3–12; the patterns map directly
  onto market-data work (tick→bars, symbols→returns tables, portfolio
  attribution by sector/regime).
