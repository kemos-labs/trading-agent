# Ch17 — Arbitrageurs

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 17.

## Purpose
Arbitrage as the law-of-one-price enforcement mechanism: how
arbitrageurs connect markets, what risks they actually bear, and why
their activity is good for market quality.

## What arbitrage is (and isn't)
- **Pure arbitrage**: simultaneously buying and selling equivalent
  claims for a riskless profit (same instrument, two venues).
- **Relative-value / quasi-arbitrage**: buying and selling *similar
  but not identical* claims — the trader bears risk (e.g. basis
  risk) but expects a profit on average. This is most "arbitrage" in
  practice.

## The main arbitrages
1. **Cross-venue**: same instrument priced differently in two markets
   (third-market, ECN vs. exchange). Enforces one price everywhere.
2. **Index/futures (program) arbitrage**: index futures vs. the
   basket of underlying stocks. The fair price is the
   **cost-of-carry** relationship:
   `F = S·(1 + r·t) − dividends(t)` (r = financing rate). If futures
   deviate from fair, arbitrageurs buy cheap / sell rich and carry
   the basis to convergence at expiration.
3. **Cross-currency / synthetic**: equivalent claims built from
   different instruments (e.g. options vs. their replicating
   portfolios).
4. **Options/conversion**: puts+calls+stock+riskless bond price
   consistency (put-call parity).

## What they provide
- **Liquidity mobility**: they move liquidity from where it is
  abundant to where it is demanded, connecting fragmented markets
  (the consolidating force of Ch26).
- **Price discovery**: their trades align prices across venues, making
  each market's price informative about conditions everywhere else.
- **Risk transfer**: program arbitrage effectively sells index
  exposure into the futures market when stock buyers are scarce.

## Their real costs
- Financing costs (carry), execution costs, basis risk, and the risk
  that mispricing persists or widens before converging ("you can be
  right but broke"). Arbitrage is not free money — it is a trade with
  a favorable mean and a scary distribution.

## Key takeaways
- Arbitrage profits are bounded by **transaction and carry costs**:
  a mispricing must exceed the round-trip cost before it is tradeable.
- Enforcing the law of one price is itself a market service: it's why
  fragmented markets can still be *effectively* consolidated.
- For practitioners: relative-value "arbitrage" is a volatility/risk
  trade dressed in a convergence story — size it as a risky position,
  not a riskless one.
