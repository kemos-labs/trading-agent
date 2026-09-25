# Ch01 — Trading Machines

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 1.

## Purpose
Introduces Haim Bodek, founder of Trading Machines LLC, and the central
mystery of the book: a sophisticated quant firm bleeding money for
reasons its own genius founder cannot explain. This is the *hook* for
the market-structure exposé to come.

## Trading Machines LLC
- Founded by Bodek in late 2007 in Stamford, Connecticut, after he
  lured ~25 traders, programmers, and quants from across Wall Street.
  It trades its own capital (no outside investors), using hundreds of
  thousands of lines of code — "the Machine."
- The algos are built on **expert systems**, a branch of AI that encodes
  the knowledge of market experts to crunch incoming data and make
  predictions; they combine options-pricing models with pit-trading
  strategies.
- Bodek's background: Hull Trading (Chicago, 1997) → Goldman Sachs
  (after its 1999 Hull acquisition) → a top-secret global desk at UBS.
  Trading Machines was his attempt to out-do them all.

## The breakdown
- In spring 2009 the Machine stops working: profits fall ~$15,000/day
  (sometimes more), throughout summer and into fall. Bodek hunts for a
  "bug" in the code — and finds nothing. It is death by a thousand cuts.
- The book's setup: the real culprit is not a bug but the market
  structure itself — abusive order types and maker-taker fees that bleed
  his limit-order strategies (revealed in ch4 and ch24).
- Trading context: Bodek trades options (extremely volatile), so he
  offsets positions with stock/ETF hedges. The Spyder (SPDR S&P 500
  ETF, first ETF, 1993) is one of his favorites — he reads it as a
  market thermometer.

## Key takeaways
- A purely technical explanation ("it's a bug") can be wrong when the
  environment — market microstructure — has changed under you.
- Options strategies are delta-hedged with stock, coupling the options
  book's fate to stock-market structure; microstructure changes in the
  stock market hit option traders asymmetrically (a theme throughout).
- The "machine vs. the market" frame: Bodek's war-song metal and
  "trading is war" ethos set the tone for the Algo Wars narrative.
