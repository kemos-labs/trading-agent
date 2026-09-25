# Ch09 — Directional Trading Around Events

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 9.

## Purpose
Event arbitrage: trading the price adjustment ("tâtonnement") that
follows scheduled news announcements, using surprise-based forecasts.

## The event-arbitrage method
- Key requirement: **events must be repetitive** (scheduled macro
  releases, earnings, Fed decisions) so historical impact can be
  estimated. U.S. unemployment/CPI release at 8:30 am ET; FOMC
  decisions at irregular times.
- **Surprise** = realized value − expectation. Expectations come from
  (a) autoregressive forecasts of prior values or (b) analyst
  consensus surveys (Barron's, WSJ, Bloomberg). The surprise is the
  tradeable component — if earnings meet expectations, no move.
- Three-stage development: (1) collect historical event dates/times;
  (2) compute surrounding returns at the trading frequency (e.g.,
  1-second moves at 8:30:00–8:30:01); (3) estimate impact via
  regression:
  `R_t = α + β·ΔX_t + ε_t` where ΔX is the surprise.
- Equity adjustments use the **market model** (Sharpe 1964):
  abnormal return `Ra_t = R_t − (α + β·R_mt)`, i.e., control for the
  broad market.

## What the research shows
- **FX**: macro news moves exchange rates significantly but briefly —
  employment and trade balance effects fade within ~2 hours; non-farm
  payroll and consumer confidence momentum can last 12+ hours
  (Almeida–Goodhart–Payne). Most currency pairs rise significantly on
  surprise increases in nonfarm payrolls, industrial production,
  durables, trade balance, consumer confidence, and the NAPM index;
  they fall on surprise rises in initial claims and M3 (ABDV 2003).
- **Equities**: prices respond strongly to rate announcements (99%
  significance for short rates); positive inflation surprises lower
  stocks. Response is **state-dependent**: higher-than-expected
  industrial production is good news in recessions, bad in booms; the
  same for unemployment (the "overheating hypothesis" — Boyd, Hu &
  Jagannathan 2005: bad news is often good for stocks in expansions).
- Volatility reliably spikes around announcements even when direction
  is ambiguous; returns are higher on major-announcement days
  (Savor–Wilson).

## Machine-readable news
- Reuters, Dow Jones, RavenPack, Semlab, etc. sell machine-readable
  news feeds — enabling fully automated capture, categorization, and
  matching of events to instruments.

## Key takeaways
- The edge in event arbitrage is **estimating the surprise**, not
  reacting to the headline — expectation is priced in before release.
- Reaction sign and size depend on the *state of the economy*, not
  just the news value — always condition on regime.
- Speed of response determines how much of the momentum wave you ride;
  event arb is naturally high-frequency.
