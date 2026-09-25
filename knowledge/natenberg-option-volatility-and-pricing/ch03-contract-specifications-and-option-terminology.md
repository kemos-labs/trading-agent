# Chapter 3 — Contract Specifications and Option Terminology

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Contract anatomy

- **Type**: call = right to buy; put = right to sell. All *rights* belong
  to the buyer, all *obligations* to the seller (unlike futures, where
  both sides have obligations).
- **Underlying**: stock options = 100 shares (round lot; flex options can
  customize). Futures options = one futures contract, usually the futures
  month matching the option expiry; **serial options** (no matching
  futures month) settle into the nearest futures beyond option
  expiration; **midcurve options** = short-dated options on long-dated
  futures (Eurodollar, Euribor, Short Sterling).
- **Expiration**: stock/index options expire 3rd Friday (last trading day
  = expiration day, minus a day when Good Friday falls in April). Stock
  index options use **AM expiration** (value from underlying *opening*
  price, avoids closing-order imbalances); stock options use PM
  expiration. Options on physical-commodity futures expire in the month
  *before* the futures month because delivery takes days.
- **Exercise/assignment**: exercising = converting option into underlying
  (call → long, put → short). Assignment (who must take the other side)
  is essentially random among open short sellers. Settlement into: (1)
  physical underlying (stock options — cash flow = strike × shares only,
  independent of market price), (2) futures position (immediately
  margined + variation payment at exercise-price vs. current futures
  price), or (3) cash (index options — payoff = (S−X) × point value).
- **Exercise style**: European = exercise only at expiration; American =
  any business day. Labels are geographic misnomers. General rule: stock
  and futures options American; index options European.

## Premium decomposition

- `intrinsic value = max(0, S−X)` (call), `max(0, X−S)` (put).
  Independent of time to expiry.
- `time value (extrinsic) = premium − intrinsic`. Premium is *always*
  exactly these two components. Time value can be zero (trading **at
  parity**); a European option can even have *negative* time value
  (ch. 16).
- Moneyness: in the money = positive intrinsic; out of the money = zero
  intrinsic (price is all time value); at the money = strike ≈ spot
  (exchange convention: the strike closest to spot; most liquid).
- At expiry, exchanges auto-exercise in-the-money options past a
  threshold (e.g., 0.05 retail / 0.02 professional) unless a "do not
  exercise" notice is filed — prevents losing intrinsic value by neglect.

## Margining rules

- Long options: risk capped at premium → margin never exceeds max risk.
- Positions with unlimited risk (short options, complex spreads): margin
  is **risk-based** — the clearinghouse (OCC's system for stock/index
  options; CME's **SPAN** on futures exchanges) prices the portfolio
  across a grid of underlying-price × volatility scenarios and sizes
  margin to the worst case.

## Key takeaways

1. Know what an option settles into (physical / futures / cash) — cash
   flows at exercise differ completely.
2. Exercise style determines whether early-exercise value exists (ch. 16).
3. Margin is scenario-based for short/complex positions, not a fixed
   rate.
