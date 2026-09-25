# Ch18 — Case Study: How to Weigh a Donkey

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 18.

## Purpose
Full lifecycle with a **custom asymmetric loss function**: estimate donkey
weight from easy measurements (girth, length, height, BCS, age, sex) so
vets can dose medicine without a scale.

## Scope & data quality
- Population: rural Kenyan donkeys. Frame: donkeys brought to 17 mobile
  deworming sites (Yatta/Naivasha districts). Sample: July 23 – Aug 11
  2010, pregnant/diseased excluded; 544 donkeys, 8 features.
- Bias checklist (ch2): coverage (only 2 districts), selection (only
  sanctuary visitors), measurement (scale calibration; 31 donkeys weighed
  twice to check repeatability — differences within ~1 kg ✓).
- Wrangling: inspect raw CSV, verify codebook, check distributions of BCS,
  age, sex vs weight.

## The asymmetric loss (anesthetic dosing)
- Overdose is worse than underdose (underdose is visible & fixable; overdose
  can be fatal). So the loss punishes **overestimates 3× harder**:
  `anes_loss(x) = x² · (1 if x ≥ 0 else 3)`, where x = relative error
  `100·(y − ŷ)/ŷ`.
- Loss design is the modeling decision: it encodes the *cost of errors*
  from the domain, replacing generic squared error.
- Fit via `scipy.optimize.minimize` (numerical optimization, ch20) since
  the asymmetric loss has no closed form.

## Model building
- Features: Girth alone is best single predictor (θ₀ = −218.5, θ₁ = 3.16),
  but Girth+Length beats it (train loss 94.4 → 65.7); adding Height barely
  helps (63.4) ⇒ choose the simpler two-variable model.
- **One-hot encode** categoricals (BCS, Age, Sex) — drop one level per
  feature to avoid collinearity; the dummies act as intercept shifts
  (parallel lines per category).
- Evaluate on **relative error** (percent), not absolute kg: a 10 kg error
  is worse for a 100 kg donkey than a 200 kg one. Residuals plotted as %
  error vs predicted weight.
- Final usable model: a simple formula a vet can compute with a tape
  measure (Length + 2·Girth − 175 style), not a black box.

## Key takeaways
- Domain cost of errors → loss function → fitted model: the loss is the
  contract between the problem and the math.
- Simplicity is a feature: a deployable model must be computable in the
  field (hand calculator).
- Validate measurements (repeat weighings) before modeling; keep scope
  limits explicit.
- Relative error beats absolute error when outcomes scale (small vs large
  donkeys).

## Notes
- Reuses ch16 model selection ideas (fewer features wins) inside a custom
  loss; the normal equations from ch15 don't apply, hence scipy minimize.
- The book's clearest example of "the right loss is the whole point."
