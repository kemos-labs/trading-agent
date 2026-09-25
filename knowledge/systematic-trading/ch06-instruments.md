# Ch06 — Instruments

**Source:** Carver, *Systematic Trading*, Chapter 6.

## Necessities (can you trade it at all?)
- **Data availability**: minimum is accurate daily prices; fast strategies
  need tick data; fundamental strategies need fundamentals. Data licences
  can make some instruments uneconomic for amateurs.
- **Minimum sizes**: JGB futures (~¥150m ≈ $1m+) mean you'd want 0.1
  contracts — impossible. Minimum sizes reduce granularity → binary
  all-or-nothing positions (ch12 handles the portfolio implications).
- **Understand what moves prices**: "more buyers than sellers" is not an
  answer. You need a mental model of what drives each market (rates, news,
  earnings) for ideas-first rule design and to avoid dysfunctional markets.
  Example: Carver avoided EUR/CHF & USD/CHF because a central-bank peg
  (not normal drivers) controlled prices — and in Jan 2015 the Swiss
  unpegged, devastating leveraged OTC traders.
- **Standard deviation (vol)**: exclude extremely low-vol instruments
  (pegged currencies). When risk normalises it does so *sharply*; low vol
  needs more leverage to reach a target, magnifying blow-ups; and low-vol
  instruments cap the whole system's achievable risk.

## Instrument choice & how to trade them
- **How many instruments**: as many as possible for diversification, bounded
  by minimum sizes, account value, and risk target. Pick low-correlation
  instruments when the count is limited (don't add a 3rd UK bank to 2 you
  own).
- **Costs**: choose the cheapest access (cheap FTSE future over spread bet).
  Expensive instruments must be traded more slowly; some are untradeable at
  any speed. Cost matters enough for its own chapter (ch12).
- **Liquidity**: less liquid = pricier to trade fast/large; evaporates in
  stress (2008 CDS). Mostly an institutional concern.
- **Skew**: static strategies inherit instrument skew; dynamic rules add
  their own — a positive-skew trend rule on a negative-skew asset alleviates
  danger. Extreme-negative-skew instruments usually also have low vol and
  get excluded on those grounds.

## Access routes
- **Exchange vs OTC**: prefer exchange when possible. Jan 2015 CHF meltdown:
  OTC brokers rejected orders, re-marked fills, some went bust; the CHF
  future traded thin but normally.
- **Cash vs derivative**: cash = own the asset directly; derivatives
  (futures, CFDs, spread bets) give simple leverage (needed to reach your
  vol target) and sometimes tax advantages (UK spread bets = gambling:
  winnings tax-free). Futures beat spread bets on cost, liquidity, and
  exchange access but have larger minimum sizes.
- **Collective funds**: passive index trackers/ETFs have low fees and
  minimums but trade costlier than derivatives; useful when leverage can't
  be used or the market isn't accessible otherwise. Active funds need
  provable manager alpha — usually unproven. Watch fund quirks: daily
  remarking, tax, internal leverage, NAV discounts.

## Summary checklist (choose your instruments)
Data ✓ · minimum sizes ✓ · know what drives returns (avoid distorted
markets) ✓ · vol not extremely low ✓ · hold the largest portfolio your
account/minimums allow ✓ · maximise diversification ✓ · cheaper access
preferred ✓ · liquidity (large investors) ✓ · handle negative skew
carefully ✓ · exchange over OTC ✓ · cash vs derivative choice ✓ · funds as
fallback ✓.

## Notes
- The recurring theme: instrument selection is where leverage, cost, and
  blow-up risk are really decided — before any rule is written.
- Forecasts come next (ch7): "now you know *what* to trade, think about
  *how*."
