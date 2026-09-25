# Ch10 — Reinforcement Learning

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 10.

## Purpose
Introduces reinforcement learning (RL) — where an agent learns trading
policy directly from the rewards of its actions — and the
DQN-style deep RL that makes it practical, plus the reasons RL is
harder to make work in finance than in games.

## RL fundamentals
- **Agent + environment + reward**: the agent observes a state s,
  takes an action a, the environment returns a new state and a reward
  r. The agent's goal is to maximize *cumulative* discounted reward,
  not the immediate one: G = Σ γᵗ·r_t with discount factor γ ∈ [0,1].
- **Policy** π(s) maps states to actions; **value function** V(s) is
  the expected future reward from state s; **action-value Q(s,a)** is
  the expected future reward from taking action a in state s.
- In trading: state = features (prices, indicators, position),
  action = buy/hold/sell (or size), reward = P&L change.

## Q-learning and DQN
- **Q-learning** iteratively updates Q(s,a) toward the Bellman
  target: Q(s,a) ← Q(s,a) + α·(r + γ·maxₐ' Q(s',a') − Q(s,a)).
  The optimal policy is greedy action selection under Q*.
- **Exploration vs. exploitation**: ε-greedy (take the best action
  with probability 1−ε, random otherwise) balances trying new actions
  against using learned ones.
- **DQN (Deep Q-Network)**: approximate Q with a neural network.
  Two tricks make it stable: a **replay buffer** (train on randomly
  sampled past transitions, decorrelating updates) and a **target
  network** (a slowly-updated copy used to compute the Bellman
  target, preventing chasing a moving goal).

## Why RL is hard in finance
- **Non-stationarity**: markets change regimes; the environment the
  agent learns is not the environment it deploys in.
- **Sparse, noisy rewards**: transaction costs, slippage, and random
  drift swamp the signal; rewards are delayed and stochastic.
- **Data hunger**: DQN needs enormous interaction data, but finance
  offers one thin historical path — no reset button, no parallel
  universes. Simulation helps but risks overfitting to the simulator.
- **Cost sensitivity**: the reward must include transaction costs or
  the agent will trade itself to death.

## Key takeaways
- RL is the most natural framing for sequential trading decisions
  (what to do *now* given *state*), but its sample complexity makes it
  the hardest technique in the book to deploy profitably.
- Include costs in the reward, discount appropriately, and validate in
  multiple regimes with walk-forward discipline.
- Treat RL results with extra suspicion: the replay buffer, target
  network, and hyperparameters all interact, and small changes can
  flip results — reproduce and stress-test before trusting.
