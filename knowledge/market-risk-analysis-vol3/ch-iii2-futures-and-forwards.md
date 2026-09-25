# III.2 Futures and Forwards

Source: Carol Alexander, *Market Risk Analysis*, Vol. III (Pricing, Hedging
and Trading Financial Instruments), ch III.2.

## Core idea

Futures are exchange-traded, margined, standardized agreements to buy an
underlying at a fixed expiry at a price agreed now; forwards are the same
structure OTC without margining. Forwards are virtually costless to enter so
they must be a **fair bet** — their prices follow a martingale. Futures/forwards
are the cheap way to trade or hedge the *level* of an underlying (options are
the expensive way to trade *volatility*).

## Market characteristics

- Notional bond futures (2/5/10-year, long bond) dominate by notional; money
  market (3-month Eurodollar, EURIBOR), commodity, stock-index, FX, and
  volatility-index futures follow.
- **Basis** = spot price − futures/forward price; zero at expiry (both are
  prices for immediate delivery), generally non-zero before. Basis is driven
  by dividends/coupons, carry costs (storage, insurance), interest-rate
  differentials, and convenience yields.
- Hedgers transfer risk to speculators; exchanges impose daily price limits.
- Futures typically more liquid than spot — often the price-discovery
  instrument; index futures tradeable where the spot basket is not.

## Pricing: no-arbitrage

Fair forward/futures price is set so there is no arbitrage between (a) holding
the spot and (b) holding the forward + investing the present value of the
forward price:

```
F = S * exp((r - y + c) * T)     (continuous, generic form)
```

- y = dividend yield / coupon (benefits of holding spot),
- c = carry costs (storage, insurance),
- r = risk-free rate.
- For FX: `F = S * exp((r_dom - r_for) * T)` — the interest-rate differential
  replaces the dividend yield (covered interest parity).
- At expiry, F = S by definition; before expiry the basis reflects the
  carry/dividend structure.

**Basis risk**: uncertainty in the spot-futures difference; greatest when the
spot cannot be traded/shorted (commodities, temperature) or with maturity
mismatch — you cannot perfectly hedge an exposure you cannot transact.

## Hedging with futures/forwards

- **Minimum variance hedge ratio**: the number of futures contracts that
  minimizes the variance of the hedged portfolio:
  `h* = rho * (sigma_S / sigma_F)` (regression of spot returns on futures
  returns). With an exact hedge held to expiry, h* = 1; with maturity
  mismatch or a proxy hedge, h* need not equal 1.
- **Insurance approach** (traditional, h=1 for exact hedges) vs
  **mean-variance approach** (speculative component; choose h* to trade off
  risk reduction against expected return).
- **Residual position risk**: integer contract constraints leave residual
  exposure; more contracts than optimal may be needed when the optimal ratio
  is not an integer.
- Practical hedges: FX forwards for international portfolios, index futures
  for stock portfolios, notional bond futures for bond portfolios. Not all
  uncertainty is hedgeable — decompose hedged-portfolio risk into hedgeable
  and residual components (energy futures case study).
- Short-term hedges: the econometric literature on optimal short-horizon
  hedge ratios is largely misconceived/flawed — simple rolling ratios are
  robust.

## Key takeaways

- Forwards are fair bets (martingales); futures approximate this with small
  margin costs.
- Basis = carry + dividends + convenience; it converges to zero at expiry
  and is the source of basis risk.
- Fair value: F = S·exp((r − y + c)T); FX substitutes the rate differential
  for the dividend yield.
- Minimum-variance hedge ratio h* = ρ·σ_S/σ_F; 1 only for exact, held-to-
  expiry hedges.

Related skills: `skills/automated-market-making`, `skills/market-micro-
structure-execution`, `knowledge/market-risk-analysis-vol2/ch-ii1` (betas
as sensitivities).
