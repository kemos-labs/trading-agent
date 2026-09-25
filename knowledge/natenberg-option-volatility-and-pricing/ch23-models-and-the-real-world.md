# Chapter 23 — Models and the Real World

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## The six assumptions of traditional models (BS / CRR)

1. Frictionless markets (free trading, unlimited borrow/lend at one
   rate, no costs, no taxes).
2. Constant interest rates.
3. Constant volatility.
4. Continuous trading (pure diffusion, no price gaps).
5. Volatility independent of the underlying price.
6. Percent changes normally distributed → lognormal terminal prices.

## Where each assumption breaks

- **Frictionless**: locked futures (circumvent via cash market, spread
  legs, or synthetic futures in options); short-sale restrictions →
  puts inflate and conversions look mispriced (carry long stock to
  hedge); margin/variation calls force liquidation before expiry (models
  assume you can always hold); borrow ≠ lend rates; transaction costs
  (worst for frequently-rebalanced high-gamma strategies). Taxes usually
  secondary.
- **Constant rates**: variable-rate financing via the clearing firm;
  only deep-ITM long-dated options care (highest rho).
- **Constant volatility — path dependence**: the same 28% close-to-close
  realized vol ordered *falling* vs. *rising* yields very different
  dynamically-hedged values for a 100 straddle — BS 10.46, falling 5.94,
  rising 12.82. Reason: ATM gamma peaks near expiry, so vol late in life
  pays most (and theta punishes most if nothing moves). For OTM options
  the effect flips (their gamma peaks early). Hedged value is *path
  dependent*; BS is the average across all paths. Stochastic-vol models
  exist but are rarely used; bonds are the canonical counterexample
  (pull-to-par ⇒ vol changes deterministically) needing special models.
- **Continuous trading — gaps**: overnight/weekend/news gaps are jumps.
  A gap while short an ATM straddle with 1 day left converts it into
  naked short deep-ITM calls (Δ→100) with no chance to re-hedge —
  damage ∝ gamma. Gap impact is worst for **ATM, near-expiry,
  low-volatility** options: the riskiest contracts to sell.
- **Vol vs. price**: equity indexes get more volatile falling; many
  commodities more volatile rising. The CEV model parameterizes this but
  is complex and rarely used.
- **Lognormality — fat tails**: real daily distributions are
  **leptokurtic** (positive kurtosis): more tiny moves, more huge moves,
  fewer intermediate ones than normal. S&P 2003–12: kurtosis 10.4; the
  +11.58% day is an 8.84σ event (1 in ~2 quintillion under normal);
  −9.03% is 6.75σ (1 in 350 billion). Skewness sign varies (euro
  positive; S&P, crude, Bund negative).

## Practical consequences

- **Models understate real-world option values** (gaps + fat tails +
  hedging demand): average implied vol > average realized vol. The
  "overpriced option" observation is partly the market's correct premium
  for jump risk.
- **Never sell large amounts of ATM options near expiry** — tail risk
  dominates the theta reward.
- **Expiration straddles**: the flip side — buy cheap ATM straddles into
  expiry. Lose most of the time (small theta bleed), win rarely but
  hugely when a gap or vol spike occurs: the roulette logic (bet 50¢ on
  a 95¢ value, 37 losses, one big win). Size it to survive the losing
  streak; skip strict delta-neutral rebalancing (model deltas are
  unreliable near expiry).
- Portfolio insurance died on 1987's gaps: continuous-rehedging
  replication fails exactly when gaps forbid adjustment.

## Key takeaways

1. Every model is a diffusion, constant-σ approximation; the errors are
   concentrated in near-expiry ATM gamma (gaps) and in fat tails.
2. Gap/gamma interplay ⇒ the cheapest option in a model is often
   undervalued in reality; sellers of near-expiry ATM vol are paid for
   taking jump risk they can't hedge.
3. Use model outputs with margin for error; experience beats added model
   complexity (jump-diffusion/CEV need inputs traders can't estimate).
