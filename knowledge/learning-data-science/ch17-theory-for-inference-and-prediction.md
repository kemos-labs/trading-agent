# Ch17 — Theory for Inference and Prediction

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 17.

## Purpose
Formalizes what earlier chapters did informally: **hypothesis tests,
confidence intervals, prediction intervals**, and the three distributions
(population / empirical / sampling) that underpin them — with simulation,
including the **bootstrap**, doing the heavy lifting.

## The three distributions
- **Population distribution**: the true (usually unknown) distribution of
  the feature over all units.
- **Empirical (sample) distribution**: the histogram of your data —
  approximates the population if the sample is representative.
- **Sampling distribution**: the distribution of a *statistic* (mean,
  slope) over repeated samples. Its SD is the **standard error (SE)**.

## Hypothesis testing (4 steps)
1. **Set up**: pick a statistic (mean, proportion, coefficient).
2. **Model**: specify the **null hypothesis** — a data-generation
   mechanism (often "no effect").
3. **Compute**: the **p-value** = chance of a statistic at least as extreme
   as observed *under the null*. Approximate by simulation (permutation /
   bootstrap) or theory.
4. **Interpret**: tiny p ⇒ data is surprising under the null ⇒ reject it
   (statistical logic: the pattern is real — then explain *why*).
- Null is set up to be rejected; the test is proof-by-contradiction.
- Examples: J&J vaccine (urn simulation: 117 vs 351 sick), Wikipedia
  award rank test (skewed data ⇒ rank-based statistic), humidity
  coefficient in the air model (bootstrap).

## Confidence intervals
- A 95% CI for θ* is constructed so that ~95% of intervals built this way
  contain the parameter. **It is not** "95% chance θ* is in this
  interval" — that's the classic misinterpretation.
- Bootstrap: resample data with replacement, recompute statistic 10,000
  times, take percentiles (e.g. 0.5–99.5 for 99% CI).
- Normal approx: θ̂ ± 2.58·SE (99%) or ± 1.96·SE (95%).
- **Inversion**: if a 95% CI excludes the null value, the p-value < 5%.
  (Used to test the humidity coefficient ≠ 0.)

## Prediction intervals
- CIs measure estimator accuracy; **prediction intervals** measure how far
  a *future observation* may be from the prediction.
- Sources of variation: observation scatter + estimation error:
  `SD(pred) ≈ SD(pop)·sqrt(1 + 1/n)`.
- Examples: bus lateness percentiles (median 0.74, 75th 3.78, 95th 13.02
  min), crab shell size, crab growth vs size (statsmodels
  `get_prediction` gives the interval along the regression line).

## Key takeaways
- Simulation (urn, permutation, bootstrap) replaces distribution tables:
  repeat the chance process, look at the tail.
- SE shrinks like 1/sqrt(n): quadrupling n halves the CI width.
- Always state scope before interpreting tests (ch2): a significant p-value
  on a biased sample proves nothing.

## Notes
- This chapter is the theory backbone: ch16's overfitting and ch20's
  optimization now have principled justification.
- The bootstrap's accuracy varies by statistic (fine for means/coefficients;
  less so for extremes) — the book notes this caveat.
