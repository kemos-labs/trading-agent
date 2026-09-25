# Ch14 — Life Cycle of a Trade

**Source:** *Volatility Trading*, 2nd ed. — Euan Sinclair (Wiley, 2013)

## The process view

A trade is not an event; it is a lifecycle with defined stages, each with
its own discipline. Volatility trading, in particular, is a *process*
business: you can be right on vol and lose money, so the process — not any
single trade — is what you bet on.

## Stages

1. **Idea/edge**: start from an explicit, testable edge (forecast vs.
   implied divergence you can explain). Document the reasoning *before*
   entering; this defeats hindsight bias and later audit-ability.
2. **Evaluation**: compute expected P&L net of costs over the full outcome
   distribution; stress vol-of-vol, skew, gap scenarios (see trade
   evaluation).
3. **Sizing**: size by the goal (profit max vs. target vs. hedge), using
   Kelly/fractional Kelly or vol targeting; aggregate risk with the existing
   book (net vega/gamma/delta).
4. **Entry & execution**: enter with discipline on price/IV (limit orders
   on IV, not just price), mindful of spread and of the surface regime
   (sticky strike vs. delta).
5. **Management (the long middle)**: this is where vol trades live or die —
   hedge policy (bands/frequency, costs), monitoring forecast vs. realized
   vol, and adjusting size as vol-of-vol realizes. Most of the trade's
   variance comes from the management phase, not entry.
6. **Exit**: pre-committed exit rules — target vol realized, forecast
   change, time decay, or risk limits (max loss, max vega). Exiting is part
   of the trade's expected value; a good entry without an exit rule is an
   incomplete trade.

## Cross-cutting disciplines

- **Records**: log entry thesis, sizing math, hedges, and exit reason for
  every trade. Without records you cannot measure your true edge, and
  without measured edge you cannot size (and should not trade).
- **Post-trade review**: score forecasts against outcomes (calibration,
  hit rate); audit decisions with hindsight-bias awareness. Feed results
  back into edge estimation and sizing.
- **Process consistency**: the same trade logic executed identically every
  time is what turns a string of uncertain individual trades into a
  profitable business. Change the process only deliberately, with data.

## Key takeaways

- Treat each trade as a lifecycle: idea → evaluation → sizing → entry →
  management → exit, each stage disciplined.
- The management phase carries most of the risk and opportunity — hedge
  policy and vol monitoring are the job.
- Pre-commit entry and exit rules; write the thesis down first.
- Comprehensive records are the foundation: they make edge measurement,
  sizing, and learning possible.
