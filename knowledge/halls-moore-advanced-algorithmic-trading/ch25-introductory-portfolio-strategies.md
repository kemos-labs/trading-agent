# Ch25 — Introductory Portfolio Strategies (ETF monthly rebalance)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 25 (QSTrader applied).

## Motivation
Many institutional asset managers are **long-only, zero/low-leverage constrained** → portfolios
highly correlated with "the market" (S&P500). Correlation can be reduced (not eliminated
without shorting) by adding **non-equity ETFs** (bonds, commodities, real estate). These
portfolios rebalance **infrequently — weekly or monthly**; fully systematic but very different
from intraday stat-arb.

## Three fixed-proportion monthly-rebalance strategies
Mechanic: at the **end of every month** the strategy fully liquidates then rebalances each asset
to a fixed dollar-weight × current equity.

1. **60/40 US equities/bonds**: SPY (large-cap US) 60%, AGG (investment-grade US bonds) 40%.
   Start 2003-09-29.
2. **"Strategic" weight (8 ETFs)** — inspired by The Capital Spectator blog (orig. 10 assets):
   SPY 25%, IJS 5% (US small-cap), EFA 20% + EEM 5% (developed/emerging intl equities),
   AGG 20% + JNK 5% (investment-grade & high-yield US bonds), DJP 10% (commodities),
   RWR 10% (REITs). Start 2007-12-04. (VWOB/BNDX dropped — only began trading late 2013 →
   too short for representative monthly-rebalance backtests.)
3. **Equal weight**: same 8 ETFs at 12.5% each. Start 2007-12-04.

Benchmark for all: **buy-and-hold SPY** (no rebalancing). Costs: **net of simulated
transaction costs** using Interactive Brokers US fixed pricing (shares, North America; doesn't
include ETF-specific commission differences — reasonably representative).

## QSTrader components used
- `MonthlyLiquidateRebalanceStrategy` (subclass of Strategy):
  - `_end_of_month(cur_time)` — uses `calendar.monthrange` to detect the last day of month.
  - `_create_invested_list()` — per-ticker boolean dict to avoid liquidating on the *first*
    allocation (housekeeping).
  - `calculate_signals(event)`: on BAR/TICK at month end → for each ticker: send **EXIT**
    (liquidate) SignalEvent if already invested, then send **long ("BOT")** SignalEvent; mark
    ticker invested.
- `LiquidateRebalancePositionSizer` (subclass of PositionSizer): init takes
  `ticker_weights` dict (weights in [0,1]; set up for weights summing to 1.0 — >1 ⇒ leverage).
  `size_order` logic:
  - EXIT (liquidate) → opposite "SLD" order for the current position quantity (nets to zero).
  - BOT (long) → price = `portfolio.price_handler.tickers[ticker]["adj_close"]`;
    shares = floor(equity × weight / price), integer quantity.
  - **`PriceParser.PRICE_MULTIPLIER`**: market price & equity must be divided by it (internal
    int-price representation).
- `monthly_rebalance_run.py`: `run_monthly_rebalance(...)` boilerplate — builds
  `YahooDailyCsvBarPriceHandler` (data), strategy, `LiquidateRebalancePositionSizer`,
  `ExampleRiskManager`, `PortfolioHandler`, `IBSimulatedExecutionHandler` (simulated IB fills),
  `TearsheetStatistics`; each backtest = a thin client file calling it with weights/dates/title.

## Results (all net of costs, benchmark buy-and-hold SPY)
1. **60/40 SPY/AGG**: Sharpe identical to benchmark (0.4); CAGR 4.43% vs SPY 5.92% (costs of
   rebalancing + AGG drag). AGG cushioned 2008 drawdown but recent 5-yr AGG underperformance
   drags results; underwater 1242 days vs benchmark 1365.
2. **Strategic weight**: far worse — **negative CAGR**; transaction costs of trading 8 securities
   monthly + most non-equity ETFs underperformed SPY (commodities & fixed income weak last 5
   yrs vs US equities).
3. **Equal weight**: worst — remains underwater from 2008; **CAGR ≈ −5%**; max daily drawdown
   ≈ **73%** (mostly attributable to the 2008 crisis; starting a year later would look very
   different).

## Takeaways / pitfalls
- Long-only ETF portfolios stay highly market-correlated; non-equity sleeves help only if those
  assets perform.
- Monthly full liquidation + rebalance incurs real transaction costs every period — they eat
  returns (visible in CAGR vs benchmark).
- Results are strongly **period-dependent** (2008 dominates drawdown stats).
- Data availability constraints dictate backtest start dates (VWOB/BNDX too new).
- QSTrader's modular pipeline (Strategy → PositionSizer → RiskManager → PortfolioHandler →
  ExecutionHandler → Statistics) makes portfolio logic easy to swap/test.