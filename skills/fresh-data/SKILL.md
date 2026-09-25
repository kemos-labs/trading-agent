# Fresh-data pulls (terminal-backed backtest data)

- **description**: Pull fresh daily OHLCV for backtesting from the same
  free-tier providers trading-terminal-pro uses, with its budget/cache/
  fail-closed discipline ported to Python: quota-ledgered calls, TTL file
  cache, provider chain, never synthetic. Reference implementation of the
  terminal's `api/deskFeeds.js` + `api/upstreamCache.js` patterns.
- **when to use it**: Extending research windows past the SHA-pinned
  2010–2024 cache, refreshing `data/live/` stores, or any diagnostic that
  needs bars newer than the last offline pull. Never for live orders
  (paper-only guard still applies).
- **method/formula/code**:
  - Keys at runtime from `TERMINAL_ENV` (default
    `/home/kalde/trading-terminal-pro/.env`); `load_terminal_keys` raises
    if unreadable. Keys never enter the repo, logs, or the browser.
  - Chain in `pull_symbol`: Massive/Polygon range aggs (adjusted, asc) →
    Alpha Vantage TIME_SERIES_DAILY compact (25/day × 0.85 headroom) →
    raise with all provider errors (yfinance stays caller-side via
    `live.load_yfinance` so API budgets burn first).
  - `QuotaLedger("data/fresh/quota.json")`: same shape as the terminal's
    quota-ledger (daily per-provider counts). Massive self-throttles 13 s
    (5/min free tier); raw JSON cached 12 h under `data/fresh/raw/`.
  - Finnhub `/quote` is last-print only (free tier 403s `/stock/candle`) —
    staleness cross-check, not history. Massive free answers `status:
    DELAYED` (15-min delay, fine for EOD research, never intraday live).
  - Validate every pull with `data_loader.validate_ohlcv` before writing
    canonical `data/research/fresh/ohlcv_{SYM}.csv`.
  - Code: `src/quantkit/fresh.py` (tests: `tests/test_fresh.py`, fully
    mocked — no network, no keys); CLI: `research/pull_fresh.py`.
- **known pitfalls**: Massive free tier covers ~2 y of EOD — it extends the
  window, it does not replace the SHA-pinned history. Alpha Vantage budget
  is tiny (shared with the terminal: 1/25 already used some days) — treat
  it as fallback only and check the ledger first. Adjusted=true: splits/
  dividends already applied, so do NOT re-apply `adjust_prices`. Finnhub
  candle 403s on free tier — don't retry it in a loop. Timestamps are UTC
  ms; weekends/holidays simply absent (same convention as yfinance).
- **source**: trading-terminal-pro `api/deskFeeds.js`, `api/upstreamCache.js`,
  `api/history/spy.js` (bars→payload + rv convention), `server/routes/
  deskFeeds.js` (budget/stale semantics). No code copied — patterns
  reimplemented (JS→Python); terminal repo untouched.
- **spine**: data (feeds µ/Σ/attribution work). **mechanism**: none — plumbing.
- **implementation**: `src/quantkit/fresh.py` + `research/pull_fresh.py`.
