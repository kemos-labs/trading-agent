# Ch11 — Machine Learning

**Source:** Grus, *Data Science from Scratch*, Chapter 11.

## Purpose
The conceptual foundation of machine learning: what models are, the two
model families, and the central problem of **overfitting**.

## Types of models
- **Supervised**: learn a function from labelled examples —
  - **Classification**: predict a discrete label (spam/ham, species).
  - **Regression**: predict a number (minutes on site).
- **Unsupervised**: find structure in unlabelled data — clustering (ch20),
  dimensionality reduction (ch10).
- **Reinforcement** (mentioned): learn by acting and receiving rewards.

## The modelling process
1. Split data into **training set** (fit the model) and **test set**
   (evaluate). The book's `split_data(data, prob)` shuffles and assigns
   ~70% to train.
2. Fit on train, evaluate on test with a metric (accuracy for
   classification, squared error for regression).
3. Iterate: choose model/hyperparameters, fit, evaluate.

## Overfitting — the chapter's core warning
- **Overfitting**: a model that memorises training data noise instead of the
  underlying pattern → great train accuracy, poor test accuracy.
- The mechanism: every added degree of freedom (extra polynomial term, extra
  feature, smaller k in k-NN) can fit the training set better *and* generalise
  worse.
- The book's demo: fitting polynomials of increasing degree to the same data;
  degree-9 wiggles through every training point but predicts badly. "A
  complex model is a sign of overfitting, not of cleverness."
- **Correctness measures**: evaluate on data the model never saw. The train
  accuracy is a lie; only the test (or validation) number counts.
- Foreshadowing: the more hypotheses you try, the more likely one looks good
  by chance (ties to ch7's multiple testing; Carver's rule-fitting tables).

## Model/algorithm families introduced (previews)
- k-Nearest Neighbours (ch12), Naive Bayes (ch13), regression (ch14–16),
  decision trees (ch17), neural nets (ch18–19), clustering (ch20).

## The bias–variance trade-off (the intellectual core)
- **Bias**: error from a model that's too simple to capture the pattern
  (underfitting).
- **Variance**: error from a model that's too flexible and chases noise
  (overfitting).
- Total test error ≈ bias + variance + irreducible noise. You trade one for
  the other; the best model sits where the sum is smallest. This is the
  chapter's most important concept and it recurs everywhere.

## Key takeaways
- **Always hold out a test set**; never judge a model on its training
  performance.
- Simple models that generalise beat clever models that memorise.
- Bias–variance trade-off: flexibility helps up to a point, then hurts.

## Notes
- No new formulas; the chapter is conceptual setup.
- `split_data` + the train/test pattern is used verbatim in ch12 (Iris) and
  ch23 (MovieLens).
