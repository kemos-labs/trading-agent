# Chapter 9 — Linear and Logistic Regression

## Core idea
Two supervised learners used to predict market movement from features:
**linear regression** for continuous targets (next-period return) and
**logistic regression** for classification (up vs down).

## Linear regression
- Model: `y = X·w + b`, fit by minimizing MSE.
- In trading: predict next-period return from lagged features (past returns,
  technical indicators).
- scikit-learn: `from sklearn.linear_model import LinearRegression; fit; predict`.

## Logistic regression
- Despite the name, a **classifier**: outputs the probability
  `P(y=1) = sigmoid(w'X + b)`; predict class 1 if probability > 0.5.
- Target: direction, e.g., `1 if next_return > 0 else 0` (the book maps
  predictions to `+1/-1` positions).
- Regularization parameter `C`: **inverse** of regularization strength — small
  `C` = more regularization, large `C` = less. High `C` on noisy financial
  features overfits; moderate `C` shrinks weights toward 0.

## Common pipeline (used for every ML chapter)
1. Feature engineering: lagged returns, moving averages, etc. (ch10).
2. Target: next-period sign (classification) or return (regression).
3. Train/test split **before** any scaling.
4. `StandardScaler` fit on train, transform on test (never fit on test).
5. Fit → predict → build strategy `sign(prediction) * returns` → backtest
   with the ch4/ch5 metrics.

## Pitfalls
- **Leakage**: scaling or feature engineering before the split leaks test
  information.
- Class imbalance: if up-days ≈ down-days, accuracy is near 50% and any edge
  is small; evaluate with the strategy backtest, not raw accuracy.
- Linear models can't capture nonlinear interactions — that's the motivation
  for SVM (ch11) and ensembles (ch12).

## Bottom line
These are the baseline learners the book compares everything against. The
workflow — features → scaler fit-on-train → fit → sign-of-prediction
strategy → backtest — is the identical skeleton used by SVM, trees, and DNNs
in the following chapters.
