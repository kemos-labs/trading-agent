# Ch17 — Deep Learning for Trading

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 17.

## Purpose
The deep-learning foundation: feedforward networks, backpropagation, regularization, and the TensorFlow/PyTorch workflow — culminating in a DNN-based trading strategy built and backtested end to end.

## Why deep learning
- **Representation learning**: DL discovers hierarchical features automatically (edges → parts → objects), instead of hand-engineered ones — critical for high-dimensional, unstructured data (images, text, time series).
- **Hierarchical composition**: each layer is a nonlinear function of the previous; deep composition can distinguish exponentially more input regions than shallow models for the same parameter count — the antidote to the curse of dimensionality.
- On tabular factor data, DL is *not* automatically better than boosted trees — match capacity to data and noise.

## Feedforward networks
- Layer: z = W·x + b; activation a = σ(z). Common activations: ReLU (default hidden), sigmoid/tanh (outputs/probabilities), softmax (multiclass).
- Loss: cross-entropy for classification, MSE for regression; with softmax, the output-layer gradient simplifies to (ŷ − y).

## Backpropagation (the core math)
- Chain rule applied to the computational graph: ∂J/∂W of each layer = (activation of previous layer)ᵀ · (error signal at this layer).
- Output layer error: δ_out = ŷ − y (for cross-entropy + softmax/sigmoid).
- Hidden layer error: δ_h = a_h·(1 − a_h) ⊙ (δ_out · W_outᵀ).
- Weight/bias gradients: ∂J/∂W = a_prevᵀ·δ; ∂J/∂b = Σδ.
- **Gradient checking**: verify analytic gradients against finite differences — catches implementation bugs.
- **Momentum** update: v ← γ·v − η·∇W; W ← W + v — accelerates and stabilizes convergence.
- Vanishing/exploding gradients: mitigated by ReLU, batch normalization, good initialization, and skip connections.

## Regularization and training
- Dropout (randomly zero units), L1/L2 weight decay, batch normalization, early stopping, data augmentation.
- SGD with minibatches + Adam/RMSProp optimizers; learning-rate schedules.
- Hyperparameter tuning on validation (time-series splits, ch6 discipline).

## Libraries
- **Keras/TensorFlow 2** (Sequential + Functional API) and **PyTorch** (nn.Module, autograd) — both covered with equivalent examples.

## Trading strategy end to end
1. Build features (returns, factors) point-in-time.
2. Design/tune an MLP predicting forward returns or direction; validate with walk-forward splits.
3. Convert predictions to a long-short portfolio (ch8): top/bottom quantiles, costed backtest.
4. Compare against linear baselines and random forest — DNN earns its keep only if out-of-sample IC improves.

## Key takeaways
- Backprop is just the chain rule; understanding the error signals makes debugging and design tractable.
- Regularization + honest validation are decisive on noisy financial data; capacity must match signal.
- DL's edge is representation learning on rich data — benchmark it against classical models before adopting.
