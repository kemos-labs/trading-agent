# Ch25 — American Options (Continuous Time)

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Preview: perpetual American put

For a non-dividend stock dS = rS dt + σS dB, the American put with no
expiration has intrinsic value (K − S)⁺. Strategy: exercise when the price
first hits some level L ≤ K (or lower). Its value (given exercise level L):

```
v_L(x) = (K − L)·E[e^{−r·τ_L}]   for x > L;   (K − x)⁺ for x ≤ L
```

The plan: compute v_L and maximize over L to find the optimal exercise
boundary. This requires the distribution of the first passage time τ_L.

## First passage time (reflection principle method)

For Brownian motion hitting level x > 0 at τ = min{t : W(t) = x}: using the
joint max/terminal density (ch20), the first-passage density is the
**inverse Gaussian**:

```
P(τ_x ∈ dt) = (x/√(2π t³))·exp(−x²/2t) dt
```

Laplace transform: E[e^{−ατ_x}] = e^{−x√(2α)}. Applied to the drifted
process (the stock's log), this gives E[e^{−rτ_L}] as a power of the stock
price — the "candidate solution" v_L(x) = C·x^{−γ} form.

## Solving the perpetual put

The value function v(x) solves the ODE from the Black-Scholes-PDE with
v_t = 0 (perpetual):

```
½σ²x²v'' + rx v' − rv = 0   →   v(x) = A·x^{γ₁} + B·x^{γ₂}
```

with γ from the characteristic equation ½σ²γ(γ−1) + rγ − r = 0.
Boundary conditions: v = K − x at the exercise boundary x = L (value
matching), v' = −1 there (smooth pasting / super-contact), v → 0 as x → ∞.
These determine A, B, L, giving the closed form:

```
L = K·γ₂/(γ₂−1)   (the optimal exercise boundary, γ₂ the negative root)
v(x) = (K − L)·(x/L)^{−γ₂}   for x > L
```

The optimal exercise boundary L is where the holder is indifferent between
holding and exercising.

## Finite-maturity American options

Same principle, PDE with the free boundary:

```
max( v_t + rSv_S + ½σ²S²v_SS − rv ,  g(S) − v ) = 0  (variational form)
```

In the exercise region v = g(S) (the payoff) with smooth pasting v_S = g'(S)
across the boundary; outside, the option satisfies the BS PDE. No closed
form generally → binomial/trinomial trees, finite differences, or MC with
optimal-stopping regression (Longstaff-Schwartz).

## Key takeaways

- Perpetual put: value = max over exercise levels L of (K−L)·E[e^{−rτ_L}];
  first-passage time is inverse Gaussian with E[e^{−ατ}] = e^{−x√(2α)}.
- Free-boundary PDE: value satisfies BS PDE in the continuation region,
  equals the payoff at the boundary, with smooth pasting v_S = g'(S).
- Early exercise is optimal only for puts (or with dividends); the
  exercise boundary is the central object.
- Numerics: trees/finite-difference/Longstaff-Schwartz handle finite
  maturity.
