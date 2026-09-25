# Chapter 13 — Risk Considerations

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## The five risks

1. **Delta (directional)**: underlying moves against you. Delta-neutral
   only neutralizes direction *within a limited range*.
2. **Gamma (curvature)**: a large move regardless of direction. Positive
   gamma is not really a risk (you profit from moves); negative gamma
   can destroy edge fast.
3. **Theta (time decay)**: the flip side of gamma — +γ implies −θ.
   Question: how much time can pass before the theoretical edge is gone?
4. **Vega (volatility)**: your vol input is wrong; in practice,
   interpreted as implied-vol sensitivity of the position.
5. **Rho (interest-rate)**: least important; usually ignored.

## Comparing spreads: edge vs. risk

Theoretical edge alone is meaningless (you can multiply size). Normalize
all candidates to the same edge, then compare risk profiles:

- With all options overpriced (model vol 18% < all IVs), candidates:
  ① short straddle (4:3 ratioed), ② ratio call spread (sell more), ③
  long put butterfly.
- **Gamma risk** (value vs. underlying): ① unlimited loss both sides;
  ② unlimited upside only (downside flattens to small profit); ③ fully
  capped both sides (max = strike spacing).
- **Volatility risk** (value vs. vol; breakeven/implied vol of the
  position): ① ≈21%, ② ≈23%, ③ ≈21.5% — so ② looks safest for a
  *moderate* rise, but at high vol ② loses almost as fast as ① (both
  straddle-like), while ③ flattens out. **Volga** explains the shape:
  ① volga ≈ 0 (constant vega), ② negative volga (vega grows more
  negative with vol — vol changes compound against you), ③ positive
  volga (vol changes work in your favor).
- Verdict: ③ long butterfly has the best risk-adjusted profile but
  needs 100×200×100 size for the same edge → execution cost and
  liquidity issues (3 legs). Practical fallback: ② ratio spread beats
  ① straddle (more margin for error on both price and vol).
- Other example (short put calendar vs. diagonal call vs. put diagonal
  ratio): IVs 20.5 / 22 / 20; γ signs differ (calendar and diagonal are
  +γ, diagonal ratio −γ); decay profiles differ sharply (diagonal call
  even turns +θ after 5 weeks). Rule of thumb: **straddles/strangles
  are the riskiest spreads, bought or sold** — least margin for error.

## Margin for error and size

- Size should scale with breakeven distance: a 2-point margin (IV 23
  vs. forecast 25) → small size; a 7-point margin (IV 18) → 10× size.
  "How much can go wrong before the strategy turns against me?"
- Stock-option spreads add rate/dividend risk: calls have +rho and −
  dividend sensitivity, puts −rho and + dividend sensitivity; magnitude
  grows with time between expiries (calendar/diagonal structures).

## What is a good spread?

A good spread is the one that loses *least* when wrong — winning trades
take care of themselves.

- **Efficiency** (same-expiry spreads): |gamma/theta| ratio; larger
  absolute value = more efficient (for −γ/+θ positions, *smaller* ratio
  is better; example: Spread 3 wins on efficiency among ①②③).
- **Adjustments**: underlying adjustments are risk-neutral (Γ/Θ/vega =
  0); option adjustments change all Greeks. Adjusting by selling
  overpriced options raises edge but *grows* the position (20 strangles
  → 48×31) — deadly on a violent move. Disciplined alternative: reduce
  size or adjust in the underlying. New traders: avoid adjustments that
  increase size.
- **Style**: −γ forces you to adjust *with* the trend; +γ forces
  adjustments *against* the trend. Pick the structure matching your
  with/against-trend preference and adjustment frequency.
- **Liquidity**: illiquid options = you're married to the position;
  demand larger edge for long-dated/ITM options; most liquid are short
  term, ATM/slightly OTM. Worst case: illiquid options *and* illiquid
  underlying — only for the experienced.

## Key takeaways

1. Normalize by theoretical edge, then judge spreads on gamma/vega
   profiles and *breakeven volatility* (position implied vol).
2. Volga (vega's vol sensitivity) determines whether vol moves compound
   for or against you — butterflies (positive volga) flatten, ratio
   spreads (negative volga) accelerate.
3. Efficiency = |γ/θ|; adjustments in the underlying are risk-neutral,
   in options they shift the whole Greek profile — and growing size to
   harvest edge is how traders die.
