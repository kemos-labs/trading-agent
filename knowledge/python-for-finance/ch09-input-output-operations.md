# Chapter 9 — Input/Output Operations

## Core idea
Data storage and retrieval layers, from simple serialization to fast
hierarchical storage. I/O is often the bottleneck — CPUs starve waiting on
disks. The book's sweet spot: analytics tasks process a few GB, ideal for
in-memory Python + fast on-disk formats.

## Basic I/O with Python
- **pickle**: serialize any Python object to a byte stream
  (`pickle.dump(obj, f)` / `pickle.load(f)`); fast for Python objects but
  Python-specific and not safe with untrusted data.
- **Text files**: read/write CSV and text with the standard library.
- **SQL**: Python's sqlite3/db-API for structured queries.
- **NumPy**: `np.save/np.load` — fast binary storage of ndarrays.

## I/O with pandas
- `pd.read_csv()`, `pd.to_csv()` — the daily workhorse.
- Also `read_json/to_json`, `read_excel/to_excel`, `read_sql`, HDF5.
- Round-trip fidelity is good; CSV is portable, binary formats are faster.

## PyTables (HDF5)
- **HDF5 standard**: hierarchical, binary, self-describing storage.
- **PyTables** provides the pandas-friendly interface; huge speedups over
  CSV for large datasets — "speed is often only bound by the hardware."
- Structure data into tables with columns; compress and query on disk
  without loading everything into RAM.
- This is the storage layer for the book's big tick datasets (ch8).

## TsTables
- Builds on PyTables specifically for **time-series data**: fast append and
  retrieval of ticks/bars by timestamp.
- Ideal for high-frequency data stores (write ticks live, read windows for
  analysis).

## Pitfalls
- CSV is slow and untyped (parse dates/types on read).
- pickle is insecure (never unpickle untrusted files) and not
  cross-language.
- HDF5 has overhead for tiny datasets — use it for large/structured data.

## Bottom line
Choose the I/O layer by data size: CSV for small/portable, pickle for Python
objects, HDF5/PyTables for large financial datasets, TsTables for time
series. The book's later chapters (ch18–21) load simulation data via these
paths. Cross-ref: `knowledge/python-algorithmic-trading/ch03` (HDF5 via
to_hdf).
