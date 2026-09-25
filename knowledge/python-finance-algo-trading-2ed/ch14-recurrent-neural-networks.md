# Chapter 14 — Recurrent Neural Networks (RNN)

## Core idea
RNNs are built for **sequences**: the same weights are applied across time
steps, so the network can learn temporal dependencies in returns. In
practice this means **LSTM** cells (Long Short-Term Memory), which handle
long-range dependencies far better than plain RNNs.

## The 3D shape requirement
RNN/LSTM layers in Keras expect input of shape
`(samples, timesteps, features)`. The book's standard conversion:
- Start with `X` as a 2D feature matrix (rows = days, cols = lagged
  features).
- Create a **lag**-step sliding window so each sample is a window of `lag`
  past observations; this reshapes data to 3D
  `(n_samples - lag, lag, n_features)`.
- The last LSTM layer sets `return_sequences=False` to collapse to a single
  output vector feeding the final `Dense(1, 'sigmoid')` (classification) or
  `Dense(1, 'linear')` (regression).

## Key practices
- **Padding predictions with zeros**: after predicting on windows, prepend
  `lag` zeros (`np.concatenate((np.zeros([lag,1]), pred), axis=0)`) so the
  prediction series aligns with the original index.
- **Dropout**: randomly switch off a fraction of neurons per layer — forces
  the remaining neurons to learn robust features and cuts overfitting.
  `pct_dropout` (e.g., 0.5) is a constructor parameter in the book's
  factorized `RNN(...)` function.
- **Standardizing the target for RNNs**: since X and y train together, scale
  y too (`sc_y`), then **inverse-transform** predictions before sizing
  trades.
- The book factors the whole model build into a reusable function
  (`number_neurons`, `number_hidden_layer`, `shape`, activation, optimizer,
  dropout) — the same parameterized pattern promoted for all deep models.

## Trading results (Netflix example)
A 3-layer LSTM classifier produced Sharpe 1.04, Sortino 1.54, alpha 28% —
but a **44% drawdown** and cVaR 67%. Lesson: good ratios, brutal tail; the
book's answer is portfolio-of-strategies (ch16) to damp volatility.

## Pitfalls
- **Expensive to train**: RNNs need many resources; use pretrained weights,
  GPU/Colab, or smaller windows.
- Wrong `return_sequences` flags break shapes (need 3D output to chain LSTM
  layers, 2D to finish).
- Forgetting the lag-zero padding misaligns predictions vs prices.
- RNNs magnify the data hunger of deep learning — insufficient history → poor
  generalization.

## Bottom line
The LSTM + 3D reshaping + dropout recipe is the book's state-of-the-art
temporal model. It extends the DNN skeleton (ch13) with sequence structure —
and its 44%-drawdown example is a vivid case for layering risk metrics
(ch5) and portfolio allocation (ch3) on top of any ML signal.
