# Ch04 — O+

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 4.

## Purpose
The revelation that reorients Bodek's hunt: at an exchange party in
December 2009, a representative admits Bodek's plain-vanilla limit
orders are structurally doomed — "you don't have a bug." Order types are
the real weapon, and Reg NMS is the framework that made them so.

## Order types as market language
- Order types are how firms "talk" to exchanges; they govern how an
  order interacts with the book. Market orders: "buy now no matter
  what." Limit orders: buy/sell within a specified price — what Bodek
  and most firms (including Schwab) used.
- The exchange rep's verdict: plain limit orders "are going to get run
  over." On a napkin, Bodek diagrams how a limit order flows into the
  exchange; each scenario ends with him losing. "Are you telling me
  you're fucked in *every* case?" "Yeah."
- The confession's motive: the exchange wants Trading Machines' flow
  back ("We want you to turn us back on again").

## Reg NMS (2007) and the SIP
- Regulation National Market System (passed early 2005, effective 2007)
  mandated that any order must route to the venue with the **best
  price**, binding the fragmented electronic market into one "national
  market system."
- Prices are shared across venues via the **SIP** (Securities
  Information Processor) feed. The SIP is slow relative to HFT feeds —
  the latency gap that later enables latency arbitrage (ch15).
- Reg NMS's order-protection architecture creates arbitrage and
  signaling opportunities that sophisticated venues and order types
  exploit; simple orders become the prey.

## The new order types
- The orders Bodek should use are compound — "Faulknerian" — with
  multiple clauses, built to interact with the book in ways plain limit
  orders cannot. Undocumented features determine whether an order gets
  priority, protection, or abuse.
- Net effect: everyday investors and Trading Machines buy a little too
  high, sell a little too low, and pay billions in take fees.

## Key takeaways
- A strategy can be sound and still lose if the *microstructure* is
  adversarially designed around your order type.
- In a best-price-routing world (Reg NMS), the game shifts to latency,
  queue position, and order-type sophistication — not price discovery.
- Know the venue's order types and their undocumented behavior before
  trading size; default limit orders are the prey of exotic order types.
