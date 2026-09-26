#!/usr/bin/env python
"""Generate dashboard/data/dashboard.json — the single source the UI renders.

Everything the dashboard shows is computed here from real stores on disk:
Phase 3 verdicts + curves, the fresh API pulls, the paper book/journal,
attribution, provider budget usage and test status. No hand-typed numbers.

    PYTHONPATH=src .venv/bin/python research/build_dashboard_data.py
"""

from __future__ import annotations

import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from quantkit.backtest import vectorized_backtest
from quantkit.data_loader import compute_returns
from quantkit.fresh import ALPHAVANTAGE_FREE_DAILY, FINNHUB_SOFT_DAILY, MASSIVE_FREE_DAILY
from quantkit.strategies import (
    donchian_breakout_position,
    dual_sma_position,
    vol_targeted_momentum_position,
)

ROOT = Path(__file__).resolve().parents[1]
P3 = ROOT / "data" / "research" / "phase3"
FRESH = ROOT / "data" / "research" / "fresh"
PAPER = ROOT / "data" / "paper"
OUT = ROOT / "dashboard" / "data" / "dashboard.json"
SYMBOLS = ("SPY", "QQQ", "TLT")
PTC = 0.001
FRESH_OOS = "2025-01-01"
P3_OOS = "2019-01-01"
STRAT_NOTES = {
    "dual_sma_9_45": "Long when the 9-day SMA is above the 45-day SMA. Classic trend filter.",
    "donchian_50_20": "Enter on a 50-day high, exit on a 20-day low. Classic breakout.",
    "vol_mom_252_60_10pct": "Long when 252-day return > 0, sized to 10% vol target (cap 1.5x).",
}
CAPS = {"massive": MASSIVE_FREE_DAILY, "finnhub": FINNHUB_SOFT_DAILY, "alphavantage": ALPHAVANTAGE_FREE_DAILY}
PROVIDER_LABEL = {
    "massive": "Massive (Polygon) — daily OHLCV, adjusted, 15-min delayed on free tier",
    "finnhub": "Finnhub — last-print quote only (free tier has no candles)",
    "alphavantage": "Alpha Vantage — TIME_SERIES_DAILY fallback (25/day budget)",
}


def sha12(path: Path) -> str:
    import hashlib
    return hashlib.sha256(path.read_bytes()).hexdigest()[:6]


def rv20(close: pd.Series) -> float:
    r = np.log(close / close.shift(1)).dropna()
    return float(r.tail(20).std(ddof=1) * np.sqrt(252))


def test_status() -> dict:
    env = {"PATH": "/usr/bin:/bin", "PYTHONPATH": "src"}
    out = subprocess.run(
        [str(ROOT / ".venv/bin/python"), "-m", "unittest", "discover", "-s", "tests"],
        cwd=ROOT, capture_output=True, text=True, env={**env, "HOME": "/home/kalde"},
    )
    m = re.search(r"Ran (\d+) tests", out.stderr + out.stdout)
    return {"ran": int(m.group(1)) if m else 0, "ok": out.returncode == 0}


def data_health() -> list[dict]:
    rows = []
    for sym in SYMBOLS:
        base = P3 / f"ohlcv_{sym}.csv"
        fresh = FRESH / f"ohlcv_{sym}.csv"
        entry = {"symbol": sym}
        if base.exists():
            b = pd.read_csv(base, parse_dates=["date"]).set_index("date")
            entry |= {"base_bars": len(b), "base_start": str(b.index[0].date()),
                      "base_end": str(b.index[-1].date()), "base_sha": sha12(base),
                      "base_close": float(b["close"].iloc[-1])}
        if fresh.exists():
            f = pd.read_csv(fresh, parse_dates=["date"]).set_index("date")
            entry |= {"fresh_bars": len(f), "fresh_start": str(f.index[0].date()),
                      "fresh_end": str(f.index[-1].date()),
                      "latest_close": round(float(f["close"].iloc[-1]), 2),
                      "chg_1d_pct": round(float(f["close"].pct_change().iloc[-1]) * 100, 2),
                      "rv20_pct": round(rv20(f["close"]) * 100, 1),
                      "spark": [round(float(x), 2) for x in f["close"].tail(60)],
                      "provider": "massive"}
        rows.append(entry)
    return rows


def leg_stats() -> tuple[list[dict], dict]:
    legs, curves = [], {}
    for name in ("dual_sma_9_45", "donchian_50_20", "vol_mom_252_60_10pct", "buy_hold"):
        series = {}
        for sym in SYMBOLS:
            p = P3 / f"backtest_{name}_{sym}.csv"
            if p.exists():
                s = pd.read_csv(p, parse_dates=["date"])
                series[sym] = s.set_index(s["date"].dt.normalize())["net"]
            elif name == "buy_hold":
                # buy & hold legs are not persisted by run_phase3 — rebuild them
                # from the same pinned OHLCV with identical cost model.
                o = pd.read_csv(P3 / f"ohlcv_{sym}.csv", parse_dates=["date"])
                o.index = o["date"].dt.normalize()
                rets = compute_returns(o["close"], log=False)
                bt = vectorized_backtest(rets, pd.Series(1.0, index=o.index), ptc=PTC, ffc=0.0)
                series[sym] = bt["net"]
                legs.append({
                    "leg": f"{name} {sym}", "strategy": name, "symbol": sym,
                    "gross": round(float(bt["gross"].fillna(0).sum()), 4),
                    "costs": round(float(bt["costs"].fillna(0).sum()), 4),
                    "net": round(float(bt["net"].fillna(0).sum()), 4),
                    "cost_share": round(float(bt["costs"].sum() / max(bt["gross"].sum(), 1e-9)), 3),
                    "turnover": round(float(bt["exposure"].diff().abs().fillna(0).mean()), 4),
                    "skew": round(float(bt["net"].fillna(0).skew()), 3),
                    "thin": bool(bt["costs"].sum() / max(bt["gross"].sum(), 1e-9) > 0.15),
                })
        if series:
            port = pd.concat(series, axis=1).mean(axis=1).dropna()
            # OOS window only, compounded to growth-of-one equity
            oos = port.loc[port.index >= pd.Timestamp(P3_OOS)]
            if oos.empty:
                oos = port
            curves[name] = (1.0 + oos).cumprod()
            for sym in SYMBOLS:
                p = P3 / f"backtest_{name}_{sym}.csv"
                if not p.exists():
                    continue
                s = pd.read_csv(p, parse_dates=["date"])
                gross, costs = float(s["gross"].fillna(0).sum()), float(s["costs"].fillna(0).sum())
                share = costs / gross if gross > 0 else float("nan")
                legs.append({
                    "leg": f"{name} {sym}", "strategy": name, "symbol": sym,
                    "gross": round(gross, 4), "costs": round(costs, 4),
                    "net": round(gross - costs, 4), "cost_share": round(share, 3),
                    "turnover": round(float(s["exposure"].diff().abs().fillna(0).mean()), 4),
                    "skew": round(float(s["net"].fillna(0).skew()), 3),
                    "thin": bool(share > 0.15),
                })
    return legs, curves


def fresh_extension() -> dict:
    """Splice base+fresh on shared dates, rerun the frozen rules, score 2025+."""
    frames = {}
    for sym in SYMBOLS:
        bp, fp = P3 / f"ohlcv_{sym}.csv", FRESH / f"ohlcv_{sym}.csv"
        if not (bp.exists() and fp.exists()):
            return {"available": False}
        b = pd.read_csv(bp, parse_dates=["date"])
        b.index = b["date"].dt.normalize()
        b = b.drop(columns=["date"])
        f = pd.read_csv(fp, parse_dates=["date"])
        f.index = f["date"].dt.normalize()
        f = f.drop(columns=["date"])
        shared = b.index.intersection(f.index)
        ratio = float((f.loc[shared, "close"] / b.loc[shared, "close"]).median())
        seam = b.loc[b.index < f.index[0]] * ratio
        frames[sym] = pd.concat([seam, f]).sort_index()
        frames[sym] = frames[sym][~frames[sym].index.duplicated(keep="last")]
    idx = frames[SYMBOLS[0]].index
    for sym in SYMBOLS[1:]:
        idx = idx.intersection(frames[sym].index)
    rules = {
        "dual_sma_9_45": lambda c, r: dual_sma_position(c, fast=9, slow=45),
        "donchian_50_20": lambda c, r: donchian_breakout_position(c, entry_window=50, exit_window=20),
        "vol_mom_252_60_10pct": lambda c, r: vol_targeted_momentum_position(
            c, r, momentum_lookback=252, vol_lookback=60, target_vol=0.10, max_weight=1.5),
        "buy_hold": lambda c, r: pd.Series(1.0, index=c.index),
    }
    rows = []
    for name, fn in rules.items():
        nets = {}
        for sym in SYMBOLS:
            close = frames[sym].loc[idx, "close"]
            rets = compute_returns(close, log=False)
            nets[sym] = vectorized_backtest(rets, fn(close, rets), ptc=PTC, ffc=0.0)["net"]
        port = pd.concat(nets, axis=1).mean(axis=1)
        oos = port.loc[FRESH_OOS:]
        if oos.empty:
            continue
        ann = float((1 + oos).prod() ** (252 / len(oos)) - 1)
        vol = float(oos.std(ddof=1) * np.sqrt(252))
        rows.append({
            "strategy": name, "bars": int(len(oos)),
            "total_pct": round(float((1 + oos).prod() - 1) * 100, 2),
            "cagr_pct": round(ann * 100, 2),
            "sharpe": round(ann / vol, 2) if vol else 0.0,
            "max_dd_pct": round(float(((1 + oos) / (1 + oos).cummax() - 1).min()) * 100, 2),
        })
    return {"available": True, "start": FRESH_OOS, "end": str(idx[-1].date()),
            "rows": sorted(rows, key=lambda r: r["sharpe"], reverse=True)}


def paper_book() -> dict:
    j = pd.read_csv(PAPER / "journal.csv")
    state = json.loads((PAPER / "state.json").read_text())
    nz = j[j["delta"].abs() > 0]
    unit = float((nz["cost"] / nz["delta"].abs()).median()) if len(nz) else float("nan")
    pos = [{"symbol": p["symbol"], "strategy": p["strategy"], "target": round(p["target"], 3),
            "exposure": round(p["exposure"], 3), "entry": p["entry_price"],
            "entry_date": p.get("bar_date")}
           for p in state["positions"].values()]
    peak = float(j["peak"].max())
    equity = float(j["equity"].iloc[-1])
    return {
        "bar_date": str(j["bar_date"].iloc[-1]), "equity": round(equity, 2), "peak": round(peak, 2),
        "drawdown_pct": round((equity / peak - 1) * 100, 3),
        "total_cost": round(float(j["cost"].sum()), 2), "rows": int(len(j)),
        "unit_cost": round(unit, 2), "cost_model_bps": int(state.get("ptc", PTC) * 1e4),
        "guard_ok": bool(j["note"].str.contains("paper_only").all()),
        "halted": bool(state.get("halted", False)),
        "positions": sorted(pos, key=lambda p: (-p["exposure"], p["symbol"])),
    }


def quota() -> list[dict]:
    path = ROOT / "data" / "fresh" / "quota.json"
    used = {}
    if path.exists():
        today = dt.date.today().isoformat()
        for prov, days in json.loads(path.read_text()).get("daily", {}).items():
            used[prov] = int(days.get(today, 0))
    return [{"provider": p, "used": used.get(p, 0), "cap": CAPS[p],
             "remaining": max(0, CAPS[p] - used.get(p, 0)), "label": PROVIDER_LABEL[p]}
            for p in ("massive", "finnhub", "alphavantage")]


def main() -> None:
    summary = json.loads((P3 / "summary.json").read_text())
    legs, curves = leg_stats()
    step = max(1, len(next(iter(curves.values()))) // 500)
    curve_json = {k: [[str(d.date()), round(float(v), 4)] for d, v in s.iloc[::step].items()]
                  for k, s in curves.items()}
    lab = []
    for name, s in summary["portfolio_oos"].items():
        lab.append({
            "strategy": name, "verdict": summary["verdicts"].get(name, "BASELINE"),
            "total_pct": round(s["total_return"] * 100, 2), "cagr_pct": round(s["cagr"] * 100, 2),
            "sharpe": round(s["sharpe"], 2), "max_dd_pct": round(s["max_drawdown"] * 100, 2),
            "vol_pct": round(s["ann_vol"] * 100, 2), "dd_days": int(s["dd_duration"]),
            "mar": round(s["mar"], 2), "note": STRAT_NOTES.get(name, "Equal-weight buy & hold baseline."),
        })
    bh = summary["buy_hold_oos"]
    lab.append({"strategy": "buy_hold", "verdict": "BASELINE",
                "total_pct": round(bh["total_return"] * 100, 2), "cagr_pct": round(bh["cagr"] * 100, 2),
                "sharpe": round(bh["sharpe"], 2), "max_dd_pct": round(bh["max_drawdown"] * 100, 2),
                "vol_pct": round(bh["ann_vol"] * 100, 2), "dd_days": int(bh["dd_duration"]),
                "mar": round(bh["mar"], 2), "note": "Equal-weight buy & hold. The bar every strategy must beat."})
    tests = test_status()
    payload = {
        "generated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
        "protocol": summary["protocol"], "lab": lab, "curves": curve_json,
        "attribution": sorted(legs, key=lambda r: -r["cost_share"]),
        "extension": fresh_extension(), "data_health": data_health(), "paper": paper_book(),
        "quota": quota(), "tests": tests,
        "costs": {"ptc_bps": int(summary["protocol"]["ptc"] * 1e4),
                  "lag": "signal decided at close, executed next bar"},
        "pass_rule": "PASS = positive total return AND Sharpe above the equal-weight buy & hold AND a shallower max drawdown AND positive in at least 2 of 3 ETFs.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    print(f"wrote {OUT} ({OUT.stat().st_size // 1024} KB)")
    print(f"  tests {tests['ran']} ok={tests['ok']} | curves {len(curve_json)} | legs {len(legs)} "
          f"| extension {'ok' if payload['extension']['available'] else 'missing'} "
          f"| paper equity {payload['paper']['equity']:,.0f} | quota "
          + ", ".join(f"{q['provider']}={q['used']}/{q['cap']}" for q in payload["quota"]))


if __name__ == "__main__":
    main()
