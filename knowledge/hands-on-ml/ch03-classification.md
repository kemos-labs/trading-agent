# Ch03 — Classification

**Source:** Géron, *Hands-On Machine Learning*, Chapter 3.

## Purpose
Classification done properly on MNIST (70k handwritten digits, 784 pixels
each): binary → multiclass → multilabel → multioutput, and — the bulk of the
chapter — **how to measure classifier performance honestly**.

## Binary classifier (the "5-detector")
- `SGDClassifier` on 60k train images; `y_train_5 = (y_train == '5')`.
- **Shuffle first**: order-sensitivity and fold-representativeness both
  require shuffling (never shuffle time series!).

## Performance measures (the core content)
- **Accuracy is a trap** on skewed data: a dummy classifier always guessing
  the majority class gets 90% on MNIST-5 (only 10% are 5s). Always compare
  against a baseline/DummyClassifier.
- **Confusion matrix** (rows = actual, cols = predicted):
  [[TN, FP], [FN, TP]]. Get clean out-of-sample predictions with
  `cross_val_predict` (k-fold, predictions on held-out folds).
- **Precision** = TP/(TP+FP) — "how many positive predictions are right?"
- **Recall** (sensitivity) = TP/(TP+FN) — "how many actual positives found?"
- **F1** = harmonic mean of precision & recall = 2·P·R/(P+R) — balances
  them; good single number for imbalanced classes.
- **Precision/recall trade-off**: raising the decision threshold raises
  precision, lowers recall. Tune per business need (spam filter wants high
  precision; fraud detection wants high recall). Use
  `precision_recall_curve` + `roc_curve`.
- **ROC curve**: TPR vs FPR across thresholds; **AUC** (area under curve)
  = probability the classifier ranks a random positive above a random
  negative. AUC 1 perfect, 0.5 random. ROC ignores class imbalance;
  precision/recall doesn't.
- Read curves like a dashboard: if a point beats the baseline at every
  threshold, the model is better.

## Multiclass strategies
- **OvR** (one-versus-rest): N binary classifiers, pick highest score —
  Scikit-Learn's default for most algorithms.
- **OvO** (one-versus-one): N(N−1)/2 pairwise classifiers, majority vote —
  preferred by SVC for small datasets.
- `SVC` uses OvO; `SGDClassifier` uses OvR. `OneVsRestClassifier` /
  `OneVsOneClassifier` wrap explicitly. Scaling inputs helps a lot (89%+).

## Error analysis
- Normalise the confusion matrix by row (`normalize="true"`) to compare
  class accuracies; weight errors-only plots with `sample_weight` to see
  which class eats the errors (many digits get misclassified as 8s).
- Plot individual misclassified examples to understand failure modes.
- Improvements flow from analysis: more data for confused classes, better
  features, better preprocessing.

## Multilabel & multioutput
- **Multilabel**: one instance, several binary labels (e.g. is it ≥7 and is
  it odd) — `KNeighborsClassifier` handles natively; `ClassifierChain`
  chains classifiers (each gets previous outputs as features) for better
  label dependence.
- **Multioutput–multiclass**: each label is itself multiclass — e.g. image
  denoising (each pixel output is a value 0–255). The blurry line between
  classification and regression is fine to cross.

## Key takeaways
- Never judge a classifier by accuracy alone on skewed data; use
  confusion matrix, precision/recall/F1, ROC/AUC.
- The decision threshold is a tunable knob, not a law (default 0.5).
- `cross_val_predict` gives clean out-of-sample predictions without
  touching the test set.

## Notes
- MNIST via `fetch_openml('mnist_784', as_frame=False)`.
- These metrics transfer directly to strategy/evaluator work: any binary
  "signal or noise" decision can use precision/recall and ROC/AUC.
