# Ch03 — Labeling

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 3.

## Purpose
Replaces the fixed-time-horizon labeling used by virtually all finance
papers with path-dependent labeling (triple-barrier) and introduces
meta-labeling — separating the *side* decision from the *size* decision.

## The fixed-time-horizon method (and why it fails)
- Labels y_t ∈ {−1, 0, 1} from the sign of the return over a fixed
  horizon h: standard but flawed. A fixed threshold τ ignores varying
  volatility (most labels become 0 in quiet periods), and it ignores
  the price path — every strategy has stop-loss limits, yet the method
  labels as profitable positions that would have been stopped out.
- Improvements: dynamic thresholds (rolling EWMA of volatility) and
  volume/dollar bars (homoscedasticity) — but both still miss the path.

## The triple-barrier method
- **Three barriers**: an upper (profit-taking) and lower (stop-loss)
  horizontal barrier, set as multiples of a target (e.g., EWMA daily
  volatility), plus a vertical barrier = expiration after h bars.
- Label by the *first barrier touched*: upper → 1, lower → −1,
  vertical → sign of return (author's preference) or 0.
- Path-dependent by construction; each barrier can be disabled (8
  configurations; e.g., vertical-only ≈ fixed-horizon, upper-only =
  take profit with no time limit).
- Implementation: events have `t1` (vertical barrier timestamp) and
  `trgt` (unit width); `ptSl` factors set barrier widths.

## Learning side and size
- Standard ML learns side and size together; better to split:
  (1) a primary model decides the *side* (long/short/flat), and
  (2) **meta-labeling** decides whether to *act* on that bet (binary
  {0,1} label), with the predicted probability driving bet size.
- Meta-labeling's payoff: correct for low precision with high recall;
  keeps ML on top of a white-box/fundamental model (the "quantamental"
  bridge); limits overfitting (ML decides size, not side); enables
  long-only and short-only sub-models with different features; sizes
  bets properly — "high accuracy on small bets and low accuracy on
  large bets will ruin you."
- Precision = TP/(TP+FP), recall = TP/(TP+FN); F1 = harmonic mean.
  Meta-labeling raises F1 by filtering false positives while the
  primary model keeps recall high.

## Key takeaways
- Labels should reflect how the strategy actually exits (stops, profit
  targets, holding limits) — labeling that ignores path dependence
  produces unrealistic targets.
- Dropping "neutral" (0) labels is usually right: a neutral case can be
  implied by a low-confidence 1/−1 prediction.
- Separate the side decision from the size decision — meta-labeling is
  the most robust labeling scheme in the book.
