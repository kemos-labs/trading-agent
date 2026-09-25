"""Fresh market-data pulls for backtesting — data refresh layer.

Reference patterns: trading-terminal-pro ``api/deskFeeds.js``
(budget-gated fetches), ``api/upstreamCache.js`` (TTL + quota ledger),
``api/providerCircuitBreaker.js`` (fail-closed, never synthetic).

Rules (terminal + repo data-integrity, combined):
- Keys are server-side only: loaded at runtime from ``TERMINAL_ENV``
  (default ``/home/kalde/trading-terminal-pro/.env``). NEVER commit keys,
  NEVER print them, NEVER synthesize bars on failure — raise instead.
- Provider chain for daily OHLCV: Massive aggs → Alpha Vantage daily
  (tight budget) → yfinance (existing ``live.load_yfinance``).
  Finnhub free has no candle access — quote endpoint is used only as a
  last-print staleness check.
- Every upstream call is quota-ledgered (``data/fresh/quota.json``) with
  per-provider daily caps × headroom, file-cached by (provider, symbol,
  window) with TTL, and self-throttled (Massive 5/min → 13 s spacing).

Traceability: skill ``skills/fresh-data/SKILL.md``.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import time
import urllib.parse
import urllib.request
from pathlib import Path

import numpy as np
import pandas as pd

__all__ = [
    "ALPHAVANTAGE_FREE_DAILY",
    "FINNHUB_SOFT_DAILY",
    "MASSIVE_FREE_DAILY",
    "QuotaLedger",
    "fetch_alphavantage_daily",
    "fetch_finnhub_quote",
    "fetch_massive_aggs",
    "load_terminal_keys",
    "normalize_massive",
    "pull_symbol",
]

MASSIVE_FREE_DAILY = 200
MASSIVE_SPACING_S = 13.0
FINNHUB_SOFT_DAILY = 1000
ALPHAVANTAGE_FREE_DAILY = 25
HEADROOM = 0.85
DEFAULT_ENV = "/home/kalde/trading-terminal-pro/.env"
MASSIVE_BASE = "https://api.massive.com"
FINNHUB_BASE = "https://finnhub.io/api/v1"
AV_BASE = "https://www.alphavantage.co/query"


def load_terminal_keys(env_path: str | None = None) -> dict:
    """Parse KEY=VALUE lines from the terminal .env (no import, no exec).

    Raises FileNotFoundError / ValueError (fail closed) when absent.
    """
    path = env_path or os.environ.get("TERMINAL_ENV", DEFAULT_ENV)
    try:
        text = Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        raise FileNotFoundError(f"terminal env not readable: {path}: {exc}")
    keys: dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        keys[k.strip()] = v.strip().strip("\"'")
    if not keys:
        raise ValueError(f"no keys parsed from {path}")
    return keys


class QuotaLedger:
    """Daily per-provider call ledger (terminal quota-ledger.json pattern)."""

    def __init__(self, path: str | Path = "data/fresh/quota.json"):
        self.path = Path(path)
        self.state: dict = {"version": 1, "daily": {}}
        if self.path.exists():
            try:
                self.state = json.loads(self.path.read_text(encoding="utf-8"))
            except (OSError, ValueError):
                self.state = {"version": 1, "daily": {}}

    def _today(self) -> str:
        return dt.date.today().isoformat()

    def used(self, provider: str) -> int:
        return int(self.state.get("daily", {}).get(provider, {}).get(self._today(), 0))

    def allows(self, provider: str, cap: int, headroom: float = HEADROOM) -> bool:
        return self.used(provider) < int(cap * headroom)

    def record(self, provider: str, n: int = 1) -> None:
        day = self._today()
        self.state.setdefault("daily", {}).setdefault(provider, {})
        self.state["daily"][provider][day] = self.used(provider) + n
        self.state["updatedAt"] = dt.datetime.now(dt.timezone.utc).isoformat()
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(self.state, indent=1), encoding="utf-8")


def _http_get_json(url: str, timeout: int = 25) -> dict | list:
    # Explicit UA: provider edges (Massive/Cloudflare) 401 the stock
    # python-urllib agent while curl succeeds.
    req = urllib.request.Request(url, headers={
        "Accept": "application/json",
        "User-Agent": "quantkit-fresh/0.7 (research backtest data; contact: repo owner)",
    })
    with urllib.request.urlopen(req, timeout=timeout) as res:
        return json.loads(res.read().decode("utf-8"))


def _cache_path(cache_dir: Path, name: str) -> Path:
    safe = "".join(c if c.isalnum() or c in "-_." else "_" for c in name)
    return cache_dir / f"{safe}.json"


def _cache_fresh(path: Path, ttl_h: float) -> bool:
    if not path.exists():
        return False
    age_h = (time.time() - path.stat().st_mtime) / 3600
    return age_h < ttl_h


def normalize_massive(payload: dict) -> pd.DataFrame:
    """Massive/Polygon aggs → canonical date-indexed OHLCV (adjusted)."""
    # Free tier answers status DELAYED (15-min delayed, fine for EOD research).
    if not isinstance(payload, dict) or (payload.get("status") not in (None, "OK", "DELAYED")):
        raise ValueError(f"bad massive payload: {str(payload)[:120]}")
    results = payload.get("results", [])
    if not results:
        raise ValueError("massive returned zero bars (fail closed)")
    rows = []
    for r in results:
        try:
            day = dt.datetime.fromtimestamp(r["t"] / 1000, tz=dt.timezone.utc).date().isoformat()
            rows.append((day, float(r["o"]), float(r["h"]), float(r["l"]), float(r["c"]), float(r["v"])))
        except (KeyError, TypeError, ValueError) as exc:
            raise ValueError(f"malformed massive bar: {exc}")
    df = pd.DataFrame(rows, columns=["date", "open", "high", "low", "close", "volume"])
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values("date").set_index("date")


def fetch_massive_aggs(
    symbol: str,
    start: str,
    end: str,
    keys: dict,
    ledger: QuotaLedger,
    cache_dir: str | Path = "data/fresh/raw",
    ttl_h: float = 12.0,
    http_get=_http_get_json,
    sleep=time.sleep,
) -> pd.DataFrame:
    """Daily adjusted bars via Massive/Polygon range aggs (5/min self-throttle)."""
    key = keys.get("MASSIVE_API_KEY") or keys.get("POLYGON_API_KEY")
    if not key:
        raise ValueError("MASSIVE_API_KEY not configured")
    if not ledger.allows("massive", MASSIVE_FREE_DAILY):
        raise ValueError(f"massive budget exhausted ({ledger.used('massive')}/{MASSIVE_FREE_DAILY})")
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    cp = _cache_path(cache_dir, f"massive_{symbol}_{start}_{end}")
    if _cache_fresh(cp, ttl_h):
        payload = json.loads(cp.read_text(encoding="utf-8"))
    else:
        q = urllib.parse.urlencode({"adjusted": "true", "sort": "asc",
                                      "limit": 50000, "apiKey": key})
        url = f"{MASSIVE_BASE}/v2/aggs/ticker/{symbol}/range/1/day/{start}/{end}?{q}"
        payload = http_get(url)
        ledger.record("massive", 1)
        cp.write_text(json.dumps(payload), encoding="utf-8")
        sleep(MASSIVE_SPACING_S)
    return normalize_massive(payload)


def fetch_finnhub_quote(symbol: str, keys: dict, ledger: QuotaLedger, http_get=_http_get_json) -> dict:
    """Last print via Finnhub /quote — staleness check only (no candle access on free tier)."""
    key = keys.get("FINNHUB_API_KEY")
    if not key:
        raise ValueError("FINNHUB_API_KEY not configured")
    if not ledger.allows("finnhub", FINNHUB_SOFT_DAILY):
        raise ValueError("finnhub budget exhausted")
    url = f"{FINNHUB_BASE}/quote?symbol={urllib.parse.quote(symbol)}&token={key}"
    q = http_get(url)
    ledger.record("finnhub", 1)
    if not isinstance(q, dict) or not (q.get("c") or 0) > 0:
        raise ValueError(f"bad finnhub quote for {symbol} (fail closed)")
    return {"symbol": symbol, "last": float(q["c"]), "prev_close": float(q.get("pc", 0.0)),
            "time": int(q.get("t", 0)), "source": "finnhub"}


def fetch_alphavantage_daily(
    symbol: str,
    keys: dict,
    ledger: QuotaLedger,
    cache_dir: str | Path = "data/fresh/raw",
    ttl_h: float = 6.0,
    http_get=_http_get_json,
) -> pd.DataFrame:
    """TIME_SERIES_DAILY compact (last 100 bars) — tight 25/day budget, fallback only."""
    key = keys.get("ALPHA_VANTAGE_API_KEY")
    if not key:
        raise ValueError("ALPHA_VANTAGE_API_KEY not configured")
    if not ledger.allows("alphavantage", ALPHAVANTAGE_FREE_DAILY):
        raise ValueError(f"alphavantage budget exhausted ({ledger.used('alphavantage')}/{ALPHAVANTAGE_FREE_DAILY})")
    cache_dir = Path(cache_dir)
    cache_dir.mkdir(parents=True, exist_ok=True)
    cp = _cache_path(cache_dir, f"av_{symbol}_compact")
    if _cache_fresh(cp, ttl_h):
        payload = json.loads(cp.read_text(encoding="utf-8"))
    else:
        params = urllib.parse.urlencode({"function": "TIME_SERIES_DAILY", "symbol": symbol,
                                         "outputsize": "compact", "apikey": key})
        payload = http_get(f"{AV_BASE}?{params}")
        ledger.record("alphavantage", 1)
        if isinstance(payload, dict) and (payload.get("Note") or payload.get("Information")):
            raise ValueError("alphavantage rate-limited")
        cp.write_text(json.dumps(payload), encoding="utf-8")
    series = (payload.get("Time Series (Daily)") or {}) if isinstance(payload, dict) else {}
    if not series:
        raise ValueError(f"no alphavantage bars for {symbol} (fail closed)")
    rows = [(d, float(v["1. open"]), float(v["2. high"]), float(v["3. low"]),
             float(v["4. close"]), float(v["5. volume"])) for d, v in series.items()]
    df = pd.DataFrame(rows, columns=["date", "open", "high", "low", "close", "volume"])
    df["date"] = pd.to_datetime(df["date"])
    return df.sort_values("date").set_index("date")


def pull_symbol(
    symbol: str,
    start: str,
    end: str,
    keys: dict,
    ledger: QuotaLedger,
    cache_dir: str | Path = "data/fresh/raw",
    ttl_h: float = 12.0,
) -> tuple[pd.DataFrame, str]:
    """Provider chain: massive → alphavantage → fail-closed (never synthetic).

    yfinance remains available via ``live.load_yfinance`` as a caller-side
    fallback (kept out of this chain so API budgets are spent first).
    Returns (bars, provider_name).
    """
    errors = []
    for name, fn in [("massive", lambda: fetch_massive_aggs(symbol, start, end, keys, ledger, cache_dir, ttl_h)),
                     ("alphavantage", lambda: fetch_alphavantage_daily(symbol, keys, ledger, cache_dir))]:
        try:
            return fn(), name
        except Exception as exc:  # noqa: BLE001 — chain must continue, errors reported
            errors.append(f"{name}: {exc}")
    raise ValueError(f"all fresh providers failed for {symbol}: {'; '.join(errors)}")
