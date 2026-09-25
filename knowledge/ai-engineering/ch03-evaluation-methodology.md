# Ch3: Evaluation Methodology

## Why evaluation is hard for foundation models

- Smarter outputs are harder to judge (PhD-level math vs first-grader math); evaluation can
  require domain expertise and fact-checking.
- Open-ended outputs have no ground truth to compare against.
- Models are black boxes (architecture/training data hidden).
- Benchmarks saturate fast (GLUE 2018→saturated in a year; SuperGLUE 2019; MMLU→MMLU-Pro).
- Scope expands: evaluation now also *discovers* new capabilities, not just measures known ones.
- Investment lags badly: few open-source eval tools vs modeling/orchestration tools; many
  teams "eyeball" results. Invest in systematic evaluation.

## Language-modeling metrics

- **Entropy H(P)**: average information per token (bits). **Cross-entropy H(P,Q) = H(P) + D_KL(P‖Q)**:
  how hard it is for model Q to predict data from true distribution P. Training minimizes it.
- **Perplexity = 2^H** (base-2) or e^H (nats, used by PyTorch/TF). ≈ the model's uncertainty,
  i.e., effective number of equally-likely next tokens. PPL 3 ⇒ 1-in-3 chance of predicting
  the next token correctly.
- Variants: bits-per-character (BPC), bits-per-byte (BPB) — tokenization-independent.
- Interpretation rules: structured data → lower PPL; bigger vocab → higher PPL; longer context
  → lower PPL. PPL rises after post-training (task-focus collapses entropy) and changes with
  quantization. Uses: proxy for capability, detecting data contamination (unusually low PPL on
  benchmark data ⇒ seen in training), deduplication, abnormal-text detection. Needs logprobs,
  which some APIs don't expose.

## Exact evaluation

- **Functional correctness** (ultimate metric, automatable when outcomes are checkable):
  code generation via unit tests — pass@k (fraction of problems solved if any of k samples
  pass); text-to-SQL (Spider, BIRD-SQL); game bots; measurable-objective tasks.
- **Similarity vs reference data** (needs curated references; references can be wrong or
  missing — Fuyu example):
  1. *Exact match* — only for short exact answers; contains-variant is dangerous (wrong answer
     can contain the right year).
  2. *Lexical similarity* — edit distance (Levenshtein: deletion/insertion/substitution),
     n-gram overlap; BLEU, ROUGE, METEOR, TER, CIDEr. BLEU correlates poorly with code
     correctness; optimized-away easily.
  3. *Semantic similarity* — embeddings (BERTScore, MoverScore); cosine similarity between
     sentence embeddings. Depends on embedding quality; BERT 768 / text-embedding-3-large 3072.
     Joint/multimodal embeddings: CLIP (text+image), ImageBind (6 modalities).
- Reference-free metrics (e.g., AI judges) avoid the reference-data bottleneck.

## AI as a judge (LLM as a judge)

- **Why**: fast, cheap, no reference data, explains its reasoning; GPT-4 agrees with humans
  85% on MT-Bench (> 81% human-human agreement); AlpacaEval's judge correlates 0.98 with
  human Chatbot Arena votes.
- **Prompt design**: state the task, the criteria (detailed), and the scoring system.
  Classification > discrete numeric (1–5) > continuous. Include examples per score. A judge
  = model + prompt + sampling config; changing any = a different judge. Don't trust a judge
  you can't inspect.
- **Limitations**: inconsistency (65%→77.5% with examples, at 4× cost); criteria ambiguity
  (MLflow/Ragas/LlamaIndex all define "faithfulness" differently — scores not comparable);
  cost/latency (judging doubles or 4× API calls; mitigate with weaker judges and spot-checking);
  biases — *self-bias* (GPT-4 favors itself +10%, Claude-v1 +25%), *first-position bias* (AI
  prefers first; humans prefer last), *verbosity bias* (longer answers win even when wrong).
- **Judge strength**: stronger judges work but can't judge the strongest; self-evaluation is
  great for sanity checks and self-correction (self-critique); weaker judges can work — judging
  is easier than generating. Specialized judges: reward models (Cappy 360M), reference-based
  (BLEURT, Prometheus), preference models (PandaLM, JudgeLM).

## Comparative evaluation (ranking)

- Pointwise (score each model) vs comparative (pairwise matches → ranking). Comparative is
  easier for subjective quality and never saturates; powers Chatbot Arena. Use Elo, Bradley–
  Terry, or TrueSkill (Arena switched to Bradley–Terry; Elo is order-sensitive).
- **Challenges**: quadratic pair growth (57 models = 1,596 pairs); transitivity assumption is
  shaky; new/private models are hard to slot in; crowdsourced comparisons lack standardization
  (simple prompts like "hello" dominate; no fact-checking); preference ≠ correctness — don't
  ask users to vote on math facts.
- Comparative gives relative ordering, not absolute quality — you still need pointwise/absolute
  evaluation to know if the winner is good enough.

## Takeaways

- Evaluation is the biggest bottleneck to AI adoption — treat it as a first-class engineering
  investment, not an afterthought.
- Use exact metrics where possible; use AI judges for what's subjective; always supplement
  AI-judge results with exact evaluation and/or humans.

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch3.
