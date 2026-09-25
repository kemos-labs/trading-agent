# Ch14 — Data Exchange

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 14.

## Purpose
Beyond CSV: binary (NetCDF), hierarchical (JSON), markup (XML/HTML) formats,
and acquiring data reproducibly over the web (HTTP, REST, scraping).

## NetCDF (binary scientific arrays)
- Model: variables as multidimensional grids (e.g. rainfall as a
  longitude × latitude × time cube). Dimensions, variables, coordinates,
  and metadata (attributes) live inside the file — self-describing.
- Advantages: compact, scalable subset access, appendable, sharable,
  self-describing, community tooling.
- Read with `xarray`: `xr.open_dataset(path)`; `ds.sel(lat=..., lon=...)`
  selects by coordinate labels; `.where(mask, drop=True)` filters.
- Other binary formats: SQLite, Feather, Apache Arrow.
- Use case: 2 GiB climate file (ERA5) as a dataframe would be hundreds of
  thousands of repeated lat/lon rows; the cube stores each coordinate once.

## JSON
- Two structures: **objects** `{"name": value, ...}` (like Python dicts)
  and **arrays** `[v1, v2, ...]` (like lists), freely nested.
- `json.loads`/`json.dumps`; the natural format for web APIs and
  semi-structured records (e.g. one JSON file per news article, ch21).

## Web acquisition
- **HTTP**: requests (GET/POST) with status codes; **REST**: resources
  addressed by URLs, acted on with methods.
- `requests.get(url).json()` for APIs; `pd.read_html` for tables on pages;
  `urllib`/`requests` + parsing for scraping.
- Reproducibility: code acquires data rather than manual downloads —
  record the date fetched, the terms of service, and save results so you
  don't re-hit servers needlessly. Check permission; prefer official
  formats/APIs over scraping; start small (polite rate).

## XML/HTML & XPath
- XML: nested tags with attributes; HTML is XML's web cousin.
- **XPath** expressions navigate trees: `//Cube[@currency="GBP"]/@rate`
  = find all Cube nodes with that attribute, return the rate attribute.
- `lxml` + `element.xpath(expr, namespaces={...})`; namespaces must be
  declared explicitly in expressions.
- Web scraping is tightly coupled to page structure — expect to re-edit
  when sites change (a maintainability caveat).

## Key takeaways
- Mental model first: understand a format's structure before reading it
  (the book's running principle).
- Choose format by data shape: cubes → NetCDF/xarray; hierarchical records
  → JSON; tabular → CSV/parquet; markup → XML/HTML.
- Fetch data with code, not copy-paste, to keep provenance and
  re-runnability.

## Notes
- Pairs with ch8 (files) and ch21 (scraping FakeNewsNet via the
  repository's own code).
- The ECB exchange-rate example (XML + XPath) is a template for reading
  financial data feeds — directly relevant to market data ingestion.
