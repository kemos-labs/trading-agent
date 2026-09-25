# HMM Market-Regime Detection

## name
Hidden Markov Model (HMM) market-regime detection

## description
Fit a Gaussian HMM to asset returns to discover latent market regimes
(e.g. low-vol/trending vs high-vol/crash), predict the current regime online,
and use it as a risk-management overlay that gates or vetoes trades.

## when to use it
- Detecting volatility/trading regimes in a return series when regimes are
  not directly observable (regulatory change, excess-volatility periods).
- As a risk filter: suppress new trades in high-volatility regimes while
  still allowing exit of open positions (Halls-Moore's QSTrader
  `RegimeHMMRiskManager` pattern).
- Caution: it is *unsupervised* — regime labels are arbitrary; validate
  against market intuition.

## method / formula / code

**Model:** hidden states s_t ∈ {1..K} following a Markov chain with
transition matrix A (K×K); each state emits observations from a conditional
Gaussian — here the daily returns. Fitting via expectation-maximisation
(Baum-Welch).

```python
import numpy as np
from hmmlearn.hmm import GaussianHMM

rets = np.column_stack([returns])          # hmmlearn wants a matrix, even for 1-D
model = GaussianHMM(n_components=2,        # 2 regimes: low-vol vs high-vol
                    covariance_type="full",
                    n_iter=1000).fit(rets)
hidden = model.predict(rets)               # per-observation regime labels
regime_today = hidden[-1]                  # latest regime
```

**Worked recipe (SPY regime filter):**
1. Train on SPY adjusted-close returns, 1993–2004 (in-sample), 2 states,
   full covariance.
2. Sanity-check: plot adjusted close masked by hidden state — confirm one
   state captures volatile/crash periods (e.g. most of 2008 in one state).
3. Serialise (pickle) the fitted model for the live/backtest process.
4. Risk manager: `predict()` on the rolling returns; if state = low-vol →
   allow new longs; if state = high-vol → **block new longs, but allow
   closing signals for existing positions** (handles trades straddling
   regimes).

**Out-of-sample result (2005–2014, trend-following underlying):**
max daily drawdown cut from ≈56% (benchmark) to ≈24%; Sharpe 0.37 → 0.48;
trades 41 → 31; no trading early-2008 → mid-2009 (sat out the crash).

## known pitfalls
- **Retrain periodically**: HMM transition probabilities are not stationary;
  the model can only predict regimes it has seen — a distribution change
  (new regulation/regime) requires refitting.
- **State labels 0/1 are arbitrary** — map to low/high-vol via sanity plots
  before use.
- Keep training data strictly **out-of-sample** from the backtest window.
- Filtering trades cuts both ways: fewer trades = less statistical validity
  (fewer positive-expectancy bets).
- HMMs are unsupervised — assess on economic plausibility and risk metrics
  (max DD, drawdown duration), not just fit score.

## source book
Halls-Moore, *Advanced Algorithmic Trading*, ch14 (Hidden Markov Models)
and ch31 (HMM market-regime filter as a QSTrader risk manager).
