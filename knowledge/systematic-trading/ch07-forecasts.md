# Ch07 — Forecasts

**Source:** Carver, *Systematic Trading*, Chapter 7.

## What makes a good forecast
A forecast is a number: positive → buy/long, negative → short, ~zero → no
position. It must be **scaled** (not binary): magnitude expresses how much
the price is expected to move. Why scaled?
1. Larger |forecast| ⇒ larger subsequent moves (rule returns increase with
   forecast size);
2. Binary rules cost more to trade (full-size round trips to flip);
3. The framework requires continuous, non-lumpy forecasts.

**Forecasts ∝ risk-adjusted expected return** (volatility standardisation):
e.g. Bunds expected 2%/yr at 8% vol → 0.25; Schatz 1%/yr at 2% vol → 0.5, so
Schatz forecast should be double Bunds'. This makes one rule usable on all
instruments, enables pooling for fitting, handles changing vol over time, and
leaves account size / risk appetite to position sizing (ch9–10). Since
return/vol = Sharpe ratio, **expected SR is a natural forecast**.

**Consistent scale**: any consistent scaling works, but Carver recommends an
**expected absolute value of 10** (+10 = average buy, −10 = average sell).

**Cap forecasts at ±20** (e.g. +25 → +20). Reasons: (1) risk control — stop
one rule dominating portfolio diversification; (2) limited data — extreme
forecasts are rare (~5% beyond ±20 for Gaussian), so their returns are
uncertain; (3) extremes often behave differently (dead-cat bounces, 50%+
dividend yields = bankruptcy); (4) high forecasts can stem from low vol,
which usually spikes later (Abe 2013 JGB example); (5) capping costs little
(~5% of cases) for large risk-control benefit. If you can't short: clamp
negative forecasts to zero.

## Discretionary forecasts (semi-automatic traders)
Quantify conviction on a −20..+20 scale (table: Very strong sell −20 …
Neutral 0 … Very strong buy +20; ±5 weak, ±10 average, ±15/20 strong).
Never change a forecast once a bet is open (meddling risk) — close positions
with a systematic **trailing stop loss** instead. Benefits of the framework:
predictable live behaviour, correct position sizing, more time for the
forecast, and stop-loss discipline ⇒ early-loss-taking behaviour ⇒ benign
positive skew.

## The asset allocating investor's 'no-rule' rule
A constant forecast of **+10 for all instruments at all times**. Because all
forecasts are vol-standardised, equal forecasts = equal expected SR across
assets — a true risk-parity ("fourth degree" static) portfolio with
time-varying vol adjustment, DIY (no fund fees), and you can still beat
equal weights via handcrafted instrument weights (ch4).

## Two example systematic rules (staunch systems traders)
1. **EWMAC (Exponentially Weighted Moving Average Crossover) — trend
   following, positive skew**: fast EWMA vs slow EWMA; fast above slow → long,
   below → short. Carver favours it: works (early-loss-taker evidence,
   academic support), explainable (prospect theory), price-only data, easy,
   benign skew. Captures momentum/trends at multiple speeds via variations.
2. **Carry (contango/roll-down) — negative skew**: the return earned if
   prices stay perfectly stable = yield − borrowing cost (FX: borrow JPY at
   0.5%, invest AUD at 3.5% → 3% carry; Eurodollar futures convergence; 2008
   crude crash). Theory says prices should offset it; usually they don't —
   steady gains with occasional violent breakdowns. Combines well with EWMAC
   (one likes trends, the other likes calm). Two rules ≈ 85% of Carver's
   full-system back-tested performance.

## Adapting/creating rules
Pare to simplicity & objectivity ("Buy if open > yesterday's close"); make
**continuous** (raw forecast = open − close); **volatility-standardise**
(raw forecast ÷ recent stdev of daily returns) so it's market-agnostic;
**recalculate every period** (continuous forecasts, no separate entry/exit
rules — explicit exits are usually over-fitted; if you must use entry/exit,
use the semi-automatic trailing-stop rule); **rescale** so expected
|forecast| = 10 via a **forecast scalar** (e.g. natural mean abs value 0.33
→ scalar = 10/0.33 ≈ 30; found by back-testing *behaviour*, not performance).

## Selecting rules & variations (recap from ch3)
Choose by behaviour, not back-tested SR: (1) drop any two variations >95%
correlated; (2) drop rules holding > a few months (too slow) or too fast to
trade given costs. 10 instruments × 3 rules × 2 variations = 60 forecasts.

## Notes
- Forecast sign + magnitude is the entire input interface to the framework —
  that's why consistency of scale and capping matter so much (ch5's
  "well-defined interface").
- Explicit exit/stop rules belong inside the *rule* (vol-based), never in
  position sizing (ch5's bad example).
