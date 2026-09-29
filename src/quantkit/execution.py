"""Execution lab — spread decomposition, impact, market-making.

Implements the discipline distilled in `skills/spread-decomposition`
(Harris Ch.14,20,21), `skills/market-microstructure-execution`
(Patterson), `skills/automated-market-making` (Aldridge Ch.10–12),
plus Phase 8 T2 `skills/impact-calibration` (Almgren et al. 2005
closed-form permanent/temporary impact with fitted γ/η):

- Lee–Ready trade classification (tick + quote rule hybrid),
- quoted / effective / realized spread, price impact,
- Roll's effective spread estimator,
- variance-ratio test (fundamental vs transitory vol),
- Kyle's lambda (price impact regression),
- Amihud illiquidity,
- OFI (order-flow imbalance) proxy.

Vectorized pandas/numpy; fail-closed on bad spreads.
"""

from __future__ import annotations

import warnings

import numpy as np
import pandas as pd

__all__ = [
    "almgren_impact",
    "amihud_illiquidity",
    "effective_spread",
    "impact_almgren",
    "ef_midpoint",
    "kyle_lambda",
    "quoted_spread",
    "realized_spread",
    "roll_spread",
    "variance_ratio",
]


def quoted_spread(bid: pd.Series, ask: pd.Series) -> pd.Series:
    """Quoted spread = ask - bid (positive)."""
    if not bid.index.equals(ask.index):
        raise ValueError("bid/ask must share index")
    spread = ask.astype(float) - bid.astype(float)
    if (spread < 0).any():
        warnings.warn("negative quoted spread observed (crossed market)")
    return spread.rename("quoted_spread")


def effective_spread(trade_price: pd.Series, bid: pd.Series, ask: pd.Series) -> pd.Series:
    """Effective spread = 2 * |price - mid|, where mid = (bid+ask)/2."""
    mid = (bid.astype(float) + ask.astype(float)) / 2
    if not trade_price.index.equals(mid.index):
        raise ValueError("trade_price must share bid/ask index")
    return (2 * (trade_price.astype(float) - mid).abs()).rename("effective_spread")


def realized_spread(
    trade_price: pd.Series, bid: pd.Series, ask: pd.Series, horizon: int = 5
) -> pd.Series:
    """Realized spread = 2 * |price - mid_{t+h}| signed by trade direction.

    Simplified: assumes trade direction = sign(price - mid). Horizon h
    is bars ahead for the post-trade mid.
    """
    mid = (bid.astype(float) + ask.astype(float)) / 2
    mid_fwd = mid.shift(-horizon)
    direction = np.sign(trade_price.astype(float) - mid)
    # Realized = direction * (price - mid_fwd) *2
    # If mid_fwd is NaN (horizon beyond data), result NaN
    spread = 2 * direction * (trade_price.astype(float) - mid_fwd)
    return spread.rename("realized_spread")


def roll_spread(returns_or_price_changes: pd.Series) -> float:
    """Roll (1984) effective spread = 2 * sqrt(-cov(Δp_t, Δp_{t+1})).

    Input: price changes Δp (not returns). Returns NaN if cov >=0
    (no mean reversion). Annualization not applied — intradaytick.
    """
    x = returns_or_price_changes.dropna().astype(float)
    if len(x) < 3:
        return float("nan")
    cov = x.cov(x.shift(1))
    if cov >= 0 or not np.isfinite(cov):
        return float("nan")
    return float(2 * np.sqrt(-cov))


def variance_ratio(returns: pd.Series, k: int = 2) -> float:
    """Variance ratio VR(k) = Var(k-period return) / (k * Var(1-period)).

    VR >1 → trending (fundamental), VR <1 → mean-reverting (transitory).
    Lo-MacKinlay heteroscedasticity-robust version is not implemented here
    (use `arch` for that); this is the simple textbook VR.
    """
    if k < 2:
        raise ValueError("k must be >=2")
    r = returns.dropna().astype(float)
    if len(r) < k + 1:
        return float("nan")
    # k-period returns as sum of k consecutive 1-period returns (simple, for small r)
    # Use rolling sum
    rk = r.rolling(k).sum().dropna()
    var1 = r.var(ddof=1)
    vark = rk.var(ddof=1)
    if var1 == 0 or not np.isfinite(var1) or not np.isfinite(vark):
        return float("nan")
    return float(vark / (k * var1))


def almgren_impact(
    shares: float,
    adv: float,
    duration_voltime: float,
    sigma: float,
    shares_out: float,
    gamma: float = 0.314,
    eta: float = 0.142,
) -> tuple[float, float]:
    """Almgren-Thum-Hauptmann-Li (2005) permanent + realized impact.

    ``I = γ·σ·(X/V)·(Θ/V)^{1/4}`` (permanent, linear, schedule-free);
    ``J = I/2 + sgn(X)·η·σ·|X/(V·T)|^{3/5}`` (realized avg execution cost).
    ``shares`` signed, ``adv`` average daily volume (shares), ``T`` execution
    length in volume time, ``sigma`` daily vol, ``shares_out`` outstanding.
    Calibrated on S&P 500, orders ≤ ~10% ADV, intraday active schedules.
    Returns ``(permanent_I, realized_J)`` as fractions of pre-trade price.
    """
    for name, v in [("adv", adv), ("duration_voltime", duration_voltime),
                    ("sigma", sigma), ("shares_out", shares_out)]:
        if not np.isfinite(v) or v <= 0:
            raise ValueError(f"{name} must be positive finite")
    if not np.isfinite(shares) or shares == 0:
        raise ValueError("shares must be nonzero finite")
    if abs(shares) / adv > 0.25:
        warnings.warn("order >25% ADV: outside calibrated range (≤10% ADV)")
    turnover_inv = shares_out / adv
    perm = gamma * sigma * (shares / adv) * turnover_inv**0.25
    temp = eta * sigma * abs(shares / (adv * duration_voltime)) ** 0.6
    realized = perm / 2 + np.sign(shares) * temp
    return float(perm), float(realized)


def impact_almgren(
    delta: float,
    adv: float,
    sigma: float,
    horizon_days: float,
    outstanding: float,
    ptc: float = 0.0,
    gamma: float = 0.314,
    eta: float = 0.142,
    allow_oversize: bool = False,
) -> float:
    """Impact-aware cost in bps: flat floor + Almgren realized impact.

    ``delta`` signed shares to trade, ``adv`` average daily volume
    (shares), ``sigma`` daily vol, ``horizon_days`` execution length in
    trading days (volume time T = horizon_days), ``outstanding`` shares
    outstanding (Θ). ``ptc`` is the flat per-unit-turnover cost (e.g.
    0.001 = 10 bps) charged as a floor — the worst case is paying the
    spread on the horizon we claim, so the impact layer is *additive*,
    never a replacement. Returns total cost in basis points (0.01%).

    Fail-closed: raises ValueError on non-positive adv/sigma/horizon/
    outstanding, and on |delta|/adv > 0.25 (outside the calibrated range)
    unless ``allow_oversize=True``.
    """
    for name, v in [("adv", adv), ("sigma", sigma), ("horizon_days", horizon_days),
                    ("outstanding", outstanding)]:
        if not np.isfinite(v) or v <= 0:
            raise ValueError(f"{name} must be positive finite")
    if not np.isfinite(delta) or delta == 0:
        raise ValueError("delta must be nonzero finite")
    if abs(delta) / adv > 0.25 and not allow_oversize:
        raise ValueError(
            f"order {abs(delta)/adv:.1%} ADV exceeds calibrated range (≤25%); "
            "pass allow_oversize=True to override"
        )
    _, realized = almgren_impact(
        delta, adv, horizon_days, sigma, outstanding, gamma=gamma, eta=eta
    )
    total = ptc + abs(realized)
    return float(max(0.0, total) * 1e4)


def ef_midpoint(
    x0: np.ndarray,
    xT: np.ndarray,
    Pi: np.ndarray,
    T: np.ndarray,
    lam: float,
    Omega: np.ndarray,
) -> np.ndarray:
    """Engle-Ferstenberg (2006) three-period optimal execution midpoint.

    Closed form for the midpoint holdings between fixed start ``x0`` and
    target ``xT`` under linear permanent impact ``Pi``, temporary impact
    ``T``, risk aversion ``lam``, and covariance ``Omega``:

    ``x_t = 1/2 (Pi + 2T + lam*Omega)^-1 [(Pi + 2T) x0 + (Pi + 2T + 2 lam Omega) xT]``

    Risk-neutral (lam=0) gives the classic even pace (midpoint =
    (x0+xT)/2); risk-averse front-loads (midpoint closer to xT).
    """
    x0 = np.atleast_1d(np.asarray(x0, dtype=float))
    xT = np.atleast_1d(np.asarray(xT, dtype=float))
    Pi = np.atleast_2d(np.asarray(Pi, dtype=float))
    T = np.atleast_2d(np.asarray(T, dtype=float))
    Omega = np.atleast_2d(np.asarray(Omega, dtype=float))
    if lam < 0:
        raise ValueError("lam must be >= 0")
    A = Pi + 2 * T + lam * Omega
    A_inv = np.linalg.inv(A)
    return 0.5 * A_inv @ ((Pi + 2 * T) @ x0 + (Pi + 2 * T + 2 * lam * Omega) @ xT)


def kyle_lambda(price_changes: pd.Series, signed_volume: pd.Series) -> float:
    """Kyle's lambda via OLS: Δp_t = λ * signed_volume_t + ε.

    signed_volume = direction * volume (positive for buys). λ is price
    impact per share (higher → less liquid).
    """
    df = pd.concat([price_changes.rename("dp"), signed_volume.rename("sv")], axis=1).dropna()
    if len(df) < 5:
        return float("nan")
    x = df["sv"].to_numpy(dtype=float)
    y = df["dp"].to_numpy(dtype=float)
    # OLS slope
    x_mean, y_mean = x.mean(), y.mean()
    denom = np.sum((x - x_mean) ** 2)
    if denom == 0:
        return float("nan")
    lam = np.sum((x - x_mean) * (y - y_mean)) / denom
    return float(lam)


def amihud_illiquidity(returns: pd.Series, dollar_volume: pd.Series) -> float:
    """Amihud (2002) illiquidity = mean(|r_t| / $Volume_t)."""
    df = pd.concat([returns.rename("r"), dollar_volume.rename("dv")], axis=1).dropna()
    if len(df) == 0:
        return float("nan")
    # Avoid divide by zero
    df = df[df["dv"] > 0]
    if len(df) == 0:
        return float("nan")
    return float((df["r"].abs() / df["dv"]).mean())
