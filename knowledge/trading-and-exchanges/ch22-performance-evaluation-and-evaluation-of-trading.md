# Ch22 — Performance Evaluation (Luck vs. Skill)

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 22.

## Purpose
How to evaluate traders and strategies honestly: the statistics of
separating skill from luck, and why most apparent outperformance is
noise.

## The evaluation problem
- Performance is a noisy signal: returns over a sample combine true
  skill with luck. With typical volatility, distinguishing a good
  trader from a lucky one requires a very long track record.
- Statistical test: is the observed mean return significantly
  different from the benchmark, given the standard error
  `σ/√n`? A 1% edge with 20% annual volatility needs ~n ≈ (20/1)² =
  400 years of independent observations — i.e., never.

## Why most results are luck
- **Selection bias**: we only see the winners — the funds that
  survived and are marketed. The 1-in-100 lucky manager looks like a
  genius in hindsight.
- **Survivorship bias**: dead funds disappear from databases; average
  reported performance overstates reality.
- **Multiple testing**: with thousands of strategies tested, some will
  beat the market by chance; without adjustment, the lucky ones are
  published and funded.
- **Trading costs**: an apparent edge is often exactly the size of the
  transaction costs the strategy pays.

## What to look for
- **Sharpe ratio** (excess return / volatility) and its statistical
  significance; information ratio vs. a benchmark.
- Consistency: a manager whose wins cluster in one period or one style
  is more likely lucky than a manager with diversified, persistent
  edge.
- Track record length and independence of observations; adjust for
  multiple testing and optionality (a strategy that is long optionality
  will have positive skew but may still be a poor bet).

## Key takeaways
- **Evaluation is a hypothesis test**: state the benchmark, compute
  the standard error, and demand significance adjusted for the number
  of trials — otherwise you are funding noise.
- For your own strategies: track records shorter than the
  `(vol/edge)²` horizon are uninformative; paper-trade and
  out-of-sample test before risking capital.
- The most common real edge is not alpha but **cost and risk
  management** — the visible, auditable parts of trading.
