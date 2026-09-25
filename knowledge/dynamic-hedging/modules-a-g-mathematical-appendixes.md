# Modules A–G — Mathematical Appendixes

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Modules A–G.

## Purpose
The mathematical back-office of the book: random walks, risk neutrality, numeraire relativity, correlation geometry, value-at-risk, and the closed-form pricing toolkit.

## Module A — Brownian motion on a spreadsheet
- Simulate a 1-asset random walk: log returns = σ·z with z ~ N(0,1); prices are the cumulative product of e^(−σ²/2 + σz) per step (driftless geometric Brownian motion). One standard deviation scales with √t (1% daily → 15.7% annual over 248 days).
- **Two-asset walk with correlation**: build the 2×2 covariance matrix, then its **Cholesky** decomposition (A with a₁₁=√C₂₂, a₂₁=C₃₂/a₁₁, a₂₂=√(C₃₃−a₂₁²)); generate independent normals z₁,z₂ and set RET_B = a₂₁·z₁ + a₂₂·z₂ — this makes B's returns correlated with A's at the target ρ.
- Visualization: pairs of returns form a concentric cloud (circle at ρ=0, line at |ρ|=1); n-asset clouds generalize to spheres.

## Module B — Risk neutrality explained
- Discrete tree: to be "probability fair" (no free lunch), p·u + (1−p)·d = 1 (driftless); a skew in step sizes is compensated by asymmetric probabilities (larger up-step → smaller up-probability).
- **The BSM argument**: delta-neutral replication removes exposure to the asset's expected return; the option is priced off volatility and the risk-free rate — the drift is replaced by the risk-neutral rate (change of probability measure / Girsanov).
- Option value = discounted expected payoff under the risk-neutral measure.

## Module C — Numeraire relativity
- Any pair (asset1, asset2) has two numeraires; the delta for one party is the *binary* for the other and vice versa — the two-country paradox.
- Via Jensen's inequality: for a convex φ, φ(E[x]) ≤ E[φ(x)]; for the inverse 1/x, 1/E(x) < E(1/x) — so expectations are numeraire-dependent.
- Ito's lemma on U = 1/S: dU/U = (σ² − μ)dt − σdZ — each operator faces a risk-neutral process as a function of his numeraire.

## Module D — Correlation triangles
- Represent assets as points in Euclidean space; the implied volatility of a pair is the *distance* between the points — v(x,y) is a metric (positive, symmetric, triangle inequality).
- With USD at (0,0), DEM at (7,12.12) → USD-DEM vol = √(7²+12.12²) = 14%. Adding JPY at distance 12 gives a triangle — the third side is bounded by the triangle inequality (the arbitrage-free band on cross-volatility).

## Module E — Value-at-risk
- VaR: the loss level not exceeded with a given probability over a horizon, from the covariance matrix of returns (Markowitz machinery).
- Portfolio VaR with diversification (Example 1: no diversification; Example 2: diversified portfolio — the covariance matrix reduces VaR).
- Caveats: VaR ignores the *liquidation costs at the stopping barrier*; distributions' tails are underweighted — the "when it goes it keeps going" problem.

## Module F — Probabilistic rankings in arbitrage
- Ranking securities/strategies by the probability of profit (rather than expected value alone) — a first-order stochastic-dominance flavor for choosing between trades.
- First-order dominance: if one distribution always gives at least as high payoff, it dominates regardless of utility; used to rank arbitrage opportunities with uncertain outcomes.

## Module G — Option pricing formulas
- Closed forms for barrier options: knock-out call = discounted expectation under measure Q of the payoff conditional on the barrier not being touched; via the **reflection principle**, the density of S_T given no touch equals that of H²/S_T — so CUO = exp(−rt)(P1 − P2) with P2 integrating the reflected paths (the h = (1/(σ√t))log(H/S₀) normalization).
- Double knock-out and double binary formulas as rapidly-converging infinite sums (Kunitomo-Ikeda; Geman-Yor Laplace-transform method); the sums converge within ±12 terms.
- Stopping time: density of first exit time with no drift ~ (h/(√(2πt³)))·exp(−h²/2t).

## Key takeaways
- Cholesky decomposition is the practical recipe for generating correlated paths (also in `kalman-filter-pairs`/portfolio sims).
- Risk-neutral pricing = expectation under the changed measure; numeraire choice changes the process and the Greeks.
- Correlation-triangle geometry gives arbitrage-free bounds on cross-volatility; VaR is a tool with tail blind spots.
