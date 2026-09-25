# Ch17 — Girsanov's Theorem and the Risk-Neutral Measure

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Statement (one-dimensional)

Let W be Brownian motion on (Ω, F, P), F(t) its filtration, and θ(t) an
adapted process. Define the density/martingale

```
Z(t) = exp( −∫₀ᵗ θ(u) dW(u) − ½∫₀ᵗ θ(u)² du )
```

(dZ = −θZ dW; Z is a P-martingale, E[Z(t)] = 1) and the equivalent measure

```
Q(A) = ∫_A Z(T) dP
```

Then under Q, the process

```
W̃(t) = W(t) + ∫₀ᵗ θ(u) du
```

is a **Brownian motion**. Technical condition: E[exp(½∫₀ᵀ θ²du)] < ∞
(Novikov) so Z is a true martingale.

**Interpretation**: changing measure adds a drift θ to the Brownian motion
(equivalently, removes the drift from the original process). θ is the
**market price of risk** (Sharpe-like): excess return per unit of
volatility.

## Application to stock price

Market: dS = μS dt + σS dW (P). Want a measure Q where the discounted stock
is a martingale. Set θ = (μ − r)/σ (market price of risk); under Q,
dS = rS dt + σS dW̃ with W̃ = W + θt. The drift disappears into the measure
change; **option prices depend only on r and σ, not μ**.

Pricing: V(t) = E_Q[e^{−r(T−t)}·payoff | F(t)] — the Black-Scholes price
as a risk-neutral expectation. The hedge (delta) implements the
replication; Girsanov just changes the probability weights.

## Pricing as a change of measure

- Z(T) is the continuous-time Radon-Nikodym derivative dQ/dP (ch9 was the
  discrete version).
- Z(t) = E_P[Z(T)|F(t)] is the state-price-density process: E_Q[X] =
  E_P[X·Z(T)]; pricing under the market measure uses Z as a deflator.
- The drift of the stock under Q is exactly r: "discounted price process is
  a Q-martingale" is the no-arbitrage condition in continuous time.

## Key takeaways

- Girsanov: under Q with density Z = exp(−∫θdW − ½∫θ²du), W + ∫θdu is
  Brownian motion — measure change ⇔ drift shift.
- θ = (μ−r)/σ is the market price of risk; it's what μ must be converted
  to (μ disappears from prices).
- Risk-neutral pricing: V = E_Q[discounted payoff]; the discounted stock is
  a Q-martingale.
- This is the continuous-time Radon-Nikodym: densities, martingales, and
  state prices unify discrete and continuous pricing.
