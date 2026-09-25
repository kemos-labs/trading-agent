# Ch20 — Model Selection & Cross-Validation

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 20.

## Model selection vs regression baseline
Supervised **regression** setting: model y = f(x) + ε (ε ~ Normal(0, σ_ε²)). x = predictors
(e.g. lagged prices/returns), y = response (tomorrow's price/return). f estimated → f̂
(linear regression, SVM, splines, trees…). There is **no universally best model** (No Free Lunch)
— pick the "best" for the data/problem at hand.

**Loss function** L(y, f̂(x)) compares predictions to truth (non-negative; 0 = perfect). Common
choice: **squared error** (y − f̂(x))². Aggregate → **training MSE** = (1/n)Σ(y_i − f̂(x_i))².

**Key problem**: training MSE (computed on fit data) is of little interest — we care about
**generalisation** to unseen data. Quantified by **test MSE** = E over all future (x₀,y₀) of
(y₀ − f̂(x₀))². Want the model with the **lowest test MSE**. But test MSE is hard to compute
when data is scarce; quant trading is usually data-rich (can hold out train/test).

**Why not just pick lowest training MSE?** Because a highly flexible model can drive training
MSE → 0 while generalising poorly → **overfitting** (fitting noise, not signal).

## The bias–variance tradeoff
Flexibility = model DoF to fit training data. Example: fitting y=sin(x) with simulated noise;
compare linear (2 DoF), cubic (m=3), high-degree polynomial (m=20).
- **Training MSE** decreases monotonically with flexibility.
- **Test MSE** is U-shaped: falls as flexibility rises then **rebounds (overfit)** — an intrinsic
  supervised-ML property.

**Mathematical decomposition** (squared-error loss at test point x₀):
E[(y₀ − f̂(x₀))²] = **σ²_ε + Bias(f̂(x₀))² + Var(f̂(x₀))**
- **Irreducible error** σ²_ε: lower bound on expected test MSE (no model can beat it).
- **Bias²**: gap between the *average* of predictions (across test sets) and the true mean value.
  High bias = model doesn't capture the true form (e.g. line on a sine ⇒ underfitting).
- **Variance**: model sensitivity to different training sets τ. High = overfit.

Flexibility ↑ ⇒ variance ↑, bias ↓. Test MSE bottoms where the two balance (bias drop slows
after a point). **Goal: choose the model minimising expected test MSE.**

## Cross-validation
CV estimates test error better than training error. Randomness/time isn't financially sound,
but CV is a key deviation.
**Validation-set approach**: split n obs randomly into two halves → fit on train set, estimate
test error on random set. Two-thirds/one-third chronological split common in trading.
Problems: (1) **high variance** of the estimate (due to randomization → can underestimate true
error via lucky split); (2) using only half the data under-trains the model (may
*overestimate* test error). (3) financial time series are **serially correlated / not iid** →
random splitting isn't strictly valid.

**k-fold CV**: divide n obs into k approximately equal **folds**. Repeatedly: hold out one fold
as validation, train on the other k−1. Test estimate:
**CV_k = (1/k) Σ_i MSE_i** (average of fold test errors). Repeated k times, each fold held out.
Choose **k=5 or k=10** (empirically).

### Leave-One-Out CV (LOOCV) — k=n
Fit n times, each leaving out a single observation. Reduces bias (nearly all data used to fit
each), but **high variance** (test error computed on a single response each). k-fold improves vs.
random-split by lowering variance (at some slight bias).

## Application on Amazon (OHLC + lagged returns)
- `create_lagged_series(symbol, start, end, lags)`: extract daily OHLC + volume; build columns
  Lag1..Lagn = close-to-close **% returns** (reflect via pct_change*100; replace ~0 returns with
  0.0001 to avoid QDA numerical issues in sklearn); add **Direction** = sign(Today) for
  classification models.
- Predictors = 10 lagged returns of AMZN (2004-01-01 → 2016-10-27); response = today's return.
- Use polynomial-feature pipeline + linear-regression to vary flexibility (degrees d=1..3).

### Validation-set demo
`train_test_split` 10 random seeds; for each: model over degrees; plot MSE curves + average.
Result: **same curves vary substantially across seeds**; low/indistinct signal in AMZN returns →

### k-fold demo (KFold k=10)
Same procedure, iterate over folds. **Curves far less variable** across folds than validation
approach- CV gives a good estimate of true test MSE, at slight bias cost.

## Takeaways / pitfalls
- Choose model by **minimum expected test MSE**, not training MSE (overfitting trap).
- **Decompose test MSE** into irreducible + bias + variance; flexible models: var↑/bias↓.
- Prefer **k-fold (usually k=10)** over naive validation set (less variance; retention of
  repeated looks).
- Always account for serial correlation in financial returns: random CV splits aren't strictly
  iid-valid; keep temporal order where possible.
- For trading, CV is used to pick model type AND to tune flexibility (degree/C/λ etc.).