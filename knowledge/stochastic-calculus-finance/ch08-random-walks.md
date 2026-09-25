# Ch8 — Random Walks

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## Setup

Symmetric random walk M_k = Σ_{j=1}^k X_j with X_j = ±1 (fair coin). The
walk is a martingale; scaled by √k it converges to Brownian motion (CLT) —
this chapter works out the hitting-time machinery on the discrete walk that
carries over to Brownian motion.

## First passage time

τ = min{k : M_k = x}, the first time the walk hits level x. Results:

- **Almost surely finite**: τ < ∞ a.s. (the walk will hit any level —
  recurrence of the 1-D random walk).
- **Moment generating function**: E[α^τ] computed by conditioning on the
  first step; solving a functional equation gives the mgf, and from it
  E[τ] = ∞? No — for the symmetric walk hitting +1, E[τ] = ∞ despite
  P(τ < ∞) = 1 (heavy tail: it almost surely hits, but the expected waiting
  time is infinite).
- **Distribution**: P(τ = 2k+1) relates to the Catalan-like reflection
  count; the reflection principle gives the joint law.

## Reflection principle

Counts paths by symmetry: the number of paths from 0 to a > x that touch x
equals the number of paths from 0 to 2x−a (reflect the path after first
hitting x). This gives P(τ_x ≤ n) and the distribution of the maximum
M_n = max_{k≤n} M_k:

```
P(M_n < x, M_n > ...)  via reflection; P(M_n ≥ x) = 2·P(M_n ≥ x) ...
```

Concretely: P(max ≤ m) and hitting probabilities reduce to counting
"reflected" paths — the same trick used later for Brownian motion and
barrier options (ch20, ch24).

## Perpetual American put (worked application)

An American put with no expiration: exercise when price hits L (or lower),
receive K − S. Using the first-passage distribution:

```
v_L(x) = (K−L)·E[e^{-r·τ_L}]   for x > L;  (K−x)⁺ for x ≤ L
```

The value function is maximized over the exercise level L — optimizing the
stopping level trades immediate exercise value (K−L) against the expected
waiting time (discounting). This is the discrete precursor of the
continuous-time perpetual put (ch25): solve for the optimal L via a
difference equation for the mgf.

## Difference equation

The mgf/expectation of the hitting time solves a linear difference
equation (discrete harmonic function), the ancestor of the ODE solved by
the continuous hitting-time problem.

## Key takeaways

- 1-D symmetric walk is recurrent: every level is hit a.s., but the
  expected first-passage time is infinite.
- The reflection principle turns path-counting into closed forms — the key
  tool for hitting/maximum distributions.
- Perpetual American put: value = max over exercise levels of
  (K−L)·discounted hitting probability — the optimal boundary problem in
  miniature.
- All of this transfers to Brownian motion in Part II.
