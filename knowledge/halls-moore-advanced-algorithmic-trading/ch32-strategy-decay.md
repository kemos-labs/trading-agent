# Ch32 — Strategy Decay & Annualised Rolling Sharpe (QSTrader)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 32 (final chapter).

## Why strategies decay
Quant strategies rely on forecasting/statistical mispricing. As more traders (retail and
institutional) run similar systematic strategies, mispricings → **price efficiency**: the edge is
eroded until it falls to the level of its own transaction costs → unprofitable. Quant trading is
**not "set and forget"**: run a *portfolio* of strategies and **rotate them out** as alpha erodes;
constant research develops new edges to replace arbitraged-away ones.

Key challenge: daily-data strategies have long stretches of mediocre returns and deep
drawdowns (fewer positive-expectancy "bets") → hard to tell **edge erosion** (retire) from a
**temporary poor patch** (hold). Need a trailing performance metric.

## Annualised Rolling Sharpe Ratio
Sharpe = mean excess return / SD of excess returns — a "broad brush" reward-to-risk measure.
**Annualised rolling Sharpe** computes this on the trailing year (k = 252 daily periods):

**S_k = √252 · E(r_{s,t−k}) / √Var(r_{s,t−k})**

- Read "continuously-updated but rearward-looking" view of reward-to-risk.
- Low (< 1.0): much volatility for little mean return. **Negative**: worse than holding the
  risk-free instrument (treasury bills) — and you've endured volatility for the privilege.
- Retirement heuristic: track it; if it trends toward 0 or negative → consider retirement.
- **Caveats**: rearward-looking; captures only return-variance risk (no info on e.g. regulatory
  surprises); **penalises upward volatility too** — large unexpected upward moves reflect
  unanticipated behaviour (e.g. a new favourable regime) and are just as dangerous to assume
  persistent as downward ones.
- **Do not compute until a full year of periods accumulated** — early ratios are inflated
  (high returns, low variance).

## QSTrader implementation (TearsheetStatistics)
- New optional chart under the equity curve: `TearsheetStatistics(..., rolling_sharpe=True)`.
  (Requires pandas ≥ 0.18.0.)
- `get_results`: compute rolling means/SDs over k periods with `rolling(k)` on strategy and
  benchmark returns; annualise via `√periods`; **no risk-free rate included — zero returns are
  the risk-free alternative**.
- `_plot_rolling_sharpe`: same colour scheme as equity curve; dashed vertical line at k
  periods in (first point the ratio exists); `plot_results` adjusts grid to 5 or 6 vertical
  sections when the flag is on.

## Applied to book strategies
1. **Kalman Pairs Trade (TLT/IEI)**: rolling Sharpe starts mid-2010 (>252 periods); rises
   past 2.0 through mid-2011; high vol + flat/dwindling 2012 → **negative territory**; recovers
   toward 2.0 after mid-2013; unclear if decaying again end-2016. Lesson: at end-2012 a live
   manager could not have easily known whether to retire it — knowing the returns
   distribution's statistical behaviour is essential.
2. **Aluminum smelting (ARNC/UNG)**: short window (<2 yrs) → little rolling history; Sharpe
   ~2.25 early (early-2015 gains) then **falls to −0.5 by early-2016** and stays — clear
   retirement signal: alpha arbitraged away or structural relationship changed (e.g. Alcoa
   began hedging gas itself → gas price less relevant to profitability).
3. **Sentdex defence sentiment**: big 2013 gains → rolling Sharpe >2.5 (3.5 by start-2014);
   flat 2014 erodes it to ~0.5–1.0 by start-2015 (similar vol, less return); ~1.5 end-2015.
   From mid-2014 strategy & benchmark Sharpe broadly similar → **little reward-to-risk reason
   to hold the strategy vs buy-and-hold SPY**.

## Takeaways / pitfalls
- Track **annualised rolling Sharpe** (k = 252 for daily) as a decay/retirement monitor; trend
  to ≤0 ⇒ retire.
- Rolling Sharpe is rearward-looking, ignores non-variance risks, penalises upside vol, and is
  meaningless before one year of data — use as one input, not gospel.
- Distinguishing decay from a bad patch is genuinely hard — pair the metric with a deep
  understanding of the strategy's return distribution and its economic rationale.
- Strategy rotation (a live portfolio of strategies) is the institutional answer to decay.