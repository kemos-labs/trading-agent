# Bond Price Sensitivities (Duration, Convexity, PV01)

## name
Fixed-income price risk: Macaulay/modified duration, convexity, dollar
duration, PV01/PVBP, and immunization of bond portfolios — the Taylor-series
sensitivities of bond prices to yield and to market interest rates.

## description
Duration, convexity, and PV01 quantify how a bond's (or bond portfolio's)
price responds to yield/rate changes. Duration is the first-order
(linear) sensitivity, convexity the second-order correction for large moves,
and PV01 the sensitivity to a 1bp change in *market interest rates* (the
risk-factor curve). Use these to estimate price changes, immunize portfolios
against parallel yield shifts, and express interest-rate risk in additive
value terms for portfolio-level risk management.

## when to use it
- Approximating bond/portfolio price change for a given yield move.
- **Immunization**: structuring assets/liabilities so duration (and
  convexity) match, making portfolio value locally insensitive to rate moves.
- Building risk-factor mappings for interest-rate portfolios (sensitivity to
  the zero-coupon curve, not just the bond's own yield).
- Comparing/aggregating rate risk across many instruments in value terms
  (value duration / PV01 are additive; per-unit duration is not).
- Cash-flow mapping between curve vertices while preserving PV, duration,
  and PV01.

## the method

### 1. Duration (first-order sensitivity)
```python
import numpy as np

def macaulay_duration(cashflows, times, ytm):
    """Weighted average time to cash flows (years)."""
    pv = np.array(cashflows) * np.exp(-np.array(times) * ytm)
    price = np.sum(pv)
    return np.sum(times * pv) / price

def modified_duration(mac_dur, ytm):
    """Sensitivity of price to yield: dP/P ~= -D_mod * dy."""
    return mac_dur / (1 + ytm)  # annual compounding; /(1+ytm/freq) per period
```
- Macaulay duration = weighted-average time to receive cash flows.
- Modified duration = first derivative of price w.r.t. yield, as % of price.

### 2. Convexity (second-order correction)
```python
def convexity(cashflows, times, price, ytm):
    pv = np.array(cashflows) * np.exp(-np.array(times) * ytm)
    return np.sum(times**2 * pv) / price   # annualized convexity
```
- Price approximation via Taylor expansion:
  `dP/P ~= -D_mod * dy + 0.5 * C * dy^2`
- Convexity corrects duration for large yield moves: the price-yield curve is
  convex, so duration alone understates the price rise from a fall in yields
  and overstates the fall from a rise.

### 3. Dollar duration and PV01
```python
# PV01 = price change for a 1bp (0.0001) move in the yield/rate
# = modified_duration * price * 1e-4 (price per unit face)
pv01 = modified_duration * price * 1e-4
```
- **PV01/PVBP** (present value of a basis point): sensitivity of a cash flow
  or portfolio to a 1bp change in *market interest rates* (the risk-factor
  zero curve) — conceptually distinct from dollar duration (sensitivity to
  the bond's own yield). PV01 vectors are the standard sensitivities for
  market risk: all bonds in a currency share one zero-curve factor set.
- Approximate PV01 for a single cash flow of value 1 at time T (continuous):
  `PV01 ~= T` (per unit of notional, in discounted absolute terms).

### 4. Immunization
- Match portfolio duration (assets = liabilities), then match convexity;
  rebalance as yields/curve change. The portfolio is then locally hedged
  against parallel yield shifts.

### 5. Portfolio level
- Value duration = sum of dollar durations; value convexity = sum of
  dollar-weighted convexities; PV01 vector = sum of PV01 vectors. Express all
  sensitivities in value terms before aggregating across instruments.

## known pitfalls
- **Duration assumes a parallel, infinitesimal shift**: it is a first-order
  local approximation; large or non-parallel (twist/butterfly) moves need
  convexity + a full curve sensitivity (PV01 vector per vertex).
- **PV01 vs dollar duration are not the same**: PV01 is w.r.t. market rates
  (risk factors), dollar duration w.r.t. the bond's own yield — they are
  close but conceptually different (Alexander's warning).
- **Non-additivity**: position (per-unit) durations don't sum; use value
  duration/PV01 for portfolios.
- **Yield conventions**: annual vs semi-annual compounding and day counts
  change duration/convexity values — state the convention.
- **Convexity sign**: options-like instruments can have negative convexity
  (callable bonds, MBS) where the price-yield curve bends the wrong way.
- Immunization only protects against parallel shifts and decays with time —
  periodic rebalancing required.

## source
Alexander, *Market Risk Analysis*, Vol. III (Pricing, Hedging and Trading
Financial Instruments), ch III.1 (duration/convexity/PV01) and ch III.5
(PV01-invariant cash-flow mapping). Knowledge notes:
`knowledge/market-risk-analysis-vol3/ch-iii1-bonds-and-swaps.md` and
`ch-iii5-portfolio-mapping.md`. Complementary: `skills/risk-metrics`,
`skills/portfolio-optimization`.
