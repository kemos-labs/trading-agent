# Chapter 13 — Deep Neural Networks (DNN)

## Core idea
A DNN stacks neuron layers: each neuron is a linear model
`z = w'X + b` followed by an **activation function**. Deep = multiple hidden
layers, which learn hierarchical feature representations.

## Building blocks
- **Neuron**: `output = activation(w'X + b)` — weights `w` and bias `b` are
  the learned parameters.
- **Activations**: linear (regression output), sigmoid (probability / binary
  classification), ReLU (hidden layers — cheap, avoids vanishing gradient).
- **Forward propagation**: data flows input → hidden → output to produce the
  prediction.
- **Gradient descent**: iteratively move weights against the gradient of the
  loss: `w := w - lr·∇L(w)`. The **learning rate** is critical — too large
  diverges/oscillates, too small converges painfully slowly.
- **Backpropagation**: the chain rule applied backward through the network to
  compute each weight's gradient; this is what makes deep training feasible.
- **Loss functions**: MSE for regression, binary cross-entropy for
  classification — and the book shows you can write **custom loss functions**
  (e.g., embedding transaction costs or asymmetric P&L into the loss).

## Trading use (Apple example)
1. Build ch10 features; classification target = next-day direction.
2. `Sequential()` model: `Dense` layers with ReLU, output `Dense(1,
   activation='sigmoid')`; compile with binary cross-entropy + Adam.
3. Fit on train, predict on test, map `prediction` to `+1/-1`, strategy =
   `sign(prediction) * returns`, backtest with the standard report card.
4. For regression: output `Dense(1, activation='linear')` with MSE/MAE.

## Pitfalls
- **Local minima / overfitting**: MSE loss is convex-ish so regression is
  safer, but classification with custom loss can trap in local minima — use
  stochastic variants and regularization.
- **No feature scaling → poor convergence**; scale with StandardScaler on the
  train split.
- DNNs need **lots of data**; the book notes some assets (1000 rows) are too
  small for deep learning, so stick to linear/SVM/trees there (ch16).
- Black-box: hard to explain which criteria the model trades on.

## Bottom line
DNN is the entry point to deep learning for trading. The architecture choice
(output activation = task type, loss = objective, lr = dial) applies verbatim
to the RNN (ch14) and RCNN (ch15) chapters that follow.
