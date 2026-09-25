# Ch25 — Internalization, Preferencing, and Crossing

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 25.

## Purpose
The economics of off-exchange order flow: how dealers buy order flow,
what "best execution" means, and who actually benefits.

## The concepts
- **Internalization**: a broker/dealer fills client orders from its
  own inventory instead of routing to the market.
- **Preferencing**: a broker routes orders to a particular dealer in
  exchange for payments for order flow.
- **Crossing**: matching buy and sell orders internally (crossing
  networks) at midpoint or better.

## Why order flow is valuable
- Uninformed marketable order flow is *profitable* to trade against:
  the dealer earns the spread and avoids adverse selection. Dealers
  therefore **pay brokers** (payments for order flow) to obtain it.
- Brokers pass part of the value back to clients as low/zero
  commissions — which is why retail trading became free.

## Best execution
- Standard: fill marketable orders at the **NBBO** (national best bid
  or offer), with price improvement where possible; fill larger orders
  at no worse than the displayed size would permit; match limit order
  protection (a preferenced limit order should execute at least as
  fast as it would in the primary market).
- Best execution is a **bundled good**: price, speed, and fill
  probability trade off. It is hard to audit — which is why SEC Rule
  11Ac1-5 (market-center execution statistics) and 11Ac1-6 (broker
  routing disclosure) exist.

## The economics
- In perfectly competitive order-flow markets, any improvement in
  execution quality demanded is offset by lower payments for order
  flow — **total net cost to clients is invariant** to how the spread
  is split between price improvement and rebates/commissions.
- But this holds only when clients can enforce quality; the **audit
  problem** (clients can't measure execution) lets dealers profit by
  skimping on price improvement and by extracting option value from
  the limit orders they are forced to accept.
- Concerns: preferencing dealers may fill limit orders early when
  prices move (harvesting their option value), and may not expose
  orders to the best market.

## Key takeaways
- Payments for order flow are not inherently evil: they are the
  competitive price of uninformed order flow — the question is
  whether execution quality is preserved.
- Measure your own fills: effective spread vs. NBBO mid, and
  limit-order fill speed, are the audit that keeps the deal honest.
- The venue that pays for flow is monetizing your *lack of
  information* — retail traders subsidize their free commissions with
  the spread they don't see.
