# Ch3 — Working with Financial Data

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## The data landscape

Four types of financial data, split along two axes:

|              | Structured            | Unstructured          |
|--------------|-----------------------|-----------------------|
| Historical   | EOD closing prices    | Financial news        |
| Real-time    | FX bid/ask quotes     | Tweets                |

The book focuses on structured data (numerical, tabular), historical and
real-time; this chapter covers importing, handling, and storing historical
structured data. "Clearly, data beats algorithms" — a trading project
starts with data quality before any hypothesis testing.

## Reading from different sources

- **Pure Python `csv` module**: `csv.reader` gives nested lists;
  `csv.DictReader` gives dicts keyed by header row. Workable but
  inefficient/unintuitive for analysis.
- **pandas**: `pd.read_csv(fn, index_col=0, parse_dates=True)` — one line
  yields a DataFrame with a datetime index; `.dropna()`, column selection,
  and `df.loc[start:end]` slicing handle the rest. This is the default.
- **Excel/JSON**: `to_excel`/`read_excel`, `to_json`/`read_json` for
  interchange.
- **Open data sources**: Quandl-style APIs provide open market data; the
  Eikon Data API (Refinitiv, via a Python wrapper) provides professional
  EOD/intraday data programmatically (used to build the book's sample
  dataset of EOD closing prices).
- **Web**: `pandas-datareader`-style access to remote CSV/API endpoints
  (the book's examples fetch a shared EOD CSV from a URL).

## Handling data

- Rename columns, compute returns (`data['return'] = np.log(data['price']
  / data['price'].shift(1))`), align with an index, and handle NaN via
  `dropna()`.
- Time-slice with `df.loc[start:end]`; resample/reindex for bar
  alignment.
- Quality checks: null counts, dtypes, range checks — the DataFrame's
  `.info()`/`describe()` summarize shape and missingness.

## Storing data efficiently

- **HDF5** (via pandas `to_hdf`/`read_hdf`, table format) is the binary
  storage format of choice for historical structured data: compact,
  fast, typed, chunked — far better than CSV for large panels.
- CSV is portable but slow and untyped for big data; HDF5 (or Parquet
  later) is the production choice.
- Store the processed form (prices + returns + metadata) so backtesting
  starts from a clean, reproducible input.

## Key takeaways

- Data beats algorithms: importing, cleaning, and storing data properly is
  the prerequisite for any backtest.
- pandas is the workhorse: `read_csv` with datetime index, log returns,
  slicing, null handling — a few lines cover the full import/handle loop.
- Structured × historical vs real-time is the organizing frame; streaming
  data comes in ch7.
- HDF5 for efficient, typed storage of historical panels; keep a
  reproducible pipeline (raw → cleaned → stored).
