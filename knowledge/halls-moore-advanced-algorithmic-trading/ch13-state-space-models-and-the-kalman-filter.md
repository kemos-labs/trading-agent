# Ch13 — State Space Models and the Kalman Filter

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 13.

## Concept
**State-space models** generalize static time-series models by letting the *parameters vary over
time*. We have *states* θ_t that evolve in time (e.g. the hedge ratio between two cointegrated
securities) but *observations* y_t of those states are noisy (e.g. market-microstructure noise),
so we can't observe the states directly. Goal: infer the states from noisy observations as new
data arrives. The **Kalman Filter** is the classic recursive algorithm for this — ubiquitous in
navigation/guidance/etc., and in trading used mainly to update **dynamic hedge ratios** in
stat-arb pairs trades.

## Three types of inference
- **Filtering** — estimate the *current* state from past & current observations (what's the
  state *right now*).
- **Smoothing** — estimate *past* states given current knowledge (retrospective).
- **Prediction** — estimate future states/observations from past & current data.

## Linear state-space model
- **Transition (process) equation**: θ_t = G_t θ_{t−1} + w_t (state is linear fn of previous
  state + system noise). G_t = time-varying state-transition matrix; w_t multivariate normal.
- **Observation equation**: y_t = F_t θ_t + v_t (observations are a linear combination of current
  state + measurement noise). F_t = observation matrix.
- Initial state θ_1 ~ N(m_1, C_1); system noise w_t ~ N(0, W_t); measurement noise v_t ~
  N(0, V_t).
- Complete spec: G_t, F_t, m_1, C_1, W_t (system), V_t (measurement).

## Kalman Filter as Bayesian conjugacy
Apply Bayes' rule to update P(θ_t | Y_t) given data up to time t:
- **Prior**: θ_t | Y_{t−1} ~ N(a_t, R_t).
- **Likelihood**: y_t | θ_t ~ N(F_tᵀ θ_t, V_t).
- **Posterior**: θ_t | Y_t ~ N(m_t, C_t).
- Because prior & likelihood are both Normal ⇒ **posterior Normal** (conjugate) — that's the
  recursive engine.
- Intuition: **posterior mean = weighting of prior mean and forecast error**:
  m_t = G_t m_{t−1} + A_t e_t, where e_t = y_t − f_t is the forecast error, G_t & A_t are
  weighting (Kalman-gain-ish) matrices. **Forecast**: prediction of tomorrow = expected value of
  the observation likelihood F_tᵀθ_t given today's data; full k-step forecasts characterised by
  both mean and variance.

## Application: dynamic hedge ratio via online linear regression
- Instead of a **rolling linear regression with a lookback window** (which adds a *lookback
  window* free parameter that needs cross-validation), use a **state space model treating the
  "true" hedge ratio as a hidden variable** estimated from noisy observations.
- Model: observations (one ETF series) ← states = (slope, intercept) of linear regression on the
  other ETF.
  - States β^T = (slope, intercept); assume next = current + system noise (**random walk**):
    transition matrix G_t = I (2D identity).
  - Observation: y_t = F_t θ_t + v_t with F_t = (x_t, 1)ᵀ (the other price + constant).
  - This is **linear regression recast as a state-space model**, solved by Kalman Filter to get
    time-varying slope/intercept as new prices arrive.

### Implementation (PyKalman, applied to TLT vs IEI bond ETFs)
- `delta = 1e-5`; `trans_cov = delta/(1−delta)·I` (controls Q / system noise) ;
  observation matrix obs_mat (TLE price + ones); KalmanFilter(n_dim_obs=1, n_dim_state=2,
  initial_state_mean=0, covariance=unit, transition=identity, observation_covariance=1,
  transition_covariance=trans_cov). `kf.filter(...)` → state_means/slope & intercept time series.
- Result: **slope drops ~1.38 (2011) → ~0.9 (2016)** despite the same pair of ETFs — dynamic
  hedge ratio is clearly time-varying → a fixed ratio is inadequate.
- **delta controls smoothness vs responsiveness**: higher delta → more responsive but noisier;
  lower → smoother but laggier. Should be optimised via cross-validation over ETF baskets.

## Takeaways / pitfalls
- State-space/Kalman avoids the *lookback-window* free parameter of rolling regression.
- The filter is conjugate-Normal so update math is closed form; leave heavy lifting for
  libraries (PyKalman).
- In production, tune the system-noise scale (delta) via cross-validation per basket.
- Kalman output naturally supports noise-aware signal handling (e.g. suppress trades during
  high-noise periods / favour low-noise pairs — per Jonathan Kinlay's suggestion).
- Later backtested with QSTrader (Kalman pairs-trading chapter).