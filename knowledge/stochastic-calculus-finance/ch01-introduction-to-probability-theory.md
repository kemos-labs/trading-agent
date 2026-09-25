# Ch1 — Introduction to Probability Theory

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, later
published as *Stochastic Calculus for Finance I & II*) — Steven Shreve
(Carnegie Mellon)

## The binomial asset pricing model

The entire course is built on one toy: a stock price that at each step goes
up by factor u or down by factor d, with 0 < d < u. With initial price S₀,
one step gives S₁ = uS₀ or dS₀; after n tosses the price S_n depends only on
the first n coin tosses (path-dependence is introduced by how many H vs T).

The no-arbitrage condition is

```
d < 1 + r < u
```

where r is the risk-free rate. If 1+r ≥ u, the bond dominates the stock
(no one buys stock); if 1+r ≤ d, borrowing to buy stock is a free lunch.
This single inequality is the seed of everything: the probabilities of H and
T are *not* specified — the model prices and hedges without them.

## Probability space machinery

- Sample space Ω = all sequences of n tosses; sample points are paths.
- A **random variable** X is a function X: Ω → ℝ; its distribution depends
  on both X and the probability measure P. The same random variable can
  have multiple distributions (market/objective vs. risk-neutral).
- A σ-algebra F on Ω collects the sets we can assign probabilities to; a
  random variable is measurable (F-measurable) if we can tell membership of
  {X ∈ B} for all Borel B.
- **Expectation**: E[X] = Σ_ω X(ω)P(ω) (discrete case).
- A stock price S_k is measurable w.r.t. the first k tosses' information —
  formalized later as the filtration F_k.

## Independence and limit theorems

- Independent random variables, law of large numbers (M_k/k → 0 a.s.), and
  the central limit theorem (M_k/√k → standard normal) are stated via
  moment generating functions. These become the bridge to Brownian motion
  in Part II: the scaled random walk converges to Brownian motion.

## Key takeaways

- The binomial model is chosen because it illuminates arbitrage pricing and
  risk-neutral pricing, approximates continuous models computationally, and
  develops the conditional expectation/martingale machinery needed later.
- The no-arbitrage condition d < 1+r < u is the fundamental constraint;
  probabilities of the stock's moves are irrelevant to pricing.
- Random variables are defined independently of their distribution — the
  same payoff has different distributions under different measures (this
  anticipates the change of measure in Part II).
