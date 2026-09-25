# Ch09 — Deep Learning II

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 9.

## Purpose
The second deep-learning chapter, focused on the architectures suited
to sequences: CNNs for local patterns, LSTMs for memory over time,
plus preprocessing (rolling windows, wavelet transforms) and the
overfitting/monitoring discipline specific to financial ML.

## Architectures
- **Convolutional Neural Networks (CNNs)**: originally for images,
  they slide filters over the input to detect local patterns. Applied
  to time series, a 1-D CNN learns short price-pattern features
  (e.g., local momentum shapes) regardless of their position in time —
  useful for pattern recognition on indicator matrices.
- **Recurrent Neural Networks (RNNs)**: process sequences step by
  step, carrying a hidden state that encodes the past.
- **LSTM (Long Short-Term Memory)**: an RNN variant with input,
  forget, and output gates that control what is remembered. It solves
  the vanishing-gradient problem of plain RNNs and is the standard
  choice for price-sequence forecasting; **GRU** is a lighter
  alternative.

## Preprocessing for sequences
- **Rolling windows**: slice the series into overlapping windows of
  length L as model inputs, with the label at the next step — turns
  one long series into many training examples.
- **Wavelet transforms**: decompose the signal into time-frequency
  components, separating low-frequency trend from high-frequency
  noise; wavelet-denoised features can stabilize models on noisy data.
- Scale features (z-score or min-max) per window or per training set —
  never with full-sample statistics (leakage).

## Overfitting and monitoring
- Financial signals are weak and non-stationary; validation metrics
  that look great in-sample routinely decay out-of-sample.
- **Watch the gap** between train and validation loss: growing gap =
  memorization. Use early stopping, dropout, and smaller capacity.
- Evaluate on multiple market regimes (bull/bear/choppy) — a model
  fit on one regime can quietly fail in the next.
- Use walk-forward or out-of-sample blocks, not random splits, to
  preserve time structure.

## Key takeaways
- LSTM/GRU for sequential price data, CNN for localized pattern
  features, MLP for tabular indicator features — match architecture
  to data structure.
- Sequence preprocessing (windows, normalization, wavelet
  denoising) often determines success more than the network choice.
- The enemy is always leakage and overfitting; every claimed
  performance number should be out-of-sample and regime-aware.
