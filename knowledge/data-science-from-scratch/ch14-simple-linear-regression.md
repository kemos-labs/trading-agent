# Ch14 — Simple Linear Regression

**Source:** Grus, *Data Science from Scratch*, Chapter 14.

## Purpose
Predict a number y from one feature x with a line `y = α + βx + ε`, fit by
least squares (with a detour through maximum likelihood).

## Least squares model
- Model: `yᵢ = α + βxᵢ + εᵢ` (α = intercept, β = slope, ε = error).
- Fit by minimising the **sum of squared errors**:
  `min Σ (yᵢ − α − βxᵢ)²`.
- **Closed-form solution** (derived in the book):
  - slope `β = Σ(xᵢ − x̄)(yᵢ − ȳ) / Σ(xᵢ − x̄)²` — covariance(x,y)/variance(x).
  - intercept `α = ȳ − β·x̄`.
- Worked fit on "minutes vs friends": β ≈ 0.90 minutes per friend.

## Fitting by gradient descent (the book's route)
- Since closed-form requires algebra, the book fits with gradient descent
  (ch8): minimise `sum of squared errors` where the gradient per point is
  `2·(prediction − y)·x`.
- Result matches the closed form to ~3 decimals — a sanity check that both
  methods solve the same problem.

## Maximum likelihood justification
- If errors are normal with mean 0 and known σ, the likelihood of the data
  is the product of normals:
  `L = ∏ (1/(σ√2π)) · exp(−(yᵢ − α − βxᵢ)²/(2σ²))`.
- Maximising L is equivalent to minimising Σ(yᵢ − α − βxᵢ)² — **least
  squares = maximum likelihood under normal errors**. This legitimises the
  squared-error choice.

## Goodness of fit: R²
- **Total sum of squares** (variation of y): `TSS = Σ(yᵢ − ȳ)²`.
- **Sum of squared errors**: `SSE = Σ(yᵢ − ŷᵢ)²`.
- **R² = 1 − SSE/TSS** — the fraction of y's variation explained by the
  model, in [0, 1] for a line.
- The chapter's model explains ~66% of variance (R² ≈ 0.66) for minutes vs
  friends; each additional friend ≈ +0.90 minutes.
- **Watch out**: R² is not a model-quality guarantee — it ignores
  linearity-of-relationship validity, and outliers can inflate it (the
  chapter explicitly lists what R² doesn't measure).

## Key takeaways
- Slope = covariance/variance (standardised rate of change); intercept =
  mean of y minus slope×mean of x.
- Squared-error minimisation ≡ normal-error maximum likelihood — the
  principled reason for least squares.
- R² = 1 − SSE/TSS tells you how much variance the model captures.
- Always sanity-check gradient-descent fits against the closed form.

## Notes
- `error(x, y, beta) = predict − y` and `squared_error` carry straight into
  ch15 (multiple regression) and ch16 (logistic).
- Outlier sensitivity: the friend count distribution is heavy-tailed; the
  chapter truncates it (friends ≤ 100) before fitting — clean data first.
