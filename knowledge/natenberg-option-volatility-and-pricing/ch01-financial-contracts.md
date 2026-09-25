# Chapter 1 — Financial Contracts

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Contract taxonomy

- **Spot/cash transaction**: terms agreed, then immediate exchange of
  money for goods. Exchange-traded stock is effectively cash settlement
  (short settlement lag ignored).
- **Forward contract**: terms agreed now, exchange of money for goods at
  a later *maturity/expiration date*. Price is the *forward price*.
- **Futures contract**: a forward contract standardized and traded on an
  organized exchange — the exchange fixes quantity, quality, delivery
  date/place, and payment method, and guarantees the contract.
- **Option contract**: one party buys the *right* (not obligation) to
  decide later whether to transact, paying a *premium* that the seller
  keeps regardless of outcome. Call = right to buy; put = right to sell.
  Insurance is the familiar analog (premium, expiration date, exercise
  price ≈ insured amount/deductible). Option valuation is probability-
  based, exactly like actuarial pricing.
- **Swap**: agreement to exchange cash flows (e.g., fixed vs. floating
  rate). Usually OTC; excluded from the book's scope.
- All of these derive value from an **underlying** asset → *derivatives*.

## Position language

- Opening trade → open position; closing trade reverses it. Open interest
  = contracts not yet closed (longs must equal shorts globally).
- *Long* = bought contract; *short* = sold contract. Confusingly, long
  also means "wants market up." For derivatives a long position can want
  the underlying down (long put). Use "long/short contract position"
  vs. "long/short market position" to disambiguate.
- Long position → debit; short position → credit (applies to spreads too:
  net debit = long, net credit = short).

## Notional value

- Physical forward: notional = units × unit price (1,000 × $75 = $75,000).
- Financial/index future: notional = index level × point value
  (825.00 × $200 = $165,000). Point value is set so the contract has a
  reasonable notional — too high = too risky, too low = prohibitive
  transaction costs per unit of exposure.

## Settlement procedures (critical distinction)

- **Stock-type settlement**: full and immediate payment; P&L stays
  *unrealized* (paper) until the position is closed.
- **Futures-type settlement** (margin and variation): initial *margin
  deposit* (security against default, still owned by trader, earns
  interest) + daily *variation* credits/debits as price moves. A rise
  from $75 to $90 on a 1,000-unit contract transfers $15,000 from seller
  to buyer; at maturity the buyer pays $90,000 − $15,000 variation =
  the original $75,000. Close via offsetting trade (final variation +
  margin returned) or physical/cash settlement at maturity.
- **Options in North America are all stock-type settled** — including
  options on futures. Pitfall: a hedge that offsets futures P&L in theory
  still produces cash-flow problems, because the losing futures side
  generates immediate variation calls while the profitable option side
  stays unrealized. Most non-North-American exchanges align option and
  underlying settlement, avoiding this surprise.

## Market integrity

- Exchange breaks the buyer-seller link and becomes counterparty to both
  sides; a **clearinghouse** (e.g., OCC for equity options, CME Clearing,
  DTCC for stock) guarantees trades. Clearing firms guarantee individual
  traders and may aggregate/net positions to reduce margin. No U.S.
  clearinghouse has ever failed.

## Key takeaways

1. Options = rights bought with premium; forwards/futures = obligations.
2. Know which settlement convention an instrument uses before designing
   hedges — the cash-flow timing, not just total P&L, matters.
