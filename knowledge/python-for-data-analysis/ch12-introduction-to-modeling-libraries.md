# Ch12 — Introduction to Modeling Libraries in Python

**Source:** Wes McKinney, *Python for Data Analysis* (3rd ed., 2022), Chapter 12.

## Purpose
The handoff from pandas wrangling to modeling: DataFrame↔NumPy conversion,
**Patsy formulas** (R-style design matrices), **statsmodels**
(classical statistics), and **scikit-learn** (ML) — enough to wire models
into the wrangling pipeline.

## pandas ↔ model code
- `df.to_numpy()` converts homogeneous DataFrames to ndarray; with mixed
  types it yields an object array (bad for models) — select numeric
  columns first via `df.loc[:, cols].to_numpy()`.
- Dummies: `pd.get_dummies(data, prefix=...)` + drop original + join —
  manual one-hot for modeling; Patsy automates it.
- Round-trip: `pd.DataFrame(array, columns=[...])`.

## Patsy (formula syntax)
- Formula strings: `y ~ x0 + x1` — terms, not arithmetic. `+` means
  "include term".
- `patsy.dmatrices('y ~ x0 + x1', data)` returns (y, X) design matrices.
- Categoricals auto-encoded: `key1[T.b]` (treatment coding, one level
  dropped as reference); interactions: `x1:x2`, `x1*x2 = x1 + x2 + x1:x2`.
- Inline transformations: `y ~ np.log(x)` works inside formulas.
- Installed with statsmodels; `smf` (formula API) uses it under the hood.

## statsmodels (classical statistics)
- `import statsmodels.api as sm`, `statsmodels.formula.api as smf`.
- Array API: `sm.OLS(y, sm.add_constant(X)).fit()` — `add_constant` for
  intercept; formula API adds intercept automatically.
- `results.summary()`: coefficients, std err, t-values, p-values, R²,
  F-stat, DW, JB — the classic regression diagnostics.
- `results.params`, `.tvalues`, `.predict(new_data)`.
- Wider scope: GLMs, robust linear models, ANOVA, mixed effects, time
  series/state space, GMM.
- Use statsmodels when you need inference (CIs, p-values, model
  diagnostics); use sklearn when you need prediction + regularization.

## scikit-learn (machine learning)
- Estimator API: `model.fit(X_train, y_train)`, `model.predict(X)`,
  `model.score(X_test, y_test)`.
- `LogisticRegression(C=10)` — regularization strength via C (smaller C =
  more regularization); `LogisticRegressionCV(Cs=10)` does a grid over C
  with built-in CV.
- `cross_val_score(model, X, y, cv=4)` — k-fold evaluation helper.
- Input must be numeric ndarray/DataFrame; scale features for many models
  (StandardScaler) — see our data-pipelines skill for the full pipeline
  discipline (fit-on-train-only etc.).

## Key takeaways
- Design matrices are the currency: Patsy builds them from formulas and
  handles categoricals safely; sklearn needs numeric features you prepare.
- Two libraries, two jobs: statsmodels = inference/diagnostics, sklearn =
  prediction with regularization and CV.
- The wrangling → to_numpy/dummies → fit → score loop is the standard
  workflow; pipelines (Géron ch2/6, our data-pipelines skill) harden it.

## Notes
- Ch13 exercises all of this: FEC/MovieLens data wrangled then modeled;
  the book intentionally stops short of deep ML — our hands-on-ml and
  ai-engineering notes carry that forward.
- For trading: statsmodels OLS is the workhorse for factor/hedge-ratio
  regressions (kalman-filter-pairs skill builds on this).
