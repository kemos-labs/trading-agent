# Ch24 — Databases and SQL

**Source:** Grus, *Data Science from Scratch*, Chapter 24.

## Purpose
Data at rest: relational databases, SQL, and why **indexes** matter. The
chapter builds a toy in-memory database (`NotQuiteABase`) to make the
concepts visible, then maps them onto real SQL.

## The toy database
- `Table` with column names and rows (dicts); operations:
  - `update(predicate, updater)`, `delete(predicate)`;
  - `select(columns, where)`;
  - `where(predicate)` → filtered table;
  - `join(other_table, left_join_key, right_join_key)` — nested loop over
    all pairs matching keys;
  - `group_by(grouping_columns, aggregates, having)` — partition rows,
    apply aggregate functions (`sum`, `count`, `avg`, `max`, `min`);
  - `order_by`, `limit`.
- Every operation **returns a new table** — the functional, pipeline style
  mirrors SQL's declarative composition.

## SQL (the real thing)
- Core statements: `SELECT cols FROM t WHERE cond JOIN t2 ON k GROUP BY g
  HAVING cond ORDER BY col LIMIT n`.
- **Joins**: INNER (matching rows only), LEFT OUTER (all left rows, NULL
  where no match), CROSS (every pair), SELF (a table joined to itself).
- The toy `join` is a nested loop; the SQL engine chooses the plan — you
  just *declare* the result you want.

## Indexes — the chapter's key lesson
- Without an index, a lookup/join scans **every row** (O(n) per table;
  nested-loop joins over two big tables ≈ forever).
- **Indexes** let the database find rows by key directly and enforce
  constraints (`UNIQUE` on `user_id` rejects duplicates on insert).
- Designing indexes is "something of a black art" — but knowing they exist
  and which columns are keys is the practical takeaway.

## Query optimisation
- Two SQL queries can produce identical results with very different cost:
  **filter before joining** (`WHERE interest='SQL'` first, then join) beats
  join-then-filter, because the join operates on far fewer rows.
- In SQL you declare intent; the **query planner** (using indexes) chooses
  the execution — trust it, but write filters early in your pipelines.

## NoSQL
- Beyond tables: document stores (MongoDB — schemaless JSON docs), column
  stores (good when few columns are queried), key/value stores (fast single
  lookups), graph databases, time-series stores, in-memory databases.
- The book's light touch: "NoSQL is a thing" — the right tool depends on
  access patterns.

## Key takeaways
- Relational data = tables; SQL is declarative composition of select/
  join/group/filter.
- Indexes turn O(n) scans into key lookups and enforce uniqueness —
  the single biggest database performance lever.
- Push filters down before joins in your own pipelines (the same rule as
  MapReduce: reduce data volume early).

## Notes
- pandas `DataFrame` (ch27) is conceptually the same Table idea with far
  better performance — the toy's `select`/`group_by` map 1:1 to pandas.
- SQLite/Postgres/MySQL are the production choices the book points to.
