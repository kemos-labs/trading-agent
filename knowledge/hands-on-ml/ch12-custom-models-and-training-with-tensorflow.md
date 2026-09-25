# Ch12 — Custom Models and Training with TensorFlow

**Source:** Géron, *Hands-On Machine Learning*, Chapter 12.

## Purpose
The lower-level TensorFlow API for the ~5% of cases Keras can't cover
directly: custom losses/metrics/layers/models, custom training loops,
autodiff, tf.function, and graphs.

## Tensors like NumPy, but different
- `tf.constant(...)` — tensors have shape + dtype; indexing like NumPy;
  ops via `tf.*` (`tf.square`, `tf.matmul` via `@`). Some names differ:
  `tf.reduce_sum/mean/max` (not np.sum), `tf.transpose(t)` (not t.T —
  returns a copy).
- **Variables**: `tf.Variable(init)` — mutable, tracked; `assign()` /
  `assign_add()`; only variables are recorded by GradientTape.
- **dtype discipline**: NumPy is float64 by default, TensorFlow float32 —
  cast explicitly (`tf.cast`) to avoid surprises; `tf.keras.backend` legacy
  functions (K.square etc.) are deprecated in favour of `tf.*`.

## Autodiff with GradientTape
- Record ops inside `with tf.GradientTape() as tape: z = f(w1, w2)`; then
  `tape.gradient(z, [w1, w2])` — reverse-mode autodiff (one forward + one
  backward pass for all gradients).
- Tapes erase after one `gradient()` call → use `persistent=True` (and
  `del tape`) for multiple calls; `tape.watch(t)` for non-variable tensors;
  `tape.stop_recording()` to pause.
- `tape.jacobian()` for per-output gradients (else vector gradients sum).

## tf.function and graphs
- `@tf.function` (or `tf.function(fn)`) traces the Python function into a
  **computation graph** — JIT-compiled, faster, portable; `tf.autograph`
  converts Python control flow into graph ops.
- **Static shapes**: TensorFlow ops know shapes but not sizes; use
  `shape`/`reshape` explicitly; be careful: `tf.shape` (dynamic) vs
  `.shape` (static).
- Graphs allow deployment to C++/mobile (TF Lite) and distributed
  execution.

## Custom components
- **Custom loss**: a function `(y_true, y_pred) -> scalar` (tensor ops
  only). Custom metric: same, but accumulates state (Keras metrics reset
  per epoch); subclass `tf.keras.metrics.Metric` with `update_state()`,
  `result()`.
- **Custom layer**: subclass `tf.keras.layers.Layer` — `__init__`,
  `build(input_shape)` (create weights there — lets Keras infer), `call()`.
  With `compute_output_shape` if shapes change. Add `@tf.function` inside
  `call` for speed (or let Keras auto-trace).
- **Custom model**: subclass `tf.keras.Model` with `call()` (needed for
  complex forward passes); `compile`/`fit` still work.
- Custom regularisers/constraints/initialisers: callables returning a loss /
  function, or subclasses.

## Custom training loop
- When `fit()` isn't enough (multiple optimisers, gradient surgery):
```python
optimizer = tf.keras.optimizers.SGD(learning_rate=…)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()
for epoch in range(n_epochs):
    for X_batch, y_batch in train_ds:
        with tf.GradientTape() as tape:
            y_pred = model(X_batch, training=True)
            loss = loss_fn(y_batch, y_pred) + sum(model.losses)  # regularizers
        grads = tape.gradient(loss, model.trainable_variables)
        optimizer.apply_gradients(zip(grads, model.trainable_variables))
```
- **Gradient clipping**: `tf.clip_by_value` / `tf.clip_by_norm` applied to
  grads before `apply_gradients` — essential for RNNs/exploding gradients.
- `model.losses` accumulates layer regularisation losses during forward.
- Watch `training=True` (dropout/BN behaviour) vs inference.

## Key takeaways
- GradientTape is the universal "compute gradients" primitive — custom
  loops are just explicit versions of what `fit()` does.
- `@tf.function` turns Python into optimised graphs; use for hot loops.
- Custom layers/models unlock arbitrary architectures; subclassing APIs
  sacrifice some inspectability for flexibility.
- Clip gradients in any recurrent or deep custom loop.

## Notes
- Serves production needs: custom quant loss functions (e.g. asymmetric
  trading costs) drop straight into this pattern.
- `model.losses` + custom metrics are how Keras integrates custom pieces
  with `fit()`.
