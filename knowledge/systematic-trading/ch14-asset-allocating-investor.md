# Ch14 — Asset Allocating Investor

**Source:** Carver, *Systematic Trading*, Chapter 14. (Example 2 of 3: static
risk-parity investing via the framework, no price forecasting.)

## Who it's for
You don't believe relative asset returns can be forecast; hold a diversified
portfolio with the 'no-rule' rule (constant forecast **+10** for everything
= all assets assumed to have the same Sharpe ratio). Example: €10,000,000
pension fund in **ETFs** (bonds + equities only, no leverage/shorting), with
trustee constraints (≤40% bonds, ≤30% EM within equities, ≤25% EM and ≤25%
inflation-linked within bonds — all risk-adjusted).

## Framework choices
- **Instruments (10 ETFs)**: choose lowest expense ratios; avoid bond ETFs
  with <5%/yr vol (can't hit target without leverage, higher standardised
  costs) → prefer longer-maturity bond funds. Trade in 100-share blocks.
  Standardised cost: use the worst (IGIL inflation-linked, 0.08 SR) for all.
- **Volatility estimation**: ETFs are expensive → use a slow **20-week (100
  business day) look-back** for price vol: turnover drops 1.6 → 0.4 round
  trips/yr, costs 0.13 → 0.032 SR (vs 5-week default). Max affordable
  standardised cost = 0.08 ÷ 0.4 = 0.20 SR; all chosen ETFs are cheaper.
- **Volatility target**: constrained by *no leverage*, not risk appetite.
  Two-step: (1) initial guess = lowest instrument annualised vol (IGIL
  6.88%); compute positions, total value, realised leverage factor (value ÷
  capital); (2) scale target to hit the **desired leverage factor of 90%**
  (keep cash reserve; just below the 100% max): 6.88% × 90/82.6 = **7.5%**
  target → €750,000 annual / €46,875 daily cash target. Implied SR 0.15
  (Half-Kelly) — easily achievable. Expectation: max after-cost SR 0.4 →
  ~3.0%/yr + risk-free; modest growth is the point. Costs: 0.032 × 7.5% =
  0.24% drag + ETF fees (0.05–0.55%).
- **Instrument weights — handcrafting** with unadjusted instrument-return
  correlations (static strategy: no ×0.7). Correlations: bonds 0.75 among
  developed, 0.3–0.35 to other bonds; bonds–equities ~0.1; developed
  equities 0.75 among themselves, 0.5 to EM.
  Grouping with constraints: developed bonds 33.3% each (US/EU/UK); developed
  equities 25% each (US/UK/EU/JP); bonds: EM 25% (constrained) + inflation
  25% (constrained) + 50% developed; equities: EM 30% + 70% developed; top:
  bonds 40% / equities 60%. Final weights: 6.67% each developed bond, 10%
  EM & inflation bonds, 10.5% each developed equity, 18% EM equity.
  **Instrument diversification multiplier = 1.61** (10 assets, these
  correlations).
  Note: 57% of *cash value* sits in bonds though only 40% of weight — the
  risk-parity signature (bonds need more cash per unit of risk).
- **Using return predictions**: translate views into annualised SRs (Euro
  Stoxx +8% target ÷ 16% vol = SR 0.5) and adjust *weights* (not forecasts —
  avoids overtrading) via ch4 table 12 **column B** ('without certainty'):
  SR +0.3 vs average → ×1.17. Renormalise; don't change the diversification
  multiplier; adjustments should be small and infrequent (they add trading).

## Weekly process
Account value → capital → annual & daily cash targets (7.5% × capital ÷ 16);
prices + FX; instrument value vols (20-week look-back); subsystem position =
volatility scalar (forecast is +10); optional SR-based weight adjustments;
portfolio position = scalar × weight × 1.61; round to 100-share blocks;
trade if >10% away (position inertia). Weekly rebalancing is right for this
low-turnover, unlevered portfolio (funds could do it intraday in stress;
amateurs annually).

## 2008 trading diary highlights
- 1 Jul 2008: initial positions from scalars (US bonds 1242 blocks of 100
  shares etc.). Everything from the fixed +10 forecasts and handcrafted
  weights — a pure risk-parity starting portfolio.
- 1 Oct 2008: strategists say equities SR 0.6, bonds 0 → weights tilt to
  equities (bonds ×0.83, equities ×1.17, renormalised; bonds 5.35% vs 8.03%,
  equities 11.88% vs 20.37%). Little trading — vol rises roughly offset by
  weight changes.
- 10 Oct 2008: crash week; capital €9,126,500 (losses limited by
  diversification). Strategists flip: bonds 0.6, equities 0 → weights invert
  (bonds up to 8.07/12.11%, equities down to 9.02/15.47%). Huge equity
  selling (Sell 268 UK equity blocks etc.) — mostly driven by **exploded
  volatility** shrinking scalars, not just the weight changes. The framework
  automatically cut equity risk as vol spiked, without discretion.

## Notes
- The asset allocator's whole edge is *diversification + vol targeting*:
  weight = product of group weights at each level; position scales with
  daily target and 1/vol.
- Constrained weights make this example richer than pure handcrafting: the
  mandate is encoded at the grouping stage.
- This is the archetype for unlevered, low-turnover, benchmark-style
  investing — SR expectations and costs are both deliberately modest.
