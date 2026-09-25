# Ch07 — Hypothesis and Inference

**Source:** Grus, *Data Science from Scratch*, Chapter 7.

## Purpose
Statistical inference: how to decide whether an observed effect is real or
just noise — the machinery of A/B tests.

## Hypothesis testing
- **Null hypothesis** H₀ (e.g. "coin is fair", "new ad has no effect") vs
  **alternative** H₁. You gather data and ask: how surprising is this data
  *if H₀ is true*?
- **p-value**: the probability of observing data at least as extreme as what
  you saw, *assuming H₀*. Small p ⇒ data is surprising under H₀ ⇒ reject H₀.
- **Significance level** α (typically 0.05): the p-value threshold for
  rejection. If p < α, "statistically significant".
- **Type 1 error**: rejecting a true H₀ (false positive) — probability α.
  **Type 2 error**: failing to reject a false H₀ (false negative).
- **Power**: 1 − P(type 2) — the probability of detecting a real effect.

## Example: the fair-coin test
- H₀: p = 0.5 (fair coin). Flip n times; count heads X ~ Binomial(n, 0.5).
- Two-sided p-value: `P(X ≥ observed) + P(X ≤ n − observed)` computed via
  the normal approximation to the binomial:
  `z = (X − n·p) / sqrt(n·p·(1−p))`; p-value = `2 * (1 − normal_cdf(|z|))`.
- This is the **z-test**: standardise the observed count, look it up in the
  normal CDF.

## Confidence intervals
- A 95% **confidence interval** for a proportion p̂ estimated from n samples:
  `p̂ ± 1.96 * sqrt(p̂(1−p̂)/n)` — using the standard error of a proportion.
- Interpretation: if you repeated the experiment many times, ~95% of the
  intervals would contain the true value (a statement about the *method*,
  not the specific interval).

## A/B testing (the chapter's real application)
- Example: compare click-through of a new ad vs an old one; run both,
  compute each rate p̂_a, p̂_b, and test whether the difference is real:
  - Combine both samples to estimate the pooled probability p̂.
  - Standard error of the difference:
    `sqrt(p̂(1−p̂) * (1/n_a + 1/n_b))`.
  - Compute z = (p̂_a − p̂_b) / SE and its two-sided p-value.
  - p < 0.05 ⇒ statistically significant difference.

## Pitfalls
- **p < 0.05 ≠ 95% chance the effect is real** — it's the probability of the
  *data* under H₀, not the probability of H₀ given data.
- **Multiple testing**: run 20 A/B tests at α = 0.05 and expect ~1 false
  positive by chance. (This foreshadows ch11's overfitting and Carver's
  multiple-testing warning in the trading books.)
- **Base rates matter**: with rare events, even significant p-values can be
  dominated by false positives — think in Bayes's terms (ch6), not just
  p-values.
- Non-response / bad experimental design invalidates the test no matter the
  p-value.

## Key takeaways
- The book's recipe: state H₀ → pick a test statistic → compute its
  distribution under H₀ (via CLT/normal approx) → compute p → decide at α.
- Confidence interval for a proportion: `p̂ ± z_{α/2} * SE`.
- Standard error shrinks with `sqrt(n)`: to halve the interval, quadruple
  the sample.

## Notes
- All formulas use the normal approximation; exact binomial is mentioned but
  the code is z-based.
- `normal_cdf` and `inverse_normal_cdf` from ch6 power every computation.
