# Ch4 — The Markov Property

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## Pricing and hedging in the multi-period binomial model

Value process (backward induction under risk-neutral measure):

```
V_k = (1/(1+r)) · Ẽ[V_{k+1} | F_k],   k = 0,...,m−1
```

Hedge ratio:

```
Δ_k = (V_{k+1}(...H) − V_{k+1}(...T)) / (S_{k+1}(...H) − S_{k+1}(...T))
```

If the payoff is a function of the *current* stock price only (V_m = g(S_m)),
then V_k is a function of S_k only — the value at time k depends on the
history only through the current stock price. This is the Markov property
in the binomial setting and it makes backward induction computationally
tractable: v_k(x) = (p̃ v_{k+1}(ux) + q̃ v_{k+1}(dx))/(1+r).

## Markov processes

A process is Markov if the conditional distribution of the future given all
past information depends only on the present:

```
E[h(X_{k+1}) | F_k] = E[h(X_{k+1}) | X_k] = g(X_k)
```

for some function g. Equivalent formulations: the future is conditionally
independent of the past given the present.

## When the payoff is path-dependent

If the payoff depends on the path (e.g. a **lookback option**
V₂ = max_{0≤k≤2}(S_k − 5)⁺), the value is no longer a function of S_k alone
— it needs an extra state variable (the running max) or the full node in
the tree. Pricing still works (backward induction on the tree), but the
state space grows. The worked lookback example: S₀=4, u=2, d=0.5, r=25%
gives V₀ = 2.24 with hedge ratios Δ₀ = 0.93, Δ₁(H) = 0.67, Δ₁(T) = 0.

## Why Markov matters

- Markov property is what lets us price with a *function* of the state
  (v_k(x)) instead of tracking the whole history — the basis of PDE pricing
  (Feynman-Kac) and of dynamic programming.
- Path-dependent options break it; they require extra state variables or
  Monte Carlo. This is the same distinction that reappears in continuous
  time (Greeks/PDEs work cleanly only for Markov payoffs).
- Checking whether a process is Markov (independence lemma: if Y ⊥ F then
  E[h(Y+g(X))|F] = g̃(X)) is a standard technique used throughout the book.

## Key takeaways

- Value = discounted risk-neutral expectation, computed backward;
  Δ_k = ratio of value differences to price differences.
- Markov property: future depends on the present only → pricing functions
  v_k(x), PDEs, dynamic programming.
- Path-dependent payoffs (lookbacks, barriers) need extra state — the
  first sign of the complexity exotic options add.
