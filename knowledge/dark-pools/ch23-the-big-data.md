# Ch23 — The Big Data

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 23.

## Purpose
The AI-investing frontier: Kinetic's failed attempt to build a
"digital analyst" from alternative data, and Cerebellum Capital's
genetic-algorithm "Invention Machine" that found a steady ~7% anomaly —
illustrating both the promise and the brutal execution realities of
machine-driven fundamental trading.

## Kinetic (Ladopoulos)
- Ioannis Ladopoulos ("Acid Phreak," ex-Masters of Deception phone
  hacker, later Instinet security chief, then D.E. Shaw-adjacent) teams
  with Roger Ehrenberg (ex-Deutsche Bank) to mine **Big Data** for
  trades — a re-run of their failed Monitor110 (which scoured 9M+
  sources and drowned in hay).
- The plan: scale down to the **Russell 2000** (small caps with less
  analyst coverage = low-hanging fruit), gather gold-standard sources
  (SEC.gov, blogs, Chinese shipping data, job listings, Twitter), and
  let AI crunch it into buy/sell probabilities — a Watson-style analyst.
- Selerity (a news-scanning service) pre-scrapes an unlinked Microsoft
  earnings URL in Jan 2011, trading before the release — machine-
  readable news as a weapon.
- It fails: the strategies lose money in test after test. The reasons
  are instructive — (1) their own trades move the small-cap prices they
  trade (market impact), (2) hunter-seeker bots detect and front-run
  them, (3) the team's faith in the machine ("The machine knows") and
  refusal to stop trading. Ladopoulos is fired Aug 2011.
- Kurzweil's FatKat (1999) is the earlier cautionary ancestor: algos in
  a Darwinian death match, little success.

## Cerebellum Capital (Andre & Teller)
- David Andre and Eric "Astro" Teller (ex-BodyMedia wearable AI) build
  the **Invention Machine**: genetic algorithms that evolve, mutate,
  breed, and kill off simulated "mini-BOT" traders, running hundreds of
  thousands of generations/day while crawling the Internet for
  predictive signals (e.g., OpenTable bookings at expensive Wall Street
  restaurants as a bullishness proxy).
- Discovery: a nearly perfect ~7%/year anomaly (stocks + options).
  The segregated **Cerebellum ATM Fund** (Dec 2009) grows to ~$50M by
  summer 2011 — evidence that AI can mine the market for strategies, at
  least at small scale.

## Key takeaways
- Alternative-data trading is an execution problem as much as a signal
  problem: market impact and front-running can kill a true edge.
- Machine learning for *strategy discovery* (genetic search) differs
  from rule-based trading; "the machine is always right" is a failure
  mode, not a virtue.
- Small-cap, low-coverage universes are easier to find edges in but
  harder to execute in — the same property cuts both ways.
- Machine-readable news creates a new information asymmetry: whoever
  parses it fastest trades first.
