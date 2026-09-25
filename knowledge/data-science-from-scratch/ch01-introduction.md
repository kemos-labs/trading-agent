# Ch01 — Introduction

**Source:** Grus, *Data Science from Scratch*, Chapter 1.

## What data science is
The book's working definition: **data science = data + questions + tools**.
The "data scientist" is the person who can find patterns and insight in data
that is messy, unwieldy, or unstructured, and communicate those insights to
non-technical stakeholders. Grus frames the discipline as "extracting
knowledge from data" using mathematics, statistics, programming, and domain
judgment — not just running libraries.

## The data scientist's mindset
- **Start with a question, not a dataset.** Every chapter in the book is
  framed as a problem the fictional company DataSciencester asks you to
  solve (find key connectors, build a spam filter, predict premium
  subscribers).
- **Always inspect your data before modelling.** Grus repeatedly loads data
  and computes simple summary statistics / counts first.
- **Beware the "no free lunch" of tooling**: you must understand the math
  underneath the library calls, or you'll misapply them. Hence the book's
  premise: implement every algorithm *from scratch* in pure Python, then
  (ch27) switch to NumPy/pandas/scikit-learn for production.

## The running example: DataSciencester
A fictional social network whose fictional executives give the reader a
steady stream of data problems:
- count of friends per user → degree centrality for "key connectors";
- recommend new interests (collaborative filtering, ch23);
- spam filter (Naive Bayes, ch13);
- predict which users pay for premium (logistic regression, ch16);
- cluster users by location (k-means, ch20).

The whole book is one continuous exercise of the data-science loop:
**acquire → clean → explore → model → validate → communicate**.

## Key takeaways
- Data science is an *iterative, messy* process — models rarely work first
  time; the skill is in the iteration.
- Simple techniques (counting, correlation, inspection) are often more
  valuable than fancy ones.
- Every chapter pairs a business question with a statistical/ML technique,
  which is the pattern to replicate: **question → data → technique →
  answer → sanity check**.
- The book is deliberately dependency-free (pure Python) so each algorithm's
  internal mechanics are visible; performance and polish come later with
  libraries.

## Notes
- This chapter contains no formulas — it is a framing/roadmap chapter.
- The rest of the book builds the needed mathematics progressively: linear
  algebra (ch4), statistics (ch5), probability (ch6), then ML models.
