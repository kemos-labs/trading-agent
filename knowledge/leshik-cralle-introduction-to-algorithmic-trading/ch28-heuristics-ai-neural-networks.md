# Chapter 28 — Heuristics, AI, Artificial Neural Networks

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Heuristics

- From Greek *heuriskein* ("to discover"); introduced to England ~1800.
  A "rule of thumb" for problems logic and probability can't handle.
  Einstein's 1905 Nobel paper used "heuristic" to mean "incomplete but
  useful."
- A computer model of a heuristic must specify: information-gathering
  steps, when to stop gathering, evaluation of alternatives, and the
  decision rule.
- *Bounded rationality*: time/processing limits of brains and machines
  make heuristics a finite, formal necessity, not a cop-out.
- "Probabilistic algos" conflate concepts — algorithms are
  *deterministic*; once probabilities enter, you're in the heuristic
  realm ("rules of thumb that usually give the required result, most of
  the time — but no guarantees").

## The frontier

- "Structured heuristics" / "Fuzzy ALPHA ALGOS" are proposed to provide
  the **requisite variety** (Ashby) — match market complexity with
  adaptive flexibility. Curse of dimensionality blocks comprehensive
  attacks; current strategy = **Occam's razor** (few dimensions, better
  generalization from examples).
- **AI/ANNs**: mixed history; computation-intensive so infeasible in
  real time until recently. The authors spent ~3 years (from 2000) with
  little success, blaming hardware. Worth revisiting as dataflow grows
  (peltarion.com). Law of requisite variety: complex problems need
  complex answers.

## Key takeaways

1. Heuristics = formalized rules of thumb for bounded-rationality
   problems; "probabilistic algo" is a misnomer.
2. Prefer simple, low-dimensional strategies (Occam) — they generalize
   better; ANNs/AI are a future bet on hardware catching data growth.
