# Ch10 — Position Sizing

**Source:** Carver, *Systematic Trading*, Chapter 10. (Sergei's third question:
"how risky is it?" — turning forecasts into actual positions.)

## How risky is one unit? (definitions)
- **Instrument block**: what 'one' of the instrument means (1 share, 1
  futures contract, £10/point spread bet, 100-share lot).
- **Block value**: P&L from a 1% price move on one block. Apple share at $400
  → $4; FTSE spread bet at £10/point → £650 for a 1% move (6500→6565); WTI
  crude (1000 bbl) at $75 → $750; Eurodollar future → $2,450 (100 − rate
  pricing; 1% price move ≈ 0.98% rate change × $1m × ¼yr).
- **Price volatility**: expected daily stdev of instrument % returns (equity
  ~1%; 2-yr Schatz ~0.02%).
- **Instrument currency volatility** = block value × price volatility (crude:
  $750 × 1.333% = $997.50/day per contract).
- **Instrument value volatility** = instrument currency vol × exchange rate
  (instrument currency / account currency). Crude for a GBP account:
  $997.50 × 0.67 = £668.325. Don't round intermediate values.

## Measuring recent volatility
Volatility persists, so recent stdev is a good predictor. Three methods: (1)
eyeball the chart (fine for semi-automatic); (2) simple moving-window stdev —
default **25 business days** (industry standard, e.g. RiskMetrics; Carver
found look-backs from days to ~6 months made almost no pre-cost difference,
so 25 avoids over-fitting); (3) EWMA stdev — smoother yet responsive,
default ~36-day equivalent. **Danger**: very low recent vol (CDS early 2007,
EUR/CHF early Jan 2015) → huge block counts → blow-up when vol returns;
another reason to avoid ultra-low-vol instruments.

## From target to position
- **Volatility scalar** = daily cash volatility target ÷ instrument value
  volatility. This is the position consistent with a *constant* forecast of
  +10 (the long-run average). Example: £1,000,000 annualised target →
  £62,500 daily ÷ £668.325 → 93.52 crude contracts (no rounding).
- **Subsystem position** = volatility scalar × forecast ÷ 10. Forecast −6 →
  (93.52 × −6)/10 = short 56.11 contracts. Forecast +5 → half of 93.52;
  −20 → short 187.04.
- Asset allocating investors (constant forecast +10) always hold exactly the
  volatility scalar.
- Drivers: larger |forecast|, bigger account, higher risk appetite, lower
  instrument vol → larger positions.

## Summary of the chain
forecast (±20, avg |·| 10) → daily cash target (annualised ÷16) → price vol
(%/day) → block → block value → instrument currency vol → × FX → instrument
value vol → volatility scalar (= daily target ÷ instrument value vol) →
subsystem position (= scalar × forecast ÷ 10).

## Worked example (WTI crude, £1m target, forecast −6)
annualised target £1,000,000 → daily £62,500; price vol 1.33% at $75; block
= 1 contract, block value $750; instrument currency vol $997.50; USD/GBP
0.67 → value vol £668.325; scalar 93.52; position = −56.11 contracts.

## Notes
- The framework's invariants hold: positions scale linearly with forecast
  (because all instruments are vol-standardised), which is why the fixed
  |forecast| scale of 10 and the ±20 caps keep the whole system calibrated.
- Rounding is deferred to the portfolio stage (ch11) and trading realities
  (ch12); fractional positions are fine mathematically here.
