# Ch14 — The Itô Integral

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Why ordinary integration fails

Brownian motion has **infinite first variation** (paths wiggle without
bound) but finite **quadratic variation** [W](T) = T. Riemann-Stieltjes
integrals ∫ f dW can't be defined pathwise because the total variation of W
is infinite. The Itô integral is defined instead in L² (mean-square), using
the quadratic variation as the measure of size.

## Quadratic variation as volatility

For a partition with mesh → 0:

```
[W](T) = lim Σ (W(t_{k+1}) − W(t_k))²  = T  (in probability)
```

For a stock, (ΔS/S)² accumulates to σ²·dt — quadratic variation of the
return process is exactly the accumulated variance, i.e. **realized
volatility**. This is the mathematical content of "volatility."

## Construction

1. **Elementary integrands**: Δ(t) constant on intervals
   [t_k, t_{k+1}), adapted (chosen using only past information — no
   look-ahead). Define I(t) = Σ Δ(t_k)(W(t_{k+1}) − W(t_k)).
2. **Key properties** (elementary case):
   - **Martingale**: E[I(t)|F(s)] = I(s) — Itô integrals of adapted
     integrands are martingales.
   - **Isometry**: E[I(t)²] = E[∫₀ᵗ Δ(u)² du] (Itô isometry) — variance
     of the integral = expected integrated squared integrand.
3. **General integrands**: approximate any adapted, square-integrable Δ by
   elementary processes; take the L² limit. The isometry is what makes the
   limit well-defined.

## Properties of the general integral

- Linearity; the integral of an adapted process is a martingale (with
  mild integrability conditions).
- **Quadratic variation**: [∫₀ᵗ Δ dW](t) = ∫₀ᵗ Δ(u)² du.
- Gaussian case: if Δ is nonrandom, ∫₀ᵗ Δ(u)dW(u) ~ N(0, ∫₀ᵗ Δ(u)² du)
  (a Gaussian process — ch29).
- The integral is evaluated at the **left endpoint** (Δ(t_k) not
  Δ(t_{k+1})): this non-anticipating choice is what makes the integral a
  martingale and is the essence of Itô vs. Stratonovich.

## Practical interpretation

dX = a dt + b dW means X(t) = X(0) + ∫ a ds + ∫ b dW: the "dW" part is a
martingale (the unpredictable shock), the "dt" part is the drift. Hedging
positions are Itô integrals of the delta process against the stock's
Brownian motion — the mathematical core of continuous-time replication.

## Key takeaways

- W has infinite first variation but finite quadratic variation → classical
  integration fails; the Itô integral is an L² limit over adapted,
  left-endpoint-evaluated simple processes.
- Itô integrals are martingales; the Itô isometry E[I²] = E[∫Δ² du] is the
  workhorse (convergence, variance, hedging).
- Quadratic variation of returns = accumulated variance = realized
  volatility — why σ² enters pricing.
- Adaptedness (no look-ahead) is sacred: the hedge Δ(t) must be F(t)-known.
