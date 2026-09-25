# Chapter 7 — Risk Measurement I (the Greeks)

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Sign conventions — effect of changing conditions

- **Rising rates** (stock options): forward price up → calls up, puts
  down; present value down → both down. Forward effect dominates (stock
  price ≫ option price), so **calls rise with rates, puts fall**.
- **Short-stock hedging** effectively reduces the rate by borrowing costs
  → lower forward → calls cheaper, puts dearer. Rule: *avoid short stock
  positions whenever possible*; carry some long stock so hedges can be
  made with long (not borrowed) stock at the ordinary long rate.
- **Futures options**: futures-type settlement (most non-US) → rho = 0
  (no cash flows). Stock-type settlement (US) → both calls and puts
  decline as rates rise (present-value effect only); still small.
- **FX options**: two rates — raising the *foreign* rate lowers the
  forward (calls down, puts up); raising the *domestic* rate raises the
  forward and dominates (calls up, puts down).
- **Dividends up** → forward down → calls down, puts up (and vice versa).

## Delta (Δ)

- Rate of change of option value wrt underlying price; slope of the
  theoretical-value curve. Calls: 0 → 100; puts: −100 → 0; underlying:
  100 (whole-number convention, 1 delta ≈ 1 share in the 100-share
  convention).
- Three equivalent interpretations:
  1. **Rate of change**: delta 25 → option moves 25% of the underlying's
     move.
  2. **Hedge ratio**: neutral hedge = 100/delta underlying contracts per
     option (call Δ50 → sell 1 underlying per 2 calls; put Δ−75 → buy 3
     underlying per 4 puts). **Delta neutral** = position deltas sum
     to 0. Hedging direction: long calls / short puts hedge with *short*
     underlying; short calls / long puts with *long* underlying.
  3. **Equivalent underlying position**: 100 deltas ≈ 1 underlying
     contract (long 10 Δ50 calls = long 500 deltas = 5 underlying).
     Theoretical only — options carry non-directional risks the delta
     ignores.
- **Probability**: |Δ| ≈ probability of finishing in the money (ATM ≈
  50; precisely, the *at-the-forward* option has Δ ≈ 50 — with S = 100,
  r = 10%, 1 yr, forward 110, the 110 call is Δ≈50 and the 105 call is
  >50). Δ alone is insufficient: winning 9 of 10 with a Δ10 short is a
  loser if the 10th loss exceeds 9× the premium — you need *how much*
  wins/losses, not just how often.

## Gamma (Γ)

- Rate of change of delta (curvature). Same for calls and puts at the
  same strike/expiry; always positive; max near the money.
- Mechanics: underlying up one point → delta += gamma; down one point →
  delta −= gamma. Long options = long gamma (delta grows as market
  rises), short options = short gamma (delta grows more negative as
  market rises — you get more bearish as the market goes up).
- Improved value estimate over a finite move (average delta):
  `ΔC ≈ ΔS·Δ + ΔS²·Γ/2`. Example: at 97.50, C = 3.65, Δ = 40, Γ = 2.5;
  underlying → 101.50: new Δ = 40 + 4·2.5 = 50, avg Δ = 45,
  C ≈ 3.65 + 4.00 × 0.45 = 5.45.
- Gamma = **magnitude risk**: positive gamma wants big fast moves;
  negative gamma wants a quiet market. Δ+Γ together tell direction and
  speed of the move you want.

## Theta (Θ)

- Time decay per day; negative for almost all options. ATM theta
  *increases* as expiry nears (≈ −0.03 at 3 months, −0.06 at 3 weeks,
  −0.16 at 3 days).
- Positive theta is possible for a *deep ITM European* option under
  stock-type settlement (its price = PV of intrinsic < intrinsic; it
  must rise toward intrinsic as time passes — negative time value).

## Vega and Rho

- **Vega**: change per 1 *percentage point* of volatility; positive for
  all options (all options gain with vol); aka kappa.
- **Rho**: change per 1 point of interest rate; sign depends on
  instrument/settlement; least important Greek (ignore in most examples
  unless the position is huge).
- Underlying: Δ = 100, Γ = Θ = vega = rho = 0.

## Portfolio risk & interpretation

- All Greeks are **additive**: multiply each by +contracts (long) or
  −contracts (short) and sum.
- Worked position (sold 10 June 95 calls @ 8.55, model value 8.33):
  edge +2.20; Δ −10 (neutral); Γ −28 (wants the market to sit still);
  Θ +0.34/day; vega −1.70 (wants implied vol down); rho −1.55.
  - **Γ and Θ are almost always of opposite sign** — movement helps
    (long Γ) XOR time passage helps (long Θ); magnitudes correlate. You
    can't have both.
  - Γ ↔ *realized* volatility preference; vega ↔ *implied* volatility
    preference — they can diverge (ch. 11).
  - Position **breakeven volatility** ≈ model vol + edge/vega:
    25 + 2.20/1.70 ≈ 26.29% (the book's printed 27.29% is an arithmetic
    slip: 25 + 1.29 = 26.29; verified against its own numbers: at 26%
    edge = +0.50, at 27% = −1.20). This is the position's *implied
    volatility*.
- A negative theoretical edge (Position 2) means the model says the
  strategy loses in the long run — exit; sometimes accepting a small
  negative edge is the whole point of hedging a larger position.
- All Greeks change constantly; the goal is identifying acceptable risk,
  not eliminating it (paralysis through analysis).

## Key takeaways

1. Greeks are additive, per-contract weighted; Δ = equivalent underlying
   exposure, Γ = magnitude/speed preference, Θ = time preference, vega =
   implied-vol preference, rho = rate preference.
2. Hedge ratios come straight from Δ: 100/Δ contracts per option,
   opposite sign for calls, same sign for puts.
3. Long gamma pays when realized moves are large; it's financed by
   negative theta (and vice versa) — the fundamental long/short-vol
   tradeoff.
