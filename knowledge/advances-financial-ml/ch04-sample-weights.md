# Ch04 — Sample Weights

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 4.

## Purpose
Addresses the non-IID nature of financial labels: overlapping bet
horizons mean observations are not independent. The chapter derives
uniqueness-based sample weights and sequential bootstrap sampling to
restore near-IID conditions for training ML algorithms.

## Overlapping outcomes
- With path-dependent labeling (triple-barrier), consecutive labels
  share common returns whenever their spans overlap → the label series
  is not IID. Restricting horizons to avoid overlap forces coarse,
  low-frequency features — a terrible trade.
- The "spilled blood tubes" analogy: standard ML assumes one clean
  observation per subject; finance gives each observation contaminated
  by its neighbors, in an unknown pattern.

## Uniqueness and concurrency
- **Concurrency**: label i and label j are concurrent at t if both
  depend on a common return r_t. Build a binary array 1_i,t = 1 when
  label i spans t.
- **Average uniqueness** of label i: mean over its lifespan of
  1_i,t / c_t, where c_t = number of concurrent labels at t. Highly
  unique labels carry more independent information.
- Use average uniqueness as `sample_weight` when training; more
  overlapping (less unique) labels get down-weighted.

## Sequential bootstrap
- Standard bootstrap samples with replacement uniformly → redundant
  (overlapping) observations get oversampled, defeating the purpose.
- **Sequential bootstrap**: sample features with probability
  proportional to their average uniqueness, then *update* uniqueness of
  the remaining features to reflect the newly sampled ones (samples
  that overlap the drawn observation become less unique). This yields
  bootstrap samples as independent as possible, improving bagging
  variance reduction.

## Return attribution and time decay
- **Return attribution**: weight each observation by the sum of
  absolute log-returns over its lifespan (attributed uniquely to it) —
  big-move events get more weight; scale so weights sum to the number
  of observations. Doesn't work with "neutral" labels (another reason
  to drop them).
- **Time decay**: markets evolve; older samples are less relevant.
  Apply a decay factor (linear or exponential per user parameter c)
  that down-weights older observations relative to the latest.

## Key takeaways
- Never assume IID in financial ML: overlapping outcomes make labels
  correlated, which inflates apparent model performance.
- Weight by average uniqueness (and optionally absolute return and
  time decay) before fitting; feed `sample_weight` through
  fit_params to sklearn estimators.
- Sequential bootstrap replaces plain bootstrap for bagging on
  financial data — it produces more diverse, more independent training
  samples.
