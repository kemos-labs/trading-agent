# Ch15 — Linear Models

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 15.

## Purpose
From the constant model (ch4) to **linear models**: simple (one
explanatory feature) and multiple, fitted by minimizing mean squared error
(MSE) — with the geometry that explains coefficients and multicollinearity.

## Simple linear model
- Model: y ≈ θ₀ + θ₁x. Fit by minimizing MSE:
  `θ₁̂ = r(x,y) · SD(y)/SD(x)`, `θ₀̂ = ȳ − θ₁̂·x̄`.
- Interpretation: for x one SD above its mean, predict y r SDs above its
  mean. The sample correlation r drives the slope.
- Equivalent form: ŷ = ȳ + r·SD(y)·(x − x̄)/SD(x).
- In code: `theta_1 = x.corr(y) * y.std()/x.std()`;
  `theta_0 = y.mean() - theta_1*x.mean()`; or `sklearn.linear_model
  .LinearRegression`.
- **r caveats** (Anscombe's quartet): identical r, means, SDs — but very
  different plots. Always plot.

## Multiple linear model
- y ≈ θ₀ + θ₁x₁ + … + θₚxₚ. Design matrix X (columns = features), fit
  minimizes ‖y − Xθ‖²; closed form θ̂ = (XᵀX)⁻¹Xᵀy (normal equations).
- Geometry: features are column vectors in n-dim space; the fitted ŷ is the
  **projection of y onto the column space of X**; residuals are orthogonal.
  Adding features always shrinks training error (→ overfitting, ch16).
- Coefficient meaning: change in y per unit change in xⱼ *holding other
  features fixed*. **Highly correlated features** make coefficients
  unstable and uninterpretable (the Gini/single_mom/travel cluster): many
  models fit equally well with features standing in for each other.

## Assessment
- Compare SD of residuals vs SD of outcome: the model "explains"
  1 − (SD_res/SD_y)² ≈ R² of the variation.
- Residual plots (residuals vs fitted): curvature ⇒ nonlinearity; funnel ⇒
  heteroscedasticity (weighted regression fix).

## Feature engineering for linear models
- Polynomials (x², x³) are still *linear* in the features (design-matrix
  columns) — ch16 shows why to use orthogonal polynomials instead.
- **One-hot encoding** of categoricals (pd.get_dummies, drop one level)
  adjusts the intercept per category — equivalent to parallel regression
  lines. Ch18's donkey model does this with a custom loss.

## Key takeaways
- Linear models are the interpretable workhorse: prediction, inference
  (ch17), and calibration (ch12) all use them.
- Multicollinearity breaks interpretation, not prediction: watch
  correlations between features before trusting coefficients.
- MSE minimization = projection; residual plots are the diagnostic.

## Notes
- Runs Chetty's upward-mobility data (AUM by commute time, gini,
  single_mom, …): single_mom is the strongest single predictor.
- Ch16 (model selection), ch17 (inference), ch20 (numerical optimization)
  build directly on this chapter.
