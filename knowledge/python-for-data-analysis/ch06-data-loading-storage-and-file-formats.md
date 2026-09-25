# Ch06 — Data Loading, Storage, and File Formats

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 6.

## Purpose
The pandas I/O toolbox: reading/writing delimited text, binary formats
(pickle, HDF5, Parquet, Feather), and databases (SQL via SQLAlchemy), plus
the web (HTML tables, JSON).

## Text loading (`pd.read_csv` and friends)
- Family: `read_csv`, `read_table`, `read_fwf`, `read_clipboard`,
  `read_excel`, `read_json`, `read_html`, `read_sql`, `read_parquet`, …
  (~50 args on read_csv — the docs are the reference).
- Key args:
  - Header/index: `header=None`, `names=[...]`, `index_col='col'` or
    `['k1','k2']` (MultiIndex).
  - Delimiter: `sep`, regex `sep=r'\s+'` for whitespace; `skiprows`,
    `skipfooter` (with `engine='python'`), `comment` char, `nrows`.
  - Types: `dtype={'col': np.float32}`, `parse_dates=[...]`,
    `date_parser`; `na_values=['NA','']` custom missing markers.
  - Iteration: `chunksize` returns a TextFileReader you loop over —
    process big files without loading all at once.
  - Thousands/decimals: `thousands=','`, `decimal='.'`.
- Writing: `df.to_csv(path, index=False)` — always set `index` explicitly;
  `to_excel`, `to_json`, `to_parquet`.
- **Type inference pitfall**: mixed-type columns silently become object;
  dates need explicit `parse_dates`. Verify with `df.info()` after load.

## Binary formats
- **Pickle**: fast, Python-only, unsafe to load untrusted files. Used
  internally, prefer other formats for exchange.
- **HDF5 (PyTables/h5py)**: hierarchical, supports compression and huge
  arrays; `df.to_hdf(path, 'key')` / `read_hdf`. Good for large,
  structured numeric data.
- **Parquet/Feather**: columnar, cross-language, compression built in —
  the modern default for large tabular data (`read_parquet`/
  `read_feather`). Type information is preserved in the format.

## Databases
- `read_sql(query, engine)` with SQLAlchemy engine
  (`create_engine('sqlite:///...')`, also postgres/mysql).
- Load results into DataFrames; write back with `df.to_sql(name, engine)`.
- SQLite is great for local; Postgres/MySQL for server workloads (see
  our learning-data-science ch7 note).

## Interacting with the web
- `pd.read_html(url)` scrapes all `<table>` elements into DataFrames
  (works on Wikipedia etc.).
- `pd.read_json` for API responses; `requests` for more control; the
  `json` module for line-delimited records (ch13's Bitly example).

## Key takeaways
- Always peek at raw files before parsing; read_csv args solve most
  messes; `chunksize` handles big data.
- Prefer binary/columnar formats (Parquet, HDF5) for repeated reads and
  large data; CSV for exchange.
- Set `index=False` on writes, `parse_dates` on reads — the two most
  common round-trip mistakes.
- SQL is the natural home for large relational data; pandas is the
  analysis layer on top.

## Notes
- Complements learning-data-science ch8/ch14 and our data-pipelines
  skill; this chapter is the authoritative pandas I/O reference.
