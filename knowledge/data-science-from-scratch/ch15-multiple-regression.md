# Ch15 — Multiple Regression

**Source:** Grus, *Data Science from Scratch*, Chapter 15.

## Purpose
Generalise linear regression to several features:
`yᵢ = α + β₁xᵢ₁ + … + βₖxᵢₖ + εᵢ`.

## The model
- Fold the intercept into the parameters by adding a **column of 1s**:
  `beta = [α, β₁, …, βₖ]`, `xᵢ = [1, xᵢ₁, …, xᵢₖ]`, then
  `predict(x, beta) = dot(x, beta)`.
- **Dummy variables** encode categories: `phd = 1 if PhD else 0` — a binary
  column makes a categorical feature numeric.

## Fitting
- Minimise the sum of squared errors over all parameters with **gradient
  descent** (ch8): gradient per point = `2·(predict − y)·x` (each feature
  gets its own partial).
- The chapter's `least_squares_fit` uses **mini-batch stochastic gradient
  descent** (learning rate 0.001, batch size 25, 5000 steps) — faster than
  full-batch on larger data.
- Closed form exists (normal equations) but is skipped; the book asserts the
  GD result matches it: `minutes = 30.58 + 0.972·friends − 1.87·work + 0.923·phd`.

## Interpreting coefficients
- Each βⱼ is an **all-else-being-equal** effect: holding other features
  fixed, +1 in feature j changes y by βⱼ.
- The model doesn't capture **interactions** — add product terms
  (friends × work hours) to let one feature's effect depend on another; add
  squares to capture diminishing returns.
- Feature selection: with unlimited candidate features (products, logs,
  powers), you need principled selection — adding features always helps
  in-sample (see R² caveat) but can overfit (ch11).

## Assumptions (and what breaks them)
1. **Columns of x linearly independent** — if one feature is a linear combo
   of others (e.g. `num_acquaintances = num_friends`), β is unidentifiable:
   you can shift weight between collinear coefficients with no change in
   predictions.
2. **Features uncorrelated with the errors ε** — if violated, estimates are
   **biased**. Worked example: omitting work hours (negatively correlated
   with the outcome but positively correlated with friends) makes the friends
   coefficient *underestimated*. Omitted-variable bias is systematic, not
   random.

## Goodness of fit
- `multiple_r_squared = 1 − SSE/TSS`; adding features mechanically increases
  R² (the simple model is a special case with β₂ = β₃ = 0).
- So use **adjusted R²** (penalises extra parameters) and check whether the
  added coefficient is meaningfully different from 0:
  `adjusted R² = 1 − (1 − R²)·(n−1)/(n−k−1)`.

## Key takeaways
- Multiple regression = `dot(x, beta)` with a 1s column for the intercept.
- Coefficients are all-else-equal slopes; interactions need explicit product
  terms.
- Watch collinearity (unidentifiable β) and omitted-variable bias (biased β)
  — both are silent and damaging.
- R² must be adjusted for model size; judge features by out-of-sample or
  adjusted metrics.

## Notes
- Reuses ch8's gradient machinery and ch14's error functions — the natural
  next chapter (16) swaps squared error for log loss to get probabilities.
