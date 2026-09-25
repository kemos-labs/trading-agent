# Chapter 15 — RCNN (RNN + CNN hybrid)

## Core idea
A bonus chapter combining two deep architectures: **1D-CNN** layers (which
extract local patterns/features with filters) plus **LSTM** layers (which
model temporal sequence structure) — keeping the best of both. CNN catches
local feature patterns; RNN catches time dependence.

## CNN essentials
- **Filters** play the role neurons do in an RNN: more filters → more
  capacity (and more training cost + overfitting risk).
- **Conv1D** is used because time-series data (like RNN input) is 3D:
  `(samples, timesteps, features)`.
- **Stride/filter length**: a short filter window focuses on local patterns;
  a too-small window overfits and trains slowly.
- **Pooling** reduces dimensionality — noted but not used in the book's model.

## The RCNN architecture (book's code)
```
LSTM(units, return_sequences=True, input_shape=shape)
  → Dropout(pct_dropout)
  → per hidden layer: Conv1D(64, 3, activation='relu')
                      LSTM(units, return_sequences=True)
                      Dropout(pct_dropout)
  → LSTM(units, return_sequences=False)   # collapse
  → Dense(1, activation)                   # output
```
- The 1D-CNN (64 filters, kernel size 3) runs over the time dimension,
  extracting local patterns that the stacked LSTMs then combine over time.
- Dropout after each LSTM keeps the deep stack from overfitting.

## Trading relevance
- Same pipeline as ch14: 3D windowed features → fit → predict with lag-zero
  padding → `sign(prediction) * returns` → standard backtest report.
- Use RCNN when both local feature structure *and* long temporal dependencies
  matter; it is strictly more expressive than plain RNN but costs more to
  train.

## Pitfalls
- Complexity ↑ → overfitting risk ↑ and training time ↑; validate on a
  held-out set, not the train set.
- Needs even more data than a plain RNN; unsuitable for short histories
  (ch16's 1000-row assets).
- Tuning doubles: both the CNN filter count/width and LSTM units/stacking
  need setting.

## Bottom line
RCNN is the book's "max power" deep architecture: local pattern extraction
(CNN) + sequence memory (LSTM) + regularization (dropout). For the knowledge
base it confirms the pattern that deep architectures share one skeleton
(ch13–15) differing only in the layer stack — the reusable factorized
build-function pattern.
