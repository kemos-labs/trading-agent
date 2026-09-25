# Ch18 — Entropy Features

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 18.

## Purpose
Estimates the informational content of price series via entropy — the
basis for features that tell ML algorithms whether momentum (low
information) or mean-reversion (high information) regimes prevail.

## Information theory essentials
- **Shannon entropy**: H[X] = −Σ p[x]·log₂ p[x], with
  0 ≤ H ≤ log₂|A|. Low-probability outcomes carry more information
  ("we learn when something unexpected happens").
- **Redundancy** R[X] = 1 − H[X]/log₂|A|; **mutual information**
  MI(X;Y) = KL divergence from joint to product of marginals —
  always ≥ 0, zero iff independent; for Normal variables,
  MI = −½·log(1−ρ²), so MI generalizes correlation to nonlinear
  association.
- **Generalized mean / diversity**: the effective number of items in a
  probability vector, N_q(p) = (Σ pᵢ^q)^(1/(1−q)); entropy is the
  limit case q→1 — a link between entropy and diversity measures.

## Estimators
- **Plug-in (maximum likelihood)**: count word frequencies in the
  sequence, Ĥ = −Σ p̂(w)·log p̂(w) over words of length w; needs
  n ≫ w for accuracy (law of large numbers on empirical distribution).
- **Lempel–Ziv (LZ)**: compress the message into a dictionary of
  non-redundant substrings; entropy rate from the dictionary size
  relative to message length. Complex (high-entropy) messages need
  larger dictionaries. Kontoyiannis's method is an efficient variant.
- **Encoding matters**: quantile vs. standard-normal encoding of
  returns (uniform codes vs. codes proportional to normal density);
  with too-small alphabets (2–5 letters), information is discarded and
  entropy is underestimated. The plug-in estimator benchmark: for an
  IID standard Normal, H ≈ 1.42 (nats, natural log — ½·ln(2πeσ²) with
  σ=1) — use this to calibrate estimator, message length, and encoding;
  don't mix units with the log₂ formulas elsewhere.

## Financial applications
- **Entropy-implied volatility**: for Normal returns,
  H = ½·log₂(2πeσ²) → σ from H — connects entropy with volatility.
- Regime/feature uses: entropy as a feature to switch between momentum
  (low info → trend) and mean-reversion (high info → fade) strategies;
  entropy of tick-rule sequences; entropy-based regime detection.
- Entropy is also used to measure market efficiency (more efficient =
  more information in prices = higher entropy).

## Key takeaways
- Entropy quantifies how "surprising" a price series is — a principled
  alternative to variance for measuring information.
- Use plug-in or LZ estimators with adequate alphabets (≥ 10 letters
  for the Kontoyiannis method) and validate against the known Gaussian
  value H ≈ 1.42.
- Entropy features pair naturally with structural breaks (ch17) as
  event triggers for event-based sampling (ch2).
