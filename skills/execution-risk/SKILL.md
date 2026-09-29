---
name: execution-risk
description: Engle-Ferstenberg (2006) — investment and execution are ONE mean-variance problem with a single risk aversion. TC variance and Cov(TC, gain) belong in ex-ante Sharpe; risk-averse paths front-load; hedge unfinished execution with futures; liquidity risk = ES of liquidation cost.
---

# Execution risk (Engle-Ferstenberg unification)

**When to use:** any ex-ante Sharpe or portfolio construction that
includes trading costs. The existing cost skills charge *expected* cost
(`impact-calibration`); this skill adds the *risk* of cost — the piece
that makes realized Sharpe disappoint.

## Core claims

1. **Single λ.** Investment and execution are one mean-variance
   problem: `max E[x_T'(p_T−p_0) − TC] − λ·V(x_T'(p_T−p_0) − TC)`.
   Splitting λ between the PMS and the execution algo is incoherent.
2. **TC variance belongs in the denominator.** `V(gain − TC) =
   V(gain) + V(TC) − 2·Cov(gain, TC)`. Frontier ordering: Pure
   Markowitz ≥ Cost-Adjusted (subtract E[TC] only) ≥ True. Planning
   under the first two lies *inside* the true frontier.
3. **Front-load when risk-averse.** The three-period closed form
   (fixed start x₀, target x_T, permanent impact Π, temporary impact T,
   covariance Ω):

   `x_t = ½(Π+2T+λΩ)⁻¹[(Π+2T)x₀ + (Π+2T+2λΩ)x_T]`

   λ=0 → even pace; λ>0 → midpoint closer to x_T (front-loaded).
   Implementation: `quantkit.execution.ef_midpoint` (tests:
   `TestEFMidpoint`; verify check 21).
4. **Hedge the unfinished book.** With cross-correlated assets, the
   optimal path trades a hedge asset (e.g. index futures) even when its
   start=target: hedge ratio ≈ β(2 on 1) × remaining primary trade.
   Unwind as the primary completes.
5. **Liquidity risk = ES of liquidation cost.** Parallel to market-risk
   VaR: the 1% quantile (prefer expected shortfall) of cash after
   *optimal* liquidation over ~10 days. Rises more than proportionally
   with vol; inflate impact parameters in crises ("liquidity black
   holes") and recompute.

## Reversals and continuations

Lagged impact polynomials change the optimal pace: permanent reversal →
less aggressive; transitory continuation → less aggressive; transitory
reversal → more early trades. Same λ throughout.

## Pitfalls

- Theory paper with illustrative simulations, not calibrated empirics.
- Assumptions A.1–A.2 rule out stochastic instantaneous costs and
  trade-dependent Ω.
- Linear permanent impact may fail for huge metaorders.
- Separation (investment window ≫ execution window) fails for
  high-turnover strategies — joint optimization needed there.
- Single-λ mean-variance ignores higher moments and discontinuous
  liquidity.

## Source

Corpus: `library/raw/drive-download-20260925T215026Z-1-001/marketimpact/Execution Risk Optimal Trading (optimaltrading_Engle_2006.pdf).md`
Spine block: Σ + costs. Mechanism: **liquidity** (impact cost risk).
