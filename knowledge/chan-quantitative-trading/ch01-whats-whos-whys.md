# Ch01 — The Whats, Whos, and Whys of Quantitative Trading

**Source:** Ernest P. Chan, *Quantitative Trading* (2nd ed., 2021), Chapter 1.

## What quantitative trading is
Quantitative/algorithmic trading = trading securities strictly on the buy/sell decisions of
computer algorithms, designed (and often programmed) by the trader, based on historical
performance of the encoded strategy against historical data.

- Broader than technical analysis: TA strategies qualify only if fully encodable (e.g. a
  subjective "head-and-shoulders pattern" lookup is *not* quantifiable); fundamental data
  (revenue, cash flow, debt/equity) and even parsed news can be inputs — anything that can be
  converted to bits/bytes.
- The book's focus: **statistical arbitrage** on the simplest instruments — stocks, futures,
  currencies. No advanced degree required; high-school math/stat/programming suffices.

## Who becomes a quant trader
Author's path: PhD physicist; research at IBM; then banks/hedge funds (Morgan Stanley, Credit
Suisse) where complex strategies produced losses; became profitable only after simplifying
("Make everything as simple as possible. But not simpler." — Einstein). Typical independents:
ex-hedge-fund traders, programmers, ex-bankers, scientists. Key attributes: prior finance/
programming exposure, savings to absorb losses (strategies have intrinsic return rates that
can't be hurried), emotional balance between fear and greed.

## The business case
- **Scalability**: scaling often means just changing the **leverage** number — brokerages
  supply capital (SEC Reg T margin; prop firms up to ~×40 intraday; futures/forex ~×10+;
  e.g. ~$12k margin for a ~$167.5k notional E-mini S&P500 contract). Not a get-rich-quick
  scheme; overleverage is dangerous (ch6).
- **Low time demand**: highly automated; manual interference usually hurts performance. Even a
  semi-automated setup needed ~2.5 hours/day (morning data processing + order launch, evening
  position exits); fully automated now = zero daily action, but monitor for software/connectivity
  breakdowns (e.g. the Covid-19 selloff in Feb 2020).
- **No marketing**: counterparties trade on price only. If managing others' money, a good
  (consistently profitable) product markets itself.

## The way forward (roadmap for the book)
1. Find candidate strategies (ch2) — recognise good vs bad *before* backtesting.
2. Backtest rigorously (ch3).
3. Implement: business structure + infrastructure (ch4), execution systems (ch5).
4. Scale capital while managing losses — money & risk management (ch6).
5. Special topics (ch7) and conclusions (ch8).

Author's timeline: 3 months from idea → backtest → brokerage ($100k) → execution system →
first profitable month (vs a dot-com needing 3× investment, 5× people, 24× time to fail).

## Key takeaways
- Simple, encodable, statistical-arbitrage strategies beat overcomplex institutional ones for
  the independent trader.
- Independence + automation + leverage (used carefully) is a viable small-business model.
- Strategy R&D is the ongoing creative work; operational trading should become fully automated.
