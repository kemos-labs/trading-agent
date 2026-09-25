# Ch04 — Modeling with Summary Statistics

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 4.

## Purpose
Introduces model fitting through **loss minimization** using the simplest
model: the **constant model**, which summarizes the outcome by one number θ.

## The constant model
Given data y₁…yₙ and candidate constant θ, the model's error for yᵢ is
yᵢ − θ. Pick θ to minimize **average loss** over the data.

Two classic loss functions:
- **Squared loss** ℓ(θ, y) = (y − θ)². Minimizing average squared loss
  gives **θ̂ = mean(y)**.
- **Absolute loss** ℓ(θ, y) = |y − θ|. Minimizing average absolute loss
  gives **θ̂ = median(y)**.

So "which summary statistic?" becomes "which loss function?" — a key
reframing. The bus-lateness example: mean 1.92 min, median 0.74 min — the
distribution is skewed, so the median (absolute loss) is the robust choice
for "typical" lateness.

## The modeling recipe (used for every later model)
1. Choose a **model** (a family of functions: constant, line, logistic…).
2. Choose a **loss function** measuring how wrong the model is per
   observation.
3. **Fit**: minimize the average loss over the training data to get θ̂.
4. **Evaluate**: assess fit on held-out data (later chapters) and inspect
   residuals.

## Signal vs noise
- Data = signal + noise. The model approximates the signal; loss measures
  the leftover noise.
- Adding model complexity always reduces training loss — so training loss
  alone can't choose complexity (that's ch16's overfitting problem).

## Key takeaways
- Mean ⇔ squared loss; median ⇔ absolute loss; mode ⇔ 0-1 loss. Your choice
  of statistic silently encodes a loss function.
- Loss functions are the bridge from "what do I want?" (domain cost of
  errors) to "what θ do I fit?" — asymmetric losses come in ch18.
- All supervised modeling in the book is the same recipe: model + loss +
  minimize + evaluate.

## Notes
- The constant model is not trivial: it's the baseline every richer model
  must beat, and it powers the "R²-style" comparisons in ch15 (SD of
  residuals vs SD of outcome).
- Analytic minimization (derivative = 0) works here; numerical optimization
  (gradient descent) arrives in ch20 for models without closed forms.
