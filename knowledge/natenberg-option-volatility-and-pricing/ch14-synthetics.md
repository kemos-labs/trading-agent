# Chapter 14 — Synthetics

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## The six basic synthetics

Options can replicate other positions exactly in payoff shape (slopes
add, prices are irrelevant to the *characteristics*). All legs same
strike and expiry:

```
synthetic long underlying  = +call  − put
synthetic short underlying = −call  + put
synthetic long call   = +underlying + put
synthetic short call  = −underlying − put
synthetic long put    = −underlying + call
synthetic short put   = +underlying − call
```

- Why +call − put ≡ long underlying: at expiry the underlying is always
  bought at the strike — by choice if above (exercise call) or by force
  if below (assigned put). Delta of a synthetic underlying ≈ 100.
- **Mnemonic**: trade one option, hedge with the underlying → you're
  synthetically in the *companion* option: buy call + sell underlying =
  buy put; sell call + buy underlying = sell put; buy put + buy
  underlying = buy call; sell put + sell underlying = sell call.

## Risk-measure implications

- Companion call and put deltas sum to ≈ 100 in absolute value (call Δ75
  ↔ put Δ−25).
- **Gamma and vega of companion calls and puts are identical** — the
  underlying has zero γ/vega, so a synthetic underlying must have zero
  net γ/vega. Volatility traders treat calls and puts at the same
  strike/expiry as the same contract; converting call↔put is just a
  trade in the underlying.
- Theta need not match: carry cost (interest on stock, or on
  stock-type-settled options) breaks the symmetry. Only with
  futures-type settlement on both legs (no cash flows) are companion
  thetas equal.

## Applications

- **Vertical spreads**: bull call spread ≡ bull put spread + long +
  short underlying that cancel; the two are identical in payoff but the
  call version is a debit and the put version a credit. At r = 0 their
  prices sum to the strike distance (max value): call spread 3.00 →
  put spread 2.00.
- **Long straddle**, three ways: (+call, +put), (+call, synthetic put =
  +call, −underlying), or (+put, synthetic call = +put, +underlying).
  Pick whichever prices best (next chapter).
- **Iron butterfly** = long strangle + short straddle centered between
  (buy outer, sell inner; credit). Same P&L as a long (traditional)
  butterfly, which is a debit; butterfly + iron butterfly prices sum to
  the strike spacing (1.75 + 3.25 = 5.00 at r = 0). Both want the
  market at the inside strike.
- **Iron condor** = long outer strangle + short inner strangle (credit);
  ≡ long condor (debit); prices sum to the spacing (3.75 + 1.25 =
  5.00). Both want the market inside the inner strikes.
- **Christmas trees**: a +95/−100/−105 call tree unwinds via synthetics
  into short 100/105 strangle + long 95 put — revealing limited
  downside, unlimited upside.

## Key takeaways

1. Any strategy can be executed in multiple synthetic forms — the
   cheapest leg construction wins (pricing in ch. 15).
2. Companion call/put have identical γ and vega; only carry costs
   differentiate their θ.
3. Iron butterflies/condors are the credit-side twins of debit
   butterflies/condors — same payoff, opposite cash flow, values pinned
   by the strike spacing.
