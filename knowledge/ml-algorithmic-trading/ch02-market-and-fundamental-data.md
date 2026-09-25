# Ch02 — Market and Fundamental Data

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 2.

## Purpose
Covers sourcing, cleaning, and working with the traditional data backbone: market prices, fundamentals, and macro series — including the pitfalls of survivorship bias, point-in-time availability, and corporate actions.

## Market data sources and access
- **End-of-day / intraday prices**: yfinance (Yahoo), Alpha Vantage, Tiingo, EOD, Quandl/Nasdaq Data Link; free tier APIs for ML research.
- **Intraday and tick**: IEX Cloud, Polygon; exchange feeds for production.
- **Futures/options**: yfinance chains, CBOE; contracts need roll logic.
- **Point-in-time caveat**: vendor data may be *restated* — always use data as it existed at the timestamp to avoid lookahead bias.

## Adjustments and cleaning
- **Corporate actions**: splits and dividends distort raw price series; use *adjusted* prices for return computation, raw prices for signals that genuinely depend on the unadjusted quote.
- **Survivorship bias**: datasets built from *current* index membership omit delisted firms, inflating backtest performance — use full-universe data with delistings.
- **Missing data**: forward-fill trading days, but distinguish "no trade" from "missing"; handle timezone/calendar alignment across exchanges (e.g., US/EU overlap).

## Fundamental data
- **Financial statements** (10-K/10-Q via SEC EDGAR, XBRL format): revenue, earnings, balance-sheet items; use point-in-time restatements.
- **Ratios**: P/E, P/B, ROE, margins, leverage; standardize for cross-sectional comparison.
- **Analyst estimates**: consensus EPS/ratings (e.g., from vendor feeds) — a classic input for surprise factors.
- **Macro data**: FRED (GDP, inflation, unemployment, industrial production), World Bank, IMF; align monthly/quarterly series to daily price grids (ffill with publication lag).

## Practical pipeline patterns
- Store data with timestamps and source metadata for auditability and reproducibility.
- Resample to a common frequency before merging: align on trading calendars, apply the *most recent published* value (avoid peeking at restatements).
- Compute returns as `pct_change()` on adjusted prices; log returns for time-series modeling.
- Cache raw downloads to files/DBs; never re-download in research loops (rate limits, reproducibility).

## Key takeaways
- Data quality is the single biggest determinant of a strategy's validity — cleaning and correct alignment beat model sophistication.
- The two silent killers are survivorship bias and point-in-time/restatement leakage.
- Cheap/robust free sources suffice for research; production-grade feeds are about latency, coverage, and cleanliness, not just price.
