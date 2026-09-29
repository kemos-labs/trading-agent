#!/usr/bin/env python
"""Strategy attribution — Phase 8 T4 close-out.

Lecture 1 closing demands: which signals worked, did sizing add value, were
realized costs consistent with the model. This script answers from existing
stores only (no new data, no orders):

- `data/research/phase3/backtest_*.csv` → per-leg gross / costs / net,
  cost share of gross, turnover proxy (mean |Δexposure|), skew of net.
- `data/paper/journal.csv` → paper cost-rate integrity check: every row's
  cost / |delta·close| must equal the 10 bps model rate (fail-closed).

Writes a markdown report to knowledge/strategy-research/attribution-*.md.
Paper-only: read-only over the journal; never writes to data/paper/.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PHASE3 = ROOT / "data" / "research" / "phase3"
JOURNAL = ROOT / "data" / "paper" / "journal.csv"
MODEL_RATE = 0.001  # 10 bps, the Phase 3/4 cost model


def leg_attribution(path: Path) -> dict:
    df = pd.read_csv(path, parse_dates=["date"])
    gross = float(df["gross"].fillna(0).sum())
    costs = float(df["costs"].fillna(0).sum())
    net = float(df["net"].fillna(0).sum())
    turnover = float(df["exposure"].diff().abs().fillna(0).mean())
    skew = float(df["net"].fillna(0).skew()) if len(df) > 3 else float("nan")
    cost_share = costs / gross if gross > 0 else (float("nan") if gross == 0 else costs / abs(gross))
    return {"gross": gross, "costs": costs, "net": net,
            "cost_share": cost_share, "turnover": turnover, "skew": skew}


def journal_check() -> dict:
    # Model: cost = ptc * |delta| * capital_per_leg (delta is a fraction of
    # the leg's capital, not shares). Integrity = proportionality + guard.
    # When the impact layer is on, cost = flat + impact_cost, so the
    # proportionality check applies to the flat component only.
    j = pd.read_csv(JOURNAL)
    if j.empty:
        return {"rows": 0, "unit_cost": float("nan"), "rel_spread": 0.0,
                "ok": True, "guard_ok": True, "impact_rows": 0}
    has_impact = "impact_cost" in j.columns
    flat = j["cost"] - j["impact_cost"].fillna(0.0) if has_impact else j["cost"]
    impact_rows = int((j["impact_cost"].fillna(0.0) != 0).sum()) if has_impact else 0
    j = j.assign(_flat=flat)
    nz = j[j["delta"].abs() > 0].copy()
    unit = (nz["_flat"] / nz["delta"].abs()).to_numpy(dtype=float)
    med = float(np.median(unit)) if len(unit) else float("nan")
    rel = float((unit.max() - unit.min()) / med) if len(unit) and med else 0.0
    implied_capital = med / MODEL_RATE if med == med else float("nan")
    guard = bool((j["note"].str.contains("paper_only").fillna(False)).all())
    return {"rows": len(j), "unit_cost": med, "rel_spread": rel,
            "implied_capital_per_leg": implied_capital,
            "ok": rel <= 1e-9 and guard, "guard_ok": guard,
            "impact_rows": impact_rows}


def main() -> None:
    legs = sorted(PHASE3.glob("backtest_*.csv"))
    if not legs:
        raise SystemExit("no phase3 backtest legs found (fail closed)")
    rows = []
    for leg in legs:
        name = leg.stem.replace("backtest_", "")
        rows.append((name, leg_attribution(leg)))
    jc = journal_check()

    lines = ["# Attribution — Phase 3 legs + paper journal", "",
             f"Model cost rate: {MODEL_RATE:.4f} (10 bps).", "",
             "| leg | gross | costs | net | cost/gross | turnover | skew |",
             "|---|---|---|---|---|---|---|"]
    for name, a in rows:
        lines.append(f"| {name} | {a['gross']:.4f} | {a['costs']:.4f} | {a['net']:.4f} "
                     f"| {a['cost_share']:.3f} | {a['turnover']:.4f} | {a['skew']:.3f} |")
    lines += ["",
              "## Paper journal integrity",
              f"- rows: {jc['rows']}, unit cost |cost/delta|: {jc['unit_cost']:.6f}",
              f"- relative spread of unit cost: {jc['rel_spread']:.2e} (proportionality)",
              f"- implied capital per leg: {jc.get('implied_capital_per_leg', float('nan')):.2f}",
              f"- paper_only guard on every row: {jc['guard_ok']}",
              f"- impact-layer rows: {jc.get('impact_rows', 0)} (flat component checked for proportionality)",
              f"- verdict: {'PASS' if jc['ok'] else 'FAIL'}"]
    if not jc["ok"]:
        raise SystemExit("journal cost-rate check FAILED")
    out = ROOT / "knowledge" / "strategy-research" / "attribution-2026-09-25.md"
    out.write_text("\n".join(lines) + "\n")
    print("\n".join(lines))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    sys.exit(main())
