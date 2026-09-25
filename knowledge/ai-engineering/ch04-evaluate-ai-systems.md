# Ch4: Evaluate AI Systems (building an evaluation pipeline)

## Evaluation-driven development

Define evaluation criteria *before* building (like TDD). An application that's deployed but
unevaluated is worse than one never shipped. Most common production apps are those with
clear criteria (recommenders → engagement; fraud → money saved; coding → functional
correctness; classification use cases). Focus on easy-to-measure apps = "looking for keys
under the lamppost" — but that's the reality of what gets deployed.

## Four criteria buckets

1. **Domain-specific capability** (can the model do the task?): exact evaluation via
   benchmarks. Coding → functional correctness (+ efficiency: BIRD-SQL checks query runtime;
   readability needs AI judges). Non-coding → close-ended MCQs (MMLU, AGIEval, ARC-C; 75% of
   lm-evaluation-harness tasks are MCQ). MCQs test recognition, not generation — good for
   knowledge/reasoning, weak for summarization/translation.
2. **Generation capability**: fluency/coherence (old NLG metrics; less critical now — models
   are fluent), faithfulness/relevance. *Factual consistency* is the big modern metric:
   local (vs given context — summarization, support bots) or global (vs open knowledge).
   Detection: AI judges, **self-verification** (SelfCheckGPT: sample N more responses, check
   agreement), **knowledge-augmented verification** (SAFE: decompose → make self-contained →
   search-verify each claim), textual entailment/NLI (DeBERTa-v3-mnli-fever-anli).
   Hallucination-prone query types: niche knowledge, things that don't exist — weight your
   benchmark toward these. *Safety*: toxicity/hate/political bias → moderation models
   (Perspective API, Llama Guard), benchmarks (RealToxicityPrompts, BOLD).
3. **Instruction-following**: IFEval (25 automatically-verifiable instruction types: keywords,
   length, JSON format) and INFOBench (content/linguistic/style constraints verified by
   yes/no criteria — often via AI judges). Curate your own instruction benchmark (e.g., test
   "don't say 'as a language model'" if that matters).
4. **Cost & latency**: Pareto trade-offs; pick non-negotiable constraints first (filter by
   latency, then pick best quality within budget). Metrics: TTFT, TPOT, time per query;
   cost per token. Hosting your own models makes cost/token cheaper at scale.

## Model selection: host vs API

Seven axes: **data privacy** (Samsung/ChatGPT leak; Zoom TOS backlash), **data lineage &
copyright** (StarCoder memorized 8% of training set; IP law unsettled — commercial contracts
may protect you; open-weight ≠ open-data), **performance** (open-source gap closing on MMLU
but likely to persist for the strongest models), **functionality** (scalability, function
calling, structured outputs, guardrails, logprobs — APIs limit you), **cost** (API per-usage
vs engineering + infra for self-host), **control/access/transparency** (rate limits, silent
model updates, provider lockout risk, over-censoring vs finetuning freedom), **on-device**
(APIs impossible).

## Public benchmarks & contamination

- Public leaderboards (HF Open LLM, HELM) aggregate a handful of benchmarks; selection and
  aggregation (plain average vs HELM's mean win rate) are arbitrary and benchmarks are
  strongly correlated (WinoGrande/MMLU/ARC-C r≈0.87–0.90 — redundant).
- **Data contamination** ("Pretraining on the Test Set Is All You Need"): models trained on
  benchmark data score deceptively high. Detection: 13-token n-gram overlap with training
  data (accurate, expensive) or unusually low perplexity (cheap, less accurate). 40%+ of
  common benchmarks were in GPT-3's training data.
- Use public benchmarks to *filter out* bad models; then evaluate your shortlist on **your
  own pipeline** with your own data.

## Designing the evaluation pipeline

1. **Evaluate every component** (PDF-extract + employer-extract example) end-to-end *and*
   per component, per turn and per task (turn = one output; task = whole goal — 2 turns vs
   20 turns to solve a bug matters).
2. **Write an evaluation guideline** — the most important step. Define what good *and* bad
   look like, out-of-scope inputs, correct-but-unhelpful responses ("You are a terrible fit").
   LangChain's State of AI 2023 found users used ~2.3 different feedback criteria per
   application on average.
3. **Use the right methods**: automatic metrics where possible, logprobs for confidence,
   human evaluation as the North Star (LinkedIn manually reviews up to 500 conversations/day).
4. **Annotate data, sliced**: multiple eval sets (production distribution, known-failure
   slices, typo-heavy inputs, out-of-scope). Watch Simpson's paradox. "If you care about
   something, put a test set on it."
5. **Size your eval sets**: sample-size rule — for every 3× smaller score difference you want
   to detect, need 10× more samples (30% diff → ~10 samples; 1% → ~10,000). Bootstrap the
   eval set to check reliability. ~300 examples absolute minimum; 1,000+ preferred.
6. **Evaluate the pipeline itself**: right signals? reproducible (judge temperature=0)?
   correlated metrics? cost/latency added? Iterate, and log everything (data, rubric, judge
   prompts/configs).

## Takeaways

- Model selection is building a *private leaderboard* from your criteria, not trusting
  public ones.
- Start simple: prompting → few-shot → RAG → finetune, with evaluation gates at every step.

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch4.
