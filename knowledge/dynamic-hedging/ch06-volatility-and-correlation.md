# Ch06 — Volatility and Correlation

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 6.

## Purpose
Volatility and correlation as the raw material of option pricing: definitions, estimators (including the Parkinson/Garman-Klass high-low estimators), GBM vs. arithmetic Brownian motion, and why volatility (and especially correlation) is unstable.

## Definitions
- **Actual (historical) volatility**: variability of returns actually experienced.
- **Implied volatility**: the volatility parameter derived from option prices via Black-Scholes-Merton (the benchmark even when believed faulty).
- **Correlation**: least-squares association between log returns of two assets; actual vs. implied correlation.
- Warning: 100% correlation does NOT mean 1% move per 1% — it means the ratio of moves equals the ratio of volatilities.

## Brownian motion choices
- **Geometric Brownian motion** (constant percentage move): volatility in dollar terms rises with price; prevents prices going negative; the standard assumption (lognormality).
- **Arithmetic Brownian motion** (constant dollar move): Bachelier (1900); a 1-bp move at low rates = huge percentage volatility — the Eurodeposit example shows the practical difference (at 0.10% rates, 1 bp ≈ 160% vol).
- Moral: treat theoretical dogma lightly; Bachelier's arithmetic model was "right" in some markets.

## Volatility estimators
- Close-to-close standard deviation σ, and the **Parkinson number** (high/low range) and **Garman-Klass** estimator combining close-to-close with high/low:
  P = 1.67·σ' — the book's empirical high/low-to-sampled-vol ratio (the theoretical constant is √(8/π) ≈ 1.60).
- Uses: pricing barrier options and American digitals (triggered by *intraday extremes*, not closes) — if P > 1.67σ' persistently, the probability of hitting a trigger is higher than the model assumes → hedge long gamma more frequently ("letting the gammas run"), or follow trends.

## GARCH and why traders prefer implied vol
- GARCH(1,1): σ²_t = ω + α·ε²_{t−1} + β·σ²_{t−1}, with α + β < 1 (near 1); models volatility clustering; α large → fat tails (positive kurtosis).
- Taleb's view: implied volatility *outperforms* GARCH because it contains information not in past prices (scheduled events, elections); GARCH would predict a volatility *drop* before a big announcement. Traders filter jumps that are non-recurring.

## Correlation instability
- Constant correlation is the most dangerous assumption — "markets have adjusted to the fact that volatility is not constant, not yet to the fact that correlation is volatile."
- Variance-ratio tests (Lo-MacKinlay) probe the randomness/mean-reversion of price paths.

## Key takeaways
- Volatility is not constant and correlation even less so — both are estimation problems.
- For barrier-type products, the distribution of the *extremes* (Parkinson number) matters more than close-to-close volatility.
- Implied volatility is a market opinion with forward-looking content — often better than econometric forecasts.
