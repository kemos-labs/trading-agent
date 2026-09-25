"""Market-data loading, cleaning, and adjustment utilities.

Module 1 of the Phase 2 core toolkit (ROADMAP). Implements the
data-quality discipline distilled in Phase 1:

- **Chan, *Quantitative Trading* ch3**: split/dividend adjustment via
  multiplicative factors so daily returns are invariant across ex-dates;
  high/low noise caution; flag returns > 4-sigma.
- **time-series-feature-engineering skill**: OHLC bar resampling with
  explicit closed/label edge conventions; returns via ``shift``.
- **data-pipelines skill**: fail closed, never silently fabricate data.

Vectorized pandas/numpy throughout; a short loop only over the (usually
tiny) corporate-action schedule.
"""

from __future__ import annotations

import warnings
from pathlib import Path

import numpy as np
import pandas as pd

# Canonical OHLCV column order for the whole toolkit.
OHLCV = ("open", "high", "low", "close", "volume")

# Case-insensitive column aliases → canonical names. "Adj Close" maps to
# close: callers that want adjusted history should pass adjusted prices.
_COLUMN_ALIASES = {
    "date": "date",
    "timestamp": "date",
    "time": "date",
    "open": "open",
    "high": "high",
    "low": "low",
    "close": "close",
    "adj close": "close",
    "adjusted close": "close",
    "volume": "volume",
}


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Rename a raw OHLCV frame to canonical lowercase columns.

    Handles yfinance's MultiIndex columns (e.g. ``[('Close','AAPL'),
    ('High','AAPL'), ...]`` for a single ticker) and mixed-case CSV
    headers (``Date``/``Open``/...). Raises if a required OHLCV column
    is missing or a multi-ticker frame is passed (this toolkit is
    single-asset per frame).

    Parameters
    ----------
    df : pd.DataFrame
        Raw data with recognizable OHLCV headers.

    Returns
    -------
    pd.DataFrame
        Frame with canonical ``open/high/low/close/volume`` columns,
        sorted by its index.
    """
    if df is None or len(df.columns) == 0:
        raise ValueError("no columns to normalize")

    columns = list(df.columns)
    if isinstance(df.columns, pd.MultiIndex):
        # yfinance: drop the ticker level; refuse multi-ticker frames.
        tickers = {str(c[1]) for c in columns}
        if len(tickers) > 1:
            raise ValueError(
                f"multi-ticker frame passed ({sorted(tickers)}); "
                "load one symbol per frame"
            )
        df = df.copy()
        df.columns = [str(c[0]) for c in columns]  # collapse to flat Index
        columns = list(df.columns)

    renamed: dict[str, str] = {}
    for col in columns:
        key = str(col).strip().lower()
        if key in _COLUMN_ALIASES:
            renamed[col] = _COLUMN_ALIASES[key]

    df = df.rename(columns=renamed)
    missing = [c for c in OHLCV if c not in df.columns]
    if missing:
        raise ValueError(f"missing required OHLCV columns: {missing}")

    df = df[list(OHLCV)].copy()
    if not isinstance(df.index, pd.DatetimeIndex):
        df.index = pd.to_datetime(df.index)
    return df.sort_index()


def validate_ohlcv(df: pd.DataFrame) -> pd.DataFrame:
    """Sanity-check a canonical OHLCV frame and drop impossible rows.

    Checks (with warnings, per Chan's data-error discipline):

    - numeric coercion (non-numeric cells → NaN, then rows dropped);
    - strictly positive prices (negative/zero quotes are impossible);
    - ``high >= low`` (H/L are the noisy pair — drop impossible bars);
    - non-negative volume;
    - duplicate timestamps (keep first, warn);
    - at least 2 remaining rows (fail closed).

    Parameters
    ----------
    df : pd.DataFrame
        Canonical OHLCV frame (see :func:`normalize_columns`).

    Returns
    -------
    pd.DataFrame
        Cleaned, sorted frame with at least 2 rows.
    """
    if set(OHLCV) - set(df.columns):
        raise ValueError("frame is not canonical OHLCV; run normalize_columns first")

    df = df.copy()
    before = len(df)

    for col in OHLCV:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    dropped = before - len(df.dropna(subset=OHLCV))
    if dropped:
        warnings.warn(f"dropped {dropped} row(s) with non-numeric prices")
    df = df.dropna(subset=OHLCV)

    price_cols = [c for c in OHLCV if c != "volume"]
    bad_price = (df[price_cols] <= 0).any(axis=1)
    if bad_price.any():
        warnings.warn(f"dropped {int(bad_price.sum())} row(s) with non-positive prices")
        df = df.loc[~bad_price]

    bad_hl = df["high"] < df["low"]
    if bad_hl.any():
        warnings.warn(
            f"dropped {int(bad_hl.sum())} row(s) where high < low "
            "(H/L are noisy — verify against the feed)"
        )
        df = df.loc[~bad_hl]

    bad_vol = df["volume"] < 0
    if bad_vol.any():
        warnings.warn(f"dropped {int(bad_vol.sum())} row(s) with negative volume")
        df = df.loc[~bad_vol]

    if df.index.duplicated().any():
        n = int(df.index.duplicated().sum())
        warnings.warn(f"dropped {n} duplicate timestamp(s), keeping first")
        df = df.loc[~df.index.duplicated(keep="first")]

    df = df.sort_index()
    if len(df) < 2:
        raise ValueError("fewer than 2 valid rows after cleaning — data source unusable")
    return df


def load_csv(
    path: str | Path,
    *,
    date_column: str | None = None,
    index_col: str | int | None = None,
) -> pd.DataFrame:
    """Load an OHLCV CSV into a canonical, validated frame.

    The date column is located automatically (``Date``/``Timestamp``/
    ``Time``) unless ``date_column`` is given; a pandas ``index_col``
    passes through unchanged when ``date_column`` is None.

    Parameters
    ----------
    path : str | Path
        Path to the CSV file.
    date_column : str, optional
        Name of the date column to use as the index. If None, any column
        recognized as a date alias is used.
    index_col : str | int, optional
        Passed to ``pandas.read_csv`` when ``date_column`` is None.

    Returns
    -------
    pd.DataFrame
        Cleaned, sorted canonical OHLCV frame.
    """
    path = Path(path)
    df = pd.read_csv(path, index_col=index_col)

    if date_column is None:
        date_candidates = [
            c for c in df.columns if str(c).strip().lower() in ("date", "timestamp", "time")
        ]
        if date_candidates:
            date_column = date_candidates[0]
        elif isinstance(df.index, pd.RangeIndex):
            raise ValueError(
                "no date column found; pass date_column= or index_col= with parsed dates"
            )

    if date_column is not None:
        df[date_column] = pd.to_datetime(df[date_column], errors="raise")
        df = df.set_index(date_column)

    df = normalize_columns(df)
    return validate_ohlcv(df)


def load_yfinance(
    symbol: str,
    start: str | None = None,
    end: str | None = None,
    *,
    interval: str = "1d",
    auto_adjust: bool = True,
) -> pd.DataFrame:
    """Load real daily OHLCV for one symbol from Yahoo Finance.

    Fails closed: raises if the feed returns nothing usable. With
    ``auto_adjust=True`` (default) the OHLC series are pre-adjusted for
    splits and dividends — the right inputs for backtests; keep it
    ``False`` only when raw prices are needed (e.g. to apply your own
    :func:`adjust_prices` schedule).

    Parameters
    ----------
    symbol : str
        Yahoo ticker, e.g. ``"AAPL"``.
    start, end : str, optional
        ``YYYY-MM-DD`` bounds (inclusive start). Defaults to the feed's
        own history length.
    interval : str, optional
        Bar size (``"1d"`` default; intraday needs ``period``-style
        bounds, not ``start``/``end``).
    auto_adjust : bool, optional
        Return split/dividend-adjusted OHLC (default True).

    Returns
    -------
    pd.DataFrame
        Canonical validated OHLCV frame, sorted ascending.

    Raises
    ------
    RuntimeError
        If the download fails, is empty, or yields fewer than 2 bars.
    """
    try:
        import yfinance as yf  # local import: optional dependency
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("yfinance is not installed in this environment") from exc

    df = yf.download(
        symbol,
        start=start,
        end=end,
        interval=interval,
        auto_adjust=auto_adjust,
        progress=False,
    )
    if df is None or df.empty:
        raise RuntimeError(f"yfinance returned no data for {symbol!r}")

    df = normalize_columns(df)
    df = validate_ohlcv(df)
    if len(df) < 2:
        raise RuntimeError(f"fewer than 2 usable bars for {symbol!r}")
    return df


def adjust_prices(close: pd.Series, events: pd.DataFrame | None = None) -> pd.Series:
    """Point-in-time split/dividend adjustment (Chan ch3 multiplier method).

    Prices *before* each ex-date are scaled so that the daily return
    across the ex-date is unchanged by the corporate action — raw
    adjusted history is continuous, removing spurious ex-date drops that
    would otherwise generate false signals.

    Each event contributes a multiplicative factor applied to every
    observation strictly before its ex-date:

    - split ``N`` for an N:1 split: factor ``1/N``;
    - cash dividend ``d`` (per share) with last close ``C_{t-1}``:
      factor ``(C_{t-1} - d) / C_{t-1}``.

    Factors compound across events (product of all factors for events
    after a given date).

    Parameters
    ----------
    close : pd.Series
        Raw (unadjusted) close prices, DatetimeIndex, ascending.
    events : pd.DataFrame, optional
        Corporate-action schedule with columns ``ex_date``
        (Timestamp), ``split_ratio`` (float, N for N:1), ``dividend``
        (float, per share). Either field may be NaN/0 and is skipped.

    Returns
    -------
    pd.Series
        Adjusted close, same index/length as ``close``.
    """
    close = close.astype(float)
    if events is None or len(events) == 0:
        return close.copy()

    adjusted = close.copy()
    for row in events.itertuples(index=False):
        ex_date = pd.Timestamp(row.ex_date)

        prev = close[close.index < ex_date]
        if prev.empty:
            continue
        prev_close = float(prev.iloc[-1])

        factor = 1.0
        split = getattr(row, "split_ratio", np.nan)
        if pd.notna(split) and float(split) > 0:
            factor *= 1.0 / float(split)
        div = getattr(row, "dividend", np.nan)
        if pd.notna(div) and float(div) > 0 and prev_close > 0:
            factor *= (prev_close - float(div)) / prev_close

        mask = close.index < ex_date
        adjusted.loc[mask] *= factor

    return adjusted


def compute_returns(prices: pd.Series | pd.DataFrame, *, log: bool = True) -> pd.Series | pd.DataFrame:
    """Daily returns from prices.

    Log returns via ``np.log(p / p.shift(1))``; simple returns via
    ``pct_change()``. First row is NaN; non-finite results (zero or
    negative prices) are coerced to NaN rather than ±inf.

    Parameters
    ----------
    prices : pd.Series | pd.DataFrame
        Prices, DatetimeIndex.
    log : bool, optional
        Log returns (True, default) or simple returns (False).

    Returns
    -------
    pd.Series | pd.DataFrame
        Returns, same shape as ``prices`` with NaN first row.
    """
    prices = prices.astype(float)
    with np.errstate(divide="ignore", invalid="ignore"):
        if log:
            out = np.log(prices / prices.shift(1))
        else:
            out = prices.pct_change()
    out = out.replace([np.inf, -np.inf], np.nan)
    return out


def to_bars(
    df: pd.DataFrame,
    rule: str,
    *,
    closed: str = "right",
    label: str = "right",
) -> pd.DataFrame:
    """Resample an OHLCV frame to coarser bars.

    Aggregations: open = first, high = max, low = min, close = last,
    volume = sum. ``closed``/``label`` follow the pandas convention —
    for sub-daily rules, ``closed='right', label='right'`` labels each
    bar with its final timestamp (the bar's close time). Note: pandas
    (>= 2.2) ignores ``closed``/``label`` for daily-and-coarser rules;
    a daily bar is labeled at its day's midnight, which is the
    standard OHLC convention, so no action is needed.

    Parameters
    ----------
    df : pd.DataFrame
        Canonical OHLCV frame, DatetimeIndex, ascending.
    rule : str
        pandas offset alias, e.g. ``"1D"``, ``"1h"``, ``"15min"``.
    closed, label : str, optional
        Interval edge conventions for ``resample`` (default both
        ``"right"``).

    Returns
    -------
    pd.DataFrame
        Resampled canonical OHLCV frame (bars with no data dropped).
    """
    if not isinstance(df.index, pd.DatetimeIndex):
        raise ValueError("frame must have a DatetimeIndex")
    agg = {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}
    out = df.resample(rule, closed=closed, label=label).agg(agg)
    return out.dropna(subset=["open", "high", "low", "close"])


def flag_outliers(returns: pd.Series, *, z: float = 4.0, window: int | None = None) -> pd.Series:
    """Flag returns more than ``z`` standard deviations from the mean.

    Chan's data-error check: ``|r - mean| > z * sigma``. Uses the
    full-sample mean/std by default, or a rolling estimate when
    ``window`` is given. NaN returns are never flagged.

    Parameters
    ----------
    returns : pd.Series
        Return series (see :func:`compute_returns`).
    z : float, optional
        Number of standard deviations (default 4.0).
    window : int, optional
        Rolling window for the mean/std; full-sample when None.

    Returns
    -------
    pd.Series
        Boolean Series aligned with ``returns`` (True = suspect).
    """
    r = returns.astype(float)
    if window is None:
        mu = r.mean()
        sigma = r.std(ddof=1)
    else:
        mu = r.rolling(window).mean()
        sigma = r.rolling(window).std(ddof=1)
    flags = (r - mu).abs() > z * sigma
    return flags.fillna(False)
