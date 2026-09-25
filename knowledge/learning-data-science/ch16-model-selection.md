# Ch16 — Model Selection

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 16.

## Purpose
Why more features ≠ better model (**overfitting**), and the three formal
tools to choose model complexity: **train-test split, cross-validation,
and regularization**.

## Overfitting
- Training MSE always falls as features are added (projection geometry,
  ch15) — so training error can't choose a model.
- Overfit models chase noise in the training data; they bend strangely and
  predict new data badly (the 12th-degree polynomial on gas-consumption
  data wiggles through points).
- The energy example: quadratic fits well; degree-12 "fits" perfectly but
  generalizes terribly. High-degree raw polynomials also create correlated
  features and ill-conditioned design matrices — prefer orthogonal
  polynomials.

## Train-test split
- Hold out a **test set** used exactly once, after committing to a model.
- Evaluate: fit on train, MSE on test. Test MSE is a valid estimate of
  generalization error; training MSE is not.
- Never iterate on the test set — you'll overfit *it* (use a validation
  split for iteration, or CV).

## Cross-validation (k-fold)
- Split the *training* data into k folds; for each fold, fit on the other
  k−1 and evaluate on the held-out fold; average errors across folds to
  choose the model form (degree, feature set, regularization strength).
- k = 5 or 10 typical; k = n is leave-one-out (LOO).
- After choosing the form via CV, refit on all training data and evaluate
  once on the test set. sklearn: `KFold`, `cross_val_score`.
- CV costs computation (k refits) but uses data efficiently — essential
  when data are scarce.

## Regularization
- Penalize large coefficients to constrain model complexity:
  - **Ridge**: add λ·Σθⱼ² (L2) — shrinks coefficients smoothly.
  - **Lasso**: add λ·Σ|θⱼ| (L1) — drives some coefficients to zero
    (feature selection).
- λ (penalty strength) is chosen by CV; no closed form for lasso ⇒
  numerical optimization (ch20).

## Bias–variance trade-off
- **Bias**: error from model simplicity (underfitting). **Variance**:
  error from model instability across samples (overfitting).
- Complexity ↑ ⇒ bias ↓, variance ↑; the sweet spot minimizes total test
  error — the U-shaped test-error curve.

## Key takeaways
- Test set: touch once. CV: for model choice. Training error: never for
  choice.
- Prefer the simplest model with comparable error (Occam, built into the
  book's practice).
- Regularization trades a little bias for a lot of variance.

## Notes
- Ch17 supplies the theory (sampling distributions) behind why train/test
  errors differ; ch20 supplies gradient descent used to fit lasso/logistic.
- ch21's fake-news case study applies CV + regularization + tf-idf
  end-to-end (LogisticRegressionCV).
