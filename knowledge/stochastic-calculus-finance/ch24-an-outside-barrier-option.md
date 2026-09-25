# Ch24 — An Outside Barrier Option

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## The payoff

An **outside (cross-asset) barrier option**: pays like a call on stock S,
but knocks out if *another* process Y (a different asset/rate) crosses a
barrier. Setup:

- Barrier process: dY/Y = λ dt + σ₁ dB₁
- Stock: dS/S = μ dt + ρσ₂ dB₁ + √(1−ρ²)σ₂ dB₂
- Payoff at T: (S(T) − K)⁺ · 1{Y*(T) < L}, with Y*(T) = max_{0≤t≤T} Y(t),
  0 < S(0) < K, 0 < Y(0) < L

The two Brownian motions B₁, B₂ are independent; ρ is the correlation
between the stock's and the barrier's shocks.

## Why two assets are needed

The payoff depends on both Y (for the barrier) and S (for the call). To
hedge it we need the money market **plus two risky assets** — here Y and S
(two traded assets for two Brownian shocks ⇒ the market is complete).

## Risk-neutral measure

Girsanov on both Brownian motions: choose θ₁, θ₂ so that discounted Y and
discounted S are martingales:

```
λ = r + σ₁θ₁
μ = r + ρσ₂θ₁ + √(1−ρ²)σ₂θ₂
```

Two equations determine θ₁, θ₂ uniquely ⇒ **unique** risk-neutral measure
Q (completeness). Under Q:

```
dY/Y = r dt + σ₁ dB̃₁,   dS/S = r dt + ρσ₂ dB̃₁ + √(1−ρ²)σ₂ dB̃₂
```

Both assets earn the risk-free rate; the cross-variation
dY·dS/(YS) = ρσ₁σ₂ dt is preserved (measure changes don't touch
quadratic/cross variation).

## Pricing

V(t) = E_Q[e^{−r(T−t)}·(S(T)−K)⁺·1{max Y ≤ L} | F(t)]. The barrier
probability is computed with the reflection principle on the *correlated*
pair (the joint law of Y's max and S's terminal value under correlation
ρ), giving a closed form in terms of bivariate normals. Key structure: the
answer factors into a "call on S" × "knockout survival of Y," tangled by
the correlation ρ (when ρ ≠ 0, survival and payoff are dependent).

## Trading takeaways

- Outside barriers embed **correlation risk**: the option's value swings
  with ρ even when S and Y are each fairly priced — an extra Greek
  (correlation delta) appears.
- Hedging requires both underlyings; residual risk lives where model
  correlation meets realized correlation (the same lesson as multi-asset
  options in Dynamic Hedging ch22).
- Model choice (vols and ρ) matters more than for single-asset barriers.

## Key takeaways

- Outside barrier = payoff on S knocked out by Y's maximum: two assets,
  two Brownian motions, complete market, unique Q.
- Risk-neutral drifts for both assets = r; market price of risk pinned by
  the MPR equations.
- Price = Q-expectation; closed form via reflection on the correlated pair
  (bivariate normal).
- Correlation ρ is a live risk dimension — hedge both assets, watch ρ.
