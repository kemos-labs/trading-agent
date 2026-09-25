# Ch08 — Wrangling Files

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 8.

## Purpose
Reading tabular data from disk: **delimited** (CSV/TSV) and **fixed-width**
(FWF) plain-text formats — the first step of any data pipeline.

## CSV/TSV (delimited)
- Rows separated by newlines, fields by a delimiter (`,` or tab). Optional
  header row.
- `pd.read_csv(path)`; parameters: `sep`, `header`, `names`, `skiprows`,
  `na_values`, `dtype`.
- Issues that break naive reads: quotes/escapes inside fields, inconsistent
  delimiters, trailing commas, missing values masquerading as blanks, and
  type inference surprises (e.g. "1,234" read as string or thousands).
- `.to_csv()` writes back; always round-trip check.

## Fixed-width format (FWF)
- Fields occupy exact character ranges (no delimiter): each row is a string
  of fixed length; columns are slices by (start, end).
- `pd.read_fwf(path, colspecs=[(0,8),(8,14),...])`.
- Use when records are inherently fixed-width (logs, legacy mainframe
  dumps); parsing is positional so off-by-one spec errors silently misalign
  columns.

## The parsing workflow
1. **Peek** at raw lines before parsing (encoding, headers, stray lines).
2. Choose parser + parameters to match the format.
3. Verify: shape, dtypes, and a sample of values against the source.
4. Handle missing values explicitly (`na_values`).

## Key takeaways
- Always eyeball the raw file first — "clean" CSV rarely is.
- Type inference from strings is fragile; pass `dtype` explicitly when the
  column's meaning matters.
- The same "mental model of the format" approach extends to binary formats
  (NetCDF, SQLite, Arrow) in ch14: understand the structure before reading.
- Encoding: specify `encoding` when non-ASCII text appears (UTF-8 vs
  Latin-1 vs UTF-16); wrong encoding silently garbles strings.

## Notes
- Chapter pairs with ch14 (Data Exchange) for richer formats; ch13 covers
  less-structured text (regex) used to clean awkward files.
- CSV is the lowest common denominator for exchange; it loses types, so
  schema knowledge must travel alongside the file.
- For very large files, read in chunks (`chunksize`) or use column
  selection to avoid loading more than needed into memory.
