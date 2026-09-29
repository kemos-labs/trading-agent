# Plan: Phase 9 — Live execution layer (impact-aware costs)

Spine (Paleologo): Σ + costs. Goal: stop understating execution cost.
Phase 3/4/6 charge a flat 10 bps per unit turnover, but the corpus
(`impact-calibration` skill, Almgren et al. 2005) says cost is
schedule- and size-dependent: permanent impact
`I = γ·σ·(X/V)·(Θ/V)^{1/4}` plus realized `J = I/2 + η·σ·|X/(V·T)|^{3/5}`,
and capacity shrinks for long horizons (size-invariant HFT Sharpe at
fixed fee) — exactly the P2 risk flagged in
`knowledge/engine-upgrade-research-2026-08-31.md` ("Daily-close-only
execution understates spread/cost").

Design rules:
- Impact cost is an *additive layer* on ptc, never a replacement: flat
  floor (conservative: worst case is paying the spread on the horizon
  we claim). Total = ptc + impact_bps.
- `execution.impact_almgren` reuses the T2 closed form (already
  verified, checks 12–13) — no new math, no new deps.
- Fail-closed: missing/zero ADV or a >0.25·ADV order raises (never a
  fabricated zero-cost fill), `impact_on=True` opt-in, default stays
  legacy flat behavior.
- Same paper-only guard, same kill-switch, same one-bar lag discipline.

## DAG

- [ ] **T1: cost model + unit test.** `execution.impact_almgren(delta,
      adv, sigma, horizon_days, outstanding, ptc, gamma=0.314, eta=0.142)`
      -> cost bps (flat floor + Almgren realized J, clipped ≥ 0). Tests:
      buy/sell symmetry, schedule monotonicity (slower ⇒ smaller J),
      fail-closed (adv ≤ 0 → ValueError; |Δ|/adv > 0.25 → ValueError
      unless explicitly allowed), matches hand J ≈ 38 bps at the T2
      reference point (X=1e6, V=1e7, T=0.1, σ=2%).
- [ ] **T2: wire into PaperTrader.** `impact_on`, `horizon_days`,
      `outstanding` (optional shares outstanding) kwargs; per-bar ADV from
      the live store (`volume.rolling(20).mean()`); journal gains an
      `impact_cost` column (sums with `cost`, keeps `paper_only; execution
      next bar` note); cost model surfaced in journal and `paper_book`
      payload. Tests: impact layer increases cost vs flat-only; journal
      column set; fail-closed when store has no volume.
- [ ] **T3: wire into BacktestEngine.** Same additive layer via
      `execution_cost_fn` hook (default None ⇒ legacy flat path);
      ADV from the backtest frame. Tests: engine matches hand-computed
      total cost at a reference order; disabled by default (Phase-3 SHAs
      unchanged).
- [ ] **T4: dashboard + docs.** `research/attribute.py` prints the
      impact layer per leg; `build_dashboard_data` cost summary reflects
      impact when enabled; PROGRESS/MEMORY update; verify_formulas.py
      check 19 (impact model reuses T2 closed form — no new formula).

## Verify (must stay green at every T)
- `PYTHONPATH=src .venv/bin/python -m unittest discover -s tests` — 190+ pass
- `PYTHONPATH=src .venv/bin/python research/verify_formulas.py` — 19 checks PASS
- `PYTHONPATH=src .venv/bin/python research/run_phase3.py --offline` — SHAs
  79d9cd/f584d0/cd13f1, verdicts unchanged
- `PYTHONPATH=src .venv/bin/python research/paper_trade.py --offline --dry-run`
  idempotent
- quantkit version bump 0.8.0 → 0.9.0; `skills/INDEX.md` execution entry
  updated; new skill only if a mechanism that isn't already covered
  appears (impact layer is the `impact-calibration` skill → code, so no
  new skill).
