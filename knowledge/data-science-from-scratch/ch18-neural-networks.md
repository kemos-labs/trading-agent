# Ch18 — Neural Networks

**Source:** Grus, *Data Science from Scratch*, Chapter 18.

## Purpose
Build a neural network from scratch and train it with **backpropagation** to
solve nonlinear problems like XOR.

## Perceptron → neuron
- A **neuron**: `output = activation(dot(weights, input) + bias)`.
- The book builds a Perceptron, then a **step function**, then the
  **sigmoid** neuron. Sigmoid makes the network trainable (differentiable):
  `sigmoid(t) = 1/(1 + exp(−t))`, derivative `σ'(t) = σ(t)(1 − σ(t))`.
- **XOR is not linearly separable** — one perceptron can't learn it. The
  chapter's motivating example: a 2-2-1 feedforward net with sigmoids
  learns XOR.

## Feedforward networks
- **Layers**: input → hidden → output; each layer is neurons with weights
  and biases. The output of one layer is the input to the next.
- **Backpropagation**: compute the output error, then propagate gradients
  backward through the layers using the chain rule:
  - For the sigmoid activation, `gradient × σ'(z)` where `σ'(z) = out·(1−out)`.
  - Weight gradient: `(error from next layer) × (this layer's input)`.
  - Bias gradient = the incoming error itself.
- The book first hand-implements backprop for the 2-2-1 XOR net with
  explicit partial derivatives — walking through each weight's contribution —
  before abstracting it.

## Training loop
```python
for epoch in range(N):
    for x, y in zip(xs, ys):
        predicted = net.forward(x)
        grad = loss.gradient(predicted, y)   # e.g. 2*(predicted − y)
        net.backward(grad)                   # propagate errors backward
        optimizer.step(net)                  # update all weights
```
- Feedforward + backward + a gradient step is the entire loop; the
  abstraction layers (Layer, Loss, Optimizer) in ch19 make it general.

## Key lessons
- **Initialisation matters** — the book's note: some networks "couldn't
  train at all" with different initialisations; random init with sensible
  scale (later Xavier) is essential.
- Hidden layers let a net compose features: XOR needs the hidden layer to
  build intermediate "and/or" detectors.
- Networks with sigmoid activations suffer the vanishing-gradient problem in
  deeper nets (foreshadows ch19).

## Key takeaways
- A neural network = composition of `dot + bias + activation` layers;
  nonlinear activations give it expressive power.
- Backprop = chain rule applied to the loss through each layer, reusing
  `σ'(z) = out·(1−out)`.
- Small nets are finicky (init, learning rate); that's why ch19 builds
  tensor-based abstractions + optimisers.

## Notes
- XOR is the canonical non-linearly-separable benchmark — it reappears in
  ch19 as the first test of the Deep Learning framework.
- The manual backprop arithmetic here is the foundation for the automatic
  layer-based version in ch19.
