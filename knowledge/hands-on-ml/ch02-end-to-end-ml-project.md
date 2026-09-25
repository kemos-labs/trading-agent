# Ch02 — End-to-End Machine Learning Project

**Source:** Géron, *Hands-On Machine Learning*, Chapter 2.

## Purpose
The full project workflow on the California housing dataset: frame → get →
explore → prepare → train → fine-tune → present → launch/monitor.

## Workflow steps
1. **Frame the problem**: ask the business objective first — it determines
   task type, algorithms, and performance measure. (Regression here;
   would-be-classification if the downstream only needs price *categories*.)
   Check assumptions early.
2. **Get the data**: real datasets (OpenML, Kaggle, UCI, PapersWithCode).
3. **Explore/visualise** (ch2): correlations, geography, distributions —
   before modelling.
4. **Prepare data** for algorithms: cleaning, feature engineering, scaling.
5. **Select + train a model** (start simple: LinearRegression, then tree,
   then random forest).
6. **Fine-tune** hyperparameters (grid/randomised search, ensembles).
7. **Present**; 8. **Launch, monitor, maintain** (data pipelines, retraining).

## Performance measures
- **RMSE** (ℓ₂): `sqrt(mean((ŷ−y)²))` — prefers error on large errors;
  the default regression metric.
- **MAE** (ℓ₁): `mean(|ŷ−y|)` — more robust when outliers are not
  exponentially rare.
- Higher-norm metrics weight large errors more; choose per data shape.
- Note: the *training loss* (easy to optimise, e.g. log loss) can differ from
  the *evaluation metric* (business-relevant, e.g. precision/recall).

## Data preparation patterns
- **Stratified sampling**: split by a relevant category (income category),
  not purely randomly, so train/test preserve the distribution. Random
  sampling can silently drop a stratum.
- **Feature scaling** — fit on TRAIN only, then transform the rest:
  - **MinMaxScaler** → [0,1] (or any range); sensitive to outliers.
  - **StandardScaler** → mean 0, std 1; robust to outliers; better default.
  - Heavy-tailed features: log / power transform first (population →
    log looks near-Gaussian); or bucketize (percentile buckets ≈ uniform).
  - Multimodal features: bucketize and one-hot, or add Gaussian RBF
    similarity features: `exp(−γ(x−35)²)` via `rbf_kernel`.
- **Categoricals**: `OneHotEncoder` (+ `handle_unknown`, sparse output),
  or `OrdinalEncoder`. Feature columns tracked via
  `get_feature_names_out()`.
- **Custom transformers**: `FunctionTransformer` for stateless ops
  (log, ratios, RBF features); subclass `BaseEstimator, TransformerMixin`
  for trainable ones (fit returns self, stores `n_features_in_`).
- **Pipelines**: `Pipeline`/`make_pipeline` chains preprocessing + model;
  `ColumnTransformer`/`make_column_transformer` routes columns to
  different transformers; `TransformedTargetRegressor` scales labels and
  inverse-transforms predictions automatically.

## Model selection & fine-tuning
- Compare with cross-validation (RMSE), not the training set.
- **GridSearchCV**: exhaustive over a param grid. **RandomizedSearchCV**
  (often better): sample params from distributions — more coverage per
  compute, and uninformative params cost nothing extra.
- **Halving** variants (HalvingGridSearchCV/RandomSearchCV): first round on
  limited resources, keep best candidates, escalate resources — big speedup.
- **Ensembles** (ch7 preview): combine good models; usually beats the best
  single model.
- Inspect `feature_importances_` (random forest) to drop useless features;
  examine per-category errors before deploying.
- Final test-set evaluation once, with a **bootstrap confidence interval**
  (scipy `stats.bootstrap`) on the error. Resist tweaking after seeing test
  results.

## Key takeaways
- Pipeline everything (fit-transforms, then transform val/test with the
  trained pipeline) — never fit on validation/test.
- Stratify splits on important categories.
- Randomised search beats grid search for hyperparameters.
- A model is only done when monitored in production: data pipelines need
  monitoring or stale/broken components go unnoticed.

## Notes
- The geo clustering (k-means on lat/lon as extra features, ch9) is a
  great example of using an unsupervised model inside a supervised pipeline.
- Log-transform of the target (via TransformedTargetRegressor) handles the
  heavy-tailed house-price distribution.
