# Ch19 — A Two-Dimensional Market Model

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Setup

Two stocks driven by two independent Brownian motions B₁, B₂:

```
dS₁ = S₁(μ₁ dt + σ₁ dB₁)
dS₂ = S₂(μ₂ dt + ρσ₂ dB₁ + √(1−ρ²)σ₂ dB₂)
```

S₁ has instantaneous variance σ₁²; S₂ has instantaneous variance σ₂²; the
two stocks have instantaneous covariance ρσ₁σ₂ — so ρ is the correlation
(ρσ₂ is S₂'s loading on the shared factor B₁, √(1−ρ²)σ₂ the idiosyncratic
part).

## Market price of risk equations

With accumulation factor β(t) = e^{∫r du}, the market price of risk
θ = (θ₁, θ₂) must satisfy two equations (one per stock):

```
σ₁θ₁ = μ₁ − r
ρσ₂θ₁ + √(1−ρ²)σ₂θ₂ = μ₂ − r
```

Two stocks, two unknowns → θ determined uniquely (when the volatility
matrix is invertible). Girsanov with this θ makes both discounted stock
prices Q-martingales; Q is the unique risk-neutral measure.

## Completeness in two dimensions

- Two risky assets, two Brownian motions → the market is **complete**:
  every claim (payoff function of both stocks) is replicable by trading
  the two stocks + money market.
- The hedge uses both assets: the claim's value process is a martingale in
  the two-dimensional filtration; MRT (2-D version) represents it against
  B₁, B₂; matching the two volatility coefficients to the two stock
  coefficients gives the hedge ratios (deltas for each stock).
- Pricing: V(t) = E_Q[e^{−r(T−t)} payoff | F(t)] — a two-dimensional
  expectation (or a 2-D PDE via Feynman-Kac).

## The general principle

**Number of traded risky assets = number of Brownian motions ⇒ complete.**
Fewer assets than shocks (e.g. one stock + stochastic volatility) ⇒
incomplete: θ can't be pinned down, Q is not unique, claims have price
intervals. This is why variance swaps, options on vol, and spanning
instruments (VIX futures/options) matter — they complete the market for
volatility risk.

## Key takeaways

- Two stocks, two Brownian motions (with correlation ρ): unique market
  price of risk θ from the MPR equations; unique risk-neutral measure;
  complete market.
- Hedging uses both stocks; pricing = Q-expectation of discounted payoff.
- Completeness ⇔ number of independent traded risk factors = number of
  Brownian shocks; missing factors (vol) ⇒ incompleteness and non-unique
  prices.
