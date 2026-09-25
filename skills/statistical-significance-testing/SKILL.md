# Statistical Significance Testing (A/B Testing)

## name
Hypothesis testing, p-values, and A/B comparison for proportions and means
(z-test framework, confidence intervals, sample-size rules).

## description
A repeatable method for deciding whether an observed difference (strategy
performance, click-through, conversion, win rate) is real or just sampling
noise: state the null, standardise the statistic, read the p-value from the
normal CDF, and size the experiment so the difference you care about is
actually detectable. Built on the central limit theorem — no heavy
statistics package required.

## when to use it
- Comparing two strategies, rules, or parameter sets: is the better
  back-tested Sharpe/win-rate real or noise?
- A/B tests in products (ads, UI variants, model variants): is the lift
  significant?
- Deciding how much history/data you need before trusting a difference
  (Carver's rule-fitting tables are the same math).
- Reporting uncertainty honestly: give confidence intervals, not point
  estimates.

## method / formula / code

**1. State the null hypothesis** H₀ (e.g. "true conversion rate p = 0.5",
"strategy A and B have equal rates"). The p-value answers: *how surprising is
this data if H₀ is true?*

**2. Pick a statistic and standardise it.**
- **One proportion** (fair-coin / baseline test): with n trials and observed
  count X, under H₀ the count is Binomial(n, p₀). Normal approximation:
  `z = (X − n·p₀) / sqrt(n·p₀·(1−p₀))`
- **Two proportions (A/B test)**: rates p̂_a = x_a/n_a, p̂_b = x_b/n_b.
  Pool the data to estimate the common probability:
  `p̂ = (x_a + x_b) / (n_a + n_b)`
  Standard error of the difference:
  `SE = sqrt(p̂·(1−p̂)·(1/n_a + 1/n_b))`
  Test statistic: `z = (p̂_a − p̂_b) / SE`
- **Confidence interval** for a proportion:
  `p̂ ± 1.96 · sqrt(p̂(1−p̂)/n)` (z_{0.025} = 1.96 for 95%).

**3. Compute the two-sided p-value** from the standard normal CDF:
`p = 2 · (1 − normal_cdf(|z|))`. Reject H₀ at significance level α (usually
0.05) iff p < α. (1.96 ≈ the z where two-sided p = 0.05.)

Reference implementation:
```python
import math
def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / (math.sqrt(2) * sigma))) / 2

def two_sided_p_value(z):
    return 2 * (1 - normal_cdf(abs(z)))

def ab_test_p_value(xa, na, xb, nb):
    pa, pb = xa/na, xb/nb
    p = (xa + xb) / (na + nb)
    se = math.sqrt(p*(1-p)*(1/na + 1/nb))
    return two_sided_p_value((pa - pb) / se)
```

**4. Size the experiment for the difference you care about.**
- Standard error shrinks like 1/√n: to halve a confidence interval, quadruple
  the sample.
- To detect a true difference δ between two rates with ~95% confidence,
  derive from the two-proportion SE at p̂ ≈ 0.5:
  `SE = sqrt(2·p̂·(1−p̂)/n) ≈ 0.707/√n`; set 1.96·SE ≈ δ ⇒
  `n ≈ 2/δ² per group`. E.g. detecting a 50% vs 60% difference (δ = 10%)
  needs ~200/group; a 5% vs 6% difference (δ = 1%) needs ~20,000/group.
  (Grus's worked example: pa=0.1 vs pb=0.12, δ=2%, needed ~2,900/group —
  consistent with the rule, which is slightly conservative.)

**5. Interpret, remembering what p is NOT.**
- p < 0.05 means "this data is unlikely under H₀" — it is NOT the
  probability that H₀ is false, and NOT a 95% chance the effect is real.
  For the probability the effect is real, reason with Bayes (prior ×
  likelihood), not the p-value alone.
- Type 1 error: rejecting a true H₀ (probability α). Type 2: failing to
  reject a false H₀. Power = 1 − P(type 2); underpowered experiments
  (small n) quietly miss real effects.

## known pitfalls
- **Multiple testing**: run 20 A/B tests at α = 0.05 and ~1 false positive is
  expected by chance. Adjust (Bonferroni: α/m) or pre-register one test. This
  is the exact trap in back-testing hundreds of rules (see Carver's tables:
  testing 100 rules needs SR cutoffs of 0.6–1.5 even with 10 years of data).
- **p < 0.05 ≠ effect is real or large** — significance ≠ importance; report
  the effect size and interval, not just the star.
- **Base rates**: with rare events, most "significant" positives can still be
  false — combine with prior reasoning.
- **Bad experiment design** (non-random assignment, feedback loops,
  peeking at results and stopping early) invalidates the test no matter the
  p-value. Decide the sample size in advance and don't peek.
- **Normal approximation** breaks for tiny n or p̂ near 0/1 (need n·p ≥ ~10);
  use exact binomial or Fisher's exact there.

## source book
Grus, *Data Science from Scratch* (O'Reilly, 2nd ed., 2019), ch7 (Hypothesis
and Inference), with ch6 probability foundation.
