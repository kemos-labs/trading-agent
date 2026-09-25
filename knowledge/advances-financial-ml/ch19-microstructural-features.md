# Ch19 — Microstructural Features

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 19.

## Purpose
Features extracted from market-microstructure data (FIX messages,
order books): trade classification, the Roll model, Kyle/Amihud,
PIN/VPIN, and data-driven features like order-size distributions and
cancellation rates.

## Three generations of models
- **1st (price-only)**: the **tick rule** — classify trade aggressor
  side: b_t = +1 if p_t > p_{t−1}, −1 if p_t < p_{t−1}, else b_{t−1}.
  High accuracy despite simplicity; transformations of the b series
  (Kalman-filtered expectation, structural breaks, entropy, run tests,
  fracdiff) are themselves informative features. **Roll (1984)**:
  with mid-prices a random walk and trades bouncing the spread,
  c = half-spread = √(−cov(Δp_t, Δp_{t−1})) — spread from the serial
  covariance of price changes.
- **2nd (volume)**: **Kyle (1985)** lambda (price impact per signed
  volume) and **Amihud (2002)** illiquidity (|r|/volume) — the
  volume-based liquidity family.
- **3rd (sequential/informed trading)**: **PIN** (Easley–O'Hara–
  Engle, 1996): the bid-ask spread is the premium market makers charge
  for the option of being adversely selected. **VPIN**: volume-clock
  version, VPIN = Σ|V^B_τ − V^S_τ|/(n·V) over n equal-volume bars —
  the order-flow imbalance rate. Studies conflict on VPIN's volatility
  predictive power (Andersen–Bondarenko negative; several others
  positive).

## Data-driven features (not from theory)
- **Distribution of order sizes**: GUI/human traders use round sizes
  (5, 10, 20, 25, 50, 100, 200, 250, 500) at abnormal frequencies
  (e.g., size 500 is 57× more frequent than 499 in E-mini S&P 500);
  silicon traders randomize. A rising round-size proportion → human
  conviction (trends); a falling proportion → sideways drift.
- **Cancellation rates / limit vs. market orders**: large cancellation
  rates → quotes published without intent to fill → low liquidity.
  Predatory algorithms leave signatures: quote stuffers (message
  flooding to slow competitors), quote danglers, liquidity squeezers
  (trading alongside a forced unwind), pack hunters (decentralized
  collusion to trigger cascades/stop-losses).
- **TWAP execution footprint**: TWAP algos leave a recognizable
  intra-bar pattern — detectable and front-runnable.

## Key takeaways
- Microstructure features encode the *intentions* of market
  participants that prices alone hide — the tick rule, Roll's spread,
  Kyle/Amihud, and VPIN are the core quantifiable set.
- Human vs. algorithmic footprints (round sizes, cancellation rates)
  are simple, powerful features directly computable from tick data.
- Theory-driven and data-driven features complement each other: use
  theory to pick what to measure, ML to learn how to combine it.
