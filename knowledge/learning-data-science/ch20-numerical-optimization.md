# Ch20 — Numerical Optimization

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 20.

## Purpose
Fitting models with **no closed-form solution** (lasso, logistic,
asymmetric losses): **gradient descent** and its variants, plus Newton's
method.

## Why not grid search
- Grid over p features with 100 values each = 100ᵖ evaluations
  (100,000,000 for p=4) — combinatorial explosion, plus range specification
  and wasted computation. Gradient descent uses the loss's *shape* instead.

## Gradient descent
- Idea: the loss is locally linear; the gradient ∇L(θ) points uphill, so
  step against it: θ ← θ − α·∇L(θ), for learning rate α > 0.
- Convergence requires the average loss to be **convex** (no local minima;
  chord-above-function) and **differentiable**. Convexity guarantees the
  global minimum is reachable with a suitable α.
- Choosing α: too small = many steps; too large = overshoot/diverge.
  Decaying schedules α(t) help.
- Stop when θ stops changing (e.g. < 0.001) or after a max iteration count
  (divergence check).

## Example: Huber loss on bus delays
- **Huber loss**: quadratic near 0, linear in the tails:
  `½(y−θ)² if |y−θ| ≤ γ else γ(|y−θ| − γ/2)` — differentiable (unlike
  absolute) yet outlier-robust (unlike squared).
- Gradient: `−(y−θ) if |y−θ| ≤ γ else −γ·sign(y−θ)`.
- Fitting the constant model by GD gives θ̂ ≈ 0.70 (close to the median
  0.74) — robust to the long tail.

## Variants
- **Stochastic (SGD)**: gradient at one random point per step — noisy but
  cheap; shuffling data first is critical; an epoch = one pass. Converges
  "on average."
- **Mini-batch**: average gradient over a random batch — the practical
  middle ground used in deep learning.
- **Newton's method**: uses the second derivative (Hessian H) to fit a
  quadratic approximation: θ ← θ − H⁻¹g. Faster near the optimum for
  smooth problems; expensive per step; needs a well-conditioned Hessian.
- In practice: use `scipy.optimize.minimize` (automatic differentiation
  not required — it's derivative-free or numerical) rather than hand-rolled
  GD.

## Key takeaways
- GD = "follow the negative gradient"; its guarantees rest on convexity +
  differentiability + a sane learning rate.
- Loss design (Huber, asymmetric anes_loss) is free — any differentiable
  loss can be minimized by GD.
- SGD/mini-batch scale to big data; Newton accelerates smooth small
  problems.

## Notes
- Used everywhere in the book: ch18's asymmetric donkey loss,
  ch19/ch21's logistic regression (LogisticRegressionCV, solver='saga' =
  SGD variant), lasso (ch16).
- Deep learning (Géron's book, our hands-on-ml notes) is essentially
  mini-batch SGD + autodiff.
