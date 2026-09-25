# Ch2: Understanding Foundation Models

## Training data

- Models are only as good as their training data. Most models use variations of Common
  Crawl (2–3B pages/month crawled) or its clean subset C4 — with questionable quality
  (fake news, propaganda). Heuristic filtering exists (e.g., GPT-2 kept Reddit links with
  ≥3 upvotes) but is crude.
- **English dominance**: 45.9% of Common Crawl is English (8× the #2, Russian 6%). Models
  underperform on low-resource languages (e.g., GPT-4's MMLU is much worse in Telugu/
  Marathi/Punjabi — the most under-represented languages). Translation round-trips lose
  information (e.g., Vietnamese relationship pronouns collapse to "I/you"). Tokenization
  is also inefficient for some languages: median 7 tokens for English vs 72 for Burmese on
  the same text → ~10× cost/latency for non-English.
- **Domain-specific models** (AlphaFold, Med-PaLM2) matter when the data is private/
  structured and absent from the public internet; otherwise general-purpose models are
  usually good enough.

## Modeling

- **Transformer** (Vaswani 2017) solved seq2seq's two problems via *attention*: (1) decoder
  previously saw only the final hidden state ("answering from a book summary"); (2) RNNs
  process sequentially (slow, vanishing/exploding gradients). Transformer = parallel
  prefill (compute-bound) + sequential decode (memory-bandwidth-bound).
- Attention uses query/key/value vectors: `Attention(Q,K,V) = softmax(QKᵀ/√d)V`.
  KV vectors for all prior tokens must be stored → context-length limits. Blocks = attention
  module (Q,K,V,O matrices) + MLP with activation (ReLU/GELU). Model size = f(model dim,
  layers, feedforward dim, vocab).
- Alternatives: RWKV (RNN-like, parallelizable training), SSMs — S4 → H3 → Mamba (linear-time
  inference, beats transformers 2× its size) → Jamba (hybrid transformer+Mamba MoE).
- **Scale numbers**: parameters ≈ capacity; training tokens ≈ knowledge; FLOPs ≈ cost.
  FLOPs ≠ FLOP/s: 1 FLOP/s-day = 86,400 FLOPs. Training GPT-3-175B (3.14×10²³ FLOPs) on
  256 H100s at 70% utilization ≈ 7.8 months, ~$4.1M. ≥70% utilization is "great".
- **Chinchilla scaling law**: for compute-optimal training, tokens ≈ 20× model size and both
  should scale equally. (Sparse MoE and synthetic data complicate this; inference-cost-aware
  variants exist.) Diminishing returns at the top: 3.4→2.8 nats cross-entropy needs 10× data.
- **Bottlenecks**: internet data will run out (28–45% of C4 already restricted); electricity
  caps data centers at ~50× growth. Proprietary data becomes the moat.
- **Emergent abilities + inverse scaling** (bigger models worse on some memorization/prior
  tasks — Anthropic 2022; Inverse Scaling Prize found no real-world examples).

## Post-training

1. **SFT (supervised finetuning)**: train on (prompt, response) demonstration data to turn
   a completion model into a conversational one. Quality labelers are expensive: InstructGPT
   used 13,000 pairs, ~$10/pair, 30 min each. ~90% of its labelers had college degrees.
2. **Preference finetuning** (RLHF / DPO / RLAIF): reward model scores responses, trained on
   *comparison data* (prompt, winning, losing) — ranking is easier and more reliable than
   pointwise scores. Loss: `-E[log σ(r_θ(x,y_w) − r_θ(x,y_l))]`. RLHF used ~2% of training
   compute; improves preference despite possibly worsening hallucination on some benchmarks.
   Cheaper variants: best-of-N with a reward model alone (Stitch Fix, Grab).

## Sampling (most underrated lever)

- Logits → softmax → probabilities → sample. **Greedy** = argmax (boring); **sampling** from
  the distribution makes outputs probabilistic (inconsistency + hallucination).
- **Temperature T**: divide logits by T before softmax. T→0 ≈ greedy; T=1 default; higher T
  → more creative. **Top-k**: softmax over top-k logits only (k 50–500). **Top-p / nucleus**:
  keep smallest set whose cumulative probability ≥ p (0.9–0.95 common). **Min-p** sets a
  minimum token probability.
- **Test-time compute**: sample N outputs, pick best (highest avg logprob, or reward-model
  score, or self-consistency majority). Verifiers gave ~the boost of a 30× larger model
  (OpenAI math). Diminishing returns: OpenAI saw gains up to 400 samples, then degradation.
- **Structured outputs** ladder: prompting (weakest) → post-processing (LinkedIn's defensive
  YAML parser: 90%→99.99%) → test-time compute → constrained sampling (filter logits by
  grammar) → finetuning/classifier head (strongest).
- **Inconsistency fixes**: caching, fixed sampling vars, seed, temperature=0 — but no
  guarantee (hardware variance). **Hallucination hypotheses**: (1) self-delusion/snowballing
  — the model can't distinguish its own generations from given facts; (2) mismatch between
  the model's internal knowledge and the labeler's knowledge taught during SFT. Mitigations:
  better reward functions, verification/retrieval, shorter outputs, RLHF (mixed evidence).

## Takeaways

- Pick models by data, size, and post-training — not just benchmark hype.
- Sampling variables (temperature, top-p, best-of-N) are a cheap, powerful performance lever.
- The probabilistic nature of LLMs is a feature for creativity, a bug for everything else —
  engineer around it (sampling control, structure, retrieval).

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch2.
