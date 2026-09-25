# Ch08 — Gradient Descent

**Source:** Grus, *Data Science from Scratch*, Chapter 8.

## Purpose
The optimisation workhorse used by every later model: **minimise a function
by repeatedly stepping downhill along its gradient**.

## The idea
- We want `minimize f` for some error/cost function. The gradient
  `∇f(θ)` points in the direction of *steepest increase*; stepping opposite
  to it decreases f.
- **Gradient step**: `θ ← θ − η · ∇f(θ)` where η (eta) is the **learning
  rate** (step size).
- Estimating gradients: either compute the analytic derivative, or use the
  **difference quotient** approximation
  `f'(x) ≈ (f(x + h) − f(x − h)) / (2h)` for a small h (the book implements
  `difference_quotient` and `partial_difference_quotient`).

## Choosing the learning rate
- η too large: steps overshoot, f may diverge/oscillate.
- η too small: convergence is glacially slow.
- The book's pragmatic rule: pick η to be just under the size at which f
  starts bouncing — "if f decreases but then starts jumping, η is too big."

## Using the gradient for a minimisation
Standard loop:
```python
def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0
    while True:
        gradient = gradient_fn(theta)
        next_thetas = [gradient_step(theta, gradient, -step) for step in step_sizes]
        # pick the step size that most decreases the target
        theta = min(next_thetas, key=lambda t: target_fn(t))
        # stop when progress is tiny
        if abs(target_fn(theta) - target_fn(previous)) < tolerance: break
```
This is *gradient descent with line search over step sizes* — robust and
easy; later chapters replace the search with a fixed η (stochastic variant).

## Variants used later
- **Batch gradient descent**: gradient computed over the whole dataset each
  step — accurate but slow for large data.
- **Stochastic / mini-batch gradient descent** (`minimize_stochastic`): take
  a gradient step on one random point (or a small batch) at a time. Much
  faster per step, noisy but effective; this is what `least_squares_fit`
  (ch15) and the neural-net training loops use, with `batch_size`
  parameterising the trade-off.
- **Momentum** (ch18's `Momentum` optimizer): keep a running average of
  gradients `update ← m·update + (1−m)·gradient`, then step by the average —
  smooths out oscillations and speeds convergence.

## Key takeaways
- `gradient_step(theta, gradient, -learning_rate)` is the single primitive
  reused by every fitting chapter (14, 15, 16, 18, 19).
- For a squared error `error²`, the gradient is `2·error·x` — the pattern
  behind linear and logistic regression gradients.
- Always verify with a known optimum (the book asserts the fitted α, β of
  ch14 match the closed form).

## Notes
- Gradient descent avoids needing matrix algebra (ch15 could use closed-form
  least squares but deliberately uses GD).
- Seeding randomness (`random.seed`) keeps experiments reproducible.
