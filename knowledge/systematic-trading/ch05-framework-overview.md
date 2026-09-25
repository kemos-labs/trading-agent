# Ch05 — Framework Overview

**Source:** Carver, *Systematic Trading*, Chapter 5.

## Why a modular framework
A trading system = trading rules (the engine, producing price forecasts)
wrapped in a position/risk management framework (chassis → turns forecasts
into positions). Every component is just "a few steps of basic arithmetic" —
no code needed. Modularity gives:
- **Flexibility**: adapt to any rule, including discretionary forecasts
  (semi-automatic) and fixed forecasts (asset allocating investors).
- **Transparent modules**: unlike PC black boxes, every component is
  explained so you can modify or rebuild it.
- **Well-defined interfaces**: a forecast of +1.5 must mean the same thing
  regardless of rule style or instrument, so swapping components works
  (like a gearbox's clockwise shaft).
- **Getting the boring bit right**: the framework (not the rules) is where
  most mistakes hide; having a standard one de-risks everything.
- **Examples as starting points** (part four of the book).

## The bad example (what NOT to do)
Typical textbook system: 20/40 MA entry, "never trade more than 10
Eurodollar futures", "never bet more than 3% per trade", "trailing stop at
3% loss, widen if triggered often". All the position/money-management rules
are a mess:
- 3% of what, for whom? Depends on account size and risk appetite — a fixed
  rule can't fit everyone. What if you hold 40 positions (40 × 3% = 120% at
  risk)?
- Stop losses based on capital/pain threshold are wrong: stops belong to the
  *market* (volatility), not your account. A stop right for oil is absurd
  for USD/CAD; right for 2006 is absurd for 2008.
- Fix: **separate the components** — (1) trading rules/stops based only on
  market volatility; (2) volatility target (how much capital to risk) based
  on account size + pain threshold; (3) position sizing based on market
  volatility, forecast confidence, and capital to gamble.

## The framework elements (in order)
1. **Instruments** — what you trade (equities, bonds, futures, CFDs, spread
   bets, ETFs/funds).
2. **Forecasts** — each rule variation produces a forecast of how much an
   instrument's price will change. N rules × M instruments = N×M forecasts.
3. **Combined forecasts** — weighted average (via **forecast weights**) of
   all forecasts for one instrument → a single combined forecast.
4. **Volatility targeting** — decide total risk: the "typical average daily
   loss you are willing to expose yourself to", based on wealth, risk
   tolerance, leverage access, expected profitability.
5. **Scaled positions** — turn the combined forecast into a position size
   given instrument risk, forecast confidence, and the volatility target.
   This forms a self-contained **trading subsystem** per instrument.
6. **Portfolios** — combine subsystems using **instrument weights** →
   portfolio-weighted positions → the trades you execute.
7. **Speed and Size** — cross-cutting principles (trading costs, account
   size) that apply to the whole system (ch12).

## Notes
- The framework is deliberately agnostic to the forecasting method: staunch
  systems traders use rules, semi-automatic traders use discretionary
  forecasts, asset allocating investors use a single fixed forecast.
- Everything downstream of the forecast is deterministic arithmetic — this
  is what makes the framework reusable across all three reader archetypes.
