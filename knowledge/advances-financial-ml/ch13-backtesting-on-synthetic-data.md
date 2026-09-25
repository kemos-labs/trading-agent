# Ch13 — Backtesting on Synthetic Data

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 13.

## Purpose
An alternative backtesting paradigm: characterize the stochastic
process generating returns from history, then derive optimal trading
rules *analytically* (or via Monte Carlo on synthetic paths) instead of
fitting parameters to one historical path — avoiding backtest
overfitting at the parameter-calibration stage.

## Trading rules and the calibration problem
- A **strategy** is a theory of market inefficiency; a **trading rule**
  is the tactic (entry/exit logic). Exit rules are usually
  profit-taking/stop-loss thresholds — equivalent to the horizontal
  barriers of the triple-barrier method (ch3).
- Calibrating thresholds by historical simulation = backtest
  overfitting: parameters target specific past observations, and the
  strategy becomes attached to the past.
- Better: derive optimal thresholds from the stochastic process itself.

## The framework
- Model the position's mark-to-market PnL: π_{i,t} = m_i(P_{i,t} −
  P_{i,0}); the trading rule R = {π̄⁺ (profit-taking), π̄⁻ (stop-loss)}
  exits when either barrier is touched first.
- Objective: maximize the Sharpe ratio over R (the "expected-profit /
  volatility" of exits), over I opportunities.
- With an Ornstein–Uhlenbeck (mean-reverting AR(1)) price process
  estimated from the observed series, run Monte Carlo simulations over
  synthetic paths and map the Sharpe heat-map across the
  (profit-taking, stop-loss) grid — thousands of unseen testing sets,
  none of them the historical path.

## Key empirical findings
- On a *random walk* (no real inefficiency): the heat-map is
  featureless — performance shows no consistent pattern, so there is no
  optimal rule; any parameter combination that looks good IS the
  overfit fluke. Synthetic testing exposes this.
- **Mean-reverting process**: optimal rules are asymmetric — high
  profit-taking (~6σ) with moderate stop-losses (4–10σ) and Sharpe up
  to ~3.2, matching how market makers trade (the "asymmetric payoff
  dilemma": market makers win small, lose big).
- **Positive-drift process** (position-taker): optimal profit-taking
  moderate, wide stop-loss region; Sharpe ~12.
- As the process half-life τ grows (→ random walk), performance drops
  and the optimal region blurs — closer to a random walk means less to
  exploit.
- Worst rule almost everywhere: short stop-loss + large profit-taking.

## Key takeaways
- Backtesting on synthetic data tells you whether a strategy's edge is
  structural (heat-map has a coherent optimum) or a statistical fluke
  (featureless heat-map).
- The optimal exit rule depends on the nature of the edge:
  market makers need tight stops and wide targets; position-takers can
  afford wide stops.
- When calibrating any threshold parameter, verify it against
  synthetic data from the estimated process before trusting history.
