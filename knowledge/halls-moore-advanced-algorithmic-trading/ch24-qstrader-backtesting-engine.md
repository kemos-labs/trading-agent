# Ch24 — QSTrader: An Open-Source Backtesting Engine

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 24 (start of Part V — QSTrader).

## Motivation: why backtests underperform live
Biggest reasons a deployed strategy underperforms its backtest:
- **Overfit models** (fit too hard to historical data).
- **Latency** to liquidity provider (time from order issue → execution).
- **Regime change** — strategy behaved well in past conditions, but markets changed
  (regulation, structure, etc.).
- **Strategy decay** — the edge gets replicated by too many traders → alpha disappears.
- **Incomplete transaction-cost handling** (most common after overfitting): spread, slippage,
  fees, market impact all reduce live profitability.

Vectorised backtests are easy to code but severely lacking: transaction costs usually ignored,
"nitty gritty" implementation details skipped. → This motivated **QSTrader**.

## QSTrader overview
Free, **MIT-licensed open-source** portfolio & order-management system (OMS) by QuantStart
(https://github.com/mhallsmoore/qstrader). Modules for: data ingestion, **event-driven
backtesting**, portfolio construction, position tracking, position sizing, risk management,
execution, statistics/tearsheets. Developed/tested on Python 2.7/3.4/3.5; influenced by
QSForex (OANDA-only via REST); eventual goal: equities, ETFs, forex under one framework
(via Interactive Brokers Python API).
Design goal: **realistic simulation mirroring live deployment** — e.g. realistic brokerage fees
are turned ON by default (unusual choice). Ambition: institutional-grade, production-ready OMS
with risk management at position/portfolio/broker levels, end-to-end automation (minimal human
intervention).

## Architecture — event-driven, modular, loosely coupled
Communicates via an events queue using subclassed `Event` objects.

**Core components** (mirror a small quant fund's bespoke stack):
- **Event** — all "messages" encapsulated (TickEvent, BarEvent, SignalEvent, SentimentEvent…).
- **Position** — data for an open position in an asset; tracks realised/unrealised PnL by
  averaging multiple entries (across lots).
- **Portfolio** — list of Positions + cash balance, equity, PnL; used by PositionSizer and
  RiskManager.
- **PortfolioHandler** — manages Portfolio (per the book text; holds portfolio state).
- **PriceHandler** (+ subclasses) — ingests pricing data from various sources (class
  hierarchies per data type).
- **Strategy** (+ subclasses) — contains the **alpha-generation** code.
- **PositionSizer** — guidance on sizing positions once a signal arrives (e.g. Kelly Criterion,
  monthly fixed-fraction rebalancing).
- **RiskManager** — can veto/suggest trades passing through from PositionSizer, based on
  portfolio composition and external risk (e.g. correlation).
- **ExecutionHandler** — sends orders to brokerages, receives "fills"; in backtest this is
  **simulated with realistic fees**.
- **Statistics** — performance reports from backtests; recent **tearsheet** capability with
  detailed equity-curve stats.
- **Backtest** — encapsulates the event-driven behaviour incl. the events queue; needs all
  other components to run a full simulation.

Extremely modular + flexible → customisation per trading style/frequency.

## Takeaways / pitfalls
- Always model **fees/slippage/spread/impact** in backtests (QSTrader defaults fees ON).
- Beware overfitting, latency, regime change, strategy decay as live-vs-backtest gaps.
- Event-driven backtesting (vs vectorised) gives realistic order/fill handling.
- A position-tracking/OMS layer with risk vetoes is what separates research code from
  deployable systems.
- QSTrader was under active development at book time — check the repo for current install.