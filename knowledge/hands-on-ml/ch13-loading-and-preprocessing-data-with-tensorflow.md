# Ch13 — Loading and Preprocessing Data with TensorFlow

**Source:** Géron, *Hands-On Machine Learning*, Chapter 13.

## Purpose
Efficient data pipelines for large-scale training: `tf.data` for loading +
preprocessing, TFRecord for storage, Keras preprocessing layers embedded in
the model (kills training/serving skew).

## The tf.data API
- Core: `tf.data.Dataset` — a lazily-evaluated sequence of items. Create
  with `Dataset.from_tensor_slices(...)`, `Dataset.range(...)`,
  `Dataset.list_files(...)`, `TextLineDataset` (CSV), `TFRecordDataset`.
- **Transformations return NEW datasets** (functional, chainable):
  - `repeat(n)` (n=0 ⇒ forever), `batch(7, drop_remainder=True)`;
  - `map(fn, num_parallel_calls=tf.data.AUTOTUNE)` — preprocessing per
    item, parallelised;
  - `filter(...)`, `take(n)`, `skip(n)`, `cache()`, `prefetch(1)` —
    prefetch overlaps next-batch loading with current-batch compute;
  - `shuffle(buffer_size, seed)`: reservoir-style random pull from a
    buffer — buffer must be large or shuffling is weak; for huge data,
    shuffle source files + interleave reads + shuffle again;
  - `interleave(lambda f: TextLineDataset(f).skip(1), cycle_length=5)`:
    read several files at once, round-robin their rows.
- Datasets handle tuples/dicts of tensors; slicing preserves structure.
- Standard recipe: list_files(shuffled) → interleave → skip header →
  parse → map(preprocess) → shuffle → batch → prefetch.

## TFRecord format
- Efficient binary format for records of varying sizes (protocol buffers);
  `tf.io.TFRecordWriter` / `tf.data.TFRecordDataset`;
  `tf.train.Example` (features: float/int64/bytes lists).
- Use `tf.io.parse_single_example(example, feature_description)` inside
  `map()` to decode. Compress with `options=TFRecordOptions(
  TFRecordCompressionType.GZIP)`.

## Keras preprocessing layers
- **Embedded in the model** ⇒ deployed model ingests raw data directly; no
  separate preprocessing code to drift (eliminates training/serving skew).
- Categories: `CategoryEncoding`, `StringLookup`, `IntegerLookup`
  (with `adapt()` to learn vocab), `Normalization` (adapt learns mean/var),
  `Discretization` (bucketize), `Hashing`, `TextVectorization`
  (tokenise; `split="character"` for char-RNNs; standardize),
  `Embedding` (id → dense vector), `Resizing`, `Rescaling` (÷255),
  `CenterCrop`, `RandomFlip`/`RandomRotation`/`RandomTranslation`/
  `RandomZoom` (augmentation), `GaussianNoise`, `MultiHeadAttention`,
  `PositionalEncoding`.
- Pattern: `norm = tf.keras.layers.Normalization(); norm.adapt(X_train)` —
  fit statistics on training data only, then embed the layer.

## TensorFlow Datasets & Hub
- `tfds.load(...)` — convenient access to many public datasets
  (returns `tf.data` datasets), with versioning and splits.
- TF Hub — download pretrained modules/embeddings to reuse (feature
  extractors, sentence encoders) — pairs with transfer learning (ch11).

## Key takeaways
- `tf.data` = lazy, chainable, parallelised data pipelines; prefetch +
  AUTOTUNE keep GPUs busy.
- Shuffle properly (large buffer or source-level shuffle + interleave).
- Bake preprocessing INTO the model (preprocessing layers) to avoid
  training/serving skew — a production-grade habit.
- Embeddings turn discrete ids into dense learnable vectors — the bridge to
  NLP (ch16).

## Notes
- The ch2 scikit-learn `Pipeline` is the non-TF analogue; same
  fit-on-train-only discipline.
- `adapt()` is the `fit()` equivalent for preprocessing layers — never
  adapt on validation/test.
