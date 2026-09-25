# Time-Series Feature Engineering (pandas)

## name
Building model-ready features from time series with pandas: returns &
lags, rolling statistics, resampling to bars, and frequency conversion.

## description
The standard, vectorized toolkit for turning raw price/tick/volume data
into the features every trading model consumes: period returns and log
returns, lagged values, rolling mean/volatility, exponentially weighted
moments, OHLC bars via resampling, and time-of-day/seasonality grouping.
Built on pandas' DatetimeIndex machinery — alignment, shift, rolling,
expanding, ewm, and resample — with the closed/label edge conventions that
silently change results if ignored.

## when to use it
- Any strategy that consumes price series: from raw (tick/minute/daily)
  data to features for regressions, ARMA/GARCH, HMM regimes, or
  volatility targeting.
- Bar construction from tick/minute data (resample to 1min/5min/1D OHLCV).
- Rolling volatility, momentum, z-scores of price, or seasonal patterns
  (intraday/weekday effects).
- Reviewing a feature pipeline for look-ahead: shift discipline and
  closed/label mistakes are the classic leakage sources.

## method / formula / code

**1. Parse & index.** Convert to DatetimeIndex first:
```python
df = pd.read_csv("prices.csv", parse_dates=["date"], index_col="date")
ts = df["close"]                      # Series indexed by timestamp
```
Keep time zones explicit: `ts.tz_localize("UTC")` then
`ts.tz_convert("America/New_York")`. Store UTC internally; localize only
at the edges.

**2. Returns & lags (no look-ahead).**
```python
ret  = ts.pct_change()                # simple period return r_t
lret = np.log(ts).diff()              # log return — addable across periods
lag1 = ts.shift(1)                    # previous close: lag features
lead = ts.shift(-1)                   # future value — ONLY for labels, never features
```
`shift(1)` moves data FORWARD in time (the value at t−1 lands at t). A
feature built with `shift(-1)` or with an unshifted future value leaks the
future into training.

**3. Rolling / expanding / ewm windows.**
```python
ma   = ts.rolling(20).mean()                      # rolling mean
rvol = ret.rolling(20).std() * np.sqrt(252)       # annualized rolling vol
med  = ts.rolling(20, min_periods=10).median()    # min_periods for early rows
z    = (ts - ma) / ts.rolling(20).std()           # z-score / mean reversion
cum  = ts.expanding().mean()                      # expanding window from start
ewma = ts.ewm(span=20, adjust=False).mean()       # exponentially weighted
evol = ret.ewm(span=20, adjust=False).std()       # EWMA volatility
```
Rolling applies a fixed-size window; expanding grows from the start; ewm
weights recent points exponentially (span ≈ 2/α − 1).

**4. Resampling (frequency conversion).**
```python
bars = df.resample("5min").agg({
    "price": "ohlc",
    "volume": "sum",
})                       # tick/minute → 5-min OHLCV bars
daily = ts.resample("D").mean()          # downsample (high → low freq)
upsampled = ts.resample("h").ffill()     # upsample (low → high freq)
```
Downsampling bins by the target frequency: `closed="left"|"right"` picks
which edge is inclusive, `label="left"|"right"` picks the bin label.
Defaults are NOT uniform across frequencies (M/A/Q default
closed="right"). These change results — set them explicitly.

**5. Seasonality / calendar features.**
```python
by_hour  = ts.groupby(ts.index.hour).mean()       # intraday pattern
by_dow   = ts.groupby(ts.index.weekday).mean()    # day-of-week effect
is_month_end = ts.index.is_month_end              # calendar flags
```

**6. Sanity checks.**
- `df.index.is_monotonic_increasing` — sorted timestamps.
- `df.index.is_unique` — no duplicate timestamps (dupes break resample/rolling).
- After any shift/roll/resample, verify no NaN spikes and that `min_periods` covers the warm-up.

## known pitfalls
- **Look-ahead leakage**: `shift(-1)` or unsorted data in features.
  Features may only use t and earlier; sort by timestamp first.
- **In-place vs new object**: rolling/ewm/resample return NEW objects —
  assign results, don't expect mutation.
- **closed/label defaults**: month/quarter/year resample defaults differ;
  always pass them explicitly when bar edges matter.
- **Duplicate or non-monotonic timestamps** silently corrupt resample and
  rolling — check before aggregating.
- **pct_change vs log returns**: use log returns for compounding across
  periods and for models assuming normality; pct_change for simple math.
- **Annualization factor mismatch**: rolling std → annualize by
  sqrt(periods_per_year) (252 daily, 52 weekly, 252*6.5*60 for minute).
- **Window warm-up**: early rows are NaN — use min_periods or dropna
  before modeling, and don't fill with 0 (destroys the signal shape).

## source book
McKinney, *Python for Data Analysis* (O'Reilly, 3rd ed., 2022), ch11
(time series: datetimes, time zones, shifting, resampling, moving
windows). Related: Halls-Moore ch10–11 (ARMA/GARCH on returns),
Carver ch9–10 (vol targeting uses rolling vol), our
`arma-garch-modeling` and `volatility-targeted-position-sizing` skills.
