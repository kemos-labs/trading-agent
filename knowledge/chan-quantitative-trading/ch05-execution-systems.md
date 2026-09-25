# Ch05 — Execution Systems

**Source:** Ernest P. Chan, *Quantitative Trading* (2nd ed., 2021), Chapter 5.

## What an ATS does
An **automated trading system (ATS)** retrieves market data (brokerage/data vendor), runs the
trading algorithm, generates orders, and submits them for execution. Fully automated →
minimizes human errors/delays (indispensable for HFT); formerly required pro C++/Java/C#
programmers, now achievable by amateurs via QuantConnect, Blueshift, MATLAB Trading Toolbox,
Python Backtrader, R's IBroker. Non-price inputs (earnings estimates, dividends, expected
earnings dates) often come free/cheap from brokers (IB: Zacks free; Wall Street Horizon fee).

## Semiautomated systems
- Generate an **orders file** (symbol, side, size + extras like Day-only/GTC) in Excel/MATLAB/
  Python/R — often the same program as the backtest, updated with latest data via broker/vendor
  API.
- Submit via brokerage's **basket trader** (upload many orders, one keystroke) or **spread
  trader** (monitor pairs, enter orders when conditions met — limits are on the *spread*, not
  individual stocks) or **DDE links** (e.g. `=accountid|LAST!IBM` fills an Excel cell; macro
  submits orders).
- Author's workflow: pre-market MATLAB run → ~1,000-line order file → BasketTrader upload →
  cancel unexecuted at close; REDIPlus spread trader for pairs; DDE for basket strategies.
- Suitable when a few order waves/day suffice; API-driven macro submission too slow otherwise.
- **Benefit over full automation: human sanity-check of orders before they reach the broker**
  (Knight Capital's $440M software-error loss, Aug 2012).

## Fully automated systems
- Loop: scan prices → generate orders → submit via API throughout the day; press start/close.
- Requires brokerage **API** (VB/Java/C#/C++), a quant platform, or **RESTful API** (Alpaca,
  IB, even Robinhood — any HTTP-capable language; slower than language-specific APIs, so not
  for latency-sensitive strategies).
- Excel+DDE full automation infeasible (slow updates, ~100-symbol limit).
- All-in-one platforms (TradeStation): trivial backtest→live but inflexible for complex math
  (e.g. PCA factor models).

## Hiring a programming consultant
$50–100/hr or $1k–5k fixed for most independent-trader projects. Broker API pages and
elitetrader.com are good sources; Upwork programmers may lack market/trading-tech depth.
Confidentiality: NDAs are unenforceable in practice; but most strategies are well-known anyway,
capacity limits impact, and **compartmentalize** (one programmer builds the infra, another the
strategy code, neither knows parameters).

## Minimizing transaction costs
- **Avoid low-priced (<$5) stocks**: more shares per dollar → higher commissions; wider % bid-
  ask spread → higher liquidity cost.
- **Cap order size at ~1% of average daily volume** (market-impact rule of thumb). Small-caps
  are illiquid: Bel Fuse (S&P600, ~30k ADV) → 300 shares ≈ $3k order cap.
- **Scale position size by market cap nonlinearly**: linear scaling gives near-zero weights to
  small caps (kills diversification; weight ratio large-cap:small-cap ≈ 10,000:1 — keep ≤10).
  **Fourth-root of market cap** scaling works, subject to the volume cap.
- Splitting large orders over time reduces impact but increases **slippage** — not for retail
  order sizes. Slippage also arises from slow brokerage software/risk checks/pipeline/dark-pool
  access → affects brokerage choice (ch4).

## Paper trading
Practically the only way to find ATS bugs without real losses; reveals **look-ahead bias**
immediately ("back to the drawing board"); compare paper P&L vs backtest-generated P&L (net of
expected costs) — differences ⇒ bugs. Gives intuition (P&L volatility, capital use, trade
frequency) and exposes operational realities (e.g. author: 20 min to download/parse data +
15 min to transmit orders pre-open — strategies needing >35-min-old pre-open data need a
different setup). A month+ of paper trading can reveal data-snooping bias (true OOS), but
neglect degrades the paper system's signal.

## Why live performance diverges from backtest
Diagnose in order: (1) ATS bugs; (2) trades don't match backtest output; (3) execution costs
higher than expected; (4) illiquid stocks → market impact. Then the two dreaded causes:
- **Data-snooping bias**: simplify (remove rules/parameters); if backtest collapses, bias
  confirmed — find a new strategy; if still fine, poor live results may be bad luck.
- **Regime shifts**:
  - **Decimalization (Apr 2001)**: stat-arb profits came from market-making frictions;
    decimalization removed them → pre-2001 stat-arb backtests are unrealistically good.
  - **Short-sale rules**: pre-2007 plus-tick rule (short only on uptick) + hard-to-borrow
    stocks mean short strategies' pre-2007 (and post-2009 under Rule 201's constraints)
    backtests are inflated; **June 2007–Feb 2010** may be the only realistic backtest window
    without modelling the rule. Hard-to-borrow stocks simply can't be shorted.
- Detection of regime shifts automatically is a ch7 topic.

## Summary
ATS benefits: faithful adherence to strategy, multi-strategy operation, fast order transmission
(essential for HFT). Minimize costs: cap size vs volume & market cap (∝ 4th-root), avoid
sub-$5 stocks. Paper trade to find bugs, biases, operational issues, and realistic costs.
Underperformance diagnosis ladder: bugs → costs → data-snooping (simplify test) → regime shift.
