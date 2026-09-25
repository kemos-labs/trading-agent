# Ch23 — Recognizing a Brownian Motion

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Lévy's theorem

A process W (on (Ω, F, P), adapted to F(t)) is Brownian motion if:

1. its paths are **continuous**,
2. it is a **martingale**,
3. its **quadratic variation** satisfies [W](t) = t
   (informally, dW·dW = dt).

That's it — three local conditions. The proof shows the conditional
characteristic function matches the normal: with E[e^{iu(W(t)−W(s))}|F(s)]
= e^{−u²(t−s)/2}, the increment is normal, mean 0, variance t−s, and
independence follows from the martingale property.

## Why this is the practical tool

In finance we rarely start from a "given" Brownian motion; we end up with
*processes we suspect are Brownian* — e.g. after Girsanov changes of
measure, or after de-trending. Lévy's theorem lets you **identify** a
process as Brownian motion from checkable local properties:

- **Girsanov output**: under Q, W̃(t) = W(t) + ∫θ du has continuous paths,
  is a Q-martingale, and has quadratic variation [W̃] = [W] = t (measure
  change doesn't alter quadratic variation). Lévy ⇒ W̃ is a Q-Brownian
  motion — a slicker proof of Girsanov's result.
- **Change of clock**: a continuous local martingale M with [M](t) = t is
  a Brownian motion (and general [M] = A(t) ⇒ M is Brownian motion with a
  time change — Dubins-Schwarz).

## Consequences

- Quadratic variation is the invariant that measure changes respect: every
  equivalent martingale measure preserves [W] = t, so the "noise content"
  of the market is the same under P and Q. Only drifts change.
- The theorem underlies model building: to check a candidate model is a
  legitimate Brownian-motion world, verify continuity + martingale +
  quadratic variation.

## Key takeaways

- Lévy: continuous + martingale + [W](t) = t ⇒ Brownian motion.
- Measure changes preserve quadratic variation → Girsanov's drifted process
  is still Brownian; vol is invariant under measure changes.
- Practical use: identify Brownian motions from local properties, build
  and verify models, and prove that "drift removal" leaves a valid BM.
