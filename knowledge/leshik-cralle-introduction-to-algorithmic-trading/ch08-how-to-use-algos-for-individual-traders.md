# Chapter 8 — How to Use Algos for Individual Traders

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## The ALPHA ALGO concept

Generic term for the authors' approach: algorithms aimed primarily at
**profit per trade** (vs. institutional impact/anonymity goals).

- **Liquidity is a non-issue**: trades are small (≈1,000–2,500 shares)
  — one or two orders of magnitude below institutional orders, so the
  individual is just "noise". *Avoid* thinly traded stocks (<500,000
  shares/session).
- **Manual trading first**: the Part II Excel-template algos are traded
  manually to build a bedrock understanding of the
  algo–market–stock triangle; order placement deliberately manual.
  Practice on simulators (e.g., TALX from TerraNova, Ameritrade's
  simulator) until running the SIM is effortless.
- **Parameterization is everything**: lookback periods vary over time
  per stock and need periodic re-adjustment driven by changes in
  activity; re-parameterize *preferably daily* with a short lookback —
  five sessions is usually plenty.
- **Know your algo**: full understanding of components, parameters,
  strengths, limitations removes the emotional burden; you are trading
  "prepackaged thinking time".
- Discipline rules: don't trade when physically/mentally unwell; don't
  second-guess the algo once the watchlist is set; mastery takes
  practice (weeks to months before OMS interactions become automatic).

## Key takeaways

1. Small size + liquid names ⇒ the individual trader competes on
   *signal quality*, not execution engineering.
2. Parameterize short and often (5-session lookbacks, daily re-tuning);
   keep emotions out by trusting a well-understood algo.
