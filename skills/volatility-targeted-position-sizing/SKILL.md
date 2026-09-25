# Volatility-Targeted Position Sizing & Risk Management

## name
Volatility-targeted position sizing and risk management (Carver framework)

## description
Size positions so each instrument/rule contributes equal expected risk: set a
fixed percentage volatility target (Half-Kelly of the realistic Sharpe ratio),
convert forecasts (scaled −20..+20, expected |·| = 10) into actual position
sizes via a volatility scalar, and scale the whole portfolio back up with
diversification multipliers. Everything is volatility-standardised so one rule
works across instruments.

## when to use it
- Building a systematic trading system where you must decide how much to bet
  given forecasts, instrument risk, and account size.
- Translating an arbitrary rule (EWMAC crossover, carry, discretionary
  forecast) into concrete positions without hand-tuned "3% per trade" rules.
- Calibrating total portfolio risk to your pain threshold instead of chasing
  back-tested Sharpe ratios.

## method / formula / code

**Pipeline (per instrument):**
1. **Price volatility**: expected daily stdev of % returns (25-business-day
   moving stdev, or EWMA ≈ 36-day equivalent; eyeball 1-month chart for
   discretionary traders).
2. **Instrument block & block value**: what "one" unit is (1 share, 1 futures
   contract, £1/point) and its P&L per 1% price move.
3. **Instrument currency volatility** = block value × price volatility;
   **instrument value volatility** = ICV × FX (instrument currency / account
   currency).
4. **Daily cash volatility target** = annualised % target × trading capital
   ÷ 16 (√256).
5. **Volatility scalar** = daily cash target ÷ instrument value volatility.
   This is the position consistent with a constant forecast of +10.
6. **Subsystem position** = scalar × forecast ÷ 10 (forecast ∈ [−20, +20],
   cap at ±20). Asset allocators always hold the scalar (constant +10).
7. **Portfolio position** = subsystem position × instrument weight ×
   instrument diversification multiplier, rounded to whole blocks. Trade only
   if >10% away from current position (**position inertia**).

**Setting the % volatility target (Half-Kelly):**
- Target = ½ × realistic expected Sharpe ratio (after costs; apply ~0.75
  pessimism factor to out-of-sample back-tested SR; cap realistic SR at 1.0
  for systems, 0.5 semi-auto, 0.4 static allocators).
- Halve the target again for negative-skew strategies. Recommended maxima
  (for back-testable systems traders, positive skew): SR 0.25 → 12%; 0.5 →
  25%; 0.75 → 37%; ≥1.0 → 50%. Use lower caps elsewhere — semi-automatic
  traders ~10–25% (max SR 0.5) and static asset allocators ~10–20% (max SR
  0.4).
- Keep the *percentage* target fixed; roll the *cash* target up/down with
  daily capital (30% of $98k after a $2k loss, not $30k).

**Diversification multipliers** (restore target risk after combining
less-than-perfectly-correlated components): multiplier = target vol ÷ natural
portfolio vol, ≈ table of (n assets × avg correlation); cap at **2.5**. Floor
negative correlations at zero. Apply once for combined forecasts and once for
instrument portfolios.

**Cost-speed limit:** standardised cost = 2 × cost-per-block ÷ (16 × ICV) in
SR units per round trip; never spend more than ⅓ of the pessimistic pre-cost
SR in costs per year (≤0.13 SR systems traders; ≤0.08 SR others) — i.e.
turnover × standardised cost ≤ limit.

## known pitfalls
- **Low-volatility instruments**: tiny natural vol → huge leverage required →
  blow-up risk (CHF unpeg Jan 2015, ~16% move wiped out >7× leverage); also
  higher standardised costs. Exclude them.
- **Over-fitting** (ch3): don't fit rules on back-tested SR; select variations
  by behaviour; pool data across instruments; expect to need 10–40 years to
  confirm profitability of realistic rules.
- **Full-Kelly is too aggressive**: use Half-Kelly; even at Kelly-optimal
  risk there is a ~10% chance of halving capital in 10 years.
- **Never round intermediate values** (volatility scalars stay fractional);
  round only at the final target position.
- **Unpredictable risk**: correlations spike in crises; vol estimates lag —
  the multiplier cap and position inertia are the safety valves.

## source book
Carver, *Systematic Trading* (2015): ch5 framework, ch7 forecasts, ch8
combined forecasts, ch9 volatility targeting, ch10 position sizing, ch11
portfolios, ch12 speed and size.
