# Ch1: Introduction to Building AI Applications with Foundation Models

## What AI engineering is

AI engineering = building applications on top of *foundation models* (large pre-trained
models someone else trained). It evolved out of ML engineering and differs from it in
three ways: (1) you adapt an existing model instead of training your own — the focus
shifts from modeling/training to *model adaptation*; (2) models are bigger, costlier,
slower → pressure for efficient inference and GPU/cluster skills; (3) outputs are
open-ended → evaluation is a much bigger problem.

## Use case evaluation

- **Why build it** (risk ranking): (1) existential threat — competitors with AI make you
  obsolete (document processing, insurance, creative work); (2) missed profit/productivity
  opportunity (most companies); (3) fear of being left behind (Kodak/Blockbuster trap) —
  an R&D-style watching brief is fine if affordable.
- **Buy vs build**: if AI is existential, build in-house; if it boosts profits, buy options
  may be cheaper and better.
- **Role of AI in the product** (Apple's framework): *critical vs complementary* (the more
  critical, the higher the accuracy bar); *reactive vs proactive* (proactive features need
  precomputation, higher quality bar — users see them as intrusive); *dynamic vs static*
  (dynamic features are continually updated with user feedback).
- **Human-in-the-loop** (Microsoft's Crawl-Walk-Run): Crawl = human involvement
  mandatory; Walk = AI interacts with internal employees; Run = AI directly serves external
  users. Escalate automation as acceptance rates justify it (e.g., 95% verbatim acceptance
  of AI-suggested replies → let AI answer simple requests directly).

## Defensibility & expectations

- The layer you build on top of a model can be *subsumed* when the model improves —
  "a feature for Google Docs" risk. The three moats: **technology, data, distribution**.
  With foundation models, technology is commoditized and distribution belongs to big
  companies → **data is the startup moat** (data flywheel: ship early, collect usage data,
  improve product).
- **Set expectations up front**: define business metrics (e.g., % of tickets automated),
  usefulness thresholds (quality, latency TTFT/TPOT/total, cost per inference), and
  milestone plans. Evaluate off-the-shelf models before committing.
- **Last-mile challenge**: "0 to 60 is easy, 60 to 100 is exceedingly challenging"
  (UltraChat; LinkedIn: 1 month to 80%, 4 more months to 95%). Demos are weekends;
  products are months-years.
- **Maintenance**: model landscape moves fast — prices halve, APIs converge, providers die,
  regulations (GDPR, compute export controls) land. Build versioning + evaluation
  infrastructure so model swaps don't hurt.

## The AI engineering stack

Three layers: **application development** (prompts, context, interfaces, evaluation) →
**model development** (training, finetuning, dataset engineering) → **infrastructure**
(serving, data, compute, monitoring). Most of the recent ecosystem growth was in the
application layer; infrastructure needs stayed stable. Enduring ML principles still apply:
map business metrics ↔ ML metrics, do systematic experimentation (with models/prompts/
retrieval/sampling instead of just hyperparameters), set up feedback loops.

## Takeaways

- AI engineering is mostly *model adaptation* (prompting → RAG → finetuning), not training.
- Think about criticality, human-in-the-loop escalation, and data moats before writing code.
- Measure success in business terms; plan for the last mile and constant model churn.

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch1.
