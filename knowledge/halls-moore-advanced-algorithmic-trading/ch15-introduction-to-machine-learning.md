# Ch15 — Introduction to Machine Learning

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 15 (survey).

## What ML is & why for quants
Machine learning couples statistics + computer science; algorithms *learn tasks* (prediction,
classification) without being explicitly programmed. In quant finance: predicting asset prices,
optimising strategy parameters, risk management, detecting... Uses in industry (Man AHL,
D.E. Shaw) are largely proprietary. Applied to: liquidity prediction, image classification
(e.g. satellite/commodity supply-demand signals), etc.

## Three learning categories
1. **Supervised learning** — uses *labelled* data (categories → classification, or numerical
   responses → regression). Train on labelled data, then predict on unseen data. E.g.
   predict tomorrow's price from past month's prices.
2. **Unsupervised learning** — no labels; finds patterns in underlying structure (canonical:
   clustering). E.g. clustering assets into correlated groups. Harder — no supervision/fitness.
3. **Reinforcement learning** — act in an environment to maximise a reward (no paired
   input/output). Famous for DeepMind's Atari/AlphaGo; applies to portfolio optimisation.
   Out of scope in this book.

## Common algorithms (quick map)
- **Linear regression** (classical statistics) — optimal linear response.
- **Classification**: Logistic Regression, LDA, Naive Bayes.
- **Decision trees** — partition feature space into hypercubes; ensembles: Random Forests,
  Gradient Boosted trees.
- **SVMs** — linear separator in a *higher-dimensional* space to handle non-linear separation.
- **Neural networks / deep networks** — hierarchy of activation neurons approximating
  non-linear functions.
- **Naive Bayes nets** (probabilistic graphical models) — inference & learning.
- **Clustering** (unsupervised) — partition into subsets.
- **Dimensionality reduction / PCA** — reduce factors explaining variation.

## ML domains applied to quant finance
- **Asset price prediction** — accuracy depends on data quality/availability, asset/market,
  time frame. Single-point or multi-step ahead (daily S&P500, intraday FX spreads, liquidity
  via order-book dynamics).
- **NLP** — quantifying structured language; **Sentiment Analysis** (bullish/bearish) and
  **Entity Extraction**; combined → strong trading signals (often social-media/news based, e.g.
  the later Sentdex chapter).
- **Factor modelling** — describe variation of many correlated observed variables via fewer
  unobserved **factors**: (1) macroeconomic (GDP, rates), (2) fundamental (book value, market
  cap), (3) latent/statistical (estimated from returns). Linked to dimensionality reduction/PCA.
- **Image classification** (CNN/deep learning) — alternative data: satellite imagery of oil tank
  heights, maritime freight → supply/demand for crude.

## Overfitting & bias-variance
Increasing model flexibility lowers training error but risks **overfitting**: aligning to
"noise" instead of "signal", harming generalisation → a bias–variance tradeoff. Mitigation:
**cross-validation** (split data into random subsets, fit & assess each, average) — length.
discussed later (model selection chapter).

## Parametric vs non-parametric
- **Parametric**: assumed form f with parameters. Canonical: linear regression, β=(β_0..β_p),
  fit by MLE (OLS for regression). Fewer data needed; under good design forms effective trading
  models; but over-parameterising → overfit.
- **Non-parametric**: no fixed parameter form; greater flexibility, needs *much more* training
  data, prone to overfitting. Example: **k-nearest-neighbours** (mode/mean of k nearest points;
  k is a **hyperparameter**, tuned by cross-validation). Given financial data's poor signal/noise
  ratio, non-parametric models are easy to overfit.

## Statistical framework
- Supervised: (x_i, y_i) pairs; fit f via **Maximum Likelihood Estimation (MLE)** (e.g. OLS
  for linear regression).
- Unsupervised: only feature vectors x_i, no y_i — no fitness function; accuracy harder to
  gauge; still widely used (factor models).

## Notes
- Survey chapter (no formulas). Reusable framing: supervised/unsupervised split, parametric vs
  non-parametric tradeoff, and the overfitting/cross-validation discipline.