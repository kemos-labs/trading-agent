# Chapter 4 — Expiration Profit and Loss

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Parity graphs (hockey-stick diagrams)

At expiration an option is worth exactly its intrinsic value. Plotting
position value vs. underlying price at expiration gives the four basic
parity graphs:

| Position | Slope below X | Slope above X |
|---|---|---|
| Long call | 0 | +1 |
| Short call | 0 | −1 |
| Long put | −1 | 0 |
| Short put | +1 | 0 |
| Long underlying | +1 | +1 |
| Short underlying | −1 | −1 |

Slope = Δ(option value)/Δ(underlying price) — the precursor of delta
(ch. 7). The option's parity graph always bends at the strike (insurance
feature); the underlying's slope is constant.

- Buyers: limited risk (premium paid), unlimited profit potential.
- Sellers: limited profit (premium received), unlimited risk.
- Sellers exist because pricing is about *probabilities* of outcomes,
  not just worst cases (foreshadow of the volatility chapters).

## Building complex graphs

- Combine positions by **adding slopes** interval by interval; connect
  segments across the sorted set of strikes. Long call + long put at the
  same strike = V-shaped position (gains on any move away from X).
- 2 long calls at X + short underlying = same graph as long call + long
  put at X → the same strategy can be built multiple ways (synthetics,
  ch. 14).
- Long call + short put at the same strike = slope +1 everywhere =
  long underlying (the fundamental synthetic).
- For complex graphs there may be no y-axis position — only slope
  structure matters.

## Expiration P&L and breakevens

P&L graph = parity graph shifted down by any debit (buying) or up by any
credit (selling).

- Long call at premium 3.50, X = 100: max loss 3.50, breakeven 103.50
  (= X + premium). Long put breakeven = X − premium.
- For complex positions: compute slopes over each interval, get P&L at
  one known point (easiest at a strike), then propagate via slopes.
  Worked example — position P&L at 95 is −3.00; slope +1 from 95→105
  gives +7.00 at 105; slope −2 above 105; breakevens: 95 + 3/1 = 98.00,
  105 + 7/2 = 108.50.
- P&L at arbitrary price from one known point: sum slope × interval
  distances (e.g., from 62.00 → 81.50 yields −13.40 in the book's
  example).

## Key takeaways

1. At expiry, value = intrinsic; everything else is time value.
2. Slope tables make arbitrary multi-leg positions tractable — compute
   per-interval slopes, anchor one P&L point, propagate.
3. Parity graphs reveal strategy equivalence, a key to pricing/arbitrage
   later (ch. 14 synthetics).
