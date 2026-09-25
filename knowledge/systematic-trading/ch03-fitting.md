# Ch03 — Fitting

**Source:** Carver, *Systematic Trading*, Chapter 3. (Relevant to staunch
systems traders; asset allocating investors and semi-automatic traders can
skip.)

## The perils of over-fitting
Fitting = selecting trading rules/variations using past data. Over-fitting =
selecting rules that fit the past too well and won't make money live. Anecdote:
"Joe" had 50 profitable back-tested rules after a month of auto-testing
software — his firm was liquidated months later. Selecting apparently
profitable rules sifted from thousands is incredibly dangerous.

## Ideas-first fitting process
1. Come up with an idea → initial rule → test on history; drop if unpromising.
2. **Calibration**: test a few *variations* (e.g. ±3% vs ±5% vs ±10% band,
   lookback 1wk/1yr/2yr), pick best by SR or desired *behaviour* (speed).
3. Allocate capital among the kept rules (next chapter).
Caveat: even ideas-first practitioners implicitly over-fit by only testing
ideas they already "know" work (market lore) — back-tested SRs are still
overstated.

## Cheating with a time machine
- **In-sample back-test**: fit on all data, then "test" on the same years.
  Dishonest but common (most back-testing packages default to it); produces
  extremely optimistic results and favours over-complex rules.
- **Half out-of-sample**: fit first half, test second half. Honest but wastes
  half the data and ignores market-structure changes.
- **Expanding window** (Carver's preference): fit on all data *up to* year
  t−1, test year t. Never cheats, wastes nothing.
- **Rolling window**: like expanding but discard old data once enough history
  exists (e.g. last 5 years) — adapts to regime change; window must be short
  enough to track change but long enough for statistical significance.

## When fitting goes bad (gold example)
Fitting the best of 90 variations of the early-loss-taker rule annually on
gold futures with a 1-year rolling window:
- Pick best variation each year → SR 0.07.
- Pick a random variation each year → SR ~0.20.
- **Keep all 90, equally weighted → SR 0.33.** (Best option!)
Why: choosing one variation = overconfidence; 1 year of data is insufficient;
too many variations tested; single-instrument fitting.

## The multiple-testing problem
Testing N unprofitable rules (true SR = 0, random data), keeping any with SR
above a cutoff:
- Even a strict cutoff of SR 2.0 accepts ~2.3 bad rules if 100 are tested
  (with 1 yr data). With 10 years of data you still need cutoffs of 0.6–1.5
  for pools of 10–100 rules.
- **History to confirm a rule is profitable** (t-test, 2σ/95%): true SR 0.2
  → 45 yrs; 0.3 → 37 yrs; 0.5 → 20 yrs; 1.0 → 6 yrs; 2.0 → 1.4 yrs. A
  realistic single-instrument rule (SR ~0.3) needs ~37 years!
- **History to distinguish two rules**: SR 0.3 vs 0.8 uncorrelated → ~30
  years; only fast when highly correlated *and* very different (0.95 corr +
  1.0 advantage → 0.5 yrs).
- **Pool data across instruments**: the same two rules across many
  instruments turn SR 0.05→0.30 into 0.13→1.13, distinguishable in ~11
  years instead of 45. Fitting each instrument separately is
  narrative-fallacy over-fitting; generic rules that work on any instrument
  enable pooling.

## Rules for effective fitting (if you must fit)
1. **Keep it simple** — complex methods hide over-fitting.
2. **Fewer alternatives** — smaller pools need far lower SR cutoffs.
3. **Ban time machines** — always rolling/expanding out-of-sample; don't make
   rolling windows too short (see tables 4–6).
4. **Don't drop rules casually** — distinguishing rules needs ~30 years;
   better to down-weight than exclude (next chapter).
5. **Pool data across instruments** — fit individually only if performance
   differs significantly across instruments (rarely true).
6. **Compare apples with apples** — SR alone misleads when comparing positive
   vs negative skew rules (negative skew flatters SR).
7. **Watch benchmark drift** — avoid rules that just correlate with an asset
   class that had a great secular run (inflation-driven; won't repeat).

## How Carver chooses rules (avoid fitting almost entirely)
1. Small number of rules from a few themes (his: 8 rules from 5 themes; start
   with trend following + carry).
2. A few variations each, chosen by *behaviour* (speed, correlation with other
   variations), **not performance**.
3. Allocate **forecast weights** to variations using returns data — poor rules
   get low weight but are rarely excluded.
Keep the count small: less over-fit risk, fewer redundant "ways to skin the
feline" (one behaviour captured many ways), less complexity. Drop variations
only if >95% correlated with another, costs too high, or trading too slow to
matter — **never on performance alone**. More instruments beat more rules:
cross-instrument correlation < cross-rule correlation.

## Notes
- T-test: an estimated SR > 2σ above zero has only ~2.5% chance of occurring
  if true SR ≤ 0 — the confidence-interval framework used throughout.
- The disciplined workflow: performance data is reserved *only* for forecast
  weights; pre-selecting rules on data contaminates the back-test.
