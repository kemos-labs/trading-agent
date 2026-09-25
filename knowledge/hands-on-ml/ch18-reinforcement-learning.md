# Ch18 — Reinforcement Learning

**Source:** Géron, *Hands-On Machine Learning*, Chapter 18.

## Purpose
Agents that maximise cumulative reward in an environment: Markov decision
processes, policy gradients, and deep Q-networks (DQN). DeepMind's Atari
breakthrough (2013) and AlphaGo.

## RL basics
- **Agent** observes state s, takes action a, receives **reward** r from
  the environment; objective: maximise **expected cumulative reward** over
  time. Reward = pleasure/pain framing.
- The **policy** (π) maps states → actions; can be a neural net.
- **Policy search** families: brute-force over params; genetic algorithms
  (evolve populations of policies); **policy gradients** (follow the
  gradient of expected reward).
- **OpenAI Gym**: standard simulated environments (`gym.make("CartPole-v1")`);
  `reset()` → observation; `step(action)` → (obs, reward, done, truncated,
  info); `action_space`, `observation_space`. (Gymnasium is the current
  fork.)

## Markov decision processes (MDP)
- Formal setting: states, actions, transition probabilities P(s′|s,a),
  reward function R(s,a), discount factor γ ∈ [0,1].
- The **return** Gₜ = Σ γᵏrₜ₊ₖ — future rewards discounted (γ<1 makes
  sums finite and values near-term rewards more).
- **Value of a state** V(s) = expected return from s; **Q-value**
  Q(s,a) = expected return from taking a in s.
- **Bellman equations**: V(s) = maxₐ E[r + γV(s′)] and
  Q(s,a) = E[r + γ·maxₐ′ Q(s′,a′)] — the recursive self-consistency that
  Q-learning exploits. Value iteration / policy iteration solve tabular
  MDPs exactly when small.

## Policy gradients (PG)
- Directly optimise the policy with **gradient ascent** on expected reward.
- **REINFORCE**: for each episode, compute the return; increase log-
  probability of actions that led to high returns (weighted by discounted
  return minus baseline — **advantage** reduces variance).
- PG is **on-policy** (learns from its own behaviour), naturally handles
  continuous actions, stochastic policies (exploration built in).
- Problems: high variance (needs many episodes, baselines, large batches);
  reward scales are fragile.

## Deep Q-learning (DQN)
- **Q-learning** is **off-policy**: learn Q(s,a) from any behaviour
  (even random exploration) by bootstrapping on the Bellman equation:
  update Q toward `r + γ·maxₐ′Q(s′,a′)` (temporal-difference, TD).
- **DQN**: a DNN approximates Q-values (input state → one Q per action).
  Key stabilisers:
  - **Experience replay**: store (s,a,r,s′) transitions; sample random
    mini-batches — decorrelates data, reuses experiences;
  - **Target network**: a slowly-updated copy of the Q-network provides
    the TD targets — prevents chasing a moving target;
  - exploration policy: ε-greedy (mostly best action, sometimes random).
- **Double DQN**: use the online net to pick the best action but the
  target net to evaluate it — fixes Q-value overestimation.
- **Dueling DQN**: split Q into V(s) + advantage A(s,a).
- **Prioritised experience replay**: sample transitions with large TD
  errors δ = r + γV(s′) − V(s) more often — learn faster.
- **Rainbow**: combines DQN + double + dueling + PER + more; SOTA baseline.

## Algorithm landscape
- Value-based (DQN family), policy-based (PG/PPO), actor–critic (both: e.g.
  A2C/A3C), model-based (learn the environment's dynamics), evolutionary.
- AlphaGo = policy network (PG) + value network + MCTS (model-based
  search); the combination beats each alone.

## Key takeaways
- RL = maximise discounted return; Bellman equations are the backbone.
- PG: simple, on-policy, high-variance. DQN: sample-efficient with replay
  + target nets; ε-greedy exploration.
- RL training is unstable by default: replay, target nets, clipping,
  and reward shaping are the practical stabilisers.
- Start with Gym/Gymnasium + CartPole to sanity-check any agent before
  scaling.

## Notes
- For trading agents (the book's own example): reward = P&L, state = price
  history, actions = buy/sell/hold — the same DQN/PG machinery applies,
  with extra care about nonstationarity and transaction costs.
- Off-policy Q-learning's "learn from a blindfolded monkey" property is why
  replay buffers are so powerful.
