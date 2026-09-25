# Ch02 — Fishing for Ideas

**Source:** Ernest P. Chan, *Quantitative Trading* (2nd ed., 2021), Chapter 2.

## Where ideas come from
Ideas are abundant: academic papers (SSRN, NBER, Quantpedia), financial blogs/podcasts
(Flirting with Models, Chat with Traders, Party at the Moontower, epchan.blogspot.com),
trader forums (Elite Trader, Wealth-Lab), Twitter (Benn Eifert, Corey Hoffstein, Euan
Sinclair). The difficulty is not finding ideas but developing *taste* for which strategies fit
you. Caveats: academic strategies are often too complex/stale/require expensive data; forum
strategies often don't survive backtesting — but a base strategy can be **modified** (holding
period, entry/exit timing) into a profitable one. Publishing a blog gives back (readers share
ideas; crowdsource backtest checks). Proprietary value = your *variations/tricks*, not the
plain-vanilla idea.

## Strategy fit — personal constraints
- **Working hours**: part-time → only overnight-holding strategies, or fully automate (ch5).
- **Programming skills**: C++/C#/Java → HFT & large universes possible; otherwise daily or
  few-instrument strategies (Excel + broker macros).
- **Capital**: <$50k not recommended. $100k = high/low dividing line. High leverage comes from
  futures/currencies/options (Reg T: ×4 intraday, ×2 overnight). Dollar-neutral/market-neutral
  (beta≈0) needs ~2× the capital of directional. Portfolio margin (IB): a $100k NAV dollar-
  neutral large-cap book can hold $250k long + $250k short. Small futures contracts (micro
  E-mini MES = 1/10 of ES's $12k margin / $167.5k notional) let small accounts in — but a 10%
  daily move wipes minimum-margin accounts.
- **Goal**: steady monthly income → shorter holding periods (and staggered subportfolios);
  long-term growth → maximum *Sharpe*, not buy-and-hold (mathematically, with leverage
  available, max growth = max-Sharpe strategy; see ch6).

## Plausibility screens (before full backtesting)
1. **Benchmark & consistency**: long-only ⇒ compare vs market index (small-cap index for
   small-caps, gold spot for gold futures); dollar-neutral ⇒ compare vs risk-free. Use
   **Information ratio** = mean excess return / SD of excess returns; **Sharpe ratio** = special
   case with risk-free benchmark (used universally for cross-strategy comparison).
   Rule of thumb: Sharpe < 1 unsuitable standalone; >2 ≈ profitable almost every month; >3 ≈
   almost every day. Deep (>10%) or long (>4 months) drawdowns ⇒ likely low Sharpe.
2. **Drawdowns**: drawdown(t) = current equity − high watermark (global max up to t);
   **max drawdown** = high watermark → subsequent global min (time-ordered); **max drawdown
   duration** = longest recovery time. Measured in % of high-watermark equity. Max DD and max
   DD-duration rarely overlap. Match to your tolerance (e.g. 20%/3 months).
3. **Transaction costs**: commission + **bid-ask spread** (limit orders avoid spread cost but
   incur opportunity cost of non-execution) + **market impact** (own order moves price) +
   **slippage** (execution delay; on average a cost — if it's a gain, delay orders!). Rule:
   ≈ half the average spread + commission; S&P500 stocks ≈ 5 bps one-way (10 bps round trip),
   E-mini ES ≈ 1 bp. Example: 5-min Bollinger mean-reversion on ES: Sharpe 3 without costs →
   **−3 with 1 bp** — costs decide viability.
4. **Survivorship bias**: databases excluding delisted/bankrupt stocks inflate backtests
   (esp. value strategies & long periods; cheap stocks were often going bankrupt). Ask for
   point-in-time data (e.g. Sharadar). Intraday strategies less affected; you can cut corners
   if aware.
5. **Performance decay over time**: most strategies did better 10 years ago (less competition,
   wider spreads, more survivorship bias far back). **Judge recent years, not overall**.
   Markets are **nonstationary** (regime shifts: decimalization, short-sale rule changes,
   subprime) — more data ≠ more robust when the process isn't stationary.
6. **Data-snooping bias**: many parameters → fit to historical accidents → poor future
   performance. More rules/parameters = more snooping; simple models stand the test of time.
7. **Fly under institutional radar**: seek low-capacity niches (trade too often, few stocks,
   infrequent positions like seasonal commodity trades) not yet arbitraged away by big funds.

## Sidebar: AI and stock picking (author's view, 2nd ed.)
AI = fitting past data with many parameters; works in marketing/fraud (huge independent sample,
consistent patterns) but **overfits financial noise** (tick data is serially correlated, far
from independent). What works for him:
- **Nonreflexive targets** (won't change because predicted): earnings surprises, nonfarm
  payroll surprises — not returns.
- Meaningful, numerous, carefully scrubbed **point-in-time features** (restated fundamentals
  embed look-ahead bias).
- **Metalabeling**: predict whether *your own* (private) trading signals will be profitable —
  no competition predicting public returns. (This is the book's 2nd-edition AI thesis.)

## Summary checklist (quick filters)
Time available · programming skill · capital · goal → then: beats benchmark? Sharpe high
enough? drawdown tolerable? survivorship-bias-free? recent performance holds? protected niche?

## Key takeaways
- Information/Sharpe ratio, drawdown (max & duration) are the primary quick-screen metrics.
- Costs (spread+impact+slippage) routinely flip a strategy from Sharpe +3 to −3.
- Beware survivorship bias, data snooping, regime nonstationarity, and strategy decay.
- Prefer low-capacity niches; use AI for metalabeling private signals, not public-return
  prediction.
