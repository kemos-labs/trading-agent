# ML Data Pipelines (Preprocessing Done Right)

## name
Building safe, reproducible data-preprocessing pipelines for ML (fit-on-
train-only, scaling, categoricals, custom transformers, tf.data, avoiding
training/serving skew).

## description
A repeatable method for turning raw data into model-ready features without
data leakage: structure every transformation as a fit-then-transform
pipeline, fit statistics ONLY on the training set, route columns to the
right transformer, and — when training at scale or in production — bake
preprocessing into the model itself so training and serving can never
drift apart.

## when to use it
- Any supervised ML project with raw data (missing values, mixed scales,
  categoricals, heavy tails) — i.e. almost always.
- Moving a model from notebooks to production, or training on datasets
  that don't fit in memory.
- Reviewing someone else's preprocessing for the classic leak: scalers
  fit on the whole dataset, or preprocessing code duplicated between
  training and serving.

## method / formula / code

**1. Split FIRST, then prepare.** Create train/validation/test sets before
any transformation (stratified on important categories if needed), then:
- fit transformers on TRAIN only (`fit_transform`);
- `transform` (never `fit`) on validation/test/new data.
This is the single most important rule: any statistic computed over
validation or test data leaks information into the model.

**2. Chain everything in a Pipeline.** `Pipeline`/`make_pipeline` (steps),
`ColumnTransformer`/`make_column_transformer` (route columns to different
transformers), and optionally `TransformedTargetRegressor` (scale labels,
auto inverse-transform predictions):
```python
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestRegressor

num_pipe = make_pipeline(SimpleImputer(strategy="median"), StandardScaler())
prep = make_column_transformer(
    (num_pipe, ["median_income", "population"]),
    (OneHotEncoder(handle_unknown="ignore"), ["ocean_proximity"]),
    remainder="passthrough")
full_pipeline = make_pipeline(prep, RandomForestRegressor())
```
Fit the whole pipeline once; `cross_val_score`/`GridSearchCV` over the
pipeline automatically re-fit each fold correctly.

**3. Per-feature decisions.**
- Missing values: median impute (or mode/custom); decide per business case.
- Scaling: `MinMaxScaler` (bounded, outlier-sensitive) vs `StandardScaler`
  (zero-mean unit-var, robust) — standardise before any distance- or
  gradient-based model. Fit on train only.
- Heavy tails: log / power transform (or bucketize to percentiles) BEFORE
  scaling so outliers don't crush the bulk.
- Categoricals: `OneHotEncoder` (nominal) / `OrdinalEncoder` (ordinal);
  keep `handle_unknown="ignore"` for unseen values.
- Engineered features: ratios, interactions, and Gaussian-RBF similarity
  features `exp(−γ||x−landmark||²)` via `FunctionTransformer`.
- Custom trainable transformers: subclass `BaseEstimator,
  TransformerMixin` (fit returns self, store learned attrs with trailing
  `_`, set `n_features_in_`).

**4. At scale / in production: tf.data + in-model preprocessing.**
- `tf.data.Dataset`: `from_tensor_slices`/`list_files` →
  `interleave` (read N files at once) → `map(preprocess,
  num_parallel_calls=tf.data.AUTOTUNE)` → `shuffle(large buffer)` →
  `batch` → `prefetch(1)`. Every method returns a NEW dataset.
- Keras preprocessing layers (`Normalization`, `StringLookup`,
  `TextVectorization`, `Rescaling`, `RandomFlip`…) with `adapt()` on train
  only, EMBEDDED in the model — deployed models ingest raw data directly.
- **Training/serving skew**: if preprocessing code exists both in training
  and in a separate serving path, they will drift. Baking it into the model
  eliminates the second copy.

## known pitfalls
- **Data leakage**: fitting scalers/imputers on the full dataset, or
  preprocessing before the train/test split. It inflates validation scores
  and collapses in production. (See also: using test set for
  hyperparameter tuning — use a separate validation set.)
- **Fitting `transform` vs `fit_transform` confusion**: validation/test
  must only be transformed.
- **`train_test_split` ordering**: shuffle (unless time series — then split
  chronologically and never shuffle).
- **Stratification**: random splits on rare categories can drop whole
  strata from train — stratify on important categoricals.
- **High-cardinality categoricals** explode with one-hot — use ordinal +
  tree models (HistGradientBoosting supports categoricals natively) or
  embeddings.
- **tf.data**: forgetting to reassign the result of dataset methods
  (they don't mutate); small `shuffle` buffers give weak shuffling;
  float64 NumPy vs float32 TF dtype mismatches.
- **Keras `adapt()`** must only see training data, same rule as `fit()`.

## source book
Géron, *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*
(O'Reilly, 3rd ed., 2023), ch2 (end-to-end project: prep, scaling,
categoricals, pipelines, GridSearch) and ch13 (tf.data, TFRecord, Keras
preprocessing layers, training/serving skew). Also relates to Grus, *Data
Science from Scratch* ch10 (rescale, PCA).
