# Ch9 — FX Trading with FXCM

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## FXCM platform profile

FXCM (FXCM Group) offers a RESTful + streaming API with a Python wrapper
package (`fxcmpy`), well suited to automated strategies for retail traders
with smaller capital. Platform criteria:
- **Instruments**: currency pairs (the focus) plus CFDs on stock indices,
  commodities, and rate products.
- **Strategies**: leveraged long and short; market entry orders, stop-loss
  orders, take-profit targets.
- **Costs**: bid-ask spread **plus** a fixed fee per trade (unlike Oanda);
  several pricing models.
- **Technology**: RESTful API via `fxcmpy`; standard desktop/mobile apps.
- **Jurisdiction**: active in multiple countries; product availability
  varies by regulation.
- **Disclaimer**: forex/CFD margin trading is high-risk; losses can exceed
  deposits (leverage works against you).

## Getting started

- `pip install fxcmpy`; open a free **demo account** and create an API
  token.
- Connect: `api = fxcmpy.fxcmpy(access_token=YOUR_TOKEN, log_level='error')`
  or read credentials from a config file (same pattern as ch8's tpqoa).
- Configure `log_level`/`log_file` in the config for error handling.

## Retrieving data

- **Candles/bars**: `api.get_candles(instrument, period, number, columns)`
  → DataFrame of OHLC bars for a symbol (e.g. 'EUR/USD').
- **Tick data**: down to the tick level for streaming/replay — the book
  shows tick-by-tick retrieval as the finest granularity for FX.
- Historic data powers vectorized backtesting (ch4) and ML training
  (ch5); streaming powers live signals (ch7).

## Working with the API

- Open/close positions: `api.open_trade(...)`, `api.close_trade(...)` with
  instrument, units (direction), stop, and take-profit.
- Account information: `api.get_accounts_summary()` (balance, margin,
  equity); order and position queries for monitoring.
- **Streaming subscription**: `api.subscribe_market_data(instrument)`
  with an `on_bar`/`on_tick` callback — push updates for live trading,
  mirroring the Oanda streaming flow with a different wrapper.
- Fills return detailed trade data (price, P&L, financing, commission).

## Key takeaways

- FXCM = FX-focused broker with REST+streaming API wrapped by `fxcmpy`;
  costs = spread + fixed fee per trade.
- Demo account + API token → connect → get_candles/tick data → open/close
  trades → account summary: the full automation loop.
- Same architecture as Oanda (ch8) — REST history + streaming ticks +
  order placement — so the strategy code transfers across brokers.
- Leverage and fee structure make cost modeling (ch4/ch6) and position
  sizing (Kelly, ch10) essential before any live deployment.
