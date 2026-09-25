# Ch31 — Cox-Ingersoll-Ross (CIR) Model

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Motivation

Hull-White/Vasicek are Gaussian ⇒ **negative interest rates have positive
probability**. CIR is the simplest short-rate model that keeps r ≥ 0: the
volatility is proportional to √r, so it vanishes as r → 0 (the diffusion
can't push r below zero).

## Construction from Ornstein-Uhlenbeck factors

Take d independent OU processes

```
dX_j = −½β X_j dt + ½σ dW_j
```

and define

```
r(t) = X₁(t)² + ... + X_d(t)²
```

Each X_j is Gaussian with mean m_j(t) = e^{−½βt}X_j(0) and covariance from
the OU solution. Then r ≥ 0 always (sum of squares). By Itô:

```
dr = (a − βr) dt + σ√r dW
```

i.e. **dr = κ(θ − r)dt + σ√r dW** (in standard notation κ=β, θ=a/β, and
W is a *single* Brownian motion via the martingale representation of the
sum). The √r vol is what guarantees non-negativity.

## Properties

- Mean-reverting with long-run mean θ and speed κ.
- **Feller condition**: if 2a ≥ σ² (i.e. 2κθ ≥ σ²), then r > 0 always
  (never touches zero); otherwise r can hit 0 but is reflected (stays
  non-negative).
- **Distribution**: r(t) is a noncentral chi-squared process; the
  transition density is known analytically.
- **Bond prices are exponential-affine**: B(t,T) = exp(−A(t,T) r(t) +
  C(t,T)) with A, C solving Riccati ODEs — same structure as HW, but
  derived from the chi-squared machinery. Closed-form yields.

## Bond pricing

From the Feynman-Kac PDE for the affine form, A(t,T) and C(t,T) satisfy
ODEs:

```
−A_t = −κA − ½σ²A² + 1,  A(T,T) = 0   (Riccati)
C_t = −κθ A,               C(T,T) = 0
```

giving explicit (exponential) formulas. Yields are affine in r:
Y(t,T) = (A(t,T)r − C(t,T))/(T−t) — hence "affine term structure."

## Trading takeaways

- CIR fixes the negative-rate problem of Gaussian models and remains
  analytically tractable (affine bond prices, known densities) — the
  classic choice for short rates in many applications.
- The Feller condition matters for calibration and simulation stability
  (if violated, the boundary behavior changes).
- Used widely for credit (intensity models), commodity convenience
  yields, and multi-factor extensions (ch32).

## Key takeaways

- CIR: dr = κ(θ−r)dt + σ√r dW; √r vol keeps rates non-negative (sum of
  squared OU processes).
- Feller condition 2κθ ≥ σ² separates "always positive" from
  "can touch zero."
- Bond prices exponential-affine with Riccati ODEs → closed-form yields.
- Choose CIR when non-negativity and analytic tractability both matter.
