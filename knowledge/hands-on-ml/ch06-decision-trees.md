# Ch06 — Decision Trees

**Source:** Géron, *Hands-On Machine Learning*, Chapter 6.

## Purpose
Interpretable (white-box) classifiers/regressors; the building block of
random forests (ch7).

## Training and prediction
- `DecisionTreeClassifier` on iris (petal length/width, max_depth=2) — the
  tree asks threshold questions (petal length ≤ 2.45?), descending to
  leaves that predict the majority class of the node's training instances.
- **Node attributes**: `samples` (instances reaching it), `value`
  (counts per class), `gini` (impurity).
- **Gini impurity**: `Gᵢ = 1 − Σ pᵢₖ²` — 0 when pure, max when evenly
  split.
- **No feature scaling or centering needed** — trees only compare
  thresholds.
- **Class probabilities**: leaf's class proportions
  (`predict_proba` = fractions in the leaf).

## CART training algorithm
- Binary trees only (splits have exactly two children; ID3 allows more).
- Greedy: for each feature k and threshold tₖ, pick the split minimising
  the **size-weighted impurity**:
  `J(k, tₖ) = (m_left/m)·G_left + (m_right/m)·G_right`.
- Complexity O(n·m·log m); scales fine.
- Regression (`DecisionTreeRegressor`): same, but minimises MSE:
  each leaf predicts the mean target of its region.

## Regularisation hyperparameters
- Trees overfit easily (they grow until leaves are pure). Constrain with:
  `max_depth`, `min_samples_split`, `min_samples_leaf`, `min_weight_fraction_leaf`,
  `max_leaf_nodes`, `max_features`; or prune with `ccp_alpha` (cost-complexity).
- Unregularised tree fits training perfectly but generalises terribly;
  `min_samples_leaf=10` fixes the regression example.

## Limitations
- **Axis-aligned splits only** → sensitive to data orientation: a linearly
  separable dataset rotated 45° produces a convoluted, overfit-looking
  boundary. (No natural way to learn oblique splits.)
- **Instability**: small data perturbations can change the whole tree
  (the book's "smallest perturbation" example flips a split).
- Greedy ⇒ can miss the global optimum tree.

## Key takeaways
- Trees = interpretable, assumption-light, scale-free models that need
  regularisation to avoid overfitting.
- Gini (or entropy) drives splits; weights by subset size.
- Axis orientation sensitivity and instability motivate ensembles (ch7).

## Notes
- White-box vs black-box framing: trees explain decisions; random forests
  and neural nets mostly can't (interpretable-ML field exists for this).
- The CART split rule (minimise weighted impurity) is the same pattern the
  book's gradient-boosting trees reuse.
