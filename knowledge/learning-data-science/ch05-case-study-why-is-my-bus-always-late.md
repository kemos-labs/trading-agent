# Ch05 — Case Study: Why Is My Bus Always Late?

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 5.

## Purpose
First full run through the lifecycle on a real question, modeled on Jake
VanderPlas's "Waiting Time Paradox" post: why does the bus always seem
late?

## Question & scope
- Refined question: how late are buses at 3rd & Pike (Seattle), comparing
  actual vs scheduled arrival times? (Not *why* — no causal claim.)
- Scope: RapidRide lines C, D, E at one stop, Mar 26 – May 27 2016. With
  all admin data in hand, population = frame = sample (small scope, honest
  generalization).
- Bias checks: administrative data quality, redundant columns
  (STOP_ID↔STOP_NAME↔DIR), missing/duplicated records.

## Wrangling
- Load CSV, check unique values to find redundant columns (two stop IDs for
  the same corner: 578 northbound, 431 southbound), drop what's not needed,
  compute `minutes_late = actual − scheduled`.
- The distribution: mostly near 0, but a long right tail (some buses >20
  min late).

## The waiting-time paradox
If buses come every 10 minutes and you arrive at random, expected wait ≈ 5
min — yet it *feels* longer. Why?
- Buses bunch / arrive unevenly. The **interarrival distribution is not
  uniform**; gaps between buses are often much longer than 10 minutes.
- If buses have 10-min average but with variation, the long gaps dominate:
  you are more likely to arrive in a long gap, and the expected remaining
  wait can exceed 5 minutes (for exponential arrivals, mean wait = mean
  interarrival time, not half).
- Constant model + simulation: simulate arrivals with realistic
  distributions and show the simulated mean wait matches the felt
  experience.

## Key takeaways
- A simple model (constant + simulation) answers a question that naive
  reasoning gets wrong; no fancy ML needed.
- The paradox is a **sampling bias**: you oversample long interarrival
  gaps because they occupy more time.
- Scope discipline: narrow the question before modeling; state what you
  can't conclude.

## Notes
- This case study foreshadows the statistical framework: the wait is a
  *random variable* with a skewed distribution; summary statistics depend
  on the loss (mean vs median, ch4).
- Great example of EDA → model → simulation → interpretation as one loop,
  the book's template for ch12, ch18, ch21.
