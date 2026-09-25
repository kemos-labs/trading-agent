# Ch19 — Deep Learning

**Source:** Grus, *Data Science from Scratch*, Chapter 19.

## Purpose
A mini deep-learning framework in pure Python: **tensors**, layered
abstractions (Layer/Loss/Optimizer), and training examples (XOR, MNIST).
The framework is a toy but every concept maps onto PyTorch/TensorFlow.

## Tensors and tensor operations
- **Tensor** = nested list of numbers with a `shape` (list of dims).
  Scalars/vectors/matrices are rank-0/1/2 tensors.
- Tensor ops built with recursion: `shape`, `tensor_sum`, `tensor_combine`
  (elementwise binary op), `tensor_apply` (elementwise unary op),
  `tensor_zip` (pair-wise), `one_hot_encode` (index → 0/1 vector).
- **Random init**: `random_uniform`, `random_normal`, and **Xavier**:
  `variance = len(dims)/sum(dims)` for the normal init — scales weights to
  keep activations/gradients from exploding or vanishing (the book notes
  some nets fail to train without it).

## Layer abstractions
- `Layer` interface: `forward(input) -> Tensor`, `backward(gradient) -> Tensor`
  (returning the gradient *to pass back to the previous layer*), plus
  `params()` / `grads()`.
- `Linear` layer: `output[o] = dot(w[o], input) + b[o]`; backward stores
  `w_grad[i][o] = input[i]·gradient[o]` and `b_grad = gradient`, returning
  `Σ_o w[o][i]·gradient[o]`.
- Activation layers: `Sigmoid`, `Tanh`, `Relu` (mostly implemented in
  exercises); `Softmax` + `CrossEntropy` for classification.
- `Sequential`: chains layers; forward passes through in order, backward
  passes the gradient in reverse.

## Losses and optimisers
- `Loss` interface: `loss(predicted, actual)` + `gradient(predicted, actual)`.
  - `SSE` (squared error): gradient `2·(predicted − actual)`.
  - `SoftmaxCrossEntropy`: softmax the logits, then −log(prob of correct
    class); its gradient collapses to `softmax(pred) − one_hot(actual)` —
    the clean "prediction error" form.
- `Optimizer` interface: `step(layer)` mutates params.
  - `GradientDescent`: `param[:] = param − lr·grad` (slice assignment so the
    original list mutates).
  - `Momentum`: keeps a running average of gradients
    `update = m·update + (1−m)·gradient`, steps by `−lr·update`. Smoothes
    noisy gradients, accelerates convergence.

## Examples
- **XOR**: 2→2 sigmoid hidden, 2→1 linear output, SSE + GradientDescent,
  3000 epochs — learns XOR (a linear-output final layer works because SSE
  doesn't need sigmoid range).
- **MNIST**: 784-30-10 net, one-hot targets, SoftmaxCrossEntropy; training
  on all 60k images with batch gradient descent shows slow progress — the
  book notes modern practice uses mini-batches, better optimisers, CNNs,
  and normalised inputs.

## Key takeaways
- Deep learning framework = layers with forward/backward + losses +
  optimisers; the same shapes exist in PyTorch.
- SoftmaxCrossEntropy's gradient `predicted − one_hot(actual)` is the
  logistic-regression gradient generalised — one pattern, many models.
- Xavier init, momentum, and proper loss choice are the difference between
  training and not.

## Notes
- The framework here is explicitly a teaching skeleton: real work uses
  PyTorch/TensorFlow (ch27).
- Slice-assignment mutation (`param[:] = ...`) is a recurring Python gotcha
  the book stresses.
