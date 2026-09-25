# Ch9: Inference Optimization

Making models faster and cheaper matters as much as making them better. Optimization
happens at three levels: model (compress/change the model), hardware (accelerators),
service (how requests are scheduled/served).

## Bottlenecks & metrics

- **Compute-bound** (prefill — parallel input processing, limited by FLOPs) vs **memory
  bandwidth-bound** (decode — one token at a time, limited by moving weights from HBM to
  compute units; also KV-cache reads). Roofline charts / arithmetic intensity
  (ops per byte) tell you which. LLM decode is bandwidth-bound; that's why MFU is low.
- **Latency**: TTFT (prefill; users want ~instant for chat), TPOT (per output token; ~120
  ms/token ≈ 6–8 tok/s beats human reading), total = TTFT + TPOT × tokens. Use percentiles
  (p50/p90/p99), not averages (outliers skew). Time-to-publish for agentic queries (first
  token *users see*).
- **Throughput**: output tokens/s (TPS); separate input vs output (different bottlenecks);
  RPS/RPM for concurrency. Throughput ∝ cost (2$/h ÷ 100 tok/s ≈ $5.56/1M output tokens).
  **Goodput** = requests/s that meet the SLO (TTFT ≤ 200ms, TPOT ≤ 100ms → count only
  compliant requests). Latency/throughput trade-off: batching can 2–3× throughput at the
  cost of TTFT/TPOT.
- **Utilization**: nvidia-smi GPU% is misleading (busy ≠ efficient). **MFU** = achieved vs
  peak FLOP/s (training >50% is good; decode MFU is low by design). **MBU** = bandwidth
  utilization. Optimize for cost+latency, not utilization.

## Hardware

- Accelerators (GPUs — thousands of small cores for parallel matmul; TPUs — tensor
  primitive; inference-specific: Apple Neural Engine, Inferentia, MTIA). Memory hierarchy:
  CPU DRAM (25–50 GB/s) ≪ GPU HBM (256 GB/s–1.5 TB/s) ≪ on-chip SRAM (>10 TB/s, ≤40 MB).
  Power: H100 at peak ≈ 7,000 kWh/yr (a US household ≈ 10,000 kWh) — electricity is a
  scaling bottleneck.
- Choose chips by: can it run it (memory size), how fast (FLOP/s, bandwidth), how much
  (price + power). Compute-bound → more FLOP/s; bandwidth-bound → more bandwidth/memory.

## Model-level optimization

- **Compression**: quantization (weight-only: FP16→INT8→INT4; ~close to the 1-bit floor —
  BitNet b1.58), distillation (small student ≈ big teacher), pruning (sparse; promising in
  research, less used in practice — needs architecture understanding, sparse-hardware).
- **Autoregressive decoding fixes**:
  - *Speculative decoding*: a small draft model proposes K tokens; the target model
    verifies them in parallel (verification ≈ prefill cost — turns decode into prefill;
    uses idle FLOPs) and accepts the longest matching prefix. DeepMind: 4B draft for
    Chinchilla-70B → >2× latency cut, no quality loss; higher acceptance on code. In
    vLLM/TensorRT-LLM/llama.cpp.
  - *Inference with reference*: copy spans from the input (retrieval/coding/multi-turn)
    instead of generating — ~2× speedup on overlapping use cases.
  - *Parallel decoding*: generate K tokens simultaneously then verify — Lookahead (Jacobi
    method), Medusa (extra decoding heads; up to 1.9× on Llama 3.1). Harder to implement.
- **Attention optimization** (attention compute is O(n²); KV cache grows O(n)):
  - *Redesign*: local windowed attention (window 1,000 vs seq 10,000 → 10× less KV),
    multi-query / grouped-query attention (share KV across heads), cross-layer attention
    (share KV across layers) — Character.AI cut KV cache >20×.
  - *KV cache management*: **PagedAttention (vLLM)** — non-contiguous blocks, less
    fragmentation; KV quantization, adaptive/selective compression.
  - *Kernels*: **FlashAttention** (fuses softmax into attention passes to avoid HBM round-
    trips). Kernel techniques: vectorization, parallelization, loop tiling, operator fusion.
    Kernels are hardware-specific (CUDA/Triton/ROCm); compilers (torch.compile, XLA, TVM,
    TensorRT) lower models to kernels. PyTorch's Llama-7B throughput ladder: torch.compile
    → INT8 → INT4 → speculative decoding.

**KV cache size** = 2 × B × S × L × H × M (batch × seq × layers × model dim × bytes).
Llama 2-13B, B=32, S=2048, FP16: 2×32×2048×40×5120×2 = 54 GB — often bigger than weights.

## Service-level optimization

- **Batching**: static (fixed batch — first request waits for the last), dynamic (time
  window — controlled latency, maybe-unfilled batches), **continuous/in-flight batching**
  (Orca — return completed responses immediately, backfill the batch; standard for LLMs).
- **Prefill/decode disaggregation**: prefill is compute-bound, decode is bandwidth-bound —
  serve them on different machines (DistServe) to stop prefills starving decodes.
  Instance ratio ~2:1–4:1 if inputs long/TTFT-priority; 1:2–1:1 if short/TPOT-priority.
- **Prompt caching** (prefix/context cache): cache the system prompt / long shared prefixes
  — process once, reuse. 1M calls × 1,000-token system prompt ≈ 1B tokens/day saved;
  Anthropic: up to 90% cost reduction, 75% TTFT cut.
- **Parallelism**: replica (duplicate the model — simplest; bin-packing replicas onto
  GPUs), tensor parallelism (split matmuls across devices; enables >1-machine models,
  lower latency, comm overhead), pipeline parallelism (stage the model across devices;
  better for training — adds latency), context/sequence parallelism (split long inputs).

## Takeaways

- Quantization + tensor parallelism + replica parallelism + attention optimization give
  the most leverage across workloads.
- Decode is the bottleneck for LLMs — speculative decoding and KV-cache management are the
  highest-impact model-level levers.
- At the service level: continuous batching, prefill/decode decoupling, and prompt caching.

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch9.
