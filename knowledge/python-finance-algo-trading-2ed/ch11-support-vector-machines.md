# Chapter 11 — Support Vector Machines

## Core idea
SVM finds a decision boundary with maximum margin between classes; with the
kernel trick it captures **nonlinear** patterns that linear/logistic
regression miss. SVR (Support Vector Regression) is the regression variant.

## Key concepts
- **Max-margin classifier**: maximize the distance between the separating
  hyperplane and the nearest training points (support vectors).
- **Kernel trick**: map features into a higher-dimensional space implicitly
  (RBF/polynomial kernels) to separate classes that are not linearly
  separable in the original space.
- **SVR**: fits a tube of width `epsilon` around the data — errors inside
  `epsilon` cost nothing, outside are penalized. `epsilon` trades
  flatness vs fit (the book uses `epsilon=1.5` on scaled features).

## Trading use
- Predict next-period direction (SVC) or return (SVR) from the ch10 features;
  strategy = `sign(prediction) * returns`, backtested as usual.
- In ch16's project, SVR is one of the three diverse learners (with linear
  regression and decision trees) run across 150 assets — diversity of model
  class is used deliberately so the ensemble of strategies is more robust.

## Hyperparameters
- `C`: penalty on misclassification / margin violation — high C = fit
  training hard (risk overfitting), low C = smoother boundary.
- `kernel='rbf'` with `gamma`: gamma controls the influence radius of each
  support vector; too large → overfit.
- `epsilon` (SVR): tube width — larger = more robust, smaller = fit harder.

## Pitfalls
- SVMs require **scaled features** (StandardScaler) — distances across
  features are the whole game.
- Costly on large datasets; not the first choice for big time series.
- Black-box boundary: hard to explain which features drive the decision
  (a real constraint for regulated trading).

## Bottom line
SVM/SVR is the book's canonical *nonlinear* baseline. It belongs to the same
skeleton as ch9 (features → scaler → fit → sign-trade → backtest), and the
knowledge base's existing ML notes (`knowledge/halls-moore.../ch19-svm.md`)
cover the theory this chapter applies with scikit-learn.
