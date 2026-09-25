# Ch16 — Supervised Learning

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 16.

## Two core supervised tasks
- **Classification**: assign a feature vector to a categorical group (binary e.g. disease/no; or
  asset-rises/falls tomorrow from N-feature history). y categorical over a finite set K.
- **Regression**: estimate a *real-valued* response from features (e.g. sales from ad budgets;
  predict tomorrow's asset value). y ∈ R.

## Two mathematical formalisms
1. **Function-estimation**: true response modelled as a function f(x) plus noise:
   **y = f(x) + ε**  (16.1). Goal: find f̂ best approximating f, then any new ŷ(x_test) = f̂.
2. **Probabilistic**: reframe as estimating a conditional distribution **p(y | x; θ)**: the
   probability y takes a value/category given features x under model parameters θ. Percents can
   be assigned to every value → more general way to choose among them.

### Classification estimate (MAP)
**ŷ = f̂(x) = argmax_{k∈K} p(y=k|x)**  (16.2) — the **Maximum A Posteriori (MAP)** estimate.
> Practical caveat for finance: consequences of a wrong pick can be severe (big losses), so
> don't just take the argmax — use a *probability threshold* so a prediction is only acted on
> when its probability is much higher than alternatives.

Common classifiers: Logistic Regression (misleading name), Naive Bayes, SVMs, deep CNNs.
Classification used esp. for **document classification** (later NLP chapter).

## Regression estimate
Same goal but preserve real-valued; choose the mode of the distribution over ℝ.
Common techniques: Linear Regression, Support Vector Regression, Random Forests.
Used for asset-price prediction (intraday trading chapter later).

### Concrete example
Model tomorrow's price of Royal Dutch Shell (LSE:RDSB) from historical crude-oil (c_ij) and
natural-gas (g_ij) prices: feature vector x_i = lagged prices of both over N days; response
y_i = RDSB price tomorrow (i+1). Goal: estimate the mapping f.

## Loss functions & training
Define a **loss** quantifying mismatch between true y_i and estimate ŷ_i:
- Classification: 0–1 loss, cross-entropy.
- Regression: **Mean Squared Error (MSE)**:  **MSE = (1/N) Σ (y_i − ŷ_i)²**  (16.3). Penalises
  far-away values heavily (squares deviations; ignores sign).
Training = adjust model params θ to minimise loss.

## Bias-variance & overfitting (core warning)
Minimising loss too aggressively on training data → **overfitting** to noise → poor
generalisation. The bias–variance tradeoff is crucial in quant trading: a badly-fit/overfit
model in production can cause substantial losses; much professional quant research is spent
avoiding overfit. (Full treatment in the cross-validation chapter.)

## Takeaways
- Supervised learning = classification (discrete) + regression (real-valued).
- Estimation can be framed functionally or probabilistically (conditional distribution).
- MAP argmax for classification; use thresholding in finance to avoid acting on weak signals.
- MSE penalises large errors; training minimises loss; guard against overfitting.