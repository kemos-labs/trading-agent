# Ch11 — General Random Variables

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## From discrete to general

So far random variables have been discrete (coin-toss space). Now X:
(Ω, F, P) → ℝ general: X is a random variable iff X^{-1}(B) ∈ F for every
Borel B (pre-images of Borel sets are measurable).

## Law and distribution

X induces a measure μ_X on (ℝ, B(ℝ)) — its **law**:

```
μ_X(B) = P(X^{-1}(B)) = P(X ∈ B)
```

Two random variables can have the same law but be different (different
payoffs, same distribution — as with the call/put example in ch1).
Densities: when they exist, μ_X(B) = ∫_B f_X(x) dx, so dμ_X = f_X dx; the
distribution function F_X(x) = P(X ≤ x) is the CDF. Expectations:
E[X] = ∫ x dμ_X(x), computed as a sum (discrete), a Lebesgue integral
(continuous density), or more generally a Stieltjes/Lebesgue-Stieltjes
integral.

## Lebesgue integral essentials

- Defined by monotone convergence: first simple functions, then
  non-negative functions, then general integrable functions.
- Lebesgue vs. Riemann: integrates w.r.t. a measure, so it handles
  discontinuous limits and exchange of limits/integrals (dominated
  convergence, monotone convergence) far more cleanly — the reason
  stochastic calculus (which needs limits everywhere) is built on it.
- The integral is linear; |∫ f dμ| ≤ ∫|f| dμ; E[X] exists if E|X| < ∞
  (integrable) — square-integrable (L²) and integrable (L¹) spaces are
  used throughout.

## Why the setup matters

- Conditional expectation E[X | G] is rigorously defined as the (a.s.
  unique) G-measurable Y with ∫_A X dP = ∫_A Y dP for all A ∈ G — an
  existence statement via the Radon-Nikodym theorem, which needs the
  general integral machinery.
- Brownian motion and Itô integrals (Part II) are built on L² limits of
  simple functions — precisely the Lebesgue-style construction.

## Key takeaways

- Random variable = measurable function; law = push-forward measure.
- Densities/CDFs characterize laws; expectations are Lebesgue integrals.
- Lebesgue integration (via simple functions and limit theorems) is the
  rigorous backbone for conditional expectation and stochastic calculus.
- Distributions are relative to the measure: the same payoff has different
  laws under P vs. Q (market vs. risk-neutral) — the recurring theme.
