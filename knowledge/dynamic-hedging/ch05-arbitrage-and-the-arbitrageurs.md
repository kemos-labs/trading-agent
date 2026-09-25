# Ch05 — Arbitrage and the Arbitrageurs

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 5.

## Purpose
Defines arbitrage as traders practice it — a spectrum from locked-in mechanical relationships to behavioral-stability bets — and the limits of each.

## Two definitions
- **Academic**: a zero-cost linear combination of securities that can never be negative and can be positive (riskless profit).
- **Trader's**: the expected value of a self-financing portfolio is positive (may be negative in some states) — weaker, allows risk.

## Orders of arbitrage
- **First order**: strong, locked-in mechanical relationship, same instrument (currency triangular, location, European conversions/reversals, crush/crack spreads).
- **Second order**: different instruments, same underlying (cash-future, program trading, delivery, distributional/option spreading, stripping) or different-but-related underlyings (value trading, bond arb, forward trading, volatility trading).
- **Third order**: different securities and instruments deemed related (bond-vs-swap asset spread, cross-market, cross-volatility, cross-currency yield curve) — correlation-based, weakest.

## Mechanical vs. behavioral stability
- **Mechanical stability**: an identifiable, reproducible link (cost of carry, cross-currency decomposition, forward-forward box) — robust.
- **Behavioral stability**: an a posteriori statistical relationship (US–Canada swap curves, German–Swiss rates) with no true link — provides booby traps when the relationship breaks.
- Third-order/correlation arbitrage is betting on *stability of correlation* — the most fragile assumption in markets.

## The deterministic relationships
- Covered interest parity: F = e^(r−rf)t·S — the first formula every trader learns; arbitrageurs enforce it.
- Conversions/reversals (put-call parity for European options): call − put = forward; execution details (pin risk, settlement) are where the "arbitrage" hides real risk.

## Key takeaways
- Arbitrage is a spectrum; most "arbitrage" is risk-taking on the stability of relationships.
- Mechanical links are strong but crowded; behavioral links are fragile — historically stable until they aren't (regimes change).
- Arbitrage enforcement is what makes markets "fair" (martingale-like) — the market maker's submartingale edge (ch3) is the flip side.

## Source note
Pairs trading as statistical arbitrage is covered by the `cointegration-testing` and `kalman-filter-pairs` skills.
