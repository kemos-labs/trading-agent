# Ch11 — Training Deep Neural Networks

**Source:** Géron, *Hands-On Machine Learning*, Chapter 11.

## Purpose
The four problems of deep nets — unstable gradients, insufficient data,
slow training, overfitting — and their fixes.

## Vanishing/exploding gradients
- Sigmoid saturates (derivative → 0) at large |z|; backprop multiplies
  tiny derivatives through layers → gradients die before reaching lower
  layers. Exploding gradients (mostly in RNNs) is the reverse.
- **Glorot/Xavier init**: variance 1/fan_avg (uniform ±√(3/fan_avg)) —
  keeps layer output variance ≈ input variance; for sigmoid/tanh/none.
- **He init** (for ReLU & variants): variance 2/fan_in. **LeCun init**
  (for SELU): 1/fan_in. Keras default is Glorot; set
  `kernel_initializer="he_normal"` for ReLU nets.
- Rule: **match init to activation** (Glorot–tanh/sigmoid, He–ReLU,
  LeCun–SELU).

## Better activations
- **ReLU** `max(0,z)`: no saturation for z > 0, fast — but **dying ReLUs**
  (weights push z < 0 forever ⇒ gradient 0; large η worsens).
- **Leaky ReLU** `max(αz, z)`: small negative slope (α ≈ 0.2) ⇒ never dies.
  **PReLU**: α learned. **RReLU**: random α (acts as regulariser).
- **ELU**: smooth, negative-capable; **SELU** (scaled ELU) — with LeCun
  init it's **self-normalising**: outputs stay mean-0/var-1 through the
  stack, making deep nets trainable without batch norm. SELU nets must use
  only SELU layers + standardised inputs.
- **GELU / Swish / Mish**: smooth ReLU alternatives popular in modern
  models. (Later chapters: conv nets use ReLU; transformers use GELU.)

## Batch normalisation (BN)
- Add a BN layer after each layer: normalise activations (mean 0, var 1)
  per mini-batch, then scale/shift with learned γ, β. **BatchNorm**:
  - makes training much faster & more stable (tames gradient issues);
  - acts as a regulariser (mini-batch noise);
  - allows higher learning rates & less dropout;
  - computes running averages at training for use at inference.
- Alternatives: **layer norm** (normalise per instance — for RNNs/
  transformers), **instance norm** (per instance per channel), **group norm**
  (per instance over channel groups — batch-size independent; used in
  vision models).

## Faster optimisers
- **Momentum**: accumulates velocity `v ← βv − η∇` (β ≈ 0.9) — escapes
  plateaus, damps oscillation. **Nesterov**: lookahead velocity —
  slightly better.
- **AdaGrad**: per-parameter scaled-down learning rates; **RMSProp**:
  AdaGrad + decaying average (works with momentum). **Adam**: RMSProp +
  momentum + bias correction — the default deep-learning optimiser.
- **AdamW**: Adam with *decoupled* weight decay (not ℓ₂ added to the
  loss) — don't use plain ℓ₂ with Adam; use AdamW instead.
- **Nadam**: Adam + Nesterov. Rule of thumb: start with Adam; try
  SGD+momentum with a good schedule for the last mile.

## Learning-rate scheduling
- **Exponential decay** (η decays per epoch/step), **piecewise constant**,
  **performance scheduling** (`ReduceLROnPlateau`: ×0.5 on validation
  plateau), **1cycle** (warmup → high η → cool down; fastest convergence,
  ~30 lines custom callback), power scheduling (`InverseTimeDecay`).
- `tf.keras.optimizers.schedules` updates per *step*; `LearningRateScheduler`
  callback per *epoch*.

## Regularisation for deep nets
- **Early stopping** (best/free), ℓ₁/ℓ₂ on weights
  (`kernel_regularizer`; ℓ₂ + Adam ⇒ use AdamW), **dropout**, max-norm.
- **Dropout**: at each training step, each neuron (not output) is dropped
  with probability p (10–50%; ~20–30% RNNs, 40–50% CNNs). Prevents
  co-adaptation; adds 1–2% accuracy. **Alpha dropout** (SELU nets) keeps
  self-normalising. **MC dropout** at inference gives uncertainty
  estimates. Dropout applies during training only.
- **Max-norm**: constrain each neuron's weight vector to ‖w‖₂ ≤ r —
  regulariser compatible with optimisers, helps unstable training.
- **Data augmentation** (vision): random shifts/rotations/flips — a
  powerful regulariser for image nets.

## Transfer learning & pretraining
- Reuse a pretrained model's lower layers + replace the head; freeze lower
  layers or fine-tune with a low learning rate. Works when the pretraining
  task shares low-level features. Unsupervised pretraining (autoencoders,
  ch17) helps when labels are scarce.

## Key takeaways
- Init must match activation; batch norm + He init tame gradients.
- Adam/AdamW + early stopping + dropout = the practical deep-net recipe.
- Learning-rate scheduling (esp. 1cycle/ReduceLROnPlateau) is a big win
  for convergence speed.

## Notes
- This chapter is the "why" behind every training recipe used in ch14–19.
- The SELU/self-normalising claim is a specific, verifiable property —
  check activations stay standardised rather than trusting it blindly.
