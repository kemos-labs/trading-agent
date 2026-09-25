# AI Evaluation Pipeline Design

## name
Designing a systematic evaluation pipeline for AI/ML systems (eval-driven development,
exact vs subjective metrics, AI-as-judge, eval-set sizing).

## description
A repeatable method for evaluating open-ended AI outputs and comparing models/
strategies: define criteria before building, evaluate every component, use exact metrics
where possible and AI judges for subjective quality, and size evaluation sets so you can
actually detect the differences that matter.

## when to use it
- Building or iterating on any AI application (chatbot, RAG, agent) where "eyeballing"
  outputs is the current practice.
- Comparing models, prompts, or retrieval configurations — before trusting a leaderboard
  or a single anecdotal win.
- Deciding whether an observed score difference (e.g. 3% better) is real or noise.
- Adapting a foundation model: the pipeline gates the prompting → RAG → finetune
  escalation ladder.

## method / formula / code

**1. Evaluation-driven development:** write the evaluation criteria BEFORE the code.
Define what "good" and "bad" outputs look like (a correct-but-unhelpful response is bad),
out-of-scope inputs, and the scoring rubric. Business metrics must map to ML metrics and
vice versa.

**2. Evaluate all components:** score end-to-end output AND each intermediate component
(e.g. PDF-text-extraction step and entity-extraction step separately), per turn (one
output) and per task (whole goal). A failure's location is invisible if you only measure
the final output.

**3. Pick methods by criterion:**
- Exact (unambiguous): functional correctness (pass@k, unit tests), exact match,
  lexical similarity (BLEU/ROUGE/edit distance), semantic similarity (embedding cosine).
- Subjective: AI-as-judge — prompt must state the task, the criteria (detailed), and the
  scoring system (classification > discrete 1–5 > continuous). A judge = model + prompt +
  sampling config; set judge temperature = 0 for reproducibility; log the judge prompt
  and model version or scores become non-comparable over time.
- AI judges have known biases: self-bias (favoring own outputs), first-position bias,
  verbosity bias (longer wins even when wrong) — randomize order, use weaker/cheaper
  judges, spot-check subsets.

**4. Size the evaluation set (the key rule):**
To be ~95% confident that system A beats system B by a score difference δ, you need
roughly:
- δ = 30% → ~10 samples
- δ = 10% → ~100 samples
- δ = 3%  → ~1,000 samples
- δ = 1%  → ~10,000 samples

i.e. for every ~3× smaller difference you want to detect, need ~10× more samples.
Minimum ~300 examples; ~1,000+ preferred. Validate reliability by bootstrapping the eval
set (resample with replacement; wildly varying results ⇒ set too small).

**5. Evaluate the pipeline itself:** same run twice → same result? Are the metrics
correlated (drop redundant ones)? What cost/latency does evaluation add? Iterate and log
everything (data, rubric, judge configs, prompt versions).

## known pitfalls
- Averages lie: use percentiles (p50/p90/p99) for latency; one outlier skews the mean.
- Public benchmarks are likely contaminated (model trained on them) — use them only to
  filter OUT bad models, never to pick the final one; check perplexity/n-gram overlap for
  contamination.
- Comparative (pairwise) ranking gives relative order, not absolute quality — "B beats A"
  doesn't tell you B is good enough.
- Don't ask users (or judges) to vote on correctness; preference voting is only valid
  where voters are knowledgeable (assistant/co-pilot contexts), not for facts.
- AI-judge criteria aren't standardized across tools (MLflow vs Ragas vs LlamaIndex
  "faithfulness") — scores between tools are not comparable.

## source book
Huyen, *AI Engineering* (O'Reilly, 2025), ch3–ch4 (evaluation methodology, evaluation
pipeline design).
