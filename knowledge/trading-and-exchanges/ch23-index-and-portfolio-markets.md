# Ch23 — Index and Portfolio Markets

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 23.

## Purpose
How indexes are built, how index funds replicate them, and the
economics of indexation — including the transaction-cost effects of
index reconstitution.

## Index construction
- **Price-weighted** (DJIA, Nikkei): proportional to the sum of
  component prices; high-priced stocks dominate. Divisor adjusts for
  splits and composition changes.
- **Value-weighted** (S&P 500, most indexes): proportional to total
  market capitalization; large caps dominate. Divisor adjusts only for
  composition changes (splits don't change value weights).
- **Equal-weighted**: an equal dollar investment in each component —
  measures small-cap tilt. **Geometric**: averages log returns.
- **Total-return (dividend-adjusted)** indexes reinvest dividends;
  they are the proper performance benchmarks.

## Index fund replication
- Value-weighted replication: hold `fund_cap / index_cap` of each
  component — rebalance only when the index changes (cheap).
- Price-weighted: equal shares of each component; rebalance on
  splits/composition changes.
- **Tracking error** = fund return − index return; frictions (fees,
  dividend reinvestment cost, rebalancing cost, cash drag) make funds
  slightly underperform.

## The Russell reconstitution effect
- Frank Russell reconstitutes annually (last trading day of June,
  based on end-May caps); index funds all rebalance at once.
- Evidence (1996–2001): additions beat deletions ~15% in June, then
  underperform ~5% in July — **the trading of index funds itself
  moves prices**; part is transitory (reversal), part persistent
  (liquidity premium/momentum).

## The case for indexation
- Active management is a zero-sum game minus costs: with no costs, the
  value-weighted average portfolio return equals the index; with
  costs, the average *active* return is below the index.
- Turnover: active funds 100%+/yr at 1–3% fees vs. passive 0–10% at
  <15 bps. Only ~1/4 of funds beat the market in a given quarter; the
  winners don't persist (luck, per Ch22).

## Key takeaways
- Indexes are **construction artifacts**: price vs. value weighting
  changes which stocks dominate returns and what the divisor does.
- Index-fund flows are a **liquidity event**: reconstitution and
  addition/deletion windows create predictable price pressure —
  tradeable for those who know the calendar.
- The indexation argument is accounting, not opinion: average active
  returns must underperform by the cost differential.
