# Ch10: AI Engineering Architecture and User Feedback

## Architecture: grow from the simplest form

Start with query → model → response. Add components as needs arise:
1. **Context augmentation** (RAG/tools for information gathering).
2. **Guardrails** (input/output moderation, PII removal) to protect system and users.
3. **Model router + gateway** (route by intent/cost/latency; one API surface, swap models,
   rate limiting, unified logging).
4. **Caching** for latency/cost (prompt cache, response cache for repeat queries).
5. **Complex logic + write actions** (agents, multi-step pipelines).

Monitoring/observability is integral, not optional. Metrics should be sliceable by user,
release, prompt version, and time; correlate intermediate metrics with the business north
star (DAU, session duration, retention). Track latency (TTFT/TPOT/total), cost (queries,
input/output tokens), and refusal rates.

**Logs and traces**: metrics tell you *something* broke ~5 min ago; logs (append-only,
log EVERYTHING: model endpoint, sampling config, prompt template, final prompt, outputs,
intermediate outputs, tool calls, timestamps + tags/IDs) tell you *what*; traces link
related events into a per-request timeline (query → retrieved docs → final prompt → each
step's time and cost) so failures are pinpointable. Manually inspect production data daily
— perceptions of good/bad outputs improve with exposure (Shankar et al.).

**Drift detection**: watch for silent changes in (a) your system prompt (template edits),
(b) user behavior (users adapt to the AI — response length drifts), (c) the underlying
model (providers update silently; GPT-4 March vs June 2023 scored very differently;
Voiceflow saw a 10% drop on a turbo model switch). Pin model versions, log prompts.

**Orchestration**: components definition + chaining (function composition with validation
of data flow between steps; parallelize independent steps for latency). Orchestrators
(LangChain, LlamaIndex, Flowise, Haystack) abstract details — start without one; when you
adopt one, check integration/extensibility, support for complex pipelines (branching,
error handling), and hidden API calls/latency. Orchestrator ≠ workflow tool (Airflow).

## User feedback

Feedback is proprietary data → the data flywheel (ch8). Types:
- **Explicit**: thumbs up/down, ratings, yes/no — sparse (users won't do extra work), biased
  (unhappy users complain more; leniency bias — Uber drivers avg 4.8/5).
- **Implicit**: inferred from actions. Conversational signals: *early termination* (stopping
  generation, leaving), *error correction* ("No, I meant…", rephrasing), *action-correcting*
  ("check the CEO's X profile"), *confirmation requests* ("Are you sure?" — signals
  distrust/insufficient detail), *direct edits* (edited code = preference data: original =
  losing, edit = winning response), *complaints* (clustered FITS types: clarify, irrelevant
  info, not grounded, not specific, refusal-y, repetitive), *sentiment*, *regeneration*
  (could be dissatisfaction OR exploration), *conversation organization* (delete = bad,
  rename = good convo + bad title), *conversation length* (good for companions, bad for
  support), *dialogue diversity* (long + repetitive = loop). Implicit is abundant but noisy
  — study your users before trusting signals; combine multiple signals to disambiguate.

**When to collect**: at signup (calibration — optional unless needed), when something bad
happens (let users fix/regenerate/transfer to human — human-AI collaboration like DALL-E
inpainting), when the model is low-confidence (side-by-side comparison → preference data),
optionally when something amazing happens (rare, positive-signal rich — but don't imply
good results are exceptions). Collect throughout the journey, non-intrusively.

**How to collect**: integrate into the workflow with zero extra effort (Midjourney's
upscale/vary/regenerate buttons are graded implicit signals; Copilot's Tab-accept/ignore).
Prefer embedded products (Gmail drafts) over standalone (ChatGPT) — you know if the draft
was sent. Provide feedback context (last 5–10 turns) via consent/donation flows. Explain
how feedback is used. Don't ask users to judge what they can't know ("I don't know" option
for math). Watch UI bugs (Luma's inverted emoji scale → 1-star "positive" votes). Public vs
private signals trade off candor (private → more/higher-quality) vs discoverability.

**Limitations**: leniency bias, randomness (users click without reading), position bias
(first option wins — randomize), preference bias (verbosity, recency), and **degenerate
feedback loops** (predictions → feedback → next model amplifies initial bias: filter
bubbles, sycophancy — models learn to flatter users instead of being accurate). Inspect
feedback distributions and don't blindly train on feedback.

## Takeaways

- Ship the simplest architecture and add context, guardrails, routing, caching, and
  actions in that order — instrument everything from day one.
- User feedback is your best (and only proprietary) data source — design for implicit,
  low-effort signals; understand its biases before acting on it.

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch10.
