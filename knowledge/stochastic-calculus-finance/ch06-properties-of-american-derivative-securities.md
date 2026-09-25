# Ch6 — Properties of American Derivative Securities

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## Setup

An American derivative security is a sequence of non-negative random
variables G_k, each F_k-measurable: exercise at any time k and receive G_k.
The structure mirrors ch5 but stated generally.

## The main properties

(a) **Value** is the supremum over stopping times:

```
V_k = max_{τ ≥ k} (1+r)^k Ẽ[(1+r)^{-τ} G_τ | F_k]
```

(b) The **discounted value process** (1+r)^{-k} V_k is the *smallest
supermartingale* dominating the payoff G_k (a supermartingale drifts down:
E[Y_{k+1}|F_k] ≤ Y_k). It is the "least expensive way to dominate the
claim" — the seller's minimal cost.

(c) A stopping time τ is **optimal** iff V_0 = Ẽ[(1+r)^{-τ} G_τ]; in
particular τ* = min{k : V_k = G_k} is optimal — exercise as soon as value
equals payoff.

(d) The **hedging portfolio** (same delta formula as European):
Δ_k = (V_{k+1}(...H) − V_{k+1}(...T))/(S_{k+1}(...H) − S_{k+1}(...T)).

(e) If V_k = G_k at some (k, ω), the owner *should* exercise: if he
doesn't, the seller can consume the difference and still maintain the
hedge (arbitrage for the seller). Intuitively: at the exercise boundary,
holding the claim has no advantage over the cash payoff.

## Why supermartingale

Once discounted, an American claim's value can only go down in expectation
(you're either collecting the payoff or waiting, and waiting has no
positive drift under the risk-neutral measure). The smallest supermartingale
dominating the payoff is the fair price — this is the same idea as the
Snell envelope in optimal stopping theory.

## Compound European derivative securities

A claim that lets you pay to extend: e.g. an option on an option
(compound option). These are priced by the same backward-induction
machinery — value at exercise decision dates is max(exercise value,
continuation value) with the continuation being another claim.

## Optimal exercise intuition

- Optimal exercise time: first time the continuation value no longer beats
  the payoff.
- The early-exercise boundary is where V_k = G_k; inside the exercise
  region, the American option is "just the payoff" and delta-hedging
  reduces to holding the underlying.

## Key takeaways

- American value = smallest supermartingale dominating the payoff
  (Snell envelope); equivalently sup over stopping times.
- Exercise exactly when value = payoff; failing to exercise lets the
  seller extract free money.
- The machinery (stopping times, supermartingales, delta formula)
  generalizes the European case with one max.
