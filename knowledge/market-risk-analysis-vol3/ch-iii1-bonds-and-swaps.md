# III.1 Bonds and Swaps

Source: Carol Alexander, *Market Risk Analysis*, Vol. III (Pricing, Hedging
and Trading Financial Instruments), ch III.1.

## Core idea

Primitive securities (bonds) have their own intrinsic price; derivative
securities (FRAs, swaps, options) have payoffs that depend on other prices.
This chapter builds the interest-rate toolkit for pricing and risk-managing
bonds and swaps: compounding conventions, spot/forward curves, duration and
convexity, PV01, curve bootstrapping, and convertible bonds.

## Interest rate mechanics

- **Discrete vs continuous compounding**: debt markets quote discrete
  (annual/semi-annual) rates with day-count conventions; banks convert to
  continuously compounded rates because they simplify price/risk analysis.
  Notation: lowercase r/f = continuously compounded spot/forward; uppercase
  R/F = discrete.
- Continuous compounding factor: `V = N * exp(r_T * T)`; discount factor
  `N = V * exp(-r_T * T)`.
- **Spot vs forward**: spot applies from now to T; forward starts at future t
  ending at T (term = time until it applies, tenor = period it covers).
  No-arbitrage linking: `exp(2r_2) = exp(r_1) * exp(f_1,1)` — investing at the
  2-year spot rate must equal rolling 1-year spot then 1-year forward.

## Bonds

Fixed coupon bonds priced as the discounted stream of coupons plus principal.
Key relationship: price vs **yield** (the internal rate of return). Floating
rate notes reprice to par at each reset.

**Risk measures on a single bond / portfolio** (Taylor expansion of price in
yield):
- **Duration** — first-order price sensitivity to yield; Macaulay duration =
  weighted average time to cash flows; modified duration = duration/(1+yield).
- **Convexity** — second-order sensitivity; corrects duration for large yield
  moves (price-yield curve is convex, not linear).
- Approximate price change:
  `dP/P ~= -D * dy + 0.5 * C * dy^2`.
- **PV01 / PVBP** (present value of a basis point) — sensitivity of a cash
  flow/portfolio to a 1bp change in *market interest rates* (the risk factor
  curve), conceptually distinct from dollar duration (sensitivity to the
  bond's own yield). PV01 is the fundamental sensitivity for market risk
  because all bonds in a currency share the same risk-factor curve.
- **Immunization**: match duration (and convexity) of assets and liabilities
  so portfolio value is locally insensitive to parallel yield shifts.

## FRAs and swaps

- **FRA**: OTC agreement to buy/sell a forward interest rate; a swap is a
  sequence of FRAs.
- **Vanilla interest rate swap**: fixed-for-floating; the swap rate is set so
  the fixed leg's PV equals the floating leg's PV (par swap). The market risk
  of a swap derives mainly from the **fixed leg**, which is analyzed as a
  bond with coupon = swap rate.
- Cross-currency basis swaps, other swap variants defined but not detailed.

## Curve construction

**Bootstrapping**: derive zero-coupon rates from money-market rates and
coupon-bond prices of successive maturities — the rate at each maturity is
solved so the model price equals the market price. Then fit smooth curves via
**splines** or **parametric models** (e.g., Svensson/Nelson-Siegel family) to
interpolate between vertices; the case study compares fitting methods on the
UK LIBOR curve. A well-fit zero curve is the basis for mapping (ch III.5).

## Convertible bonds

Hybrid securities: a bond with an embedded option to convert into the issuer's
stock — downside protection of the bond, upside participation in equity.
Valuation must account for stock price, credit, interest rates, and the
conversion option; pricing models surveyed (typically reduce to a barrier- or
American-style option component).

## Key takeaways

- Use continuously compounded rates for analysis; discrete for market quotes.
- Duration + convexity = first/second-order Taylor sensitivity to yield;
  PV01 = sensitivity to the market rate curve and is additive across the
  portfolio.
- Swap risk ≈ fixed-leg bond risk; the swap rate makes fixed = floating PV.
- Zero curves are bootstrapped from liquid instruments then smoothed
  (splines/parametric) — the backbone of all rate risk work.

Related skills: `skills/risk-metrics`, `knowledge/market-risk-analysis-vol1/
ch-i1` (calculus: Taylor series, duration as a derivative).
