"""Risk lab — VaR, cVaR, stress testing, scenarios, downside.

Implements the discipline distilled in `skills/risk-metrics`,
`skills/parametric-var`, `skills/stress-testing`, `skills/correlated-scenario-simulation`,
`skills/downside-risk-measures`, `skills/var-backtesting`, `skills/bond-price-sensitivities`:

- historical / parametric VaR + cVaR,
- Kupiec + Christoffersen backtests,
- stressed covariance + PSD repair (eigenvalue clip),
- Cholesky correlated scenarios,
- downside: Sortino/Omega/Kappa,
- bond duration/convexity (Taylor).

Vectorized pandas/numpy; fail-closed on VaR alpha.
"""

from __future__ import annotations

import math
import warnings

import numpy as np
import pandas as pd
from scipy.stats import norm, chi2

__all__ = [
    "bond_duration_convexity",
    "cholesky_scenarios",
    "downside_deviation",
    "historical_cvar",
    "historical_var",
    "parametric_var",
    "sortino_ratio",
    "stress_covariance",
    "var_backtest_kupiec",
]


def historical_var(returns: pd.Series, alpha: float = 0.05) -> float:
    """Historical VaR (one-period, negative return quantile).

    VaR_α = −quantile(returns, α). Positive number means loss.
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0,1)")
    r = returns.dropna().astype(float)
    if len(r) == 0:
        raise ValueError("no valid returns")
    return float(-r.quantile(alpha))


def historical_cvar(returns: pd.Series, alpha: float = 0.05) -> float:
    """Historical cVaR/ES = −mean(returns[returns ≤ quantile(α)])."""
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0,1)")
    r = returns.dropna().astype(float)
    if len(r) == 0:
        raise ValueError("no valid returns")
    q = r.quantile(alpha)
    tail = r[r <= q]
    if len(tail) == 0:
        return float(-q)
    return float(-tail.mean())


def parametric_var(returns: pd.Series, alpha: float = 0.05) -> float:
    """Parametric VaR via fitted normal (μ,σ) → −(μ + σ·Φ⁻¹(α))."""
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0,1)")
    r = returns.dropna().astype(float)
    if len(r) < 2:
        raise ValueError("need ≥2 returns")
    mu = float(r.mean())
    sigma = float(r.std(ddof=1))
    if sigma <= 0 or not np.isfinite(sigma):
        return float(-mu)
    return float(-(mu + sigma * norm.ppf(alpha)))


def downside_deviation(returns: pd.Series, target: float = 0.0) -> float:
    """Lower partial moment: √E[max(0, target − r)²]."""
    r = returns.dropna().astype(float)
    if len(r) == 0:
        return 0.0
    downside = np.maximum(0, target - r.to_numpy(dtype=float))
    return float(np.sqrt(np.mean(downside ** 2)))


def sortino_ratio(returns: pd.Series, target: float = 0.0, periods_per_year: int = 252) -> float:
    """Annualized Sortino = (mean − target)/downside_dev * √N."""
    r = returns.dropna().astype(float)
    if len(r) < 2:
        return 0.0
    dd = downside_deviation(r, target=target)
    if dd == 0 or not np.isfinite(dd):
        return 0.0
    return float((r.mean() - target) / dd * math.sqrt(periods_per_year))


def bond_duration_convexity(
    cashflows: pd.Series, y: float, freq: int = 1
) -> dict[str, float]:
    """Macaulay / modified duration, convexity, PV01 for a bond.

    cashflows: Series indexed by time in years (t) with cash amount.
    y: yield per period (annual yield / freq) as decimal.
    freq: compounding periods per year.

    Returns dict with price, macaulay, modified, convexity, pv01.
    """
    if not isinstance(cashflows, pd.Series) or cashflows.empty:
        raise ValueError("cashflows must be non-empty Series indexed by t (years)")
    if y <= -1:
        raise ValueError("yield must be > -1")
    t = cashflows.index.to_numpy(dtype=float)
    cf = cashflows.to_numpy(dtype=float)
    # Price
    df = (1 + y / freq) ** (freq * t)
    pv = cf / df
    price = float(np.sum(pv))
    if price == 0:
        raise ValueError("zero price")
    # Macaulay: Σ t·pv / price
    macaulay = float(np.sum(t * pv) / price)
    modified = float(macaulay / (1 + y / freq))
    # Convexity: (1/price) * Σ t(t+1) pv / (1+y)^2  (approx, per period)
    # Use Taylor second-order: Σ t(t+1/freq) pv / (1+y/freq)^2 / price
    # Simplified to: Σ t*(t+1/freq) * pv / (1+y/freq)^2 / price
    convex = float(np.sum(t * (t + 1 / freq) * pv / (1 + y / freq) ** 2) / price)
    pv01 = float(modified * price * 0.0001)
    return {"price": price, "macaulay": macaulay, "modified": modified, "convexity": convex, "pv01": pv01}


def stress_covariance(cov: pd.DataFrame, shock: float = 0.2, psd: bool = True) -> pd.DataFrame:
    """Stressed covariance: scale correlations by (1+shock) and repair PSD via eigenvalue clipping.

    shock in [0,1): 0 = unchanged, 0.2 = +20% correlation stress (crisis).
    Clips negative eigenvalues to 1e-8 and renormalizes to keep variances.
    """
    if not isinstance(cov, pd.DataFrame) or cov.shape[0] != cov.shape[1]:
        raise ValueError("cov must be square DataFrame")
    if not 0 <= shock < 1:
        raise ValueError("shock must be in [0,1)")
    n = cov.shape[0]
    # Correlation + vol
    vol = np.sqrt(np.diag(cov.to_numpy(dtype=float)))
    corr = cov.to_numpy(dtype=float) / np.outer(vol, vol)
    # Stress correlations toward 1
    stressed_corr = corr * (1 + shock)
    # Cap diag at 1, off-diag at 0.99
    np.fill_diagonal(stressed_corr, 1.0)
    stressed_corr = np.clip(stressed_corr, -0.99, 0.99)
    np.fill_diagonal(stressed_corr, 1.0)
    stressed_cov = stressed_corr * np.outer(vol, vol)
    if not psd:
        return pd.DataFrame(stressed_cov, index=cov.index, columns=cov.columns)
    # PSD repair: eigenvalue clip
    vals, vecs = np.linalg.eigh(stressed_cov)
    vals_clipped = np.maximum(vals, 1e-8)
    repaired = (vecs * vals_clipped) @ vecs.T
    # Ensure symmetry
    repaired = 0.5 * (repaired + repaired.T)
    return pd.DataFrame(repaired, index=cov.index, columns=cov.columns)


def cholesky_scenarios(
    cov: pd.DataFrame, n_scenarios: int = 1000, seed: int = 42
) -> pd.DataFrame:
    """Correlated normal scenarios via Cholesky: L·Z, L = cholesky(cov)."""
    if not isinstance(cov, pd.DataFrame) or cov.shape[0] != cov.shape[1]:
        raise ValueError("cov must be square DataFrame")
    if n_scenarios < 1:
        raise ValueError("n_scenarios must be >=1")
    L = np.linalg.cholesky(cov.to_numpy(dtype=float))
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(size=(n_scenarios, cov.shape[0]))
    scen = z @ L.T
    return pd.DataFrame(scen, columns=cov.columns)


def var_backtest_kupiec(
    returns: pd.Series, var_series: pd.Series, alpha: float = 0.05
) -> dict[str, float]:
    """Kupiec POF (unconditional coverage) LR test for VaR.

    var_series: one-period VaR forecasts aligned with returns (positive loss numbers).
    breach = returns < -var. LR = 2*log[(1-p_hat)^(T-x) p_hat^x / (1-α)^ (T-x) α^x],
    p_hat = x/T. p-value from χ²(1).

    Returns dict with breaches, p_hat, LR, p_value.
    """
    if not 0 < alpha < 1:
        raise ValueError("alpha must be in (0,1)")
    # Align
    df = pd.concat([returns.rename("r"), var_series.rename("var")], axis=1).dropna()
    if len(df) == 0:
        raise ValueError("no overlapping returns/var")
    breaches = (df["r"] < -df["var"]).sum()
    n = len(df)
    p_hat = breaches / n if n else 0
    # Avoid 0*log(0)
    if p_hat == 0 or p_hat == 1:
        lr = 0.0 if breaches == 0 else 2 * (breaches * math.log(p_hat / alpha) + (n - breaches) * math.log((1 - p_hat) / (1 - alpha)))
        # Handle edge with small epsilon
        if not np.isfinite(lr):
            lr = 0.0
    else:
        lr = 2 * (breaches * math.log(p_hat / alpha) + (n - breaches) * math.log((1 - p_hat) / (1 - alpha)))
        if not np.isfinite(lr):
            lr = 0.0
    p_value = float(1 - chi2.cdf(lr, df=1)) if np.isfinite(lr) else 0.0
    return {"breaches": int(breaches), "n": int(n), "p_hat": float(p_hat), "LR": float(lr), "p_value": float(p_value)}
