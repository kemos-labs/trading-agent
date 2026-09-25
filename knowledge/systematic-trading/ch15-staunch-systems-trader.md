# Ch15 — Staunch Systems Trader (+ Epilogue)

**Source:** Carver, *Systematic Trading*, Chapter 15 + Epilogue. (Example 3 of
3: full multi-rule, multi-instrument futures system.)

## Setup
$250,000 trading capital; part-time; free daily data; futures only. The full
framework end-to-end: EWMAC trend + carry rules, six instruments, handcrafted
weights, 20% vol target.

## Instrument choice
Six futures, one per asset class, all with max positions ≥ 4 contracts and
standardised cost ≤ 0.01 SR: Eurodollar (0.008 SR, max pos 8), US 5-yr note
(0.004, 5), Euro Stoxx (0.002, 4 — close to the limit), V2TX European vol
index (0.009, 11 — negative skew but only ~10% weight), MXP/USD (0.007, 15),
Corn (0.005, 9). Trade Eurodollar ~3 years out (near months have near-zero
vol under ZIRP); stitched prices via the Panama method; carry needs non-nearest
delivery where liquid (V2TX, Eurodollar, corn only).

## Rule selection & forecast weights
Use at least 3 EWMAC variations (insufficient evidence to prefer fewer) +
carry. Raw turnovers: EWMAC 2,8 → 54 (max cost 0.0024), 4,16 → 28 (0.0046),
8,32 → 16 (0.0081), 16,64 → 11 (0.012), 32,128 → 8.5 (0.015), 64,256 → 7.5
(0.017), carry → 10 (0.013). Fast rules only work on cheap instruments (2,8
only Euro Stoxx; 4,16 also T-note; 8,32 too fast for V2TX). For simplicity
drop the fast ones → **EWMAC 16/32/64 + carry = 4 variations**, all
affordable everywhere.
Handcrafted forecast weights (same as ch8): EWMAC 16,64 21%, EWMAC 32,128 8%
(highly correlated with neighbours), EWMAC 64,256 21%, carry 50%. Forecast
diversification multiplier **1.31**. Equal pre-cost SR assumed across rules
(max cost spread only 0.031 SR → no SR adjustments needed).

## Volatility target
Back-tested (out-of-sample bootstrap) SR 0.53 after costs → ×0.75 (table 14)
→ realistic 0.40 → table 25 col A (positive/zero skew; 90% benign assets +
10% V2TX) → **20% target** → $50,000 annual / $3,125 daily. Check account
daily. Cost check: weighted rule turnover 9.57 × 1.31 = 12.5 combined; ×
worst instrument cost 0.009 → 0.113 SR/yr ≤ 0.13 speed limit. Vol look-back:
5-week default vs 20-week saves only 0.008 SR → **keep 25-day / EWMA 36**.
2.3% annual drag at 20% vol on V2TX (less elsewhere) + small roll costs.

## Portfolio weights (handcrafted, dynamic → ×0.7 correlations)
Subsystem correlations (table 46): rates pair 0.35; equities pair 0.42;
everything else 0.07–0.18. Groups: interest rates (STIR + bonds) 50/50;
equities Euro Stoxx 66.6% / V2TX 33.3%; FX 100% MXP; commodities 100% corn.
Top level: inter-group correlations ≈ 0 → equal 25% each, but **Euro Stoxx
needs ≥20% weight for min 4-contract positions** → equities group bumped to
30% (⅔ Euro Stoxx = 20%, ⅓ V2TX ≈ 10%), leaving 23.3% each for rates/FX/
commodities. Final weights: Eurodollar 11.7%, T-note 11.7%, Euro Stoxx 20%,
V2TX 9.8%, MXP 23.3%, Corn 23.3%. Instrument diversification multiplier
**1.89**. No cost-based weight adjustments (no evidence post-cost SRs
differ).

## Daily process
Account value → capital → 20% × capital ÷ 16 = daily cash target; prices +
FX (USD/EUR); EWMA price vol (36-day) → instrument value vol; forecasts per
rule variation (cap ±20) → combined forecast (weights + multiplier 1.31, cap
±20) → volatility scalar → subsystem position (combined × scalar ÷ 10) →
portfolio position (× weight × 1.89) → round to whole contracts → trade if
>10% from current (position inertia).

## Diary snapshots (late 2014)
- 15 Oct 2014: scalars 5.7–29.3; combined forecasts: T-note +20 (strong
  momentum + carry >19), V2TX −11.7 (carry −20), corn −11.6. Positions: long
  6 Eurodollar, long 5 T-note, short 6 V2TX, short 5 corn, etc.
- 1 Dec 2014: capital $260,000 → daily target $3,250; equity rally → Euro
  Stoxx now long 1, V2TX short deepened to −11 (carry weakened); scalars
  reshaped by vol changes; trades happened almost daily between snapshots.

## Epilogue — what makes a good systematic trader
- **Humble**: underestimate your skill/luck; assume it will go badly; don't
  be clever.
- **Sceptical**: trust nobody — brokers, course sellers, authors.
- **Pessimistic**: back-tests overstate; cap SR expectations (1.0 systems,
  0.5 semi-auto, 0.4 asset allocators); steady small gains = hidden negative
  skew, cut risk.
- **Thoughtful**: know why you'd make money and why not.
- **Thrifty**: know costs; speed limit = ≤⅓ of pessimistic SR on costs.
- **Nervous**: only risk money you can afford to lose; **Half-Kelly** (target
  = ½ pessimistic SR); diversify; avoid low-vol instruments.
- **Diligent in design, lazy in operation**: commit and don't meddle.
- **Lucky**: even doing everything right, luck decides — quantify and
  withstand the downside.

## Notes
- This chapter is the culmination: every earlier concept (vol standardisation,
  forecasts, handcrafting, multipliers, speed limits, max positions) is used
  exactly once in one deterministic pipeline.
- The takeaway structure: rules (engine) are the only discretionary part;
  everything else is fixed arithmetic + fixed risk discipline.
