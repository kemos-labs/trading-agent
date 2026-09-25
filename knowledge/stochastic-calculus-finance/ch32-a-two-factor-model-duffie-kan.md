# Ch32 — A Two-Factor Model (Duffie & Kan)

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Setup

Two state variables with *affine* drift and *square-root* volatility —
the Duffie-Kan affine term-structure family:

```
X₁ = short rate r(t)
X₂ = yield at time t on a bond maturing at t+τ₀ (a long rate)

dX₁ = (a₁₁X₁ + a₁₂X₂ + b₁) dt + σ₁√(β₁X₁ + β₂X₂ + α) dW₁
dX₂ = (a₂₁X₁ + a₂₂X₂ + b₂) dt + σ₂√(β₁X₁ + β₂X₂ + α) (ρ dW₁ + √(1−ρ²) dW₂)
```

Both factors share the *same* square-root volatility driving term
Y = β₁X₁ + β₂X₂ + α — this shared factor keeps the model affine (rates
are affine functions of the factors; bond yields are affine in X₁, X₂).

## Why two factors

A single factor can't reproduce both the level and the *slope/curvature*
dynamics of the yield curve. Two factors (short rate + long rate, with
correlation ρ) capture:
- parallel shifts (level) and slope steepening/flattening;
- richer term-structure vol and correlation patterns;
- better fit to empirical yield-curve movements (principal components:
  level, slope, then curvature).

## Non-negativity and consistency

The shared Y term makes the model a *generalized* CIR: with the right
parameter constraints, Y ≥ 0 so the volatilities are real and rates stay
non-negative. The model is built so that **bond prices are
exponential-affine in both factors**:

```
B(t, T) = exp( −A₁(t,T)X₁ − A₂(t,T)X₂ + C(t,T) )
```

with the Aᵢ, C solving ODEs (affine/Riccati system) obtained from the
PDE. Yields are affine in the two factors: the "affine term structure"
property in full.

## Practical notes

- Duffie-Kan is the general two-factor affine framework; CIR and
  Vasicek/HW are one-factor special cases (fewer factors, fewer
  parameters).
- Calibration: match the current curve (level) plus the vol/slope
  structure; more parameters = better fit, more overfitting risk —
  validate out-of-sample.
- Hedging: the two factors require two hedging instruments (e.g. two
  bonds or a bond + a swaption) to span the risk — analogous to the
  two-asset completeness condition of ch19.

## Key takeaways

- Duffie-Kan: two factors, affine drifts, shared square-root vol
  (generalized CIR); yields and bond prices affine in the factors.
- Two factors capture level + slope (and more correlation structure) than
  one-factor models — the standard upgrade path.
- Bond prices exponential-affine with ODEs for the coefficients; hedge
  with two instruments.
- It is the bridge from single-factor tractability to realistic
  term-structure dynamics.
