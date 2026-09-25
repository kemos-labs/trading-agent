# Ch20 — Pricing Exotic Options

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Reflection principle for Brownian motion

Let M(T) = max_{0≤t≤T} W(t). The reflection principle (same idea as the
discrete random walk, ch8) gives the joint law of the running maximum and
the terminal value:

```
P(M(T) ≥ m, W(T) ≤ b) = P(W(T) ≥ 2m − b)      (m > 0, b < m)
```

Derivation: reflect the path after first hitting m; the reflected path
ends at 2m − b. Since the hitting time and the reflected path are
independent-ish, the two probabilities are equal. Concretely:

```
P(M(T) ≥ m) = 2·P(W(T) ≥ m) = 2·(1 − Φ(m/√T))
```

so the max of Brownian motion has the same tail as the terminal value times
2. The joint density and the **first-passage-time density** follow by
differentiating:

```
P(τ_m ∈ dt) = (m/√(2π t³))·exp(−m²/2t) dt      (inverse Gaussian)
```

## Pricing barrier-style claims

The reflection principle converts "stay below a barrier" probabilities into
ordinary normal probabilities — the key to closed-form prices for:
- **Up-and-out / down-and-out barrier options**: knockout probability =
  P(some path hits the barrier) computed via reflection (a "mirrored"
  probability).
- **Lookback-style payoffs** (max/min of the path) and their distributions.
- The same technique appears in ch25 (American puts) and ch24 (outside
  barriers with two processes).

## Joint maximum/terminal density (key formula)

For m > 0, b < m:

```
P(M(T) ∈ dm, W(T) ∈ db) = (2(2m−b)/√(2π T³))·exp(−(2m−b)²/2T) dm db
```

This single density prices many path-dependent claims: any payoff function
of (M(T), W(T)) integrates against it.

## Trading implications

- Exotics that depend on the *path* (barriers, lookbacks, Asians) are not
  priced by terminal distribution alone — they need joint laws like the
  reflection-principle density.
- Closed forms exist for the classic barriers because of reflection;
  otherwise price by PDE or Monte Carlo.
- Barrier risk (pin risk, gap risk near the barrier) is where model
  assumptions hurt the most — the market for these options embeds these
  probabilities, and hedging near the barrier is discontinuous.

## Key takeaways

- Reflection principle: P(M(T) ≥ m, W(T) ≤ b) = P(W(T) ≥ 2m − b);
  first-passage time is inverse-Gaussian.
- P(M(T) ≥ m) = 2P(W(T) ≥ m): the max tail is twice the terminal tail.
- Joint (M, W) density prices barrier/lookback-style claims in closed form.
- Path-dependence ⇒ joint laws; reflection is the master trick for
  barrier-type payoffs.
