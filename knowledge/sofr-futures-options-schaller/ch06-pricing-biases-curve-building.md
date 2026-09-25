# Chapter 6: Pricing Biases and SOFR Curve Building

## Eurodollar Futures Biases (Background)
Two distinct biases affect ED futures relative to forward rates:

1. **Financing bias** (Cox, Ingersoll & Ross 1981): When the futures price is negatively correlated with the margin interest rate (as with rate futures), daily margining systematically disadvantages the long position. The short profits more on margin when rates are high (position is profitable) and pays less when rates are low (position is losing). The futures rate therefore systematically **overstates** the forward rate.

2. **Convexity bias** (Hoskins & Burghardt): The futures payout at time S is reinvested at the term rate RS from S to T, making the all-in return a **concave (quadratic) function** of RS. By Jensen's inequality, the expected value of this concave function is less than the function at the expected value — meaning the market must set the futures rate higher than the forward rate to equate expected returns. This bias is an increasing function of time to expiry and rate volatility.

## Biases in SOFR Futures

### 3M SOFR Futures: No Convexity Bias
The 3M SOFR contract's time-T payout, combined with overnight compounding, yields an **exact forward rate** — no nonlinear transformation. Unlike ED futures, where the payout is a linear function of the 3M rate but compared at the wrong point in time, the SOFR payout and the overnight compounding operate on the same daily SOFR values. **No convexity adjustment is needed** for 3M SOFR futures.

### 1M SOFR Futures: Slight Bias from Simple Averaging
The 1M contract settles to an **arithmetic average** of daily SOFR, while the "correct" forward rate uses compounding (geometric average). Since compounding ≥ arithmetic average (for positive rates), the 1M futures rate slightly understates the true forward rate. The difference is:
- <0.1bp at current low rates (~100bp)
- ~1bp at 500bp SOFR
- Practically negligible when within the bid-ask spread, but worth monitoring as rates rise.

### Financing Bias for Both
SOFR futures have a strong negative correlation between price and the overnight margin rate → a financing bias exists. Its magnitude depends on:
- Correlation strength (higher for shorter-dated contracts)
- Time to expiry (longer for back-months)
- Whether margin interest flows through to P&L (many prop desks don't track it)

In practice, if both futures and FRAs/swaps are subject to similar margining, the financing biases may cancel in relative value trades.

## Building a SOFR Curve

### Bootstrapping vs Fitting
With ~18 futures contracts but only ~10 FOMC meeting dates per year defining the step function, the curve is **overdetermined** — fitting (minimize sum of squared pricing errors) is preferred over bootstrapping (exact repricing of selected contracts).

**Example (Feb 25, 2022):** Bootstrapping with 1M contracts produces average absolute pricing errors of 0.83¢ for 1M contracts and 1.36¢ for 3M contracts. Fitting produces 1.10¢ and 0.50¢ respectively — fitting spreads errors more evenly and avoids large outliers.

### Discontinuities
Unlike LIBOR curves (smooth 3M segments), SOFR curves naturally feature **step discontinuities at FOMC meeting dates**. The basic building block is the overnight rate, which changes only at policy meetings (in a jump-process framework).

### Regularity Condition
Raw fitted curves can be noisy (implausible rate reversals). A penalty function penalizing large butterfly spreads (sum of squared differences between adjacent steps, scaled by λ) smooths the curve at the cost of slightly worse fit. This is analogous to the λ parameter in the CME Term SOFR calculation.

### Practical Considerations
- Choose the step function's anchor points: FOMC dates for the short end, cubic splines for the long end.
- Combine jumps (FOMC) with a smooth curve (splines) to produce a single yield curve from short to long.
- The financing bias and simple-average bias for 1M contracts should be evaluated in context — at current rates they're within noise; at higher rates they may warrant explicit adjustment.

**Key takeaway:** 3M SOFR futures are "cleaner" building blocks than ED futures — no convexity bias, no nonlinearities. The curve is a piecewise step function anchored at FOMC dates.
