# Ch14 — Hidden Markov Models (Market Regime Detection)

**Source:** Halls-Moore, *Advanced Algorithmic Trading*, Chapter 14.

## Motivation
Financial market behaviour changes over time due to policy/regulatory/macro shifts → **market
regimes**. Regimes alter returns via shifts in mean, variance, autocorrelation, covariance —
causing non-stationarity, dynamically-varying correlation, fat tails, heteroskedasticity,
skew. Detecting regimes matters for optimal strategy deployment and re-tuning (position
sizing, risk management). **Hidden Markov Model (HMM)** is the key tool: the *latent* process is
the hidden regime state; *asset returns* are the noisy indirect observations.

## Markov Models taxonomy (by autonomy × observability)
| | fully observable | partially observable |
| autonomous | Markov Chain | **Hidden Markov Model (HMM)** |
| controlled (agent) | Markov Decision Process (MDP) | POMDP |
- **Markov Property / "memoryless"**: jump probability depends only on the current state, not
  earlier ones (e.g. random walks; MCMC chains).
- **Markov Chain**: autonomous + fully observable. Transition via time-invariant matrix A.
- **HMM**: autonomous + partially observable — latent states with transition probabilities,
  not directly observable; they influence observations. (No need for observations to be Markov.)
- **RL family** (controlled): MDP, Q-Learning, Deep-Q-Networks (Atari/AlphaGo), POMDP —
  out of scope here. (Note: continuous-time Markov processes / stochastic calculus used for
  derivatives pricing are also out of scope.)

## Mathematical specification
For a **Discrete-State Markov Chain** (K states), the joint density factorises as
p(X_1..X_T) = p(X_1) Π_{t=2..T} p(X_t|X_{t−1}), with time-invariant transition function/times.
- **Transition matrix A (K×K)**: A_ij = P(z_t = i | z_{t−1}=j) (probability of going j→i);
  each column sums to 1. **n-step** transition: A(n)=A(1)ⁿ (powers of the one-step matrix).

**HMM** adds: discrete hidden states z_t ∈ {1..K} (often K≤3 for regime detection) plus an
observation probability model p(x_t|z_t). Observations don't affect states; states affect
observations. Joint density:
p(z_1..z_T, x_1..x_T) = Π p(z_t|z_{t−1}) · Π p(x_t|z_t)
- For continuous returns, **observation model = conditional Gaussian**: x_t|z_t=k ~ N(μ_k, Σ_k).
- The model tends to *stay in a state then suddenly jump* — exactly the desired regime
  behaviour (slow-moving regulatory/macro effects).

**Inference tasks**: filtering (current state from past+current obs), smoothing (past states),
prediction (future). For regime detection we do **filtering**: posterior probability of the state
at time t given observations up to t — computed by **recursive Bayes** (like the KF) or via
Forward/Viterbi algorithms (derivations beyond scope).

## Key caveat — the problem is unsupervised learning
There's no "ground truth"/labels; we don't know how many states exist a priori (2? 3?). The
answer depends on asset class, timeframe, data. E.g. daily equity returns often show long calm
low-vol periods plus rare "panic/correction" high-vol bursts → 2 states natural; a 3rd
intermediate-vol state is plausible. Careful research needed before overlaying HMM on a
risk manager.

## Simulated two-regime experiment
Simulate 5 "stitched" regime periods: bull = N(0.1, 0.1), bear = N(−0.05, 0.2), random N_k days
each. Fit HMM (2 states, `Gaussian()`) with `depmixS4::depmix(...)` + `fit()` via **EM**; plot
posterior regime probabilities vs known true states — model does a good job tracking switches. ✓

## Applied to S&P500 returns
- **Two states**: HMM gives high posterior to "calm" regime #2 during 2004–07; rapid
  regime-probing during 2007–09 crisis; back to calm after 2011; choppy 2015 flagged.
- **Three states**: in calm 2004–07 the model switches between #2 & #3; in volatile 2008/2010/
  2011 regime #1 (high-vol) dominates; after 2011 reverts to switching #2/#3.
- Choosing the number of states is a persistent challenge tied to asset class, trading style,
  and time horizon.

## Takeaways / pitfalls
- HMM regime detection is *unsupervised* — no ground truth for state count.
- Filtering (online) is what you need for live trading overlays.
- Later used as a **RiskManager subclass in QSTrader** to veto/close signals from a
  strategy, aiming to improve profitability vs no risk management.
- Sources: Murphy (2012), Bishop (2007); applied recipes by Systematic Investor (depmixS4/
  RHmm), Gekkoquant (HMM trend-following, Sharpe 0.857), Slaff (EUR/USD vol regimes).