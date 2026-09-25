# Kalman Filter Pairs Trading

## name
Kalman-filter dynamic hedge-ratio pairs trading

## description
Use a Kalman filter (state-space model) to recursively estimate a *time-varying*
hedge ratio between two assets, and trade the spread when the filter's
forecast error exceeds its own prediction-uncertainty threshold — no free
spread-threshold parameter needed.

## when to use it
- Pairs trading where the hedge ratio is unstable over time (static OLS β
  would go stale) — e.g. TLT/IEI, EWA/EWC.
- When you want entry/exit thresholds to emerge from the model's own
  uncertainty rather than being hand-tuned (avoids an extra overfitting
  parameter).
- Online/streaming regime: the filter updates after every new observation.

## method / formula / code

**State-space model:**
```
Transition:  θ_t = G_t θ_{t−1} + w_t      # w_t ~ N(0, W_t)
Observation: y_t = F_t θ_t + v_t          # v_t ~ N(0, V_t)
```
θ_t = hidden state = (intercept, slope/hedge-ratio β_t); F_t = [x_t, 1]
(observation matrix); y_t = dependent series price.

**Kalman update (per new bar):**
1. Predicted state & covariance: θ̂_t = G_t θ̂_{t−1}, P_t = G_t P_{t−1} G_tᵀ + W_t.
2. Forecast error: **e_t = y_t − F_t θ̂_t**; prediction variance
   **Q_t = F_t P_t F_tᵀ + V_t**.
3. Update (posterior): θ̂_t += A_t e_t with Kalman gain
   A_t = P_t F_tᵀ Q_t⁻¹; P_t = (I − A_t F_t) P_t.

**Trading rules (Halls-Moore / Ernie Chan):**
```
e_t < −√Q_t  → long the spread:  buy N of y, short ⌊β_t·N⌋ of x
e_t > +√Q_t  → short the spread: short N of y, buy ⌊β_t·N⌋ of x
Exit when e_t reverts past the opposite threshold.
```

**Worked parameters (TLT/IEI strategy):**
- System noise W_t = δ/(1−δ)·I₂ with **δ = 1e-4**; measurement noise
  **V_t = 1e-3**.
- N = 2,000 units on $100k equity; re-hedge quantity
  ⌊β_t·N⌋ recomputed whenever β_t changes.
- Result reported: CAGR 7.66%, Sharpe 0.65, max DD 17.46% (net of costs),
  with an 817-day max drawdown duration.

## known pitfalls
- **Event-driven timing**: in backtests wait until *all* constituents have
  same-day prices before updating the filter (events can arrive out of order).
- Use integer price storage (or divide by a PRICE_MULTIPLIER) to avoid
  floating-point drift over long backtests.
- Long flat/drawdown stretches (817 days here) make the strategy hard to
  hold and capital-intensive — size and risk-manage accordingly.
- δ and V_t are still model choices; they control how fast β adapts
  (grid-search for robustness).

## source book
Halls-Moore, *Advanced Algorithmic Trading*, ch13 (state-space models &
Kalman filter) and ch28 (Kalman pairs trading strategy on TLT/IEI).
