# Ch2 — Conditional Expectation

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## Information in the binomial model

The filtration F_k = σ(S₁,...,S_k) = σ(Y₁,...,Y_k) encodes what is known
after k tosses. S_k is F_k-measurable (depends only on the first k tosses).
Sets "determined by the first k tosses" form a σ-algebra; being measurable
w.r.t. F_k is exactly "knowable at time k."

## Conditional expectation

E[X | F_k] is the random variable that best predicts X given the
information at time k: it is F_k-measurable and satisfies the **partial
averaging** (tower) property:

```
E[E[X | F_k]] = E[X]
```

Key properties:
- Linearity; takes out what is known: if X is F_k-measurable,
  E[XY | F_k] = X·E[Y | F_k].
- Tower property: for j < k, E[E[X | F_k] | F_j] = E[X | F_j].
- Independence: if X ⊥ F_k then E[X | F_k] = E[X].
- Computed pathwise by averaging the two children in the tree:
  E[X | F_k](ω₁...ω_k) = p̃·X(ω₁...ω_k,H) + q̃·X(ω₁...ω_k,T) under the
  risk-neutral probabilities.

## Martingales

A process M_k is a **martingale** if M_k is F_k-measurable and

```
E[M_{k+1} | F_k] = M_k
```

(and E|M_k| < ∞). "Best guess of the future is the present." Examples in
the binomial model: the discounted stock price S_k/(1+r)^k is a martingale
under the risk-neutral measure; the cumulative sum of independent zero-mean
steps is a martingale.

## Why it matters for finance

- Conditional expectation is the pricing operator: option value at time k =
  discounted conditional expectation of the payoff under the risk-neutral
  measure (shown next chapter).
- Martingale property is the risk-neutral measure's defining feature: the
  discounted price process being a martingale is equivalent to "no
  arbitrage."
- The tower property is what makes dynamic programming/backward induction
  work: value today = discounted expectation of value tomorrow.

## Key takeaways

- Filtration = information flow; measurability = knowability.
- Conditional expectation is the fundamental prediction operator with the
  tower property at its core.
- Martingales are "fair games": conditional expectation of the future equals
  the present.
- Discounted prices are martingales under the risk-neutral measure — this
  single idea drives all pricing.
