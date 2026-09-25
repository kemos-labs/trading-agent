# Chapter 9 — Risk Measurement II (how the Greeks change)

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

Nothing stays constant: every risk measure is itself sensitive to
market conditions. Time and volatility usually push Greeks in the same
direction (both increase the likelihood of large moves) — if unsure
about the time effect, reason about the volatility effect instead.

## Delta behavior

- **Volatility up** → OTM deltas rise, ITM deltas fall, both → 50. ATM
  stays ≈ 50. Lognormality pushes even the at-the-forward call slightly
  above 50 as vol rises. **Time** does the same as volatility; near
  expiry one day can swing the delta dramatically.
- **Implied delta**: use implied vol for Δ. A "delta-neutral" book is
  only neutral at the *guessed* vol — if implied vol rises 32→36%,
  40 calls (Δ25→30) vs. 10 short underlying turns from 0 to +200 deltas
  (bullish) with no trade at all.
- Higher-order: **vanna** = Δ sensitivity to vol (= vega sensitivity to
  underlying, mathematically identical); **charm** = Δ sensitivity to
  time (delta decay). Both ≈ 0 near Δ 50/−50, peak near Δ 20/80 (−20/−80
  puts); vanna falls as vol rises, charm rises as time passes.

## Theta behavior

- Theta is greatest **at the money**; decays toward 0 for deep ITM/OTM
  (little time value). ATM theta ∝ exercise price (X=1,000 call has
  100× the theta of an X=10 call).
- Time shape: early in life decay is similar across moneyness; late in
  life ITM/OTM decay *slows*, ATM decay *accelerates* toward infinity at
  expiry.
- ATM theta ∝ volatility, and vol ∝ √t, so ATM theta ∝ √t:
  `TV_{t−1} ≈ TV_t·√((t−1)/t)`, `theta ≈ TV_t·[1 − √((t−1)/t)]`.
  Example: TV = 2.50 at 30 days → theta ≈ 2.50×(1 − √(29/30)) ≈ 0.042;
  at 29 days the daily decay rises to ≈ 0.043.
- For equal OTM distance under lognormality, the *higher-strike* call
  (OTM call) has more time premium than the lower-strike put → decays
  faster. Vol 0 → theta 0 (ignoring interest); theta falls with vol but
  can hit 0 before vol does.

## Vega behavior

- Vega is greatest **at the money** and ∝ exercise price (X=100 vega =
  2× X=50). Long-term options always have higher vega.
- ATM vega is *constant in volatility* (straight line in
  value-vs-vol); ITM/OTM vegas *rise* with vol as their deltas converge
  to 50.
- Higher-order: **volga/vomma** = vega sensitivity to vol (≈0 ATM, max
  near Δ10/90); **vega decay/DvegaDtime** = vega sensitivity to time
  (biggest for Δ10–90 options, grows as expiry nears).

## Gamma behavior

- Gamma is greatest **at the money**; *inversely* proportional to
  exercise price (X=50 gamma = 2× X=100) because models measure
  percentage moves.
- ATM gamma **rises as time passes or vol declines** — a 100 call at
  97.50 near expiry/low vol can have Δ 25 that jumps to 75 on a 5-point
  move (γ≈10); far from expiry/high vol Δ moves only 45→55 (γ≈2).
- **Gamma options** — ATM, near expiration, low volatility — are among
  the riskiest: Δ ≈ 50 but swings violently toward 0 or 100 on small
  moves.
- Higher-order: **speed** = gamma sensitivity to underlying (max at
  Δ15/85; ≈0 ATM); **color** = gamma sensitivity to time; **zomma** =
  gamma sensitivity to vol (both ≈0 at Δ15/85, large positive near
  Δ5/95).

## Lambda (Λ) — percentage elasticity

`Λ = Δ × (S / TV)` — percent change in option per percent change in
underlying (leverage). Example: TV = 4.00, Δ = 20, S = 100 → 0.20 ×
100/4.00 = **5** (underlying +1% → option +5%).
- Calls positive, puts negative; greatest for **OTM** options; falls as
  vol or time rises. Max leverage = OTM, near-expiry, low vol — at the
  cost of liquidity and gamma risk.

## Key takeaways

1. Gamma, theta, vega are all maximal **at the money**; that's why ATM
   options dominate volume.
2. Two rules of thumb: time ≡ volatility for delta/theta effects; ATM
   theta ∝ X and ∝ √t, ATM vega ∝ X, ATM gamma ∝ 1/X.
3. Implied-vol-based ("implied") Greeks keep a hedged book honest — a
   static hedge is only neutral at the volatility you guessed.
4. Higher-order Greeks (vanna, charm, volga, speed, color, zomma) matter
   for large books; second-order sensitivities of Δ, third-order of Γ.
