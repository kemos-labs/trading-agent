# Ch01 — Trading Basics

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 1.

## Purpose
Establishes the vocabulary and mechanics of financial trading — who
trades, how orders work, and the core concepts (leverage, hedging,
volatility) that the rest of the book's ML models are applied to.

## Who trades and why
- **Buyers and sellers** are the two sides of every trade; a trade only
  happens when they agree on a price. Buyers want low prices, sellers
  want high prices, and their tension creates the market price.
- **Types of market participants**: retail traders, institutional
  investors (funds, pensions), market makers (provide liquidity,
  profit on the spread), and speculators (bet on direction).
- **Long vs. short**: going long profits from a price rise; going short
  (borrowing an asset, selling it, and buying it back later) profits
  from a price fall. Shorting is riskier in principle because losses are
  unbounded if price keeps rising.

## Orders and order books
- **Market order**: execute immediately at the best available price.
  Guarantees execution but not price.
- **Limit order**: execute only at a specified price or better.
  Guarantees price but not execution.
- The **order book** lists all resting buy (bid) and sell (ask) limit
  orders; the **spread** is the gap between the best bid and best ask.
  Tighter spreads mean cheaper trading.

## Leverage and margin
- **Leverage** multiplies exposure with borrowed capital (e.g., 2×
  leverage on a position). It amplifies both gains and losses — a 10%
  adverse move wipes out 20% of capital at 2×.
- **Margin** is the collateral required to open a leveraged position;
  a **margin call** forces the trader to add funds or close positions
  when losses erode the collateral.

## Hedging and risk
- **Hedging** opens an offsetting position to reduce risk (e.g., buying
  puts against a stock holding). It costs money (premium) but caps
  downside.
- **Volatility** is the standard deviation of returns — the market's
  uncertainty meter. Low-volatility regimes reward trend-following;
  high-volatility regimes reward range trading and options strategies.

## Time frames
- Different strategies live on different time scales: scalping
  (seconds–minutes), intraday (minutes–hours), swing trading
  (days–weeks), and position trading (weeks–months). The choice of
  time frame determines data frequency, holding-period costs, and which
  ML features are relevant.

## Key takeaways
- Every strategy is ultimately a decision about **direction**, **size**,
  and **timing** — ML models in later chapters automate the direction
  and timing parts.
- Understand **costs** (spread, commissions, slippage) before
  measuring any strategy's edge: an edge smaller than round-trip costs
  is no edge at all.
- Never trade a strategy you can't explain in one sentence — this
  book's models are tools to confirm or refine hypotheses, not
  replacements for them.
