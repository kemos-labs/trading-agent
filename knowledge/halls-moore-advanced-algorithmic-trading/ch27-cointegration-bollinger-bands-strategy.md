# Ch27 — Cointegration + Bollinger Bands Strategy (ARNC/UNG)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 27 (QSTrader application).

## Hypothesis
Structural economic link: aluminum smelting (Bayer + Hall-Héroult processes) needs huge
electrolysis electricity; CCGT power uses natural gas as main fuel → natural-gas price affects
aluminum producer profitability. Hypothesis: **Alcoa (ARNC) stock and natural-gas ETF (UNG)
are cointegrated** → mean-reverting spread trade (inspired by Ernie Chan's GLD-GDX strategy
and Quantopian CEO John Fawcett's post on aluminum smelting).

## Testing (R)
- Data: ARNC & UNG adjusted closes, 2014-11-11 → 2017-01-01 (quantmod).
- Scatter: slight partial positive correlation only.
- **Linear regression** ARNC ~ UNG → slope (hedging ratio) = **1.213**.
- **CADF/ADF test on residuals**: **insufficient evidence to reject the null of no
  cointegration** — the structural relationship isn't statistically supported. Still implemented
  to (a) show flexible QSTrader backtesting machinery for any cointegration pair, and
  (b) see how a pair trades when the null isn't rejected.

## Strategy: Bollinger Bands on the z-scored spread
- **Bollinger Bands**: rolling SMA of the price series ± scalar multiple of rolling SD (same
  lookback) — a rolling volatility estimate.
- Compute **z-score** of the latest portfolio market value: z = (P − rolling mean)/rolling SD.
- Entry/exit rules:
  - z ≤ −z_entry → **long** the portfolio (long ARNC, short 1.213×UNG).
  - z ≥ +z_entry → **short** the portfolio (short ARNC, long 1.213×UNG).
  - Already invested & z ≥ −z_exit → close long; z ≤ z_exit → close short.
- Params (arbitrary): lookback = 15 bars, z_entry = 1.5, z_exit = 0.5; base_quantity = 10,000
  units (fractional share 1.213 × base rounded via floor to integer share quantities).
- Costs: net of simulated IB US fixed pricing (as ch25).

## QSTrader implementation details
`CointegrationBollingerBandsStrategy(AbstractStrategy)` params: lookback, weights (fixed
hedging ratios / Johansen eigenvector components), entry_z, exit_z, base_quantity.
- `_set_correct_time_and_price`: populates `self.latest_prices`; **only trades when all
  tickers have same-timestamp prices** (handles out-of-order market events; works for any
  number of tickers, not just pairs).
- Rolling window via `collections.deque(maxlen=lookback)` of "unit portfolio market value"
  (dot product of latest prices with weights).
- `go_long_units` / `go_short_units`: per-component SignalEvents — short components with
  negative weight, long positive; quantities = floor(qty × weight_i).
- `zscore_trade(zscore)`: long entry (z < −z_entry), short entry (z > +z_entry), close long
  (z ≥ −z_exit), close short (z ≤ +z_exit); tracks `self.invested`.
- `calculate_signals`: on BAR → update prices → if all present, append port market value,
  compute z-score (only after lookback bars elapsed), call zscore_trade.
- Backtest wrapper `coint_bollinger_backtest.py`: builds YahooDailyCsvBarPriceHandler,
  PriceParser(500,000 initial equity), IBSimulatedExecutionHandler, TearsheetStatistics.

## Results & critique
- **Implicit look-ahead bias**: hedging ratio (1.213) was computed on the *same sample* the
  strategy runs on → grossly exaggerated performance vs real implementation (needs separate
  estimation vs trading samples).
- Reported: **Sharpe ≈ 1.22**, max daily drawdown ≈ 7.02%. Majority of gains in a single month
  (Jan 2015); poor afterwards; in drawdown through 2016 — consistent with no significant
  cointegration found.
- Improvements: refine smelting economics (electricity from many sources — hydro, coal,
  nuclear, not just gas); Alcoa itself hedges commodity exposure; consider a broader portfolio
  (aluminum price + producers + multiple energy ETFs).

## Takeaways / pitfalls
- **ADF rejection of cointegration ⇒ don't trust the pair**; results here mostly reflect
  look-ahead + a lucky month.
- Always split estimation vs trading samples to avoid implicit look-ahead from fixed ratios.
- Bollinger/z-score bands are simple volatility-threshold entries — calibrate lookback &
  entry/exit z via optimisation/grid search.
- QSTrader pattern: strategy with weights + deque-based rolling stats works for arbitrary
  multi-asset cointegrated portfolios.