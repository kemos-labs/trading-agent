# Binomial Tree Option Pricing

## name
Binomial tree (CRR) pricing and hedging: risk-neutral backward induction
for European/American options with delta extraction.

## description
Price European and American options by building a binomial tree of stock
prices (u, d from volatility and time step), then discounting the payoff
backward under the risk-neutral probabilities. American early exercise is
handled with a max(continuation, exercise) at every node; the hedge ratio
(delta) comes from value differences over price differences. Simple,
transparent, and the conceptual foundation of risk-neutral pricing.

## when to use it
- You need a fast, dependency-light reference price for European/American
  calls and puts (vanilla options) to sanity-check Black-Scholes or
  market quotes.
- You need an *intuitive* check on how a price behaves (Greeks, early
  exercise, dividends, volatility) without PDE or Monte Carlo machinery.
- You are teaching/auditing the risk-neutral principle: the tree is the
  discrete proof that price = E_Q[discounted payoff] and delta = hedge.
- Whenever you want a self-contained pricing oracle that is easy to read
  and verify (better for audits than a black-box BS library).

## the method

### 1. Tree parameters (Cox-Ross-Rubinstein)
Given volatility σ, time step Δt = T/N, risk-free rate r, dividend yield q:

```
u = exp(σ·√Δt)
d = 1/u
p̃ = (exp((r−q)·Δt) − d) / (u − d)     # risk-neutral up probability
q̃ = 1 − p̃
```

No-arbitrage requires d < e^{(r−q)Δt} < u (else the tree is degenerate).
Stock prices at node (k, j) [k steps, j up-moves]: S = S₀·u^j·d^{k−j}.

### 2. Payoffs at maturity (k = N)
```
call: max(S − K, 0)      put: max(K − S, 0)
```

### 3. Backward induction
For k = N−1 ... 0, at each node:

```
continuation = exp(−r·Δt) · (p̃·V_up + q̃·V_down)
European:    V = continuation
American:    V = max(continuation, intrinsic)     # early exercise
```

The option value at the root node is the price V₀.

### 4. Delta (hedge ratio)
At any node: Δ = (V_up − V_down) / (S_up − S_down). This is the number of
shares to hold per option for a locally risk-free hedge — the tree's
discrete answer to the Black-Scholes delta.

## example (vectorized numpy)
```python
import numpy as np

def binomial_price(S0, K, T, r, sigma, N=100, q=0.0, american=False, is_call=True):
    dt = T / N
    u = np.exp(sigma * np.sqrt(dt)); d = 1.0 / u
    pu = (np.exp((r - q) * dt) - d) / (u - d)      # risk-neutral prob
    disc = np.exp(-r * dt)
    # terminal prices on a binomial lattice (vectorized)
    j = np.arange(N + 1)
    S = S0 * u**j * d**(N - j)
    V = np.maximum(S - K, 0) if is_call else np.maximum(K - S, 0)
    for _ in range(N):
        V = disc * (pu * V[1:] + (1 - pu) * V[:-1])
        if american:
            j = np.arange(len(V))
            S = S0 * u**j * d**(len(V) - 1 - j)
            intrinsic = np.maximum(S - K, 0) if is_call else np.maximum(K - S, 0)
            V = np.maximum(V, intrinsic)
    return V[0]
```

Convergence check: N = 100–1000 gives BS-consistent prices for vanillas
(the tree converges to Black-Scholes as N → ∞; European results match
Black-Scholes to ~1–2 cents at N = 500 for typical parameters).

## known pitfalls
- **Degenerate probabilities**: if e^{(r−q)Δt} is outside [d, u], p̃ is
  not in [0,1] and prices are meaningless — check the no-arbitrage
  condition first.
- **N too small**: coarse trees misprice (early-exercise boundary
  resolution, convergence oscillation). Use N ≥ 100; report N.
- **American puts need the max at EVERY node**, not just at maturity —
  forgetting early exercise returns the European price (an easy silent
  bug).
- **Dividends**: use continuous q in the drift; discrete dividends require
  adjusting the tree (subtract PV of dividends from spot or branch the
  tree) — don't ignore them for high-yield underlyings.
- **Not for path-dependent payoffs**: lookbacks, Asians, and barriers
  need extra state variables (augmented trees) or Monte Carlo — the plain
  tree only prices payoffs that are functions of the terminal price.
- **Numerical stability**: use d = 1/u (CRR) to keep the tree
  recombining; otherwise node counts explode.

## source
Shreve, *Stochastic Calculus and Finance* (1997 notes), ch1–5 (binomial
asset pricing model: risk-neutral probabilities, backward induction,
American early exercise, delta hedging) — the CRR tree in its rigorous
form.
