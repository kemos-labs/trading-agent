# Chapter 6 — Currently Popular Algos

Source: Leshik & Cralle, *An Introduction to Algorithmic Trading* (2011)

## Institutional execution algos (mid-2010)

Prime function: get the trade done with **minimum market impact,
anonymity, speed, without being front-run** — immediate profit is
secondary for Tier 1 (longer-duration trades). Only HFT firms, happy
with a couple of bps/trade, are immediate-profit oriented.

- **VWAP** (Volume-Weighted Average Price): the oldest, most-used algo
  and a buy-side/sell-side benchmark.
  `P_vwap = Σ(P·V) / ΣV`.
  Slices a large order into waves sized proportional to expected market
  volume per time slice (real-time + historical volume data), following
  the intraday "volume smile" (more activity at open and close). Tweaks:
  lookback choice, execution-price or volume constraints, guaranteeing
  brokers, participation algos. Pitfalls: volume is a moving target —
  daily patterns vary by stock (thinly traded stocks worst); traders can
  be "discovered" and front-run.
- **TWAP**: equal slices over a set timeframe — convenient but
  *predictable*; counter with fuzzy/randomized wave spacing, wave sizes,
  or RNG-driven execution.
- **POV** (Percentage of Volume): participate at a low % of current
  volume to "stay under the radar."
- **Black Lance / liquidity search**: pings dark-pool venues, analyzes
  responses to find liquidity.
- **Peg**: limit orders that follow the market like a trailing order,
  sizes randomized.
- **Iceberg**: hides a large order by slicing into randomized small
  segments (limit-order variant for longer horizons).
- Structural algos: recursive (self-calling until a condition), serial,
  parallel (multi-core), iterative (if/then, do-while, for-next with
  parameterizable tests).

## Pair trading (the original statarb)

- Market-neutral by construction: depends on correlation/anti-correlation
  of two stocks (usually same sector), not market direction.
- Tartaglia (Morgan Stanley, 1980s, team incl. Bamberger): when a
  correlated pair diverges, short the outperformer, long the
  underperformer; expect mean reversion; close when parallel again.
- Risks: one leg's liquidity crisis (can't close); correlation can
  break. Sources: impactopia.com (Prof. Vandewalle's stock topology),
  cluster/XY analyses for cohort selection.

## Individual vs. institutional

Individual traders (≈1,000-share orders) need *immediate* returns —
hence the authors' **ALPHA ALGOS** (Part II), distinct from these
institutional tools.

## Key takeaways

1. Execution algos are about impact/anonymity engineering (VWAP/TWAP/
   POV/iceberg/peg), not alpha.
2. Predictable execution = exploitable (front-running) — randomize.
3. Pair trading is the canonical market-neutral mean-reversion template;
   liquidity risk is its Achilles heel.
