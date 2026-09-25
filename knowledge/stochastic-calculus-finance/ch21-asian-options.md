# Ch21 — Asian Options

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Setup

Stock dS = rS dt + σS dB (risk-neutral). An Asian option pays on the
**average** of the stock over the life of the option, e.g. a fixed-strike
Asian call:

```
V_T = h( (1/T)∫₀ᵀ S(t) dt )
```

or more generally h(∫₀ᵀ S(t) dt) with the average embedded. The average
is a *path functional*, so the option value depends on the running
integral of the path — not Markov in S alone.

## The auxiliary process trick

Introduce the integrated process Y(t) = ∫₀ᵗ S(u) du (dY = S dt). The pair
(S, Y) is Markov: S and Y together summarize everything the payoff needs.
Define

```
u(t, x, y) = E^{t,x,y}[ h(Y(T)) ]
```

the undiscounted expected payoff starting from S(t) = x, Y(t) = y. The
option value at time t is u(t, S(t), ∫₀ᵗ S du) — one extra state variable
captures the path dependence.

## Feynman-Kac PDE

u solves the 3-variable PDE (backward equation for the two-state system):

```
u_t + r·x·u_x + ½σ²x²·u_xx + x·u_y = 0,
u(T, x, y) = h(y),   u(t, 0, y) = h(y)
```

The x·u_y term is the contribution of the running integral (dY = x dt).
This is the standard way to handle one class of path-dependent options:
**augment the state** until the payoff is Markov, then solve the
higher-dimensional PDE (or use Monte Carlo).

## Solving & practical remarks

- The PDE is solvable in closed form for some Asian payoffs (e.g.
  geometric-average Asians have lognormal averages → analytic prices); the
  arithmetic-average case has no simple closed form → PDE numerics or MC.
- Monte Carlo is the natural alternative: simulate S, accumulate the
  average, average the discounted payoffs — no PDE state explosion.
- The volatility-reduction observation: the average has lower variance than
  the terminal price (averaging smooths), so Asian options are cheaper
  than plain-vanilla at the same moneyness — the source of their
  popularity (less manipulation risk too).

## Key takeaways

- Asian payoff depends on the integral/average of the path — augment state
  with Y(t) = ∫₀ᵗ S du to restore the Markov property.
- Feynman-Kac gives a 3-variable PDE (u_t + rxu_x + ½σ²x²u_xx + xu_y = 0);
  geometric-average variants have closed forms, arithmetic ones need
  numerics/MC.
- Averaging cuts realized variance → cheaper options and reduced
  price-manipulation exposure.
- The "augment the state" method generalizes to lookbacks, barriers, and
  other path-dependent claims.
