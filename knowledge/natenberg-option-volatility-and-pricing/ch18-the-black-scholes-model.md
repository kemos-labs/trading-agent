# Chapter 18 — The Black-Scholes Model

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## The equation and its solution

The Black-Scholes PDE states that a correctly hedged option position
must break even as S and t move, with σ and r held constant over the
option's life (the ch. 8 assumption). Its pieces: Δ, Γ, Θ; rS (spot →
forward), rC (discounting), and (σ²/2)S²Γ (vol × curvature).

Solution for a European call on a non-dividend stock:

```
d1 = [ln(S/X) + (r + σ²/2)·t] / (σ·√t)
d2 = d1 − σ·√t
C  = S·N(d1) − X·e^(−rt)·N(d2)
P  = X·e^(−rt)·N(−d2) − S·N(−d1)   (via put-call parity)
```

**Interpretation**: the call = (average value of all stock above X at
expiry) − (expected amount paid for it). N(d1) weights the forward
price Se^(rt) (the lognormal *mean* is right of the mode by σ²t/2);
N(d2) is the true probability of finishing in the money (from the
*median*, which lies σ√t left of the mean). Discounting by e^(−rt)
turns Se^(rt)N(d1) − XN(d2) into the familiar form.

**Adjustment factor b (carry) for other underlyings**: stock b = r;
futures b = 0; FX b = r − r_f (etc.) — the model family differs only in
the forward and settlement.

## The 40% rule (hand valuation)

Exactly at-the-forward European option, r ≈ 0, 1 year, 1% vol:
d1 = 0.005, d2 = −0.005, N(d1) − N(d2) = 0.501995 − 0.498005 =
0.003990 (= the standard-normal peak 0.399/100). So:

`EV ≈ 0.4 × S × σ × √t` (0.4·one standard deviation of the forward)
`TV ≈ EV / (1 + r·t)` (or discount by e^(−rt))

Example: σ = 18%, t = ¼, X = 65, r = 4% → EV ≈ 0.4×65×0.18×0.5 =
2.34; TV ≈ 2.34/1.01 ≈ 2.32. Caveats: approximation runs slightly
*high* at long t/high σ because ATM vega declines with vol (e.g., 40%,
2yr: approx 14.60 vs. true 14.48).

## Greeks from the model

- **Delta = N(d1)** — always > N(d2), the ITM probability. So an
  at-the-forward call has Δ > 50 and the companion put < −50; an
  at-the-forward straddle is delta positive. Exactly neutral straddle
  requires `S = X·e^[−(r+σ²/2)t]` — the delta-neutral underlying price
  falls well below the strike at high vol/long time.
- **Theta** has three components: (1) decay of volatility value — the
  *driftless theta* (same sign for calls and puts, dominates); (2)
  spot-to-forward drift (b − r)S·N(d1); (3) changing present value
  rXe^(−rt)N(d2). With r = 0 or futures-type settlement only component 1
  survives.
- **Max gamma/theta/vega are not exactly at the money**: with b = 0,
  max vega/theta occur at the same price above X, max gamma below X;
  rising rates pull theta/vega maxes down and gamma max up. In terms of
  higher-order Greeks: gamma max at speed = 0, theta max at charm = 0,
  vega max at vanna = 0.
- **Vega can *decrease* with time** for stock options: as t grows the
  forward (S·e^rt) moves away from the strike, cutting vega. At r = 0
  vega always rises with time; at r = 10% it peaks at ~33 months; at
  r = 20% at ~10 months (visible in vega decay turning negative).

## Key takeaways

1. BS = discounted expected payoff under lognormality: `C = S·N(d1) −
   Xe^(−rt)N(d2)`, with N(d1) = delta and N(d2) = ITM probability.
2. Fast sanity check: at-the-forward option ≈ 0.4·S·σ·√t (undiscounted),
   scaling with both vol and √time, proportional to strike.
3. "At the money" is a trader's shorthand; the exact maxima of Γ/Θ/vega
   and the delta-neutral point shift with rates, dividends, and vol.
