# Ch3 — Arbitrage Pricing

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## The fundamental example

One-step binomial model: u=2, d=0.5, r=25%, S₀=50. A call with strike 50
pays V₁ = max(S₁−50, 0) = 50 if H, 0 if T. The APT (arbitrage pricing
theory) value is V₀ = 20 — obtained by constructing a portfolio that
replicates the option in every state: sell 3 options, buy 2 shares, borrow
$40. Zero initial outlay, zero terminal payoff in both states. The value
does not depend on the probabilities of H and T.

Assumptions: unlimited short selling, unlimited borrowing at r, no
transaction costs, small investor (no price impact).

## General one-step APT

Let V₁ be F₁-measurable (the payoff depends only on the stock's move — this
measurability is why we can't hedge a derivative with an unrelated asset).
Wealth evolution with Δ₀ shares and the rest in the money market:

```
X₁ = (1+r)V₀ + Δ₀(S₁ − (1+r)S₀)
```

Choose V₀, Δ₀ so X₁ = V₁ in both states — two equations, two unknowns:

```
Δ₀ = (V₁(H) − V₁(T)) / (S₁(H) − S₁(T))    (delta hedge ratio)
V₀ = (1/(1+r)) · [p̃·V₁(H) + q̃·V₁(T)]
```

where p̃ = (1+r−d)/(u−d), q̃ = 1−p̃ are the **risk-neutral probabilities**.
V₀ is the discounted risk-neutral expectation of the payoff — the
**binomial pricing formula**.

## Risk-neutral probability measure

p̃ makes the discounted stock price a martingale:
Ẽ[S₁/(1+r)] = S₀. It is defined purely from u, d, r — no market
probabilities. Pricing = Ẽ[discounted payoff]; hedging = hold Δ₀ shares.

## Completeness

The binomial model is **complete**: every simple European derivative can be
replicated by trading stock + money market, so every derivative has a
unique arbitrage-free price. One risky asset, one source of randomness (the
coin), one derivative price — the number of states matches the number of
assets (stock + bond), making perfect replication possible.

## Key takeaways

- Arbitrage-free price = cost of the replicating portfolio; probabilities
  of the real world are irrelevant.
- Risk-neutral pricing: V₀ = (1+r)^{-1} Ẽ[V₁] with p̃ = (1+r−d)/(u−d).
- Hedging ratio Δ = (V_u − V_d)/(S_u − S_d) — the derivative's "delta."
- A model is complete when every claim is replicable; completeness gives
  unique prices and is the bridge to Black-Scholes in continuous time.
