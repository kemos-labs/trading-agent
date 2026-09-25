# Data Loader (quantkit.data_loader)

## name
Market-data loading, cleaning, and point-in-time adjustment: canonical
OHLCV frames, Chan-style split/dividend adjustment, returns, bar
resampling, outlier flags.

## description
The data-quality front door of the Phase 2 toolkit. Loads OHLCV from CSV
or yfinance into a canonical, validated frame (lowercase
open/high/low/close/volume, DatetimeIndex, sorted); adjusts history for
splits and dividends with multiplicative factors so daily returns are
invariant across ex-dates (Chan ch3); computes log/simple returns; resamples
to coarser bars with explicit closed/label conventions; and flags returns
more than z-sigma from the mean. Fails closed: never returns empty or
garbage frames, never fabricates data.

Implemented in `src/quantkit/data_loader.py` (module 1 of ROADMAP Phase 2);
tests in `tests/test_data_loader.py` (stdlib unittest).

## when to use it
- Any strategy/backtest pipeline that needs trusted OHLCV input — this is
  the load → clean → adjust → returns stage.
- Before backtesting with raw prices that have splits/dividends:
  unadjusted history shows spurious ex-date drops that generate false
  signals (the loader's `adjust_prices` removes them).
- As the shared column convention (`open/high/low/close/volume`) for the
  whole toolkit, so every downstream module speaks the same schema.
- Auditing a data feed: impossible bars (high < low, non-positive prices,
  negative volume, duplicates, >4-sigma returns) are dropped/flagged with
  warnings rather than silently used.

## the method

### 1. Load and canonicalize
`normalize_columns()` maps mixed-case CSV headers and yfinance's
MultiIndex columns (`[('Close','AAPL'), ...]`) to the canonical lowercase
five; multi-ticker frames are refused (single asset per frame).
`load_csv()` auto-detects the date column; `load_yfinance()` wraps
`yf.download` with `auto_adjust=True` by default and raises
`RuntimeError` if the feed returns nothing usable.

### 2. Validate (fail closed)
`validate_ohlcv()` coerces to numeric, then drops — with a warning —
rows with non-positive prices, high < low (H/L are the noisy pair),
negative volume, and duplicate timestamps (keep first). Fewer than two
valid rows → `ValueError`. This is Chan's data-error discipline: a
backtest is only as honest as its input.

### 3. Adjust for splits and dividends (Chan multiplier method)
For each corporate action at ex-date with prior close `C_{t-1}`:

```python
split_factor  = 1 / N                    # N:1 split
div_factor    = (C_{t-1} - d) / C_{t-1}  # $d cash dividend
```

Every observation strictly before the ex-date is multiplied by the
product of the factors of all later events:

```python
import pandas as pd
from quantkit import data_loader as dl

adj = dl.adjust_prices(raw_close, events)   # events: ex_date, split_ratio, dividend
```

Result: `100 → 50` across a 2:1 split becomes `50 → 50` — the daily
return across the ex-date is 0%, exactly as if the action never
happened. Verified in tests (`test_returns_invariant_across_split`).

### 4. Returns
`compute_returns(prices, log=True)` — log via
`np.log(p / p.shift(1))`, simple via `pct_change`; first row NaN;
zero/negative prices coerce to NaN instead of ±inf.

### 5. Bars and outliers
`to_bars(df, rule, closed='right', label='right')` — open=first,
high=max, low=min, close=last, volume=sum (the close-time label
convention). `flag_outliers(returns, z=4.0, window=None)` — boolean
`|r - mean| > z·σ`, full-sample or rolling.

## known pitfalls
- **Unadjusted prices in backtests**: split/dividend history must be
  adjusted or ex-date returns are fake — the #1 silent data bug (see
  Chan ch3). Use `auto_adjust=True` or your own `adjust_prices`
  schedule; never mix adjusted and raw in one series.
- **MultiIndex columns**: yfinance frames have `('Close','AAPL')`-style
  columns; normalize before indexing by name or every `df['close']`
  fails. `normalize_columns` handles it; multi-ticker frames raise.
- **H/L overconfidence**: recorded high/low may not be reachable at a
  limit price (small prints, wrong exchange) — H/L-based backtests
  overstate returns; the loader only guarantees internal consistency
  (high ≥ low), not fillability.
- **Survivorship bias**: this loader fixes the series you hand it; a
  universe built from today's listings still needs point-in-time
  snapshots of delisted names.
- **Resample edge conventions**: `closed`/`label` change which bar owns
  a boundary timestamp — be consistent across the pipeline, or bars
  silently mislabel.
- **Return edge cases**: zero/negative prices (bad data or a suspension)
  produce NaN, not ±inf — don't fill them with 0 (a 0 return is a claim
  about the market; NaN is a claim about the data).

## source
Chan, *Quantitative Trading*, 2nd ed., ch3 (split/dividend adjustment,
H/L noise, >4σ return flagging); skill `time-series-feature-engineering`
(returns via shift, OHLC bar edge conventions); skill `data-pipelines`
(fail-closed, no-fabrication discipline). Module: `src/quantkit/
data_loader.py`.
