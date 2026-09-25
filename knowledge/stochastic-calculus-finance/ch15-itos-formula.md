# Ch15 — Itô's Formula

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Statement (one-dimensional)

For a C² function f and Brownian motion W:

**Differential form** (the working version):

```
df(W(t)) = f'(W(t)) dW(t) + ½ f''(W(t)) dt
```

**Integral form** (the rigorous version):

```
f(W(t)) − f(W(0)) = ∫₀ᵗ f'(W(u)) dW(u) + ½ ∫₀ᵗ f''(W(u)) du
```

The ½f''dt term is the **Itô correction**: it appears because W has
quadratic variation dt (second-order terms in the Taylor expansion don't
vanish — (dW)² = dt). Heuristic multiplication table:

```
(dW)² = dt,  dW·dt = 0,  (dt)² = 0
```

## Derivation sketch

Taylor-expand f across partition points: f(x_{k+1}) − f(x_k) ≈ f'(x_k)Δx +
½f''(x_k)(Δx)². Sum: the first terms → Itô integral; the second terms →
Σ ½f''(W)(ΔW)² → ½∫f''du because (ΔW)² → dt. For quadratics the Taylor
expansion is exact; in general the error vanishes in the limit.

## Geometric Brownian motion

The flagship application: S(t) = S₀·exp(σW(t) + (μ − σ²/2)t). Its SDE:

```
dS = μS dt + σS dW
```

Verify by Itô on f(x) = S₀·e^{σx + (μ−σ²/2)t}: the σ²/2 in the exponent is
exactly the Itô correction that makes the drift μ. Key results:
- Quadratic variation of returns: [dS/S]² = σ² dt; σ is the **volatility**.
- log S is a drifted Brownian motion: d(log S) = (μ − σ²/2)dt + σ dW —
  log-returns are normal; levels are lognormal.

## Black-Scholes (first derivation)

dS = rS dt + σS dW under the risk-neutral measure. Consider a claim V =
v(t, S) and its self-financing hedge (Δ shares + cash). Itô on v(t, S)
gives dv; matching the dW term to the hedge (Δ = v_s, the delta) and
requiring no arbitrage (drift = r·v) yields the **Black-Scholes PDE**:

```
v_t + r·S·v_s + ½σ²S²·v_ss = r·v
```

with the terminal condition v(T, S) = payoff. This is the pricing engine:
solve the PDE (or take the risk-neutral expectation).

## Multi-dimensional Itô formula

For correlated Brownian motions (dW_i·dW_j = ρ_ij dt) and functions of
several processes, the correction becomes ½ Σ v_{x_i x_j} dX_i dX_j with
the cross-variations dX_i dX_j = σ_iσ_jρ_ij dt — needed for multi-asset
pricing and for interest-rate models.

## Key takeaways

- Itô: df = f'dW + ½f''dt — the extra ½f''dt is the quadratic-variation
  correction; (dW)² = dt.
- GBM: dS = μSdt + σSdW ⇔ log S ~ N((μ−σ²/2)t, σ²t): the σ²/2 drift
  correction is ubiquitous (also the r−σ²/2 in risk-neutral pricing).
- Itô + delta-hedging ⇒ Black-Scholes PDE v_t + rSv_s + ½σ²S²v_ss = rv.
- Multi-dim version with cross-variation terms handles correlated assets.
