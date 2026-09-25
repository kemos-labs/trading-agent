# Ch07 — Working with Relations Using SQL

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 7.

## Purpose
**Relations** (SQL tables) as an alternative to dataframes, and the SQL
language for manipulating them. Replicates ch6's baby-names analysis in SQL
for direct comparison.

## Relation vs dataframe
- Relation: rows have **no labels**, rows are **unordered**; columns have
  labels (attributes). Dataframes add row labels and ordering.
- Relations suit large data on disk: SQL engines manage paging/joins
  transparently; pandas loads everything into memory.

## SQL basics
- Query shape: `SELECT columns FROM table WHERE predicate ORDER BY col
  LIMIT n;`
- Slicing columns: list them in SELECT; slicing rows: LIMIT.
- Filtering: `WHERE` with comparisons and `AND/OR/NOT`.
- Grouping: `GROUP BY col` + aggregate functions (`COUNT`, `SUM`, `AVG`,
  `MIN`, `MAX`); `HAVING` filters groups (WHERE filters rows *before*
  grouping).
- Joins: `JOIN ... ON key` (inner); `LEFT/RIGHT/FULL JOIN` for outer
  variants. Multiple tables join in sequence.
- Sorting: `ORDER BY`; `DISTINCT` de-dupes.
- `pd.read_sql(query, engine)` runs SQL and returns a dataframe —
  `sqlalchemy.create_engine('sqlite:///file.db')` connects to SQLite
  (Postgres/MySQL share the core syntax).

## Key takeaways
- WHERE before GROUP BY; HAVING after. The most common SQL bug.
- Join keys must be well-defined; like merge, duplicate keys multiply rows.
- Typical workflow: subset/aggregate big data in SQL, pull down a smaller
  dataframe for visualization/modeling.
- Relations and dataframes are complementary mental models — the same
  operations exist in both; choose by data size and workflow.

## Notes
- The book uses SQLite + sqlalchemy for local files; production systems
  (Postgres, MySQL) add concurrency and scale.
- Relational algebra (tuples, attributes) is the formal underpinning;
  SELECT-FROM-WHERE is its practical face.
- SQL excels at set-based operations on data that lives on disk; pandas
  excels at in-memory analytics. Moving data between the two via
  `pd.read_sql` is the standard glue.
