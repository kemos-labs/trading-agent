# Ch8: Dataset Engineering

Data is the main differentiator when models are commoditized (GPT-3 had 2 people on data;
GPT-4 credited 80). Data-centric AI (improve the data) vs model-centric AI (improve the
model) — both matter, but quality data is what most teams can control.

## Data curation: quality, coverage, quantity

**Quality** — six characteristics: *relevant* (to the task, not 19th-century law for
today's Q&A), *aligned with task requirements* (not just "accurate" — a correct-but-hurtful
response can be wrong for the task), *consistent* (across examples and annotators — needs
a good annotation guideline), *correctly formatted* (strip HTML, trailing whitespace,
inconsistent casing; a float column stored as int rounds values), *sufficiently unique*
(dupes cause bias + contamination), *compliant* (PII, regulations).
- Small high-quality beats large noisy: Yi's 10K curated instructions > hundreds of
  thousands noisy; LIMA's 1,000 curated prompts ≈ GPT-4 in 43% of judged cases (but not
  robust); Llama 3 used AI-assisted annotation for safety data (humans were inconsistent).

**Coverage (diversity)** — include the range of real usage: detailed AND short instructions,
typos if users typo, the languages you serve, output formats/lengths. Phase-dependent
mixes (Llama 3): pre-training 50% general/25% math-reasoning/17% code; SFT boosts exam-like
and long-context; preference data skews to general knowledge (users' real distribution).
Code+math data punches above its weight for reasoning. Find the mix via small-model
scaling experiments.

**Quantity** — 1 example to millions both work, depending on task; diminishing returns
(plot performance vs 25/50/100% of data to see the slope); task diversity matters more
than raw count (gains from 9→282 tasks, plateau ~282→1,836). Budget-first: annotation
cost × examples vs compute.

## Acquisition

Best source = **your own application data** (perfectly relevant, matches your distribution)
→ the data flywheel. Otherwise: public datasets (HF, Kaggle, Google Dataset Search,
Data.gov, ICPSR, UCI/OpenML, lm-evaluation-harness for PEFT-scale sets — avg 2,000+
examples) — but verify licenses and provenance (a "commercial" dataset may contain
non-commercial parts). Typical curation: find → filter low-quality → re-annotate weak
responses → synthesize to fill gaps → re-validate. Annotation guidelines are the hardest
part and double as evaluation rubrics (reuse them!).

## Data augmentation & synthesis

- *Augmentation*: new data from real data (image flips/crops — AlexNet; word swaps for
  debiasing "She's a fantastic nurse"→"He's…"; perturbation/adding noise — one-pixel
  attacks, ImageNet-C). *Synthesis*: mimic real data (rule-based templates — Faker for
  transactions; procedural generation — AlphaGeometry's 100M synthetic geometry problems;
  simulation — CARLA/Waymo for self-driving, Sim2Real gap).
- **AI-generated data**: the new dominant technique. Purposes: quantity (scarce events),
  coverage (targeted characteristics, rare classes, adversarial examples), quality (AI can
  beat humans where human data is inconsistent — tool-use traces, complex math, preference
  ratings), privacy (synthetic patient records), **distillation** (teacher's outputs train
  a smaller student).
- Typical flow: hand-write a few instruction templates → generate many instructions →
  (re)label with AI or humans → verify. Quality gate everything: inspect samples, run
  dedup (perplexity-based), verify facts.
- **Caveats**: synthetic ≠ free — models trained on model outputs can collapse (model
  collapse / recursive training degrades over generations); mixing human + AI data usually
  wins; verify synthetic data quality and diversity before trusting it.

## Takeaways

- Quality, coverage, quantity are the three knobs — quality and coverage beat raw quantity.
- Annotation guidelines ARE evaluation rubrics; invest once, reuse everywhere.
- Synthetic data scales you, but human data grounds you — blend, validate, dedup.

## Source

Huyen, *AI Engineering* (O'Reilly, 2025), ch8.
