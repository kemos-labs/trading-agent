# Chapter 21 — Market-Based Valuation

## Core idea
The DX capstone: value **non-liquidly traded options** by calibrating a
model to **liquid market quotes** (DAX 30 European options) and using the
calibrated model to price the rest — the standard market-based approach.

## The data
- DAX index level + quoted European calls/puts (from Thomson Reuters Eikon):
  `CF_DATE`, `EXPIR_DATE`, `PUTCALLIND`, `STRIKE_PRC`, `CF_CLOSE`,
  `IMP_VOLT`.
- Split into calls and puts; visualize market prices and **implied
  volatilities** per strike (the vol smile).

## Model calibration
1. **Select relevant quotes**: only options near the money
   (`abs(strike - S0) < limit`, e.g. 500) — far ITM/OTM quotes are noisy.
2. **Choose the model**: e.g., a jump-diffusion or CIR-type process
   parameterized by `(vola, lambda, mu, delta)`.
3. **Objective**: minimize the mean squared error between model prices and
   market quotes:
   ```
   MSE(params) = mean((model_price(strike; params) - market_price(strike))^2)
   ```
4. **Two-stage optimization** (avoids local minima):
   - Coarse **global grid search** over parameter ranges (e.g.,
     `vola=0.10..0.20`, `lambda=0.1..0.7`, ...) — record the best grid point
     (MSE 17.95).
   - **Local refinement** from the grid best with
     `scipy.optimize.fmin` (`xtol/ftol=1e-5`) — MSE drops to ~7.37.
5. **Validate**: compare model prices to market quotes at all strikes;
   pricing errors in percent.

## Portfolio valuation with the calibrated model
- Use the calibrated parameters to simulate the DAX index and value the
  non-traded options in the book (ch19/20 classes).
- Estimate **risk measures** at position and portfolio level (VaR) from the
  simulated joint distribution.

## The key insight
Calibration absorbs the market's risk-neutral dynamics: the model is not a
truth claim about the world but a consistent interpolation/extrapolation
device for market prices — exactly the Fundamental Theorem's martingale
measure made practical.

## Pitfalls
- Global vs local optimization: one-stage local optimization sticks in
  local minima — always coarse-grid first.
- OTM options carry noisy implied vols; selecting near-the-money quotes
  stabilizes calibration.
- Over-parameterized models fit but don't generalize; report out-of-sample
  pricing errors.
- Calibrated parameters are regime-specific — recalibrate as the market
  moves.

## Bottom line
The full market-based workflow: quotes → near-money selection → grid+local
calibration → pricing and risk on the book. This is the practical payoff of
ch17's theory and ch18–20's library. Cross-ref:
`knowledge/stochastic-calculus-finance/ch28` (term structure), Natenberg
notes on the vol smile.
