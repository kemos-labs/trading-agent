# Ch22 — Summary of Arbitrage Pricing Theory

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## The two-period binomial recap (pricing formulas)

Portfolio evolution: X_{k+1} = Δ_k·S_{k+1} + (1+r)(X_k − Δ_k S_k).
Given a European payoff V₂(ω₁,ω₂), the self-financing replicating
portfolio (4 unknowns X₀, Δ₀, Δ₁(H), Δ₁(T)) solves 4 equations. Solution:

```
X₁(ω₁) = (1/(1+r)) [ (1+r−d)/(u−d)·V₂(ω₁,H) + (u−1−r)/(u−d)·V₂(ω₁,T) ]
X₀      = (1/(1+r)) [ p̃·X₁(H) + q̃·X₁(T) ]
Δ₁(ω₁)  = (V₂(ω₁,H) − V₂(ω₁,T)) / (S₂(ω₁,H) − S₂(ω₁,T))
Δ₀      = (X₁(H) − X₁(T)) / (S₁(H) − S₁(T))
```

with p̃ = (1+r−d)/(u−d), q̃ = 1−p̃. **Probabilities of the paths are
irrelevant**: the hedge works on every path; all that matters is that the
model's tree includes all possibilities (the paths must span the states).

## The invariance principle

Pricing formulas depend on u, d, r only through:
- the risk-neutral probabilities p̃, q̃ (from the no-arbitrage condition),
  and
- the **quadratic variation** of log S: (log S_{k+1} − log S_k)² = (log u)²,
  accumulating at rate σ² = (log u)² per unit time.

Changing u changes σ and changes prices — the single relevant "market"
quantity is volatility. This is the discrete-form lesson that carries to
continuous time: **option prices depend on volatility, not drift**.

## Continuous-time analog

The same structure survives the limit:
- discounted wealth is a martingale; delta hedges the claim;
- the drift (μ) vanishes; only σ remains in the PDE;
- the "all paths included" condition becomes the completeness/Martingale
  representation story (ch18).

## The state-price deflator view

Discounted wealth differences:

```
X_{k+1}/β_{k+1} − X_k/β_k = Δ_k·(S_{k+1}/β_{k+1} − S_k/β_k)
```

Under Q, S/β is a martingale, so X/β is a Q-martingale; prices are
Q-expectations of discounted payoffs. The entire theory in one line:
**no arbitrage ⇔ an equivalent measure under which discounted prices are
martingales; price = that expectation; hedge = the martingale
representation.**

## Key takeaways

- Binomial pricing/hedging formulas: X from backward induction under p̃,q̃;
  Δ = value-difference over price-difference.
- Prices depend on u,d,r only through risk-neutral probabilities and
  quadratic variation σ² — never on real-world probabilities or drift.
- The complete-market recipe (discrete and continuous):
  martingale measure → price = E_Q[discounted payoff] → hedge via
  representation.
