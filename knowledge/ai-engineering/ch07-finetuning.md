# Ch7: Finetuning

Finetuning = adapting a model by updating weights (vs prompting/RAG which leave weights
untouched). A form of transfer learning that's hugely sample-efficient (a few hundred
examples vs millions from scratch).

## When to finetune (and when not to)

- **Finetune for**: task/domain capability, output *formats* (JSON/YAML/domain-specific
  syntax), bias mitigation (expose to counter-stereotypical data), style/instruction
  following, distillation (small student mimics big teacher — Grammarly's Flan-T5 60×
  smaller than GPT-3 text-editing, trained on 82K pairs).
- **Don't finetune for**: things prompting can fix (most cases — people over-claim
  prompting failed after unsystematic experiments); general improvements where it
  degrades other tasks (alignment tax); if you lack data/ML talent/ops budget. Models
  churn faster than your finetune cycle — switching base models needs constant re-eval.
- **Finetuning vs RAG**: "**finetuning is for form, RAG is for facts**". Information
  failures (missing/outdated knowledge) → RAG (RAG beats finetuning on current-events QA,
  and RAG on the *base* model beat RAG on finetuned models in Ovadia et al.). Behavioral
  failures (irrelevant, malformatted, unsafe outputs) → finetuning. Start RAG first —
  simpler, bigger wins; combine both when needed (helped 43% of the time in the study).
- Escalation path: prompting → more examples → simple RAG → advanced RAG (embeddings) or
  finetuning → both. Evaluate at every step.

## Memory bottlenecks (back-of-napkin math)

- **Inference**: weights `N × M` bytes (13B params × 2 bytes = 26 GB) + ~20% for
  activations/KV cache → `N × M × 1.2` ≈ 31 GB.
- **Training** = weights + activations + gradients + optimizer states. Each trainable param
  needs 1 gradient + 0–2 optimizer values (SGD 0, momentum 1, Adam 2). 13B full-finetune
  with Adam at 2 bytes: 13B × 3 × 2 = 78 GB — way over consumer GPUs. Activations can
  dwarf weights; gradient checkpointing trades recompute for memory.
- **Numerical formats**: FP32/FP64/FP16/BF16 (Google, more range less precision)/TF32
  (NVIDIA, 19 bits)/INT8/INT4. Load models in their intended format (Llama 2 is BF16 —
  loading in FP16 degraded quality). **Quantization** = lower precision; inference
  quantization is standard (weight-only is the go-to: FP32→FP16 halves memory; LLM.int8(),
  QLoRA 4-bit; BitNet b1.58 → ~1.58 bits/param era). Training quantization is harder
  (backprop is precision-sensitive) → mixed precision (AMP), or QAT (simulate low precision;
  doesn't speed training), or full INT8 training (Character.AI).

## PEFT (parameter-efficient finetuning)

- **Full finetuning** updates all params (huge memory + data); **partial** (freeze layers)
  needs ~25% of params for near-full performance (Houlsby) — inefficient.
- **PEFT** = strong performance with orders of magnitude fewer trainable params:
  - *Adapter-based*: insert small modules (Houlsby adapters — 3% params, within 0.4% of full
    FT, but adds inference latency). **LoRA** is dominant: decompose a weight matrix
    `W (n×m)` into `A (n×r) × B (r×m)` (low-rank factorization), update only A,B, merge
    back — **no added inference latency**. GPT-3 LoRA: ~4.7M trainable params (0.0027% of
    full FT) with comparable performance. Also: BitFit, IA3, LongLoRA.
  - *Soft prompts*: trainable continuous tokens (prefix-tuning, P-Tuning, prompt tuning —
    differ in insertion points).
- **Model merging** (complement to finetuning): *summing* — linear combination / task
  vectors (finetuned − base = task vector; add/subtract capabilities; Model Soups),
  SLERP (spherical interpolation); *pruning* — TIES/DARE prune redundant task-vector
  params before merging (top 20% of params ≈ 100%); *layer stacking* — frankenmerging,
  MoE from dense checkpoints, model upscaling (SOLAR 10.7B from 7B); *concatenation* —
  not recommended (no memory win).

## Tactics

- **Paths**: progression (cheap model → middling → best, map price/performance frontier) or
  distillation (small data + strongest model → generate data → train cheaper model).
- **Hyperparameters**: learning rate 1e-7–1e-3 (loss curve: noisy = too high; flat = too
  low; schedules), batch size (≥8; gradient accumulation when memory-tight), epochs
  (1–2 for millions of examples, 4–10+ for thousands; watch train/val loss divergence for
  overfitting), **prompt loss weight** (~10% default: learn mostly from response tokens).
- **Frameworks**: finetuning APIs (easy, limited) vs LLaMA-Factory/unsloth/PEFT/Axolotl;
  distributed training via DeepSpeed/PyTorch Distributed for multi-machine.

## Takeaways

- RAG for facts, finetuning for form — escalate only when evaluation says prompting/RAG
  fail.
- Memory math guides everything: params × bytes × (1 + gradient/optimizer multipliers).
- LoRA is the default finetuning technique: cheap, no latency cost, modular serving.

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch7.
