# Ch18 — Tree-Based Methods (DT/CART & ensembles)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 18.

## Decision Trees / CART
Supervised technique learning decision *rules* from features (regression or classification).
A DT/CART is an **adaptive basis-function model**: the basis/features are learned *from the
data* (vs fixed expansions). Unlike linear regression it is **nonlinear in parameters** → only a
*local* (not guaranteed global) optimum of the MLE can be computed.

Mechanism: partition feature space R^p into simple **axis-parallel rectangular regions**; the
prediction for an observation = **mean** (regression) or **mode** (classification) of the training
samples in its region.

Model (probabilistic adaptive-basis form): **f(x) = Σ_{m=1}^M w_m 𝟙(x∈R_m)**, w_m = mean
response in region R_m; splits defined by thresholds on each feature (v).

**Growing the tree — Recursive Binary Splitting (RBS)**:
- Minimise **Residual Sum of Squares (RSS)** = Σ_m Σ_{i∈R_m}(y_i − ŷ_{R_m})².
- Exhaustive search over all partitions is NP-complete → use a *greedy* approach: start at the
  top, split into two branches repeatedly, at each step choose the split minimising current RSS.
  Greedy = evaluate at each recursion rather than look ahead — computationally feasible.
- **Stopping criteria**: max depth, min samples-per-region, region homogeneity ("balance").
- Overfitting danger → **prune**. **Cost-complexity pruning**: add tuning param α balancing
  tree depth vs training fit (like LASSO/Tibshirani). He al library abstracts it (sklearn).

**Classification trees**: predict category = *mode* of region. Splitting metric ≠ RSS:
- **Hit Rate** = fraction of training obs in region not in the most common class
  (error-rate / misclassification).
- **Gini Index** (region purity): Gini = Σ_c π̂_mc(1−π̂_mc); lower = purer (mostly one class).
- **Cross-Entropy / Deviance**: −Σ_c π̂_mc log π̂_mc.
  Gini & Deviance used more than hit-rate for accuracy.

**DT pros/cons**:
- Pros: interpretable if-then-else rules; handle mixed categorical+continuous features;
  automatic feature selection (no subset selection).
- Cons: **unstable / high-variance** (small data changes → big tree changes); poor standalone
  prediction accuracy. → Excellent in ensembles.

## Ensembles
**The Bootstrap** (frequentist resampling): sample *with replacement* to generate multiple
training sets — crucial because in finance there's only ONE price history (can't get more data).
Used to reduce variance of meta-learners.

### Bootstrap Aggregation (Bagging)
DTs are high-variance; average many trees over B bootstrapped samples:
**f̂_avg(x) = (1/B) Σ_b f̂_b(x)** — variance reduced ~ /N (if iid with var σ², mean variance
σ²/N). Grow hundreds/thousands of deeply-grown (non-pruned) trees, average → big variance cut.
- **Cannot overfit by increasing B** (true for bagging *and* RF, NOT boosting).
- Cost: reduced interpretability.

### Random Forests (RF)
Bagging + **feature bagging**: at each split *randomly* select a subset of the p features, then
CART. This deliberately reduces **correlation** between trees (avoids all trees using one strong
feature). If p selected → plain bagging. **Rule of thumb: use ~√p features** at each split.

### Boosting
Different: no bootstrap; models built **sequentially**, each fits the *residuals* of the current
ensemble:
1. Init f̂(x)=0, residuals r_i = y_i.
2. For b=1..B: (a) fit tree to residuals r_i; (b) accumulate **f̂ ← f̂ + λ f̂_b** (shrinkage).
3. Final f̂ = Σ_b λ f̂_b.
- Learns "slowly", improving weak spots. **Hyperparameters**: tree depth k, # boosted trees B,
  shrinkage rate λ (set by cross-validation).
- **Boosting CAN overfit with too many estimators** (unlike bagging/RF) — important pitfall.
- Sequential ⇒ not parallelisable (bagging/RF are).

## Applied example: predict AMZN daily returns from 3 lagged returns (sklearn)
- Build `create_lagged_series` DataFrame (today/lag1-3 returns, volume); create returns via
  `pct_change()*100`, drop NA, `scale()` to [−1,1]; train/test 70/30.
  **Caveat**: financial returns are serially correlated ⇒ train/test samples aren't truly
  independent (introduces error — noted as a limitation).
- Compare BaggingRegressor, RandomForestRegressor, AdaBoostRegressor (decision-tree base) MSE
  over 1–1000 estimators (step 100), learning_rate λ=0.01 for AdaBoost.
- Result: bagging & RF MSE **settles down** with estimators (no overfit, converge together);
  AdaBoost **overfits** as estimators increase past ~100 → MSE rises.
- For a boosting-based strategy, keep # estimators modest or MSE/performance degrades.

## Takeaways / pitfalls
- Prefer ensembles of DTs (low-bias, high-variance) over single DTs.
- Use √p feature per RF split; monitor boosting #estimators to avoid overfit.
- Tree ensembles auto-select features but are hard to interpret; fine for trading research.
- Only-of-one history + no new data → bootstrap is key for variance reduction here.