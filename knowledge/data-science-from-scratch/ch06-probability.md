# Ch06 — Probability

**Source:** Grus, *Data Science from Scratch*, Chapter 6.

## Purpose
The probability toolkit needed for inference (ch7) and probabilistic models
(Naive Bayes, ch13): events, conditional probability, Bayes's theorem,
random variables, and distributions.

## Core ideas
- **Events and probabilities**: `P(A)` = proportion of outcomes in A.
  Probabilities are between 0 and 1; complementary events: `P(¬A) = 1 − P(A)`.
- **Conditional probability**: `P(A|B) = P(A and B) / P(B)` — the
  probability of A given that B happened.
- **Independence**: A and B independent iff `P(A and B) = P(A) * P(B)`
  (equivalently `P(A|B) = P(A)`).
- **Bayes's theorem** — the key formula:
  `P(A|B) = P(B|A) * P(A) / P(B)`
  The book frames it as *updating beliefs*: prior `P(A)`, evidence `B`,
  posterior `P(A|B)`. This is the engine of ch13's spam filter.
- **Law of total probability**: `P(B) = P(B|A)P(A) + P(B|¬A)P(¬A)` — used
  to expand the denominator of Bayes.

## Random variables and distributions
- A **random variable** is a variable whose values follow a probability
  distribution; `P(X = x)` denotes the probability the variable equals x.
- **Uniform distribution**: every value in a range equally likely.
- **Normal (Gaussian) distribution**: the bell curve, parameterised by mean
  μ and variance σ²:
  `f(x) = 1/(σ√(2π)) · exp(−(x−μ)²/(2σ²))`.
  - The book implements `normal_pdf` and `normal_cdf` (integrated via the
    error-function approximation `math.erf`) and the inverse CDF.
  - **68–95–99.7 rule**: ~68% of mass within 1σ, ~95% within 2σ, ~99.7%
    within 3σ of the mean.
- **Bernoulli distribution**: single coin flip; p = probability of success.
- **Binomial distribution**: number of successes in n independent flips with
  success prob p — implemented via combinatorics `n choose k`.
- **Central Limit Theorem** (stated): sums/averages of many independent
  variables look normal regardless of the underlying distribution — the
  justification for treating sample means as normal (ch7).

## Key takeaways
- Bayes's theorem is the single most reused formula in the book (ch13 spam
  filter, ch23 recommender's prior reasoning, ch26 fairness debates).
- Conditional-probability language (`given`, `if`) maps directly onto
  `P(A|B)`; practise converting sentences into the formula.
- Normal CDF/inverse CDF utilities are used later to generate random normal
  data (ch18 neural nets) and to compute p-values/confidence intervals (ch7).

## Notes
- Continuous distributions use PDFs/CDFs; discrete use PMFs — the book
  keeps both concrete and minimal.
- `inverse_normal_cdf` via `erf` inversion is reused verbatim in ch18's
  weight initialisation.
