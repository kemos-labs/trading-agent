# Ch07 — Linear Models: From Risk Factors to Return Forecasts

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 7.

## Purpose
The workhorse of quantitative finance: linear regression and its regularized variants, from Fama-French factor models to ML-style shrinkage, and how to use them for return/direction forecasts.

## Regression as the financial baseline
- Model: y = Xβ + ε; OLS minimizes ‖y − Xβ‖².
- **Fama-French factor models**: excess return = α + β_m·MKT + β_smb·SMB + β_hml·HML + …; α is the strategy's true skill after factor exposure is removed.
- **Interpretation**: coefficients are conditional sensitivities; t-stats and standard errors matter (use robust/HAC standard errors for serial-correlated financial residuals).

## From returns to probabilities
- **Logistic regression** for direction/event prediction: p = σ(Xβ), cross-entropy loss; odds ratios e^β interpretable.
- Evaluation: AUC, precision-recall; threshold choice is a decision (see `loss-function-design`).

## Regularization (the ML upgrade)
- **Ridge (L2)**: penalize ‖β‖²; shrinks coefficients, handles collinearity — good when many correlated features.
- **Lasso (L1)**: penalize ‖β‖₁; drives coefficients to zero → feature selection; unstable with highly correlated groups.
- **Elastic net**: λ₁‖β‖₁ + λ₂‖β‖²; combines both — the practical default.
- Regularization strength tuned by cross-validation (α/C hyperparameter); bias-variance sweet spot (ch6).

## Practical considerations for financial data
- **Standardize features** (z-score) so penalties treat them fairly; fit scaler on train only.
- **Collinearity**: financial factors are correlated; ridge/elastic-net handle it; inspect variance inflation.
- **Nonlinearity**: linear models miss interactions — add engineered interaction terms or move to trees/NNs; check residuals for patterns.
- **Stationarity**: run on returns/differenced series, not levels (see `arma-garch-modeling`).

## Feature engineering for linear models
- Alpha factors from ch4 as features; demean/neutralize (industry, size, beta).
- Time-lagged features, dummy variables for regimes/days, and rolling statistics (see `time-series-feature-engineering`).

## Worked use cases in the book
- Predicting daily/weekly returns from factor exposures; evaluating IC and quintile spreads.
- Logistic classification of up/down moves with AUC evaluation and walk-forward splits.
- Using factor model α (after hedging market beta) as the strategy signal.

## Key takeaways
- Linear models give transparent, robust forecasts and the statistical machinery (α, t-stats) finance is built on.
- Regularization + proper scaling + honest CV close most of the gap to fancier models on tabular data.
- Always report α *after* common-factor adjustment — raw strategy returns are mostly beta.
