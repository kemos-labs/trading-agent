# Ch29 — Gaussian Processes

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Definition

X(t) is a **Gaussian process** if every finite set of its values
(X(t₁),...,X(t_n)) is jointly normally distributed. Its distribution is
completely determined by:

- the mean function m(t) = E[X(t)], and
- the covariance function c(s,t) = Cov(X(s), X(t)).

Joint density (n-variate normal):

```
f(x) = (2π)^{-n/2} (det Σ)^{-1/2} exp( −½(x−m)ᵀ Σ⁻¹ (x−m) )
```

with moment generating function
E[exp(uᵀX)] = exp(uᵀm + ½uᵀΣu).

## Brownian motion is Gaussian

W(t) is Gaussian with m(t) = 0 and c(s,t) = min(s,t) — check via the
increment decomposition Cov(W(s),W(t)) = E[W(s)²] = s for s ≤ t. Any
Itô integral of a **nonrandom** integrand is Gaussian:

```
X(t) = ∫₀ᵗ Γ(u) dW(u)  ⇒  m(t) = 0,  c(s,t) = ∫₀^{s∧t} Γ(u)² du
```

(Itô isometry gives the covariance; the integral of a normal
martingale-generating process is Gaussian). Note: if Γ is random, the
integral is a martingale but generally NOT Gaussian.

## Why Gaussian processes matter in finance

- **Short-rate models** (Hull-White, ch30; Vasicek) are Gaussian: rates
  are jointly normal, so the integral of the short rate is Gaussian and
  **bond prices are exponential-affine** — closed-form yields and option
  prices.
- **Gaussian HJM / forward-rate models**: Gaussian forward rates lead to
  lognormal-free bond prices with explicit formulas.
- **Risk**: Gaussian assumptions understate tail risk (fat tails in
  markets); used for tractability, not fidelity. The normal distribution
  of log-returns in the BS model is the same assumption.

## Practical use

- To prove a process is Gaussian: show the mgf has the exponential-quadratic
  form (or check joint normality of linear combinations).
- Covariance functions (like min(s,t) or ∫Γ²) are the modeling input —
  they encode dependence structure across time, the key to term-structure
  and multi-period models.
- When simulating, draw from the multivariate normal N(m, Σ) — the
  Cholesky-based correlated-simulation skill applies directly.

## Key takeaways

- Gaussian process ⇔ all finite-dimensional distributions are joint
  normal; fully specified by mean and covariance functions.
- Brownian motion and nonrandom-integrand Itô integrals are Gaussian
  (covariance = ∫Γ²du).
- Gaussian short-rate/forward models ⇒ exponential-affine bond prices and
  analytic tractability — the workhorse of classical rate modeling.
- Watch the tail gap: Gaussian ≠ fat-tailed markets; use for
  tractability, validate the risk.
