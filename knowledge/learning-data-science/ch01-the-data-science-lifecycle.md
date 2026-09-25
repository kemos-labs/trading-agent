# Ch01 — The Data Science Lifecycle

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 1.

## Purpose
Frames all of data science as a **lifecycle** of four high-level stages:
formulate a question → obtain data → clean/wrangle → explore → model →
communicate. Every analysis, however messy, loops through these.

## The lifecycle
- **Formulate a question** — the most important step. A good question is
  specific enough to answer with data, and the answer is actionable.
- **Obtain data** — from files, databases, APIs, or scraping. Scope matters
  (ch2): what population, what access frame, what sample.
- **Clean and wrangle** — make the data tidy and machine-readable: fix
  types, join tables, handle missing values, derive new features.
- **Explore** (EDA) — summary statistics and plots to understand shape,
  distributions, relationships, and anomalies.
- **Model** — approximate the *signal* in the data while tolerating noise
  (ch4 onwards).
- **Communicate** — findings mean nothing if they don't reach a decision.

Real work is not linear: you jump backward and forward as cleaning reveals
new questions, as models reveal data problems, and as stakeholders reframe
the problem.

## Key ideas
- **Scope** (population / access frame / sample) is set by the question and
  drives every bias concern downstream. A great model on a bad sample is
  worthless.
- **Signal vs noise**: data = signal (the pattern you care about) + noise
  (chance variation). Models approximate the signal; statistics quantify
  how much of what you see could be noise.
- **Reproducibility**: write code that re-runs the whole pipeline; keep
  provenance of where data came from and when.
- Analyses live in a **context** — ethics, costs of errors, who is
  affected — which the lifecycle steps must respect.

## Case-study arc (preview)
The book's running examples all follow the lifecycle end-to-end: Seattle
bus lateness (ch5), air-sensor calibration (ch12), donkey weighing (ch18),
and fake-news detection (ch21).

## Key takeaways
- Start with the question, not the data or the tool.
- Every stage loops back into every other; expect iteration.
- Scope + loss + model choice are the three levers that decide whether an
  analysis is trustworthy.

## Notes
- Book's thesis: you can reason about sampling (ch3), modeling (ch4), and
  inference (ch17) with simulation and simple math rather than formal
  statistics textbooks.
