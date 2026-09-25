# Ch19 — Training and Deploying TensorFlow Models at Scale

**Source:** Géron, *Hands-On Machine Learning*, Chapter 19.

## Purpose
Production ML: serving models, GPU/TPU acceleration, distributed training,
and cloud ML (Vertex AI).

## Serving a model
- Decouple the model behind a service (REST/gRPC) so infrastructure can
  query it, versions can swap, A/B experiments run, and components stay
  independent.
- **SavedModel** format: `model.save(model_path, save_format="tf")`;
  version via subdirectories (`my_mnist_model/0001/`). SavedModel = graph +
  signature defs (`saved_model_cli show`); Keras saves a `serve` metagraph
  with a `serving_default` signature.
- **Bundle preprocessing INTO the model** (preprocessing layers) so the
  deployed model ingests raw data — no training/serving skew.
- **TF Serving** (`tensorflow_model_server`): C++ server, high load,
  multi-version; serves gRPC (port 8500) + REST (8501); watches a model
  repo and auto-deploys newest versions. Install via Docker
  (`tensorflow/serving`) or apt. REST query: JSON `{"signature_name":
  "serving_default", "instances": [...]}`; gRPC via `tensorflow_serving`
  client libs.
- **Cloud**: Vertex AI endpoints — managed serving + monitoring.
- **Edge**: TF Lite (`TFLiteConverter` → `.tflite`, quantisation) for
  mobile/embedded; TF.js for browsers; TF Micro for MCUs.
- **Online vs batch**: batch = nightly script over a store; online = live
  service (potentially TF Serving).

## GPU/TPU acceleration
- GPUs parallelise matrix ops (thousands of cores); TF places ops on
  devices automatically (`tf.config.list_physical_devices`).
- **Profiling**: TF Profiler / TensorBoard PROFILE tab finds bottlenecks;
  `tf.profiler.experimental.start/stop` around training.
- **Performance tips**: pin ops to GPU, avoid GPU→CPU copies,
  `tf.function`-wrap hot loops, use mixed precision
  (`mixed_float16` policy — FP16 matmuls with FP32 accumulation, often
  ~2× faster on modern GPUs), large batch sizes.
- **TPUs**: custom ASICs for deep learning; use `TPUStrategy`; compile for
  TPU shape constraints.

## Distributed training
- **Data parallelism**: replica the model per device; each trains on a
  shard; **all-reduce** gradients (MirroredStrategy — single machine,
  multi-GPU). `tf.distribute.MirroredStrategy()`.
- **Multi-machine**: `MultiWorkerMirroredStrategy` (synchronous, NCCL
  all-reduce); `ParameterServerStrategy` (parameter servers + workers,
  async — scales to many machines); TF handles checkpointing + worker
  coordination (`TF_CONFIG` env var).
- **`tf.distribute.Strategy.scope()`** wraps model building so Keras
  replicates automatically; callbacks (`ModelCheckpoint` with
  `save_best_only`) work under strategies.
- Only the chief worker saves checkpoints/evaluates; all workers run the
  training loop.

## Vertex AI (cloud scale)
- **Training**: Vertex Training (custom containers or prebuilt TF images,
  multi-GPU/TPU clusters, hyperparameter tuning jobs with early stopping).
- **Deployment**: Vertex endpoints (managed TF Serving), online prediction,
  model registry + versioning; monitoring for drift.
- The book's pattern: local prototype → Vertex AI training job with a
  tuned-hyperparameter search → endpoint for predictions.

## Key takeaways
- Production = versioned SavedModels + TF Serving (or Vertex AI) +
  preprocessing baked into the model.
- GPU/TPU + mixed precision + profiling for speed; distribution strategies
  for scale.
- Retraining, monitoring, and A/B rollout are part of the model lifecycle,
  not afterthoughts.

## Notes
- The "bake preprocessing in" rule (avoid training/serving skew) is the
  single most transferable production lesson — applies to any ML stack,
  including quant pipelines.
- TF Lite quantisation (~4× smaller models) matters for edge/embedded
  deployment.
