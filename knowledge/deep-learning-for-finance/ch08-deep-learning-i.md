# Ch08 — Deep Learning I

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 8.

## Purpose
The first deep-learning chapter: how neural networks are built from
perceptrons, why activation functions matter, how they are trained
(loss, backpropagation, optimizers), and the regularization that keeps
them honest on financial data.

## Building blocks
- A **perceptron** computes output = activation(w·x + b): a weighted
  sum of inputs plus a bias, passed through a nonlinearity. Stacking
  perceptrons into layers creates a **multilayer perceptron (MLP)**.
- A network's **weights and biases** are its parameters; the hidden
  layers progressively build higher-level features from raw inputs.
- **Universal approximation**: a network with enough hidden units can
  approximate almost any continuous function — which is exactly why it
  can overfit noise if unconstrained.

## Activation functions
- **ReLU** (max(0, x)): default for hidden layers; cheap and avoids
  vanishing gradients, but can "die" (output stuck at 0).
- **Sigmoid/tanh**: squash outputs to (0,1)/(−1,1); good for final
  probabilities, but saturate and kill gradient flow in deep nets.
- **Softmax**: turns raw scores into a probability distribution over
  classes — the standard output for multi-class problems.
- Output choice matters: linear for regression, sigmoid for binary
  classification, softmax for multiclass.

## Training
- **Loss functions**: MSE for regression, binary/multi-class
  cross-entropy for classification.
- **Backpropagation**: the chain rule (ch4) propagates the loss
  gradient back through layers to compute each weight's update.
- **Optimizers**: SGD with momentum, Adam (adaptive learning rates)
  — Adam is the sensible default in finance. The **learning rate**
  is the key hyperparameter: too large diverges, too small stalls.
- **Epochs and batches**: one epoch = one pass over the training set;
  mini-batches update weights on subsets for stability and speed.

## Regularization and generalization
- **Dropout**: randomly zeroes a fraction of activations each
  iteration — forces the network not to rely on single neurons.
- **L1/L2 weight penalties**: add a penalty on weight magnitudes to
  the loss; L1 encourages sparse weights, L2 shrinks them.
- **Early stopping**: monitor validation loss and stop when it stops
  improving — the single most useful guard against overfitting.
- Keras/TensorFlow provide all of this declaratively: layers, losses,
  optimizers, and callbacks compose in a few lines.

## Key takeaways
- Deep learning is a feature-learner: it replaces hand-crafted
  features with learned representations — but on small financial
  datasets, hand-crafted indicator features (ch5) often win.
- The three overfitting guards (dropout, weight decay, early
  stopping) are not optional in finance, where signal-to-noise is low
  and the noise is non-stationary.
- Validate everything on out-of-sample data; a network that fits
  training data perfectly is usually memorizing it.
