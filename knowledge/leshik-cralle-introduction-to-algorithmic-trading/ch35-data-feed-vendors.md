# Chapter 35 — Data Feed Vendors, Real-Time, Historical

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Real-time feed

Most brokerage platforms include a feed accessible from Excel — query
the technical support team on **feed handlers** to pipe real-time ticks
into the spreadsheets.

## Historical tick data

- Brokerages usually give only ~5 sessions of history — not enough for
  the stock-personality clustering work.
- NASDAQ/NYSE tick data from many vendors (list at nasdaqtrader.com).
- Suggested lookback: **60 trading sessions (3 months)** is more than
  adequate for fast tick-oriented trades; longer lookbacks aren't
  particularly useful at this timescale (though very-long-term patterns
  may reward a different, much heavier research program with orders of
  magnitude more data and many more variables).
- Delivery on an **external hard disk** (don't agree to a block
  Internet download — too much data, too error-prone). Archive on a
  ~750GB external drive; copy day's data in by hand (discipline-heavy;
  automation is the obvious improvement). Allow plenty of time to get
  feed-handler integration working.

## Key takeaways

1. 60 sessions of clean tick data is the working dataset for the
   method; longer horizons need a fundamentally different research
   program.
2. Data delivery logistics (disk, not internet block download) and
   feed-handler support are vendor-selection criteria.
