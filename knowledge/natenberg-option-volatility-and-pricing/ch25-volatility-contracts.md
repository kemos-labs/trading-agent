# Chapter 25 — Volatility Contracts (Variance Swaps & VIX)

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Why volatility contracts exist

Trading vol via options requires dynamic hedging — path-dependent
results, gap risk, fat tails (ch. 23) and rebalancing transaction costs
weaken the edge. Volatility contracts give pure, model-light exposure.
Two kinds: **realized** (variance swaps) and **implied** (VIX).

## Realized volatility / variance swaps

- Settlement = annualized σ of log price returns over the contract life
  (daily settlement prices; ~252 trading days). Conventions: **population
  SD** (÷n — it's the *true* vol, not an estimate) and **zero mean**
  (vol is trend-independent).
- Quotes: price in vol points + **notional vega** (P&L per vol point).
  Example: buy 20 with $10,000/pt → realized 23.75 ⇒ +$3,750;
  18.60 ⇒ −$1,400.
- Most settle in **variance points**: variance ∝ time, so consecutive
  periods combine cleanly (2-mo 25% + 1-mo 22%: σ² = (25²·2 + 22²·1)/3
  for the 3-month annualized variance). Conventionally each variance
  point = notional vega/(2 × vol price): buy 20 at $10,000 vega → $250/
  variance point → realized 23% ⇒ +$250×(529−400) = +$32,250; 19% ⇒
  −$9,750; 50% ⇒ +$525,000 — capped (e.g., cap 40 ⇒ max ~$300k),
  especially on single names (jump risk).

## VIX

- History: launched 1993 on OEX; from 2003 calculated on **SPX** — a
  theoretical 30-day implied vol.
- **New (current) methodology** (Demeterfi-Derman-Kamal-Zou, Goldman
  1999): value = cost of a strip of **out-of-the-money options at every
  strike weighted 1/X²** — the portfolio with *constant variance
  exposure* (a long-ATM vega decays as spot moves; 1/X² weighting
  cancels both moneyness and strike-level effects). Details: OTM vs. the
  put-call-parity **forward**; bid/ask midpoints; no pricing model
  needed — just option prices + T-bill rate; spacing weighting; two
  bracketing expiries interpolated to 30 days.
- **Characteristics**: strong negative correlation with S&P (−0.7444;
  ~5.7× leveraged inverse), but changes in the VIX do **not** predict
  realized vol changes (+0.1561, insignificant) — the *fear index*,
  driven by protection demand. Falling markets genuinely are more
  volatile (realized-vol vs. 30-day-change correlation −0.39).

## Trading the VIX (no index replication)

- **Futures** ($1,000/pt, cash-settle into Wednesday's opening print):
  typically **contango** (long maturities rich) ⇒ long futures *bleed*
  as time passes; futures move **less than the index** (VIX +4.4 →
  Aug-11 front future +2.0; VIX −7.5 → Jan-09 future −5.0); converge at
  expiry. Rules: (1) contango ⇒ decay, (2) futures almost never move as
  fast as the index, (3) convergence at expiry, (4) no replication for
  most traders. Spreads: flat-slope term structure ⇒ spread value
  static; curved ⇒ near months move fastest — in contango buy long/sell
  short; in backward buy short/sell long; structural flips (2008)
  dominate spread P&L.
- **Options** (European, $100/pt): VIX itself is super volatile (50-day
  vol 50–200%!), but the hedge instrument is the *futures*, which is
  less volatile — so VIX option IVs run below index-implied levels.
  Skew = "half frown": low strikes drop fast (VIX < 10 deemed near
  impossible), high strikes flatten; implied distribution has restrained
  tails vs. lognormal, with a touch of far-right-tail risk.

## Replication & applications

- **Replicating variance**: buy 1/X² of every strike + dynamic delta
  hedging ⇒ realized variance exactly. Constant-variance ≠ constant-vol
  exposure (vol = √var) — another reason swaps settle in variance.
  Arbitrage: short variance @ 20 vs. long strip @ 19 ⇒ locked
  +39 × $250 = $9,750. VIX replication is impractical: strip expiry
  mismatch (5-day naked long strip, Friday straddling Wednesday), ITM↔
  OTM conversions needing an SPX-like underlying (futures proxy or
  combos), bid-ask on every leg.
- **Uses**: speculate (long/short realized → variance; long/short
  implied → VIX futures/options); hedge gamma with variance swaps, vega
  with VIX; equity-portfolio hedges (long VIX offsets equity losses via
  the inverse correlation). Indirect vol positions to hedge: market
  makers (volume ↑ with vol → long vol → short VIX), periodic portfolio
  rebalancers (costs ↑ when vol spikes → short vol → long VIX), covered
  call writers (a quiet-market preference → short vol → long VIX
  futures).

## Key takeaways

1. Variance swaps = clean realized-vol exposure, variance-settled
   because variance is time-additive and replicate-able (1/X² strips).
2. The VIX is a 30-day constant-variance OTM-strip cost converted to a
   vol number — model-free but not tradable directly; its derivatives
   lag the index and decay in contango.
3. VIX is a fear/hedging-demand gauge (no realized-vol forecasting
   power); use it to hedge gamma, vega, equity, and structural vol
   positions.
