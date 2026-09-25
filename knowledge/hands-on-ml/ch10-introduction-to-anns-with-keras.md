# Ch10 — Introduction to Artificial Neural Networks with Keras

**Source:** Géron, *Hands-On Machine Learning*, Chapter 10.

## Purpose
ANNs from biology to MLPs, then practical deep learning with Keras:
sequential/functional/subclassing APIs, callbacks, TensorBoard, tuning.

## History & basics
- McCulloch–Pitts (1943) neurons; Rosenblatt's Perceptron (1957) — a layer
  of **threshold logic units** (TLU: `z = wᵀx + b`, then step function).
  Perceptron learning rule: `w ← w + η(ŷ − y)x` (Hebbian, error-driven).
  Perceptron convergence theorem: converges iff linearly separable —
  hence the 1960s AI winter and the need for hidden layers.
- **MLP** = input + one or more hidden layers + output; each layer computes
  `Ŷ = φ(XW + b)`; trained by **backpropagation** (chain rule through the
  network; reverse-mode autodiff), which was the 1986 revolution.
- Modern wave driven by: huge data, cheap GPUs, training-algorithm
  improvements (ReLU, init, optimisers, dropout), and benign local optima
  (local optima ≈ global in large nets).

## Regression & classification MLPs
- **Regression**: 1 output neuron (no activation), MSE or MAE loss; scale
  targets too; Huber loss robust to outliers.
- **Binary classification**: 1 neuron, sigmoid, binary crossentropy.
- **Multiclass**: one neuron per class, softmax, sparse categorical
  crossentropy; outputs are probabilities summing to 1.
- Keras `Sequential`: `Dense` layers; `compile(loss, optimizer, metrics)`;
  `fit(..., validation_data, epochs)`; `predict`.

## The three Keras APIs
1. **Sequential**: linear stacks — simple models.
2. **Functional**: any graph (multiple inputs, multiple outputs, shared
   layers) — build Wide & Deep nets; `tf.keras.Model(inputs=…, outputs=…)`.
3. **Subclassing**: define `call()` in Python — maximal flexibility (custom
   forward passes); harder to save/inspect.
- Wide & Deep: concatenate a "deep" branch (hidden layers) with the raw
   "wide" features — learns both generalisations and memorised patterns.

## Saving, callbacks, TensorBoard
- `model.save()` (SavedModel format) / `load_model()`; `save_weights()` for
  checkpoints.
- **Callbacks** (passed to `fit`): `ModelCheckpoint` (save best,
  `save_best_only`), `EarlyStopping` (`patience`, `restore_best_weights`),
  `TensorBoard`, `LearningRateScheduler`; custom callbacks override
  `on_epoch_end` etc.
- **TensorBoard**: log dir per run; SCALARS/GRAPHS/PROJECTOR/PROFILE tabs;
  `tensorboard --logdir=…` (port 6006); `tf.summary` for arbitrary scalars.

## Hyperparameter tuning
- Many knobs: #layers, #neurons, activation, init, optimizer, learning
  rate, batch size. **Start simple, overfit a small set, then scale**.
- Use `RandomizedSearchCV`/Keras Tuner (bayesian/hyperband strategies) with
  TensorBoard integration. A rule of thumb from the book: hidden layers'
  sizes can taper (e.g. 300 → 100); activation heuristics per task.

## Key takeaways
- MLP = fully connected layers + activation + backprop; Keras makes it
  ~10 lines.
- Pick loss by task: MSE (regression), binary crossentropy (2 classes),
  sparse categorical crossentropy (n classes).
- Callbacks (early stopping + checkpointing) are non-negotiable for real
  training; TensorBoard for debugging learning curves.
- Functional API for anything non-linear (multi-input/output).

## Notes
- This chapter's "start simple, overfit deliberately, then regularise"
  workflow recurs: it's the practical face of ch1's bias/variance chapter.
- `get_run_logdir()` (timestamped dirs) is a tidy logging pattern.
