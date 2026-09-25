# Ch11 — Time Series

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 11.

## Purpose
The pandas time-series toolkit — the most finance-relevant chapter:
datetimes, DatetimeIndex, time zones, shifting, **resampling**, moving
windows, and date ranges.

## Date/time types
- stdlib: `datetime`, `date`, `time`, `timedelta`, `tzinfo`.
- pandas: `Timestamp` (scalar), `DatetimeIndex`, `to_datetime` (parses
  many formats, None → **NaT**), `date_range(start, periods, freq=...)`.
- Format codes: `%Y %m %d %H %M %S %f %j %w %z %F %D` — `strftime` out,
  `strptime` in; `pd.to_datetime` preferred for arrays.
- Frequencies: `D` day, `B` business day, `H` hour, `T/min` minute, `S`
  second, `M` month-end, `A` year-end, `W` week, `Q` quarter, plus
  multiples like `5min`, `2H`, and anchored offsets `BM`, `BQ`, `W-MON`.

## Time series basics
- A Series with a DatetimeIndex; arithmetic aligns on dates (partial
  overlap → NaN). `ts[::2]`, slicing by dates `ts['2011-01-02':'2011-01-08']`.
- Indexing by year: `ts['2011']`, `ts['2011-06']`.
- `DatetimeIndex` stores `datetime64[ns]`; scalar elements are Timestamps.

## Time zones
- Naive by default (`tz=None`). `tz_localize('UTC')` assigns a zone
  (validates ambiguous DST times); `tz_convert('America/New_York')`
  converts. Internally stored as UTC nanoseconds — converting doesn't
  change `.value`.
- Mixing zones in arithmetic yields UTC. DateOffset arithmetic respects
  DST transitions (Hour() vs fixed timedelta).
- Use `ZoneInfo`/pytz for names; store/compare in UTC.

## Shifting
- `ts.shift(1)` moves data forward in time (lags); `ts.shift(-1)` leads.
- `tshift` was removed in pandas 2.0 (deprecated earlier) — use `shift`
  with freq-aware offsets where needed.
- Rolling/shifting is the machinery for return/lag features.

## Resampling (frequency conversion)
- `ts.resample(rule)` → groupby on time bins, then `.mean()/.sum()/
  .ohlc()/.first()/.last()`.
- **Downsampling** (high→low freq): define bin edges; `closed='left'|
  'right'` (which side inclusive), `label='left'|'right'` (which edge
  labels the bin). Defaults vary by freq (M/A/Q default closed='right').
- **Upsampling** (low→high): fill with `ffill()/bfill()` or interpolate;
  `limit` caps fill distance.
- `ohlc()` aggregation is the standard bar construction for OHLCV.
- Grouping by time-of-day/weekday: `ts.groupby(ts.index.hour).mean()`,
  `groupby(ts.index.weekday)` — intraday seasonality analysis.

## Moving window functions
- `ts.rolling(window, min_periods=...)`: `.mean()/.std()/.sum()/.apply(fn)`
  — rolling volatility, moving averages.
- `expanding()`: cumulative window from start (e.g. expanding mean).
- `ewm(span=..., adjust=False)`: exponentially weighted — the 
  exponentially weighted moving average/std for vol models.

## Key takeaways
- Resample + rolling + shift cover the full feature-engineering core for
  time-series models (returns, lags, rolling vol, OHLC bars).
- Watch `closed`/`label` defaults in downsampling — they change results;
  keep data tz-aware in UTC and localize only at the edges.
- shift(1) creates lags; rolling().std() estimates volatility — these feed
  our arma-garch and volatility-targeting skills directly.

## Notes
- The book's ch13 (US baby names / FEC) and the time-series examples
  (stock data) apply these tools end-to-end.
- For finance, combine with resample('D').ohlc() to build bars from
  tick/minute data — a Phase 2 toolkit building block.
