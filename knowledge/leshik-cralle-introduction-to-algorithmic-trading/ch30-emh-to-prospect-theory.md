# Chapter 30 — From the Efficient Market Hypothesis to Prospect Theory

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## EMH vs. behavioral finance

- **EMH** (Eugene Fama, 1950s): markets are information-driven; all
  info is instantly, equally distributed and discounted into prices;
  traders act rationally. Makes TA and trading itself pointless.
  By the 1990s the behavioral school found enough anomalies that EMH
  was amended into **weak, semi-strong, and strong** forms (still with
  us to some degree).
- **Behavioral finance** (Kahneman, Tversky et al.): traders do not
  act rationally; choices depart systematically from expected utility
  theory. The "Electronic Pit" is decision-making under uncertainty
  facing unknown participants watching identical data.

## Prospect Theory and biases (the authors call them "heuristics")

- **Loss aversion** (Tversky & Kahneman): losses are ~2× as
  psychologically powerful as gains; people sell winners too early and
  hold losers hoping for a bounce.
- **Representativeness**: classify by similarity to a known class; we
  force-fit new items, neglect base-rate frequency and sample size
  ("law of small numbers"); redundant correlated variables inflate
  confidence while decreasing accuracy.
- **Availability**: judge frequency by ease of recall (a gory pileup
  → drive more carefully for a few days).
- **Anchoring and adjustment**: weight a starting point (yesterday's
  close) too heavily; adjustment away from the anchor is hard even
  with contradicting evidence.
- **Endowment effect** (Thaler): ownership itself adds psychological
  value (don't sell stocks held a while).
- **Status quo bias**: inertia in changing established behavior.

## Trend = difference of opinion

- Price unchanged + high volume = strong disagreement (buyers vs.
  sellers; every trade has a counterparty). A *trend* = supply/demand
  imbalance — steeper slope = greater disagreement. Volume and
  transaction frequency gauge trend health; a marked volume drop
  signals the trend's end.
- Bubbles/crashes: positive feedback of sufficient magnitude,
  persistence, and speed.

## Implications for the Leshik-Cralle method

- The method is deliberately **local and short-lookback** (5–60
  sessions); volatility regime shifts are just large perturbations in
  the general turbulence. Temporal stratification matters for long
  lookbacks (ecology, regulation, Kondratieff cycles) — the Holy Grail
  would be an algo working "from the beginning of time"; the authors
  haven't found one. (100 stocks × 60 sessions = 6,000 Excel files.)
- Greed, fear, regret, envy overlay the dispassionate analysis.

## Key takeaways

1. EMH is flawed; behavioral biases (representativeness, anchoring,
   availability, endowment, status quo, loss aversion) explain
   systematic departures — and the TA that exploits them.
2. Trend strength = volume × slope (difference of opinion); falling
   volume = trend exhaustion.
3. The authors deliberately stay local/short-lookback to sidestep
   regime/ecology stratification problems.
