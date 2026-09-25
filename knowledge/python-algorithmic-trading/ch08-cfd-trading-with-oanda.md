# Ch8 — CFD Trading with Oanda

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## Choosing a trading platform

Selection criteria: instruments (stocks, ETFs, bonds, FX, commodities,
options, futures), strategies supported (long-only vs short selling),
costs (fixed + variable — can decide profitability), technology (desktop/
mobile tools + APIs), jurisdiction (regulation constrains products per
residence).

## Oanda profile

- **Instruments**: contracts for difference (CFDs) on FX pairs, gold,
  stock indices, bonds — a global-macro product range.
- **Strategies**: long and short; market/limit orders with profit targets
  and (trailing) stop losses.
- **Costs**: no fixed fees; a **bid-ask spread** is the variable cost.
- **Technology**: fxTrade apps + RESTful and **streaming APIs** (Oanda
  v20 API) with a Python wrapper package (v20 / tpqoa). Free paper-trading
  (practice) accounts give full API access — ideal for development and a
  clean path to live trading.
- **Jurisdiction**: FX CFDs broadly available; index/stock CFDs vary by
  residence.

## Contracts for difference (CFDs)

CFDs are leveraged derivatives (e.g. 10:1, 50:1) traded on margin — you
can lose more than your initial capital. Although based on an underlying
(index, pair), a CFD is a separate product issued and quoted by the broker,
so trading liquidity and counterparty risk are the broker's. The Swiss
Franc (SNB) event, which bankrupted several brokers, illustrates the
risks.

## API workflow (tpqoa wrapper)

- Configure credentials in a config file (account id, token); connect via
  the wrapper (`api = tpqoa.tpqoa('pyalgo.cfg')`).
- **Historical data**: `api.get_history(instrument, start, end, granularity,
  price)` → DataFrame of OHLC data for backtesting.
- **Streaming data**: `api.stream_data(instrument)` with an
  `on_success` callback receiving each new tick; used with the socket
  patterns of ch7 for live signal generation.
- **Trading**: `api.create_order(...)` (market/limit, units, sl/tp);
  orders return filled transactions with price, P&L, commission,
  half-spread cost.
- **Account info**: balance, open trades, recent transactions.

## Live strategy loop

Real-time strategy: stream ticks → update rolling window → generate signal
→ place order via API → monitor fills. The "practice" account makes the
whole loop testable without capital risk.

## Key takeaways

- Platform choice = instruments × strategies × costs × technology ×
  jurisdiction; costs can decide profitability.
- CFDs are leveraged margin products with broker-specific risk: spread is
  the cost; losses can exceed capital.
- Oanda's REST + streaming API (via the tpqoa wrapper) covers the full
  loop: history → stream → signal → order → account.
- Paper trading with the same API is the safest way to validate an
  automated strategy before going live.
