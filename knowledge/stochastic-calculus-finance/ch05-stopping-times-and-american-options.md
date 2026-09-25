# Ch5 — Stopping Times and American Options

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## European recap (Markov case)

If payoff V_n = g(S_n), backward induction gives v_k(x) =
(p̃v_{k+1}(ux) + q̃v_{k+1}(dx))/(1+r), with hedge Δ_k =
(v_{k+1}(uS_k) − v_{k+1}(dS_k))/((u−d)S_k).

## American options

The holder may exercise at any time k ≤ n, receiving g(S_k). The hedge
must maintain wealth X_k ≥ g(S_k) at all times (the seller must always be
able to cover early exercise).

**American algorithm** (backward induction with the max):

```
v_n(x) = g(x)
v_k(x) = max( (p̃v_{k+1}(ux) + q̃v_{k+1}(dx))/(1+r),  g(x) )
```

i.e. value = max(continuation value, exercise value). Worked example
(American put, S₀=4, u=2, d=½, r=¼, K=5): v₂(16)=0, v₂(4)=1, v₂(1)=4;
v₁(8)=max(0.40, 0)=0.40, v₁(2)=max(2, 3)=3 (exercise!); v₀(4)=max(1.36, 1)
= 1.36. The hedge must hold Δ so that X₁(H) = v₁(8) and X₁(T) = v₁(2).

## Stopping times

A **stopping time** τ is a random time whose occurrence is decidable with
current information: {τ ≤ k} ∈ F_k for all k ("you know when you're
stopped"). The American option value is a supremum over stopping times:

```
V_k = max_{τ ≥ k} (1+r)^k Ẽ[(1+r)^{-τ} G_τ | F_k]
```

the optimal exercise time is τ* = min{k : V_k = G_k} (exercise exactly
when value equals payoff), and τ* is an optimal stopping time.

## Information up to a stopping time

The σ-algebra F_τ of events up to the stopping time: A ∈ F_τ iff A ∩ {τ ≤ k}
∈ F_k for all k. If X is adapted, X_τ is F_τ-measurable. This machinery
(optional stopping) is used to prove optimal exercise properties.

## Key takeaways

- American price = backward induction with v_k = max(continuation,
  exercise); the max term is the only change from European.
- The value is the best you can do over all stopping times — optimal
  exercise is τ* = first time value hits the payoff.
- Stopping times are decision rules based on observable information only
  (no look-ahead); they are the formal tool for American claims.
- American value ≥ European value (the max adds optionality); the gap is
  the early-exercise premium.
