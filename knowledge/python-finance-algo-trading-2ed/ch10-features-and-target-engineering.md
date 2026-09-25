# Chapter 10 — Feature and Target Engineering

## Core idea
ML trading strategies live or die by the features fed to the model and the
target it learns. This chapter systematizes both.

## Feature engineering
- **Lagged returns**: `df["return_1"] = df["returns"].shift(1)`,
  `shift(2)`, ..., capturing short-term serial dependence (momentum or
  reversal, per the sign of the learned weights).
- **Technical indicators**: rolling means (SMA), rolling std (volatility),
  momentum over multiple horizons, RSI-style normalized moves.
- **Transformations**: `StandardScaler` (z-scoring) so features share scale;
  this matters most for distance-based and gradient models.
- Features are built **only from past information** — every `shift` moves
  information forward in time, preserving causality.

## Target engineering
- **Classification**: `target = 1 if next_return > 0 else 0` (or `+1/-1`).
  Thresholded direction targets.
- **Regression**: `target = next_return` directly (continuous).
- For RNNs (ch14) the target may be scaled too, and inverse-transformed after
  prediction to restore the tradable scale.

## Discipline rules
- Split **train/test first, then engineer/scale on the train side only**;
  apply the fitted scaler to test/validation.
- Lag alignment: after `shift`, the first rows are NaN — drop them before
  fitting so the model never sees NaN inputs.
- In ch16's full project, features and targets are engineered per-asset with
  a shared function, and the strategy Sharpe is computed on the **test set
  only** — never on data the model saw in training.

## Pitfalls
- **Look-ahead**: an unscaled or unshifted feature that includes today's
  close leaks tomorrow's signal.
- Feature explosion: more features → more overfitting risk, especially with
  trees and DNNs on limited data.
- Scaling the target in classification is pointless; scaling y in regression
  is optional but speeds up RNN training (ch14) — just remember the inverse
  transform.

## Bottom line
The feature/target layer is the shared foundation of every ML strategy in the
book (ch9, 11–14). It pairs with `skills/alpha-factor-evaluation` in the
knowledge base: features are alpha factors, and the discipline here is the
leakage-free construction both demand.
