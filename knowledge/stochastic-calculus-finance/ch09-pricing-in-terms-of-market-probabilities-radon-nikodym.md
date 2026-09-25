# Ch9 — Pricing in Terms of Market Probabilities: The Radon-Nikodym Theorem

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## Radon-Nikodym theorem

Let P and Q be two probability measures on (Ω, F). Q is **absolutely
continuous** w.r.t. P if P(A)=0 ⇒ Q(A)=0. Then there is a non-negative
random variable Z (the **Radon-Nikodym derivative** dQ/dP) with

```
Q(A) = ∫_A Z dP
```

so expectations convert as E_Q[X] = E_P[X·Z]. If also P ≪ Q, the measures
are **equivalent** (same null sets) and Z > 0, with dP/dQ = 1/Z.

## Radon-Nikodym martingales

In the binomial model: let P be market probabilities, Q the risk-neutral
measure. Z(ω) = Q(ω)/P(ω) is the density; the process

```
Z_k = E_P[Z | F_k],   k = 0,...,n
```

is a P-martingale (by the tower property) with E_P[Z_k] = 1. Crucially,
for any F_k-measurable X:

```
E_Q[X] = E_P[X·Z_k]      (Lemma 2.28)
```

— the change of measure can be done at time k using Z_k instead of Z.

## The state price density process

Z_k is also called the state price density (SPD): Z_k(ω) = Q(ω)/P(ω)
restricted to time-k information. Pricing under the market measure:

```
V_k = (1/(1+r)) · E_Q[V_{k+1} | F_k] = (1/(1+r)) · (1/Z_k) · E_P[Z_{k+1}·V_{k+1} | F_k]
```

This expresses the risk-neutral price in terms of the market measure and
the density process — the discrete ancestor of Girsanov's theorem (ch17).
The market-price-of-risk θ appears: Z_{k+1}/Z_k relates to the excess
return of the stock over the bond.

## Stochastic volatility binomial model

If the up/down jump sizes themselves are random (vol is state-dependent),
the market may be **incomplete**: one stock, two (or more) sources of
uncertainty → the risk-neutral measure is not unique, so the derivative
price is not unique. The density process Z_k (choice of Q) parameterizes
the possible prices; each equivalent martingale measure gives a
consistent no-arbitrage price. Completeness ⇔ the EMM is unique.

## Key takeaways

- Change of measure: E_Q[X] = E_P[X·Z]; equivalent measures have the same
  null sets and Z > 0.
- Z_k = E_P[Z|F_k] is a P-martingale; it lets you price at time k under
  the market measure — the discrete Girsanov.
- State price density converts risk-neutral prices into market-measure
  expectations with a density twist.
- Stochastic volatility → incomplete market → non-unique prices: the
  choice of measure (density process) is the extra degree of freedom.
