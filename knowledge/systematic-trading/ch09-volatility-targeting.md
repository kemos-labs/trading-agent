# Ch09 — Volatility Targeting

**Source:** Carver, *Systematic Trading*, Chapter 9. (Sergei's second question:
"how much can you afford to lose?")

## The importance of risk targeting
Deciding overall risk is the most important design decision. Most amateur
traders lose money because positions are too large for their account; painful
losses are the main driver of meddling. Two things must be understood: (1)
**your system** — likely performance, skew, and no over-fitted SR
expectations; (2) **yourself** (and your clients) — can you really face
losing 5–20% in a day?

## Setting the volatility target
- **Volatility target** = the expected (predictable) standard deviation of
  portfolio returns — the long-run average of expected risk. Percentage
  target × trading capital = cash target (annualised cash vol = daily × 16).
- Four questions: (1) how much can you lose? — never trade borrowed money or
  funds earmarked for debts; (2) can you cope? — table 20: at 100% target on
  $100k, expect a $10k worst daily loss monthly, ~$30.5k cumulative loss 10%
  of the time; at 200% target you have a 93% chance of losing half your
  capital over ten years (table 23); (3) can you realise it? — no leverage →
  limited to natural instrument risk; very low-vol instruments need insane
  leverage (EUR/CHF ~1%/yr natural vol → 50× leverage for a 50% target;
  the Jan 2015 16% CHF move wiped out anyone >7× leveraged); (4) is it right
  for your system (SR & skew)?
- **Skew matters**: negative-skew strategies have much worse worst days
  (option-selling: worst monthly every 10 yrs is ~$36k at 50% target vs
  $32k zero-skew) and margin-call risk; positive-skew trend following has
  gentler extremes but higher typical cumulative drawdown (psychological
  challenge). Halve targets for negative skew.

## Kelly criterion → optimal risk
- Compounding means over-betting destroys wealth (win 190% after a 90% loss
  leaves 29%). **Kelly: optimal % volatility target = expected SR** (SR 0.5
  → 50% target; SR 2.0 → 200% → 400%/yr expected). But full Kelly is too
  aggressive: even with correct SR, bad luck gives huge drawdowns (10% chance
  of losing half your capital in 10 years at Kelly-optimal 50%).
- **Use Half-Kelly**: target = ½ × realistic SR. And beware over-fitted
  back-test SR — apply the table-14 pessimism factor (e.g. ×0.75 for
  out-of-sample bootstrap) and cap realistic SR at 1.0. Carver: back-tested
  SR 1.0 → realistic 0.75 → half-Kelly 37%.
- **Recommended targets (tables 25–26)**: staunch systems trader, positive
  skew: SR 0.25→12%, 0.5→25%, 0.75→37%, ≥1.0→50% (negative skew: halve —
  6/12/19/25%). Asset allocating investor: SR 0.2→10% … 0.4→20% (cap; they
  rarely can realise it without leverage). Semi-automatic: 0.2→10% (pos.
  skew) / 5% (neg. skew) … 0.5→25%/12%. **Never run higher than these.**
- Don't change the percentage target (meddling); if you grossly
  miscalculated tolerance, change once, only downwards. Better: start with
  lower capital and scale in.

## Rolling up profits and losses
Keep the *percentage* target fixed; adjust the cash target as capital moves.
$100k at 30% → $30k target; lose $2k → target 30% of $98k = $29.4k (keeping
the old $30k silently raises risk to 30.6%). After gains, roll up: $103k →
$30.9k (compounding). Update on profits, losses, withdrawals, injections
(margin top-ups excluded). Check hourly if automated; at least daily above a
15% target; always weekly if leveraged.

## Traditional "% of capital per trade" — the trap
Traditional systems cap each bet at X% of capital. Convert: implied annualised
vol target ≈ (max % per trade) × (avg 2 bets) × √(256/avg holding days)/
2-ish (average bet = half max). A "sedate" rule (week holding, 10% max per
trade, avg 2 positions) implies a suicidal ~160% vol target → Kelly-optimal
SR ≥ 1.6, i.e. 256%/yr expectation — pure overconfidence.

## Summary
- Percentage volatility target: your long-run expected annualised vol — the
  min of (comfort per tables 20–23, attainable with your leverage/instruments,
  safe given leverage needs, and table 25/26 recommendations). Unchanged over
  time.
- Trading capital: account value, updated daily with P&L and flows.
- Annualised cash target = capital × % target; daily = ÷16.

## Notes
- The whole chapter is one discipline: pick the *maximum* risk you'd ever
  run from Half-Kelly + skew haircuts, express it as a fixed percentage,
  and let position sizing (ch10) do the work — never chase returns by
  raising risk.
- Cross-check with ch1: the 200% vol / SR 0.8 example and the "lose 40% in
  one day every ~3 years" stats are the concrete versions of these tables.
