# Ch20 — Barrier Options (II)

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 20.

## Purpose
Reverse barriers, double barriers, and barrier variations (rebates, exploding options, caps, alternative barriers) — the difficult, in-the-money-terminating family.

## Reverse knock-outs
- **Reverse KO**: terminates *in the money* → large value discrepancy across the barrier; nearly decomposable into a regular KO plus an American bet (but with the opposite gap delta).
- Bizarre behavior: can have **negative delta** near the barrier (price falls as the market rallies toward the trigger); priced abnormally low; **negative decay** (value moves inversely to time) — attractive to sell to corporates, a nightmare to hedge.
- View them as American binaries with a high payout; near the barrier they look like a bet, not an option.

## Case study: the "salvation trade" (USD-FRF)
- A French corporate long dollars at 5.60, down ~12%; sold a 5.60 knock-out put that terminates at 4.85, one year out, ~0.8% of face. If the dollar recovers to 5.60, the customer recoups the loss.
- Lessons: the structure only "saves" the customer if the market behaves; the seller's profile depends on the path; salespeople exploit *distributional confusion* — customers think in terminal states, sellers in path distributions.

## Double barriers and variations
- **Double barriers** (e.g., double KO): expire when either barrier is touched; priced via infinite-series methods (Kunitomo-Ikeda) or as combinations; the vega of the structure can *decrease* in a rally (vega neutrality loses).
- **Rebates**: a payment at termination; make the barrier closer to an American binary.
- **Exploding options**: pay a fixed amount when a level is touched — equivalent to a reverse KO with a rebate equal to the exploding payoff; cheap alternative to call/put spreads.
- **Capped index options (CAPs)**: reverse KO paying a rebate = strike − outstrike at *settlement*; behave like American binaries (monotonically long/short vega) except near expiration, where they turn European (mixed gamma).
- **Alternative barriers (SCUDs)**: option on asset A with a barrier on asset B (e.g., Nikkei put with dollar-yen KO) — two correlated deltas; correlation decides whether it looks like a regular barrier or a bet on the other asset.

## Reading a risk management report
- Scenario reports (spot sensitivity grids) are the daily risk tool; for barriers they must include the *execution* of hedges at the trigger (gap delta, liquidation) — shadow reports for barrier books.
- Example: short $100M of a 3-month call on SYD with KO at 97; the report shows P/L across spot with 0.25-std increments, delta in the numeraire, and the barrier unwind behavior.

## Key takeaways
- Reverse barriers trade their termination risk for cheapness — their negative delta/decay near the trigger is the trade's essence.
- Always model the hedge *execution* at the barrier (gap deltas, slippage) — never get involved in a KO in an illiquid market without compensation for liquidity-hole risk.
- Double-barrier and settlement-based variations complicate vega and gamma sign stability; scenario analysis over (spot, vol) is required.
