# Ch21 — Brute Force and Quantum Computers

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 21.

## Purpose
Shows how an intractable financial ML problem — dynamic portfolio
optimization with non-convex, non-continuous transaction costs — can be
discretized into an integer optimization amenable to brute-force search,
and ultimately to quantum computers (qubit superposition evaluates all
feasible solutions at once).

## Combinatorial optimization and quantum computing
- Combinatorial problems have finitely many feasible solutions but
  exhaustive search becomes impractical as combinations explode (e.g.,
  traveling salesman — NP-hard).
- Classical computers evaluate/store solutions sequentially; quantum
  qubits hold a *linear superposition* of states, so in principle all
  feasible solutions can be evaluated simultaneously — the natural fit
  for NP-hard combinatorial search.

## The problem: dynamic portfolio optimization
- N assets, H horizons, returns multivariate Normal with time-varying
  mean μ_h and variance V_h. A trading trajectory ω (N×H matrix)
  defines allocations. Expected returns r = μ·ω − τ[ω], where τ[ω] is
  an arbitrary (non-continuous) transaction-cost function, e.g.,
  per-asset square-root-of-change scaled costs.
- Objective: maximize the Sharpe ratio of r — a *global dynamic*
  optimum, unlike the static mean-variance optimum. Not convex for
  three reasons: (1) returns not identically distributed (μ, V vary
  with h); (2) transaction costs non-continuous and time-varying;
  (3) the Sharpe objective is non-convex.

## The integer optimization approach
- Discretize the allocation space: **pigeonhole partitions** — K units
  of capital among N assets, counting the number of ways (combinatorial
  counting), i.e., the number of feasible trajectories.
- Each trajectory is a discrete combination; the search is
  exhaustive over feasible allocations — tractable for moderate N×H,
  and structured so a quantum annealer/search could evaluate the full
  feasible set.
- No analytical property of the objective is used (no convexity,
  no gradients) — hence the approach generalizes to any cost function,
  including realistic non-smooth market-impact models.

## Key takeaways
- Frame intractable problems as *discrete* optimization to make them
  searchable; quantum computers change the feasible-combination scale
  by evaluating superpositions.
- Non-convex, cost-aware dynamic optimization is exactly where
  mean-variance breaks; discretization + search is the general escape.
- The practical takeaway for current infrastructure: brute-force
  integer search on discretized portfolios is a workable fallback for
  small-to-moderate problems even before quantum hardware matures.
