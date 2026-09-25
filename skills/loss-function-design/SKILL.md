# Loss-Function Design (Model the Cost of Errors)

## name
Choosing and fitting the loss function that encodes the real-world cost of
errors — the constant-model baseline, symmetric vs asymmetric losses, and
the mean/median/mode equivalence.

## description
Instead of grabbing squared error by default, make the loss function an
explicit design decision: what does each type of error actually cost in the
domain? The loss defines the model — a constant model fit under squared
loss gives the mean, under absolute loss the median, under 0-1 loss the
mode. For asymmetric costs (e.g. an overdose is worse than an underdose;
a missed trade worse than slippage), build a custom asymmetric loss and
minimize it numerically. This turns "which summary statistic?" and "how
should I penalize errors?" into one principled question.

## when to use it
- Deciding which summary statistic to report (mean vs median vs mode) —
  the choice encodes a loss, whether you intended it or not.
- Any problem with asymmetric error costs: financial (short vs long
  deviations, false positives vs false negatives), medical dosing, fraud
  detection, forecasting (under- vs over-forecast).
- Baseline modeling: before any complex model, fit the constant model as
  the benchmark every richer model must beat.
- Robustness: choosing a loss that down-weights outliers (Huber) instead
  of the SD-dominated squared loss.

## method / formula / code

**1. The loss-defines-the-model result (constant model).**
For data y₁…yₙ, minimize average loss L(θ) = (1/n)Σℓ(yᵢ, θ):

| Loss            | ℓ(y, θ)         | Minimizing θ |
|-----------------|-----------------|--------------|
| Squared         | (y − θ)²        | mean(y)      |
| Absolute        | \|y − θ\|        | median(y)    |
| 0-1             | 1[y ≠ θ]        | mode(y)      |

So "mean or median?" is really "squared or absolute loss?" — pick by what
the summary is for (robustness → absolute/median).

**2. Asymmetric loss (the key pattern).**
Weight errors differently by sign. Example from donkey dosing
(Lau/Gonzalez/Nolan ch18) — overestimating weight is 3× worse than
underestimating, using *relative* error x = 100·(y − ŷ)/ŷ:

```python
def anes_loss(x):
    w = (x >= 0) + 3 * (x < 0)      # overweight penalized 3x
    return np.square(x) * w

# fit by numerical optimization (no closed form):
from scipy.optimize import minimize
loss = lambda theta: np.mean(anes_loss(100 * (y - X @ theta) / (X @ theta)))
theta_hat = minimize(loss, np.ones(X.shape[1]))['x']
```

General recipe: (a) define error in a scale where "10%" means the same
regardless of magnitude (relative error); (b) assign a weight per sign
(and optionally per magnitude) reflecting domain cost; (c) minimize the
average weighted loss with any numerical optimizer.

**3. Robust middle ground: Huber loss.**
Quadratic near 0 (smooth, differentiable), linear in the tails
(outlier-robust): with γ the transition point,
`ℓ(y, θ) = ½(y−θ)² if |y−θ| ≤ γ else γ(|y−θ| − γ/2)`. Gradient:
`−(y−θ) if |y−θ| ≤ γ else −γ·sign(y−θ)`. Minimizer sits between mean and
median (e.g. bus-lateness example: mean 1.92, median 0.74, Huber 0.70).

**4. Classification analog.**
Log loss (cross-entropy) is the natural loss for probabilities; class
imbalance is handled by weighting the smaller class more heavily in the
loss — the classification mirror of asymmetric regression loss.

## known pitfalls
- **Defaulting to squared loss**: it's dominated by outliers and encodes a
  symmetric cost you never chose. Check the tail before committing.
- **Choosing the statistic, then pretending there's no loss**: reporting a
  mean when you need robustness, or a median when you need the expected
  value — the loss should follow the use case.
- **Asymmetric loss + absolute error on scaled data**: weight by sign is
  meaningless if error units differ by magnitude — normalize (relative
  error, z-scores) first.
- **Non-differentiable losses**: absolute/0-1 loss break gradient descent
  — use Huber (differentiable) or subgradient/SGD methods.
- **Fitting constant loss minimizers on skewed data**: mean vs median can
  differ hugely; report the distribution, not just the number.
- **Ignoring the baseline**: always fit the constant model first — if a
  complex model can't beat the loss-minimizing constant, stop.

## source book
Lau, Gonzalez & Nolan, *Learning Data Science* (O'Reilly, 2023): ch4
(mean⇔squared, median⇔absolute, the constant model), ch18 (asymmetric
anes_loss for donkey dosing), ch20 (Huber loss, gradient descent for
non-closed-form losses). Related: Grus ch5–7 (statistics, probability),
Huyen ch3 (evaluation loss design).
