# Chapter 15 — Option Arbitrage (put-call parity & friends)

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Put-call parity (European options)

The combo value (C − P, same strike/expiry) is pinned by the forward:

- **Futures, futures-type settlement** (most non-US): `C − P = F − X`
  (no cash flows → r = 0). Ex: C = 5.25, P = 1.50 → fair F = 103.75;
  futures at 104 → **reverse conversion** (buy combo = +C/−P, sell
  futures) profits the 0.25 mispricing.
- **Futures, stock-type settlement** (North America): `C − P =
  (F − X)/(1 + r·t)`. Ex: F = 97.25, X = 100, r = 6%, t = ½ → C − P =
  −2.67 → with C = 4.90, P = 7.57.
- **Stock**: forward first — F = S(1 + r·t) − D; then `C − P =
  (F − X)/(1 + r·t)`. Ex: S = 68.50, r = 4%, t = ½, D = 0.45 →
  F = 69.42, C − P = 4.33 → with C = 8.00, P = 3.67.
- **Approximation** (fast, short-term): `C − P ≈ S − X + X·r·t − D`
  (error 0.02 in the example: 4.35 vs. 4.33).
- **Locked futures markets**: when the future is limit-up/down, trade it
  synthetically through options — F = C − P + X.

From PCP, solve for any missing input: *implied interest rate* or
*implied dividend* (the market's view; e.g., combo implying D = 0.30
when you assumed 0.47 → dividend-cut warning).

## Conversions & reversals

- **Conversion** = +underlying + put − call (sell the combo, buy stock).
- **Reversal** = −underlying − put + call (buy the combo, sell stock).
- Classic arbitrage; prices self-correct within seconds, so only
  low-cost pros trade them, in size.

### Risks (very few strategies are truly riskless)

1. **Execution risk**: legs must be assembled piecemeal; prices move
   before the position is complete.
2. **Pin risk**: underlying = strike at expiry. ATM options *are*
   exercised in practice (exercise is cheaper than trading the
   underlying), but you don't know about assignment until the next day.
   Guess wrong on a big conversion book → naked underlying positions the
   next morning. Mitigations: reduce size into expiry, or cross with the
   opposite trader at even money (cash-settled index options have no pin
   risk).
3. **Settlement risk** (options stock-type, underlying futures): the
   futures leg throws daily variation (real interest cost/gain) while
   the option leg's P&L stays unrealized. The synthetic's delta ≠ 100:
   `Δ_synthetic ≈ 100 × (1 − r·t)` (93 at r = 10%, t = ¾; 99 at 4%, 1
   month). 300 conversions × +2 deltas = +600 deltas ≈ 6 extra futures.
   This is the same *tailing* issue that physical-commodity hedgers face.
   No settlement risk when both legs share one settlement convention.
4. **Interest & dividend risk** (stock): conversion = −rho, *positive
   dividend risk* (long stock); reversal = +rho, negative dividend risk.
   Combo sensitivity: r 4%→5% moves the 65 combo 4.35→4.68; D 0.45→0.65
   moves it 4.35→4.15.

## Boxes, rolls, time boxes

- **Box** = conversion at X₁ + reversal at X₂ (underlyings cancel):
  worth exactly the strike spacing at expiry → today PV(spacing)
  (90/100, 3 mo @ 8% = 9.80). Also = bull call spread + bear put spread
  (6.00 + 3.80 = 9.80). Cash-settled European boxes = pure borrowing/
  lending: selling the 90/100 box at 9.70 = borrowing 3 months at 12%.
- **Roll** = conversion in one month + reversal in another, same strike
  (stock market only — futures of different months don't cancel):
  value = (C_l − P_l) − (C_s − P_s) ≈ `X·r·t − D` between expiries
  (June/Aug 90 roll: 0.90 − 0.40 = 0.50 vs. exact 0.47). Also = call
  calendar spread − put calendar spread (2.25 − 0.47 = 1.78). Rolls with
  the same dates differ by interest on the strike difference (90 roll
  0.47 → 80 roll 0.37).
- **Time box / diagonal roll**: different strikes *and* months; value =
  discounted-strike difference − dividends (June 90/Aug 100 = −9.33,
  paid as a debit); decomposes into a box + a roll.

## Using synthetics to trade volatility spreads cheaper

With bid/ask quotes, the best construction of a *strategy* isn't
arbitrage — it's execution choice:
- Buy the 50 straddle: outright 4.20 + 2.40 = 6.60; synthetic call leg
  (put + stock) = 4.15 → total 6.55 (−0.05). Conversions/reversals are
  blocked by the spread, but the straddle can still be assembled
  cheaper.
- Buy the 45/50/55 butterfly: call butterfly 1.32, put butterfly 1.30;
  iron butterfly should trade at PV(5.00) − 1.30 = 3.65, and selling it
  at 3.70 is −0.05 better.
- General rule: always price the alternative synthetic constructions of
  any strategy before executing (but respect transaction costs — a
  3-leg synthetic isn't always better for a retail trader).

## Key takeaways

1. PCP pins every combo: C − P = (F − X)·discount; it's the mother
   relationship for conversions, reversals, boxes, rolls, and strike
   selection.
2. Conversion/reversal/box risks are real: pin, settlement (tailing),
   rates, dividends — size them accordingly.
3. Always check the synthetic alternative for the strategy you want;
   small per-contract savings compound over a career.
