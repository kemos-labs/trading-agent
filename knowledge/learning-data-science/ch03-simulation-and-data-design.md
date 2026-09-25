# Ch03 — Simulation and Data Design

**Source:** Lau, Gonzalez & Nolan, *Learning Data Science*, Chapter 3.

## Purpose
Reasoning tool for sampling: the **urn model**. Simulate chance processes
to study bias, variance, and experimental design without calculus-heavy
statistics.

## The urn model
A population is an urn of marbles; a sample is draws. Three parameters:
number of marbles, labels/colors, and number of draws; plus **with or
without replacement**. Built on Jacob Bernoulli's original formulation.

- `np.random.choice(urn, size=k, replace=False)` simulates draws.
- **Simple random sample** = draws without replacement: every sample of
  size k is equally likely. P(any one sample of k from n) = 1/C(n,k).
- Simulation replaces enumerating all C(n,k) samples: run 10,000 trials,
  average the outcome — you get the *expected value* of a statistic under
  the chance process.

## What simulation is for
- **Sampling variation**: how much does a statistic (mean, proportion) vary
  from sample to sample? Central to ch17's inference.
- **Response/coverage bias demo**: the 2016 Pennsylvania poll example —
  simulating the poll with realistic response bias shows the poll skews
  even with huge n. **More data does not fix bias.**
- **Experimental assignment**: the J&J vaccine trial simulated as an urn
  shows the expected outcome under random assignment — evidence that
  observed differences (117 vs 351 sick) are not chance.
- **Measurement processes**: simulate instrument fluctuation to calibrate
  sensors and quantify noise.

## Randomized controlled experiments
- Random assignment makes treatment/control groups exchangeable; any
  difference is attributable to the treatment (up to chance).
- The urn analogy: assignment is a chance mechanism, so we can compute how
  surprised to be by the observed split.

## Key takeaways
- A sample can be representative of the frame yet biased relative to the
  population — simulation makes this concrete.
- Simulation = "do the chance process many times, look at the typical
  outcome"; it beats closed-form probability when the process is
  complicated.
- Simple random sampling (with or without replacement) is the baseline
  design; clusters, strata, and convenience samples trade efficiency or
  feasibility for bias.

## Notes
- The chapter deliberately stays computational: distributions (binomial,
  normal) appear as *outputs* of simulation, not as prerequisites.
- Randomization is the cure for confounding, but only if assignment is
  truly random and compliance is high.
