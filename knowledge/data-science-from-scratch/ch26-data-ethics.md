# Ch26 — Data Ethics

**Source:** Grus, *Data Science from Scratch*, Chapter 26.

## Purpose
A framework for thinking about right and wrong in data work: bad products,
accuracy-vs-fairness trade-offs, and the personal responsibility of the
practitioner.

## What data ethics is (and isn't)
- Data ethics = ethics applied to data work: a *framework for wrestling with
  questions*, not a commandments list. Reasonable people disagree on subtle
  cases; the real obligation is to **consider the consequences of your
  work**, not to parrot someone's manifesto.
- Why it matters more for tech: **technology scales**. A tweak to a news
  algorithm affects millions; a flawed parole algorithm used nationwide
  harms far more people than a flawed parole board.

## Building bad data products (failure by neglect)
- **Tay (Microsoft chatbot)**: echoed whatever it was fed; the internet got
  it to tweet offensive content. Nobody explicitly built a "racist bot" —
  they failed to think through *how it could be abused*.
- **Google Photos** labelling Black people "gorillas": not a deliberate
  decision — a mix of bad training data, model inaccuracy, and the
  offensiveness of the error. Lesson: **training/test on diverse inputs
  isn't enough**; you can't enumerate every input that will embarrass you.
- Takeaway: think adversarially about how what you build *could* be abused,
  before release.

## Accuracy vs fairness (the chapter's core worked example)
A model predicts who will take an action; overall it looks fine (predicted-
unlikely group acts 20% of the time, predicted-likely acts 60%). But split
by group A/B the same data reveals a puzzle — each argument "proves"
unfairness in a different sense:
1. **Different predictions**: 80% of A predicted "unlikely" vs 80% of B
   predicted "likely" — the model treats groups differently.
2. **Calibration**: within each group, "unlikely" ⇒ 20% action and "likely"
   ⇒ 60% — the model is equally *accurate* for both groups.
3. **Different false-label rates**: 32% of B were falsely labelled "likely"
   vs 8% of A — the model stigmatises B.
4. (Residual: B takes the action more often overall — maybe the model is
   just *correct* that B acts more.)
- The lesson: **"fairness" has multiple mutually inconsistent definitions**;
   you cannot satisfy all of them at once. You must pick what fairness means
   for your product, justify it, and understand the trade-off you're
   accepting. Metrics alone can't settle it — values do.

## Key takeaways
- Anticipate abuse and harm *before* shipping; neglect, not malice, causes
  most damage.
- Fairness is multi-criterion and internally contradictory: prediction
  parity, calibration, and error-rate parity can't all hold simultaneously.
- Your job is to reason about consequences and document the choices, not
  just hit a metric.
- Small data choices (training data composition, thresholds) encode ethics.

## Notes
- Pairs with ch7's multiple-testing warning: statistical rigor and ethical
  rigor are both about not fooling yourself.
- The chapter explicitly refuses to hand down rules — it models the
  "reasonable disagreement" stance it advocates.
