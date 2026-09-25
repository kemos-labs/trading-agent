# Ch07 — Ensemble Learning and Random Forests

**Source:** Géron, *Hands-On Machine Learning*, Chapter 7.

## Purpose
Wisdom of the crowd: combine many predictors so the ensemble beats its best
member. Voting, bagging/pasting, random forests, boosting, stacking.

## Voting classifiers
- **Hard voting**: majority class vote over diverse classifiers (logistic,
  SVM, RF, k-NN) — often beats the best member. Weak learners (51%)
  aggregate to a strong learner via the law of large numbers — but only if
  errors are **uncorrelated**; same-data models share errors, so use diverse
  algorithms.
- **Soft voting**: average class *probabilities*, pick max — usually better
  than hard voting (weights confident votes more). Needs `predict_proba`.

## Bagging & pasting
- Train the same algorithm on **random subsets** of the training set:
  bagging = sampling **with replacement** (bootstrap); pasting = without.
- Bagging's extra diversity ⇒ slightly higher bias but lower variance than
  pasting; bagging usually wins.
- Aggregation: mode (classification) / average (regression).
- Parallelises across cores/servers (`n_jobs=-1`); each predictor has higher
  bias, but aggregation reduces both bias and variance — net: similar bias,
  lower variance.
- `BaggingClassifier`/`BaggingRegressor`: `max_samples`, `bootstrap`,
  `n_estimators`.
- **Out-of-bag (OOB) evaluation**: with bootstrap, each predictor misses
  ~37% of instances; evaluate the ensemble on the union of OOB instances for
  a free validation score (`oob_score=True`).

## Random forests & extra-trees
- **Random forest** = bagging of decision trees + **feature sampling**:
  each split considers only a random subset of features (`max_features`) —
  extra diversity, less correlated trees, less variance.
- `RandomForestClassifier`: `n_estimators`, `max_depth`, `max_features`,
  `bootstrap`. Feature importances via `feature_importances_` (mean impurity
  decrease).
- **Extra-trees** (Extremely Randomized Trees): even more random — random
  *thresholds* per feature instead of searching the best one. Higher bias,
  much lower variance, faster training; often as good or better.

## Boosting
- **AdaBoost**: sequentially fit weak learners, each **weighting the
  misclassified instances more**; final = weighted sum. Sensitive to
  outliers (overweighting). Tweak: if underfitting, add estimators / lower
  learning rate.
- **Gradient boosting (GBRT)**: sequential trees, each fitted on the
  **residuals** of the previous ensemble (gradient of the loss).
  - Hyperparameters: `learning_rate` (shrinkage — lower ⇒ slower but
    better), `n_estimators`, `max_depth` (usually ≤ 6).
  - **Early stopping** via `validation_fraction` / `n_iter_no_change`.
  - `subsample < 1` ⇒ **stochastic gradient boosting** (random instance
    subsample per tree) — higher bias, lower variance, faster.
- **Histogram-based GBT** (`HistGradientBoostingRegressor`): bins features
  into ≤255 integers — O(b·m) instead of O(n·m·log m); hundreds of times
  faster on large data; supports categoricals + missing values natively.
- Production: **XGBoost, CatBoost, LightGBM** — specialised, GPU-accelerated.

## Stacking
- Train a **blender / meta-learner** on the base predictors' *out-of-sample*
  predictions (`cross_val_predict`), then retrain base models on full data;
  blender takes their predictions as input features.
- `StackingClassifier`/`StackingRegressor` (`cv=5`): final estimator
  defaults to LogisticRegression / RidgeCV; can stack multiple layers.

## Key takeaways
- Diversity (algorithms, data subsets, features) is what makes ensembles
  work — correlated errors cancel the benefit.
- Random forests + GBRT are the first models to try on tabular data:
  little preprocessing needed, strong and fast.
- Read the classic failure modes: bagging fixes variance; boosting fixes
  bias; stacking squeezes the last bit.

## Notes
- "Which hyperparameters fix under/overfitting?" — the chapter's exercises
  drill the mental model: overfit → more regularisation/less estimators;
  underfit → more capacity/less shrinkage.
- Ensemble ideas transfer to strategy research: combining multiple
  uncorrelated signals/rules is the same wisdom-of-the-crowd principle.
