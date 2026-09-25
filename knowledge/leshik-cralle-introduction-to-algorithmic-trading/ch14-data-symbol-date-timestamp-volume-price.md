# Chapter 14 — Data: Symbol, Date, Timestamp, Volume, Price

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Input data (severely restricted)

Only five fields: **SYMBOL, DATE, TIME OF TRADE, VOLUME, PRICE** —
often only price and symbol are used. Tick-level real-time data comes
bundled from the broker or a specialist tick-resolution vendor; one
stock per Excel template, each template in its own Excel instance.

## Excel layout

- Col A Row 1: ticker symbol. Col A Row 3: date (mmddyyyy). Col B:
  timestamp (hhmmss; millisecond resolution exists but unnecessary for
  this methodology). Col C: volume in shares (integer, as in the Time &
  Sales column of Level II). Col D: trade price $ with two decimals.
- Vendor request strings are cleaned by copying cols B–D to E–H (the
  initial array-written columns can't be edited in Excel).
- Worked example adds SMA(200T) and LMA(600T) columns plus a DIFF
  column = LMA − SMA — the DIFF TRIGGER precursor of ALPHA-1.

## Key takeaways

1. Minimal tick schema (symbol/date/time/volume/price) is sufficient
   for the ALPHA ALGO family; price (and symbol) dominate.
2. Real-time tick feed → one-stock-per-template Excel instances; the
   SMA/LMA/DIFF columns foreshadow the trigger architecture.
