# Ch19 — Classification

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 19.

## Purpose
Predicting **nominal outcomes**: the constant classifier, **logistic
regression**, and evaluation metrics (accuracy, confusion matrix,
precision/recall) via the wind-damaged-trees (windthrow) example.

## From regression to classification
- Same recipe as regression: model + loss + fit + evaluate — but the model
  is nonlinear, the loss is log loss, and errors come in two kinds.
- **Constant model**: predict the most common class; average 0-1 loss =
  error rate (35% for windthrow: 65% standing). Baseline every real model
  must beat.

## Logistic regression
- Model probability p = σ(θ₀ + θ₁x), σ(t) = 1/(1+e^(−t)).
- **Log odds**: log(p/(1−p)) = θ₀ + θ₁x — linear in x. A unit increase in
  x multiplies the odds by e^θ₁.
- **Log loss** (cross-entropy): ℓ(p,y) = −y·log(p) − (1−y)·log(1−p).
  Minimizing it over a constant gives p̂ = n₁/n (the class proportion);
  for features, minimize via numerical optimization (ch20, no closed form).
- sklearn: `LogisticRegression` / `LogisticRegressionCV` (CV-chosen
  regularization).

## From probabilities to decisions
- Default decision rule: predict 1 if p > 0.5 (τ = 0.5). The best τ may
  differ — tune it with CV.
- **Class imbalance** skews τ and accuracy: if 1% fraud, always-predict-0
  gets 99% accuracy yet is useless. Fixes: resample, or penalize the
  smaller class more in the loss.

## Evaluation
- **Confusion matrix**: TP/FP/FN/TN — the four possible outcomes; compare
  counts, then rates.
- **Accuracy** = (TP+TN)/n — misleading under imbalance.
- **Precision** = TP/(TP+FP) — of predicted positives, how many are right.
- **Recall** = TP/(TP+FN) — of actual positives, how many found.
- Choose per domain cost: ch21's fake-news case prefers precision
  (don't mislabel real news as fake); medical screening wants recall.
- Precision/recall trade off via τ.

## Key takeaways
- Logistic regression outputs *probabilities*; the threshold is a separate
  decision, tunable and domain-dependent.
- Accuracy alone is never enough; always look at the confusion matrix and
  the class balance.
- Log loss ties to likelihood: fitting = maximum likelihood estimation.

## Notes
- Windthrow data: fallen trees are bigger (12 cm vs 6 cm) and in stronger
  storms — both features drive the model: σ(−7.4 + 3.0·diameter).
- ch21 applies logistic + tf-idf to fake news and reads coefficients as
  odds multipliers per word.
