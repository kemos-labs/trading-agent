# Ch22 — Deep Reinforcement Learning: Building a Trading Agent

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 22.

## Purpose
RL for goal-directed decision-making: MDPs, value iteration, Q-learning, and deep Q-networks — culminating in an OpenAI Gym agent and a framework for a trading agent.

## RL elements
- **Agent** interacts with an **environment** over discrete steps: observes state s, takes action a, receives reward r, transitions to s′.
- **Policy** π: state → action(s). **Reward**: the scalar feedback; designing it well is the hardest part (trading rewards must encode risk/drawdown, not just P&L).
- **Value function**: expected cumulative (discounted) future reward from a state or state-action — the basis for long-run decisions.
- **Model-based vs. model-free**: model-based learns the environment's dynamics and plans; model-free (Q-learning, policy gradients) learns from trial and error.

## Key challenges
- **Credit assignment**: which past actions caused today's reward? (In trading: 100 positions, one portfolio return.)
- **Exploration vs. exploitation**: try new actions vs. use what's learned — ε-greedy (take random action with prob ε, decaying) is the standard.

## Algorithms
- **Dynamic programming** (known dynamics): value iteration / policy iteration on Bellman equations V(s) = max_a E[r + γV(s′)].
- **Q-learning** (model-free, tabular): Q(s,a) ← Q(s,a) + α[r + γ·max_a′ Q(s′,a′) − Q(s,a)] — off-policy TD learning.
- **Deep Q-Network (DQN)**: neural network approximates Q(s,a) for continuous/high-dim states.
  - **Experience replay**: store (s,a,r,s′) transitions, sample minibatches — breaks autocorrelation, reuses data, stabilizes.
  - **Target network**: a slowly-updated copy of the Q-network generates TD targets — stabilizes learning by decorrelating targets from the online net.
  - **Double DQN (DDQN)**: use the online net to *select* the best next action and the target net to *estimate* its value — removes Q-value overestimation bias.
  - Rainbow combines replay, prioritization (TD-error-based sampling), double Q, dueling, and distributional value.

## OpenAI Gym
- Standard RL API: `env.reset()`, `env.step(action)` → (obs, reward, done, info); register custom environments.
- Lunar Lander: 8-dim state, 4 discrete actions; solved at ≥200 average reward over 100 episodes — a canonical DDQN benchmark.

## Trading agent design
- State: returns, positions, technicals, market conditions; actions: buy/sell/hold (discrete) or target positions (continuous); reward: P&L minus risk terms (volatility, drawdown, transaction costs).
- **Dangers in practice**: market simulation is a weak environment model — RL agents overfit the simulator, and reward shaping can encode lookahead; use realistic costs and out-of-sample evaluation (ch8).
- RL is a framework for policy optimization — its value in trading is real but demands honest simulation; most reported "RL trading bots" fail this test.

## Key takeaways
- RL optimizes sequential decisions under delayed rewards — the natural fit for trading, in principle.
- DQN's stability tricks (replay, target net, double Q) are essential — naive Q-networks diverge.
- The environment (simulator, costs, reward) determines everything: an unrealistic environment trains an unrealistic agent.
