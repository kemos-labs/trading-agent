---
name: optimal-turnover-liquidity
description: Cost-aware turnover target from alpha half-life, Kyle lambda, and risk aversion (Baldacci-Benveniste-Ritter 2022). Replaces "more turnover = more IR" with a closed-form optimal turnover and steady-state IR net of quadratic costs.
---

# Optimal turnover, liquidity, and autocorrelation

**When to use:** sizing how fast to trade a signal sleeve; diagnosing
overtrading; budgeting net IR before launch. The cost-aware companion to
the fundamental law (`allocation-discipline` skill) — FLAM says more
breadth is better; this says there is an optimal turnover given impact.

## Method

For an OU alpha process `dμ = -φμ dt + ν dW` (half-life `ln2/φ`) traded
under linear (Kyle-λ) impact with risk aversion κ and vol σ, define the
trading-speed rate `γ = √(κσ²/λ)`. Then (BBR 2022, Eqs. 20/23):

- **Optimal steady-state turnover** = `γ·√(φ/γ + 1)` (fraction of book
  per unit time)
- **Steady-state IR (net of costs)** = `ν/(2σ)·√(γ/(φ(φ+2γ)))`
- Multi-asset: multiply IR by `√N` for N *statistically independent*
  assets — in equities, trade **residual assets** (stock + factor
  hedges) so breadth is not overstated.

Implementation: `quantkit.portfolio.optimal_turnover(gamma, phi)` and
`quantkit.portfolio.steady_state_ir(nu, sigma, gamma, phi)` (tests:
`TestOptimalTurnover`; verify checks 20).

## Desk example (paper's calibration)

κ=1e-6, σ=1%/day, λ=10 bp per 1% ADV → γ=0.1/day; φ=0.2/day
(half-life ≈ 3.5 days) → optimal turnover ≈ **17.3%/day**, IR ≈
`0.56·ν/σ`. Compare realized two-way turnover to this band: far above =
overtrading vs the linear-impact optimum; far below = leaving alpha on
the table.

## Comparative statics

- Higher φ (faster alpha decay) → higher optimal turnover, lower IR for
  fixed ν.
- Higher λ (worse liquidity) → lower γ → lower turnover and IR.
- Higher κ → higher γ → more aggressive trading toward the aim.

## Pitfalls

- **Linear impact only.** Empirics favor square-root impact for large
  clips; treat the formula as a heuristic/bound — if the linear-impact
  optimum already says slow down, square-root usually says slow down
  more.
- OU-specific: multi-horizon signals need the general Theorem-1
  integral, not a sum of single-OU turnovers.
- Parameter errors (λ, φ, ν, κ) map nonlinearly into the target.
- Infinite-horizon/no-discounting baseline; finite mandates need
  truncation.

## Source

Corpus: `library/raw/drive-download-20260925T215026Z-1-001/portfolioconstruction/Optimal Turnover Liquidity and Autocorrelation (OptimalTrading_RitterBaldacciBenveniste_2022.pdf).md`
Spine block: optimization (cost-aware FLAM). Mechanism: **liquidity**
(Kyle λ) + **information** (alpha half-life φ).
