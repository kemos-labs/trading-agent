# Chapter 33 — Brokerages

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Account & platform selection

- "Pattern trader" (SEC term for frequent/day trader) needs a $25,000
  minimum margin account — in practice ~$50,000 for slack. PDT rules
  (4:1 intraday leverage; flat by 4:00pm close). Never use money that
  would change your lifestyle if lost.
- Platforms vary widely in functionality; try demos before choosing;
  this is one of the more important decisions. Toolkits vary (e.g.,
  TDAmeritrade provides wide tool sets).
- **Direct-access platforms**: Townsend Analytics' **RealTick** OMS/
  execution (the authors' preference; Stuart & Margwen Townsend
  pioneered direct-access trading in the early 1990s). Available via
  TradePro brokerage and direct-access brokers (eoption, Investscape,
  Hampton, Lightspeed, MasterTrader, Terra Nova, Tradewithvision).
- Other major brokerages: Interactive Brokers, TradeStation, Goldman
  Sachs RediPlus, TDAmeritrade.
- Commission costs vary; offers can be confusing — hunt around for the
  best deal *as long as the required functionality is provided*. Test
  accounts are usually available.

## Key takeaways

1. Direct-access brokerages with RealTick-class OMS + Excel feed-handler
   support are the working baseline; commission structure gates the
   bp-sec economics.
2. The $25K PDT minimum is a floor, not a working balance — ~$50K is
   realistic.
