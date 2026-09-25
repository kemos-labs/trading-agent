# Ch18 — Martingale Representation Theorem

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Statement

Let W be Brownian motion, F(t) its generated filtration. If X(t) is a
martingale adapted to F (i.e. the Brownian motion is the *only* source of
randomness), then there is an adapted process Γ(t) such that

```
X(t) = X(0) + ∫₀ᵗ Γ(u) dW(u)
```

**Every martingale in this filtration is an Itô integral against W.** The
converse is already known: any Itô integral of an adapted process is a
martingale. So martingales ⇔ Itô integrals, when the filtration is
Brownian-generated.

## Why it matters: hedging

In the Girsanov setting (ch17), suppose a claim's discounted value
Y(t) = E_Q[e^{−rT}V_T | F(t)] is a Q-martingale. The representation theorem
gives Γ with dY = Γ dW̃. Since the discounted stock also satisfies
d(S/β) = σ(S/β) dW̃, we can choose the hedge Δ = Γ/σ(S/β) so that the
replicating portfolio's discounted value matches Y exactly. **The
representation theorem is what guarantees a perfect hedge exists** — it is
the continuous-time completeness theorem.

## Hedging application (worked structure)

1. Value the claim: V(t) = E_Q[discounted payoff | F(t)].
2. By MRT, its discounted value process is an Itô integral against W̃.
3. Read off the hedge ratio: Δ(t) = (vol of claim's value)/(vol of stock
   per share) — delta = ratio of quadratic variations.
4. The portfolio (Δ shares + money market) replicates the claim a.s.;
   no-arbitrage price = initial portfolio value.

Completeness: every contingent claim is attainable because every
Q-martingale is a W̃-integral and the stock "spans" W̃ (same Brownian
motion). One stock + one Brownian motion = complete market.

## Key takeaways

- MRT: in a Brownian filtration, every martingale is an Itô integral
  against the Brownian motion.
- It is the theoretical basis of delta-hedging: the claim's value process
  is representable, and the representation gives the hedge.
- Completeness ⇔ every claim attainable ⇔ the market's risk factor is
  exactly the traded asset's risk factor (same W).
- Without it (incomplete markets, e.g. stochastic vol), perfect
  replication fails and prices are not unique.
