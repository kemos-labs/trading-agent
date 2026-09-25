# Chapter I.4 — Introduction to Linear Regression

## Core idea
The linear regression model — the workhorse for modelling one random
variable's dependence on others: OLS estimation, hypothesis testing, the
assumptions and their violations (autocorrelation, heteroscedasticity), and
financial applications (CAPM, index models, hedging).

## The model
- Multiple linear model: `Y = β1·X1 + β2·X2 + ... + βk·Xk + ε`.
- Y = dependent variable; X's = explanatory (independent) variables; β's =
  coefficients (effects); ε = error process.
- Used to: forecast Y from scenarios on X; test economic/financial theory;
  estimate hedge quantities for portfolios and trading strategies.
- Data: time series (t), cross-sectional (i), or panel (i,t).

## Simple linear regression
- `Y = α + βX + ε` — intercept α, slope β; the error term lets points
  deviate from the line.
- Scatter plot of (X,Y); fitted line; caret (^) denotes estimators.
- Example: Amex vs S&P 500 daily log returns — a single-index model.

## OLS estimation
- Minimize the sum of squared residuals (vertical distances to the fitted
  line).
- In matrix notation: `β̂ = (X'X)⁻¹X'Y` — the multivariate generalization.
- ANOVA (analysis of variance) decomposes total variation into explained
  (regression) and unexplained (residual).

## Assumptions and properties of OLS
- Standard OLS assumptions on the error process (zero mean, constant
  variance, no autocorrelation, independent of X).
- Under these: OLS estimators are unbiased and (Gauss-Markov) BLUE —
  best linear unbiased estimators.
- **Hypothesis testing**: t-tests on coefficients (is β significantly
  different from 0?); F-tests on the model; confidence intervals for
  coefficients; R².

## Violations of assumptions
- **Autocorrelation** (serial correlation of errors) and
  **heteroscedasticity** (non-constant error variance) — tests for both.
- With large samples + robust standard errors, OLS is fine; with small
  samples, use **generalized least squares (GLS)**.
- **Multicollinearity**: highly correlated explanatory variables inflate
  coefficient standard errors — detect and deal with it.

## Financial applications
- CAPM / single-index model: stock returns regressed on index returns →
  beta (systematic risk).
- Hedging: regress asset returns on hedging instruments to estimate hedge
  ratios.
- Factor models, event studies, forecasting.

## Pitfalls
- Spurious regression: regressing non-stationary series on each other gives
  misleadingly high R² (needs care with trends).
- Correlation ≠ causation; omitted variables bias.
- Multicollinearity: correlated regressors make individual coefficients
  unreliable even if the model fits well.

## Bottom line
OLS is the estimation workhorse: the matrix formula β̂ = (X'X)⁻¹X'Y, the
BLUE property under classical assumptions, and the diagnostic toolkit
(autocorrelation, heteroscedasticity, multicollinearity) that the later
volumes rely on for GARCH, VaR, and factor models.
