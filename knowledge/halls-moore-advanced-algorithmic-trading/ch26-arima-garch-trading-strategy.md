# Ch26 — ARIMA+GARCH Trading Strategy on S&P500

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 26 (QSTrader: Part V application).

## Strategy
Combines ARIMA (mean) + GARCH (variance) to predict next-day S&P500 return direction.
1. Each day n, take the previous k=500 days of **differenced log returns** of the index as a
   rolling window.
2. Fit the "best" ARMA and a GARCH model to the window; predict next-day returns.
3. Negative prediction → **short** at previous close; positive → **long**.
4. Same direction as previous day → hold (no change).

Backtest is **vectorised in R** (NOT QSTrader event-driven) → real results would be slightly
lower due to commissions/slippage. Uses `quantmod`, `lattice`, `timeSeries`, `rugarch`.

## Indicator generation (R, rugarch)
- Data: S&P500 (Yahoo, ^GSPC) back to 1950; differenced log returns of closing price.
- Loop over each day d (window k..end):
  - Rolling window of k returns.
  - **ARMA order search**: p∈{0..5}, q∈{0..5} (skip p=q=0), fit `arima(order=c(p,0,q))` — note
    **d=0** ⇒ really ARMA not ARIMA (returns already differenced); wrapped in `tryCatch` to skip
    non-converging fits; pick min **AIC** order.
  - `ugarchspec`: variance model **GARCH(1,1)**, mean model **ARMA(final p,q)**, error
    distribution **sged** (skewed generalised error).
  - `ugarchfit` with `hybrid` solver (tries multiple solvers → better convergence).
  - If GARCH doesn't converge → default prediction "long" (a guess). Else output date +
    predicted direction (+1/−1).
- Write `forecasts.csv`.

## Critical: removing look-ahead bias
The raw CSV has each date's prediction for *tomorrow* — using it directly would introduce
**look-ahead bias** (prediction made with info including that day). Fix: **shift the predicted
value one day ahead** (Python one-liner) → `forecasts_new.csv`.

## Backtest (R)
- `read.zoo` the corrected CSV; intersect dates with S&P500 returns; compute strategy returns
  (long/short per signal); equity curves via **log(cumprod(1+r))** for strategy vs buy-and-hold;
  `merge(all=F)` + `xyplot(superpose=T)`.

## Results & critique
- **65-year period**: ARIMA+GARCH significantly beats buy & hold, but the majority of gains
  came 1970–1980; volatility low until early 80s then higher, returns less impressive.
- Caveats (why "real" performance wouldn't hold):
  - **Anachronism**: ARMA published 1951 (widely used after Box & Jenkins 1970s); **ARCH
    discovered early 80s (Engle)**. Applying these models to pre-invention history is not
    appropriate for a live strategy.
  - Index isn't tradeable directly — would need S&P500 futures or SPDR ETF.
- **2005→today**: equity curve below buy-and-hold for ~3 years, then **excels during the
  2008/09 crash** (strong serial correlation captured by ARIMA+GARCH). Post-2009 recovery
  (stochastic-trend-like) → performance suffers again.
- Easily adapted to other indices/assets — encouraged to research.

## Takeaways / pitfalls
- Rolling ARMA+AIC search + GARCH(1,1) (sged errors, hybrid solver) is a workable daily
  signal generator, but computationally heavy (24 ARMA fits/day).
- **Always shift forecasts by one day** to avoid look-ahead bias; validate with corrected CSV.
- Model-performance caveats: anachronism of the models, index not tradeable, regime dependence
  (works best in strongly serially-correlated, crash periods).
- Non-convergent GARCH → fall back to a default (long) signal, but flag it as a guess.