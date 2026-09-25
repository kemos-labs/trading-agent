# Ch02 — Probabilistic Methods

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 2.

## Purpose
Covers the probability toolkit every trading ML model rests on:
conditional probability, Bayes' theorem, the key probability
distributions, and Monte Carlo simulation.

## Probability fundamentals
- **Probability** P(A) ∈ [0,1] measures how likely an event is.
  **Joint probability** P(A∩B) is the chance both happen;
  **conditional probability** P(A|B) = P(A∩B)/P(B) is the chance of A
  given B.
- **Bayes' theorem**:
  P(A|B) = P(B|A)·P(A) / P(B)
  It updates a prior belief P(A) into a posterior P(A|B) after seeing
  evidence B. In trading this is the formal statement of "update your
  view when new data arrives."

## Key distributions for finance
- **Normal distribution**: symmetric bell curve; returns are often
  *assumed* normal, but real returns are fat-tailed (see ch3).
- **Log-normal distribution**: if returns are normal, prices are
  log-normal (prices can't go below zero, and compounding makes price
  changes multiplicative). Used in option pricing and Monte Carlo.
- **Uniform distribution**: equal probability over an interval;
  standard input for generating random scenarios.
- **Binomial distribution**: counts successes in n trials (up/down
  moves in a simplified price process).

## Monte Carlo simulation
- Generate thousands of random paths for an asset using a chosen
  return distribution, then summarize the distribution of outcomes
  (mean, percentiles, worst-case).
- Typical price-path model: P_{t+1} = P_t·(1 + μ·Δt + σ·√Δt·ε),
  where ε ~ N(0,1), μ is drift and σ volatility. This is the
  discrete version of geometric Brownian motion.
- Monte Carlo answers questions like "what is the 5th-percentile loss
  over a month?" without closed-form math. Caveat: garbage-in,
  garbage-out — the answer is only as good as the distribution and
  parameters you assume.

## Key takeaways
- Bayes' theorem is the mathematical backbone of updating beliefs with
  evidence — directly applicable to any model that revises its signal
  as new prices arrive.
- Choose distributions deliberately: normal is convenient but
  underestimates tail risk; log-normal respects price non-negativity.
- Monte Carlo turns distribution assumptions into tradable numbers
  (VaR, drawdown probabilities), but always stress-test the
  assumptions — the model never warns you that its inputs are wrong.
