# Glossary (starter)

Working definitions of core terms used across `/knowledge` and
`/skills`. One line each, in the vocabulary of the books that introduced
them. Add entries as new material lands; keep definitions terse and
cross-referenced to skills where useful.

## A
- **Alpha**: risk-adjusted excess return over a benchmark; in factor
  terms, the return unexplained by systematic risk factors.
- **ADF test (Augmented Dickey-Fuller)**: unit-root test; failure to
  reject → series is non-stationary (I(1)) → cointegration methods apply.
- **American option**: option exercisable any time before expiry; early
  exercise can be optimal (dividends, deep-ITM puts).
- **Annualized Sharpe**: `√N_T × period Sharpe`, where N_T = trading
  periods per year (√252 daily, √1638 NYSE-hourly).

## B
- **Basis**: spot price minus futures price; basis risk = uncertainty in
  the hedge ratio when spot and futures don't move together.
- **Black-Scholes-Merton (BSM)**: closed-form European option pricing
  under GBM; `d1 = [ln(S/X) + (b + σ²/2)t]/(σ√t)`, `d2 = d1 − σ√t`.
- **Binomial tree (CRR)**: discrete lattice (u = e^{σ√Δt}, d = 1/u)
  with risk-neutral backward induction; the discrete proof of
  price = E_Q[discounted payoff].

## C
- **CIR process**: square-root mean-reverting diffusion, `dr = κ(θ−r)dt
  + σ√r dW`; used for interest rates; positive if Feller condition holds.
- **Cointegration**: two I(1) series whose linear combination is I(0) —
  a stationary spread; the basis of pairs trading.
- **Convexity**: second derivative of bond price w.r.t. yield; corrects
  the duration approximation: `dP/P ≈ −D·dy + ½C·dy²`.
- **CPCV (Combinatorial Purged CV)**: purged cross-validation producing
  multiple out-of-sample backtest paths for path-dependent labels.
- **cVaR / Expected Shortfall (ES / ETL)**: average loss beyond the VaR
  quantile; coherent risk measure, unlike VaR.

## D
- **Delta**: ∂V/∂S of an option; the hedge ratio of underlying shares
  per option.
- **Downside deviation**: `√(E[max(0, τ−X)²])` — second lower partial
  moment; the denominator of the Sortino ratio.
- **Drawdown**: `(1+cumret)/(1+highwatermark) − 1`; max drawdown = worst
  peak-to-trough loss; drawdown duration = longest run of non-zero DD.
- **Duration (modified)**: Macaulay duration / (1 + yield); first-order
  bond price sensitivity to yield. **PV01** = −∂P/∂y × 0.0001.
- **Dupire local volatility**: σ(S,t) consistent with the whole implied
  vol surface; the dual of the IV surface.

## E
- **ECM (Error Correction Model)**: models Δ of a cointegrated system
  with a lagged disequilibrium term (sign conditions θ₁<0, θ₂>0 for a
  valid pair) — combines long-run equilibrium with short-run dynamics.
- **Engle-Granger**: two-step cointegration test (regress Y on X, ADF on
  residuals); limited to one cointegrating vector.
- **ETL**: expected tail loss — see cVaR.
- **EWMA / RiskMetrics**: exponentially weighted variance with λ = 0.94
  daily; conditional volatility, no long-run mean.

## F
- **Feller condition**: `2κθ > σ²` — sufficient for a CIR process to
  stay positive.
- **Filtered historical simulation**: GARCH model + bootstrap residuals;
  conditional historical VaR (Barone-Adesi).

## G
- **Gamma**: ∂²V/∂S² of an option; curvature / delta instability; hedged
  with other options (the underlying has no gamma).
- **GARCH(1,1)**: `σ²_t = ω + α·r²_{t−1} + β·σ²_{t−1}`; stationary when
  α+β<1, long-run variance ω/(1−α−β).
- **Gaussian copula**: dependence structure with zero tail dependence
  for ρ<1 — understates joint extremes.
- **Greeks**: option price sensitivities (delta, gamma, vega, theta,
  rho, volga); value Greeks add across a book, position Greeks do not.

## H
- **Hedge ratio (min-variance)**: `h* = ρ·σ_S/σ_F` for futures hedging.
- **HMM**: hidden Markov model; latent regime states driving observable
  returns; used for regime detection (e.g. GaussianHMM on returns).
- **Historical simulation**: empirical-quantile VaR from past P&L
  scenarios; no distributional assumption.

## I
- **IC (Information Coefficient)**: period-by-period rank correlation
  between a factor and forward returns; factor-signal screen.
- **Implied volatility**: the σ that makes model price = market price;
  the only unobservable BSM input.
- **I(1) / I(0)**: integrated of order one (unit root, non-stationary
  level) / zero (stationary).

## J
- **Johansen test**: multivariate cointegration test; up to n−1
  cointegrating vectors for n series.

## K
- **Kalman filter**: recursive state estimation (predict/update); used
  for dynamic hedge ratios in pairs trading.
- **Kelly criterion**: fraction of capital `f* = p − q/b` (discrete) or
  `m/σ²` (continuous) maximizing long-run growth; over-betting past ~2f*
  gives negative growth.
- **Kupiec test**: unconditional coverage LR test for VaR backtesting,
  ~χ²(1); **Christoffersen** adds an independence test; combined ~χ²(2).

## L
- **Look-ahead bias**: using future information at signal time (e.g.
  missing `position.shift(1)`); the classic backtest inflator.
- **LPM (lower partial moment)**: `E[max(0, τ−X)ⁿ]`; family behind
  downside deviation, Sortino (n=2), omega (n=1).
- **LSM (Longstaff-Schwartz)**: American option pricing by regressing
  continuation value on in-the-money paths.

## M
- **Macaulay duration**: weighted average time to cash flows (years).
- **MAR ratio**: CAGR / max drawdown — leverage-relative return measure.
- **Market impact / Kyle's lambda**: price move per unit of traded
  volume; liquidity-cost parameter.
- **Markowitz frontier**: efficient portfolios maximizing return for a
  given variance (`w'Σw`); max-Sharpe, min-variance solutions.
- **Mean reversion**: tendency of a series/spread to revert to a mean;
  tested via variance ratio, Hurst exponent, half-life.

## O
- **O-GARCH**: PCA + univariate GARCH on principal components; gives
  always-PSD covariance matrices.
- **Omega ratio**: gains/losses ratio over a threshold (n=1 LPM family).
- **Order types**: market, limit, stop, maker/taker (maker rebates,
  taker fees) — the microstructure cost layer of execution.

## P
- **Put-call parity**: `C − P = S·e^((b−r)t) − X·e^(−rt)`; no-arbitrage
  link between calls and puts of the same strike/maturity.
- **PCA**: eigen-decomposition of the covariance matrix; factor
  reduction (e.g. 60 rates → 3 factors: shift, tilt, curvature).
- **PSR/DSR**: Probabilistic / Deflated Sharpe Ratio — significance of a
  Sharpe given number of trials.
- **PV01-invariant mapping**: splitting a cash flow between two
  curve-vertices `x = (T−T1)/(T2−T1)` preserving PV01 exposure.

## Q
- **Quantile regression**: models a conditional quantile, minimizing
  asymmetric loss `ρ_τ(u) = u(τ − I(u<0))`; robust to tails.
- **QSTrader**: open-source event-driven backtesting/OMS (events queue,
  price handler, strategy, portfolio, sizer, risk manager, execution).

## R
- **RAROC**: expected profit / economic capital; return on risk capital
  for capital allocation.
- **Risk-neutral measure**: measure under which all assets grow at the
  risk-free rate; option value = discounted expected payoff under Q.
- **Roll's estimator**: serial-covariance-based effective spread
  estimate.

## S
- **Sharpe ratio**: (strategy return − risk-free) / volatility; for
  dollar-neutral portfolios don't subtract risk-free.
- **Sortino**: excess return / downside deviation — penalizes only
  downside.
- **Square-root-of-time rule**: h-day vol = √h × 1-day vol — valid only
  under i.i.d. returns; real scale exponents differ (≈0.5 equities/FX,
  0.55–0.6 rates, <0.5 vol indices).
- **Straddle/strangle/butterfly/condor**: volatility strategies
  isolating vega from direction.
- **Survivorship bias**: databases missing delisted stocks inflate
  backtest returns.

## T
- **Taylor expansion**: `dP/P ≈ −D·dy + ½C·dy²` — the backbone of
  duration/convexity and delta-gamma approximations.
- **Theta**: time decay of option value; ATM options lose value fastest.
- **Tracking error**: volatility of active return; only a valid active
  risk measure for benchmark trackers.

## V
- **VaR**: worst loss at confidence α — the −α quantile of the P&L
  distribution (`Φ⁻¹(1−α)σ − μ` under normality); not sub-additive
  (unlike cVaR).
- **Variance ratio test**: compares multi-period variance to one-period;
  distinguishes fundamental vs transitory (mean-reverting) volatility.
- **Vega**: ∂V/∂σ; hedged with options (underlying has zero vega).
- **Volatility targeting**: scaling positions so each unit of forecast
  risk carries target vol (Half-Kelly / scalar pipeline).

## P
- **Paper trading**: live-feed simulation without real orders; journal is append-only, cost/lag disciplined (`paper_only; execution next bar`), state in `data/paper/state.json`. See `skills/live-paper`.
- **PTC (proportional transaction cost)**: `ptc × |Δpos|` per bar (e.g. 0.001 = 10 bps); plus `ffc` flat cost. Charged at decision, realized next bar.

## W
- **Walk-forward validation**: sequential train/test splits honoring
  time order; fit-on-train-only preprocessing; report OOS numbers only.
- **Winsorize/z-score/neutralize**: factor preprocessing pipeline
  (cap outliers, standardize, remove benchmark exposure) before IC
  evaluation.
