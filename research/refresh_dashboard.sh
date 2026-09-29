#!/usr/bin/env bash
# Refresh the dashboard end-to-end (Phase 7 maintenance loop).
#
#   research/refresh_dashboard.sh [--no-pull] [--start YYYY-MM-DD] [--end YYYY-MM-DD]
#
# Steps:
#   1. Pull fresh bars via research/pull_fresh.py (SKIPPED when TERMINAL_ENV
#      is unset or --no-pull is passed — the TTL file cache in data/fresh/raw
#      makes repeats free, and the dashboard rebuilds from staged CSVs).
#   2. Rebuild dashboard/data/dashboard.json via research/build_dashboard_data.py
#      (runs the full unittest suite at build time; fails closed on bad data).
#   3. Print a one-line verification summary (tests, equity, quota).
#
# Cron (weekdays after US close, UTC):
#   30 22 * * 1-5  cd /home/kalde/trading-agent && research/refresh_dashboard.sh >> /tmp/refresh-dashboard.log 2>&1
#
# Manual offline rebuild (no provider calls):
#   research/refresh_dashboard.sh --no-pull
set -euo pipefail
cd "$(dirname "$0")/.."

PULL=auto
START="2024-12-01"
END="$(date +%F)"
for arg in "$@"; do
  case "$arg" in
    --no-pull) PULL=skip ;;
    --pull) PULL=force ;;
    --start=*) START="${arg#--start=}" ;;
    --end=*) END="${arg#--end=}" ;;
    --start|--end) echo "usage: $0 [--no-pull] [--pull] [--start=YYYY-MM-DD] [--end=YYYY-MM-DD]" >&2; exit 2 ;;
    *) echo "unknown flag: $arg" >&2; exit 2 ;;
  esac
done

if [ "$PULL" = "skip" ]; then
  echo "[refresh] --no-pull: skipping provider pull, rebuilding from staged CSVs."
elif [ -z "${TERMINAL_ENV:-}" ]; then
  echo "[refresh] TERMINAL_ENV unset: skipping provider pull (fail-closed, no synthetic data)."
  echo "[refresh] To pull: export TERMINAL_ENV=<path> or pass --pull with keys configured."
  if [ "$PULL" = "force" ]; then
    echo "[refresh] --pull forced without keys — aborting instead of fabricating data." >&2
    exit 2
  fi
else
  echo "[refresh] pulling SPY/QQQ/TLT $START -> $END ..."
  PYTHONPATH=src .venv/bin/python research/pull_fresh.py --start "$START" --end "$END"
fi

echo "[refresh] rebuilding dashboard JSON (runs test suite) ..."
PYTHONPATH=src .venv/bin/python research/build_dashboard_data.py

.venv/bin/python - <<'EOF'
import json
d = json.load(open("dashboard/data/dashboard.json"))
assert d["tests"]["ok"], "test suite failed during dashboard build"
print(f"[verify] tests {d['tests']['ran']} OK | paper equity {d['paper']['equity']:,.0f} "
      f"({d['paper']['bar_date']}) | guard_ok={d['paper']['guard_ok']} | halted={d['paper']['halted']}")
print("[verify] quota " + ", ".join(f"{q['provider']}={q['used']}/{q['cap']}" for q in d["quota"]))
print(f"[verify] data through {d['data_health'][0]['fresh_end']} | generated {d['generated_at']}")
EOF
echo "[refresh] done."
