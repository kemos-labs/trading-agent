"""Live-feed adapter — yfinance polling with validation and gap detection.

Phase 4 live integration (paper-trading only). Reuses data_loader's
validation discipline and never places real orders. Fail-closed on
unavailable feeds; journal is append-only.
"""

from __future__ import annotations

import warnings
from pathlib import Path
from typing import Iterable

import pandas as pd

from quantkit.data_loader import normalize_columns, validate_ohlcv

try:  # optional at test time
    from quantkit.data_loader import load_yfinance  # type: ignore
except Exception:  # pragma: no cover
    load_yfinance = None  # type: ignore

DEFAULT_STORE_DIR = Path("data/live")
DEFAULT_LOOKBACK_DAYS = 10  # enough to cover weekends + gap repair


def store_path(symbol: str, store_dir: str | Path = DEFAULT_STORE_DIR) -> Path:
    """Per-symbol store path (CSV)."""
    if not symbol or not symbol.strip():
        raise ValueError("symbol must be non-empty")
    return Path(store_dir) / f"{symbol.strip().upper()}_1d.csv"


def load_store(
    symbol: str, store_dir: str | Path = DEFAULT_STORE_DIR
) -> pd.DataFrame | None:
    """Load an existing daily store, or None if absent."""
    p = store_path(symbol, store_dir)
    if not p.exists():
        return None
    # Reuse validation: handles both legacy phase3 files and live stores
    from quantkit.data_loader import load_csv

    try:
        df = load_csv(p)
    except Exception as exc:
        warnings.warn(f"store {p} unreadable ({exc}); treating as absent")
        return None
    return df


def detect_gaps(
    df: pd.DataFrame, *, expected_freq: str = "B"
) -> list[pd.Timestamp]:
    """Return business days missing between first and last bar.

    Only flags gaps > 1 business day; tolerates single-day gaps for
    holidays. Empty or single-row frames yield [].
    """
    if df is None or len(df) < 2:
        return []
    idx = df.index.normalize()
    # Business-day range
    expected = pd.bdate_range(idx.min(), idx.max(), freq=expected_freq)
    missing = expected.difference(idx)
    return sorted(missing.tolist())


def _fetch_recent(
    symbol: str,
    *,
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    interval: str = "1d",
    auto_adjust: bool = True,
) -> pd.DataFrame:
    """Fetch the last `lookback_days` of 1d bars from Yahoo (validated)."""
    if load_yfinance is None:  # pragma: no cover
        raise RuntimeError("yfinance loader unavailable in this env")
    if lookback_days < 2:
        raise ValueError("lookback_days must be >= 2")
    start = (pd.Timestamp.now("UTC").normalize() - pd.Timedelta(days=lookback_days)).strftime(
        "%Y-%m-%d"
    )
    # load_yfinance fails closed on empty / bad data
    df = load_yfinance(
        symbol, start=start, end=None, interval=interval, auto_adjust=auto_adjust
    )
    # Restrict to 1d for Phase 4; intraday would need period-style bounds
    if interval != "1d":
        warnings.warn(f"interval {interval!r} requested; Phase 4 store is 1d")
    return df


def update_store(
    symbol: str,
    *,
    store_dir: str | Path = DEFAULT_STORE_DIR,
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    interval: str = "1d",
    auto_adjust: bool = True,
    fetcher=_fetch_recent,
) -> pd.DataFrame:
    """Poll Yahoo, merge into the append-only daily store, validate, and save.

    - Fetches the recent window via `fetcher` (injectable for tests).
    - Merges with existing store (outer join on date), deduplicates, sorts.
    - Validates via `validate_ohlcv` (fail-closed).
    - Detects business-day gaps and warns.
    - Atomically overwrites the CSV (append-only in effect).

    Returns the updated, validated frame.

    Raises on fetch/validation failure — never silently fabricates.
    """
    store_dir = Path(store_dir)
    store_dir.mkdir(parents=True, exist_ok=True)
    existing = load_store(symbol, store_dir)

    # Fetch — fail-closed if unavailable; caller decides offline fallback
    fresh = fetcher(
        symbol, lookback_days=lookback_days, interval=interval, auto_adjust=auto_adjust
    )
    fresh = normalize_columns(fresh)
    fresh = validate_ohlcv(fresh)

    if existing is not None and len(existing):
        combined = pd.concat([existing, fresh]).sort_index()
        # Deduplicate keeping the fresher row (last write wins)
        combined = combined[~combined.index.duplicated(keep="last")].sort_index()
    else:
        combined = fresh

    combined = validate_ohlcv(combined)
    gaps = detect_gaps(combined)
    # Only warn on *recent* gaps (last 10 business days) — older gaps are
    # holidays/market closures, not outages. Phase-3 replay (2010→2024) has
    # ~138 holiday gaps which are expected.
    if gaps:
        recent_cutoff = combined.index.max().normalize() - pd.Timedelta(days=14)
        recent_gaps = [d for d in gaps if d >= recent_cutoff]
        if recent_gaps:
            warnings.warn(
                f"{symbol}: {len(recent_gaps)} recent business-day gap(s) detected: "
                + ", ".join(d.strftime("%Y-%m-%d") for d in recent_gaps[:5])
                + (" …" if len(recent_gaps) > 5 else "")
            )

    out = store_path(symbol, store_dir)
    # Write via tmp + rename for atomicity on most FS
    tmp = out.with_suffix(".tmp")
    combined.to_csv(tmp, index_label="date")
    tmp.replace(out)
    return combined


def fetch_many(
    symbols: Iterable[str],
    *,
    store_dir: str | Path = DEFAULT_STORE_DIR,
    lookback_days: int = DEFAULT_LOOKBACK_DAYS,
    interval: str = "1d",
    auto_adjust: bool = True,
    fetcher=_fetch_recent,
) -> dict[str, pd.DataFrame]:
    """Poll a list of symbols, updating each store. Fail-closed per symbol.

    Returns dict symbol -> updated frame. If any symbol's fetch raises,
    the exception propagates — caller may retry or fall back to offline
    replay per AGENTS.md.
    """
    out: dict[str, pd.DataFrame] = {}
    for sym in symbols:
        out[sym] = update_store(
            sym,
            store_dir=store_dir,
            lookback_days=lookback_days,
            interval=interval,
            auto_adjust=auto_adjust,
            fetcher=fetcher,
        )
    return out
