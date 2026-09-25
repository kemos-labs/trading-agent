# Chapter 14 — The FXCM Trading Platform

## Core idea
Connecting to a live broker programmatically: FXCM's RESTful/streaming API
wrapped by the `fxcmpy` Python package — the bridge between strategy research
(ch15) and automated trading (ch16).

## Getting started
```python
import fxcmpy
api = fxcmpy.fxcmpy(access_token='YOUR_FXCM_API_TOKEN', log_level='error')
# or via config file:
api = fxcmpy.fxcmpy(config_file='fxcm.cfg')
```
- Free demo account with an API token is enough to develop.
- `fxcm.cfg` holds `access_token`, `log_level`, `log_file` — credentials out
  of code.
- Defaults to the demo server; a `server` parameter switches to live.

## Capabilities
- **Retrieving data**: historical price data (down to tick level) and
  account data.
- **Streaming data**: subscribe to real-time price streams.
- **Orders**: place market and limit orders programmatically.
- **Account**: query balances, open positions, margin.
- Products: FX pairs and CFDs on indices/commodities — tradeable with small
  capital, which is why FXCM suits individual algo traders.

## Typical workflow
1. Connect with token/config.
2. Pull historical data to backtest a strategy.
3. Deploy an online algorithm (ch16) that consumes the streaming feed,
   generates signals, and places orders through the API.

## Pitfalls
- **Leverage risk**: FX/CFDs on margin can lose more than deposited funds —
  the book prints a full risk disclaimer; size positions accordingly.
- API token security: keep in config file, not committed to repos.
- Demo vs live: behavior and fills differ; validate on demo first.
- API docs can change (fxcmpy is a community wrapper — pin versions).

## Patterns worth reusing for any broker API
- **Config-file connection**: credentials in `fxcm.cfg`, loaded by the
  wrapper — keeps secrets out of code and version control.
- **Separation of concerns**: data retrieval methods vs order methods vs
  account methods — the same shape as Oanda's `tpqoa` and FXCM's `fxcmpy`
  in Hilpisch's other books.
- **Demo-first workflow**: build and validate on a demo token before any
  live capital; treat the API wrapper as the thin layer between your
  strategy and the market.
- **Streaming + batch duality**: pull historical data for backtests, then
  subscribe to streaming data for live signals — one API, two modes.

## Bottom line
The broker-connectivity chapter: with ~30 lines you can pull ticks and place
orders. It completes the research→backtest→live loop that ch16 automates.
Cross-ref: `knowledge/python-algorithmic-trading/ch09` (FXCM via fxcmpy)
— same wrapper, more detail.
