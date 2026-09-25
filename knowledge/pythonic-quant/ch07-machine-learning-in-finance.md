# Chapter 7 — Machine Learning in Finance

## Core idea
ML in finance: supervised/unsupervised/reinforcement learning, the
overfitting problem and regularization, and the main applications — asset
pricing, sentiment analysis (NLP), fraud detection, credit risk.

## Learning paradigms
- **Supervised**: labeled data, input-output pairs — predictive tasks (stock
  forecasts, credit scoring, credit risk).
- **Unsupervised**: unlabeled data, find structure — clustering for portfolio
  diversification, anomaly detection for fraud, market segmentation.
- **Reinforcement learning**: an agent learns actions to maximize cumulative
  reward — adaptive, dynamic trading strategies.

## The central challenge: overfitting vs underfitting
- **Overfitting**: model learns training noise → poor generalization.
- **Underfitting**: model too simple to capture the pattern.
- **Regularization**: Lasso (L1) and Ridge (L2) penalize weights to balance
  fit and generalization.

## Applications
- **Predictive modeling for asset pricing**: historical prices + economic
  indicators + corporate actions + sentiment → price forecasts; linear
  regression to deep networks.
- **NLP / sentiment analysis**: news, financial reports, social media →
  sentiment scores feeding trading strategies.
- **Deep learning**: complex non-linear relationships — forecasting, fraud
  detection (at the cost of compute and data).
- **Credit risk**: borrower creditworthiness from wider data.
- **Fraud detection**: anomaly detection cutting false positives.
- **Customer service**: chatbots.

## Challenges
- Data quality: models are only as good as their data.
- Interpretability: black-box models are hard to justify in regulated
  finance.
- Computational requirements.
- **Ethics**: data privacy, model transparency, algorithmic bias — a
  principled approach is required.

## The ML workflow in practice
1. Define the target (direction, return, default flag) and features.
2. Split train/test — scale on train only (no leakage).
3. Fit a model family; tune regularization to balance bias/variance.
4. Evaluate by financial metrics (strategy P&L), not just accuracy.
5. Monitor for drift; retrain as the market regime changes.

## When to prefer which
- Linear/logistic: interpretable baselines.
- Trees/ensembles: robust to noise, feature importance available.
- Deep learning: high capacity, but needs data and compute; hardest to
  justify under regulation.

## Bottom line
The ML overview. It frames the supervised/unsupervised split and the
overfitting/regularization trade-off that all of the knowledge base's ML
notes share — `knowledge/python-finance-algo-trading-2ed/ch09–14`
(regression → SVM → ensembles → DNN/RNN) and
`knowledge/halls-moore.../ch15–21` (ML chapters).
