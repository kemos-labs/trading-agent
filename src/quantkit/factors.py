"""Alpha-factor evaluation — IC & quantile spreads.

Implements the discipline distilled in ``skills/alpha-factor-evaluation``
(Jansen, ML for Trading Ch.4) plus Phase 8 T2
``skills/country-industry-neutralization`` (Heston-Rouwenhorst constrained
dummy regression for pure country/industry factor returns):

- winsorize / z-score / neutralize per cross-section,
- period-by-period Spearman IC (mean, t-stat, hit rate),
- quantile long-short spread (monotonic decile check).

Vectorized pandas/numpy; no look-ahead (each period cleaned separately).
"""

from __future__ import annotations

import warnings

import numpy as np
import pandas as pd
from scipy.stats import spearmanr

__all__ = [
    "information_coefficient",
    "neutralize",
    "pure_factor_returns",
    "quantile_spread",
    "winsorize",
    "zscore",
]


def winsorize(s: pd.Series, limits: tuple[float, float] = (0.01, 0.99)) -> pd.Series:
    """Clip a cross-section at the given quantile limits.

    Parameters
    ----------
    s : pd.Series
        Factor values for one period (assets as index).
    limits : tuple[float,float]
        Lower / upper quantiles to clip at (e.g., 0.01/0.99).

    Returns
    -------
    pd.Series
        Clipped series, same index.
    """
    if not isinstance(s, pd.Series):
        raise ValueError("s must be a Series")
    if len(s) < 3:
        return s.copy()
    lo, hi = limits
    if not 0 <= lo < hi <= 1:
        raise ValueError("limits must satisfy 0 <= lo < hi <= 1")
    q_lo, q_hi = s.quantile([lo, hi])
    return s.clip(lower=q_lo, upper=q_hi)


def zscore(s: pd.Series) -> pd.Series:
    """Cross-sectional z-score: (x - mean) / std (ddof=1, 0 if std=0)."""
    if not isinstance(s, pd.Series):
        raise ValueError("s must be a Series")
    mu = s.mean()
    sd = s.std(ddof=1)
    if sd == 0 or not np.isfinite(sd) or pd.isna(sd):
        return pd.Series(0.0, index=s.index)
    return (s - mu) / sd


def neutralize(
    factor: pd.Series, exposures: pd.DataFrame | pd.Series
) -> pd.Series:
    """Residualize factor against exposures via cross-sectional OLS.

    factor_i = exposures_i · beta + residual_i  →  return residual_i

    Parameters
    ----------
    factor : pd.Series
        Factor values for one period (assets as index).
    exposures : pd.DataFrame | pd.Series
        Exposures to neutralize (e.g., industry dummies, size, beta),
        same index as factor. A Series is treated as one exposure.

    Returns
    -------
    pd.Series
        Residual factor (neutralized), same index.
    """
    if not isinstance(factor, pd.Series):
        raise ValueError("factor must be a Series")
    if isinstance(exposures, pd.Series):
        exposures = exposures.to_frame()
    # Align
    df = pd.concat([factor.rename("factor"), exposures], axis=1, join="inner").dropna()
    if len(df) < 2 or df.shape[1] < 2:
        # No variation to neutralize — return as is (winsorized already)
        return factor.copy()
    y = df["factor"].to_numpy()
    X = df.drop(columns=["factor"]).to_numpy()
    # Add intercept implicitly via exposures? No — if exposures already includes constant, keep as is.
    # Solve beta via lstsq (more stable than inv)
    try:
        beta, *_ = np.linalg.lstsq(X, y, rcond=None)
        resid = y - X.dot(beta)
        return pd.Series(resid, index=df.index).reindex(factor.index)
    except Exception as exc:  # pragma: no cover
        warnings.warn(f"neutralize lstsq failed ({exc}); returning original")
        return factor.copy()


def pure_factor_returns(
    returns: pd.Series,
    industry: pd.Series,
    country: pd.Series,
    weights: pd.Series | None = None,
) -> dict:
    """Heston-Rouwenhorst pure country/industry factor returns (one cross-section).

    ``R_i = α + β_{j(i)} + γ_{k(i)} + e_i`` with value-weighted constraints
    ``Σ W_j β_j = 0``, ``Σ V_k γ_k = 0`` (count-weighted when ``weights``
    is None). Solved by constrained WLS via substitution of the last
dummy in each set. Returns dict with ``alpha`` (cap-weighted market),
    ``industry`` / ``country`` (pure-effect Series), ``resid``.
    """
    df = pd.DataFrame({"r": returns, "ind": industry, "cty": country}).dropna()
    if df.empty:
        raise ValueError("no overlapping observations")
    if df["ind"].nunique() < 2 or df["cty"].nunique() < 2:
        raise ValueError("need ≥2 industries and ≥2 countries")
    w = pd.Series(1.0, index=df.index) if weights is None else weights.reindex(df.index).astype(float)
    if ((w <= 0) | ~np.isfinite(w)).any():
        raise ValueError("weights must be positive finite")
    inds = sorted(df["ind"].unique())
    ctys = sorted(df["cty"].unique())
    W = df.groupby("ind").apply(lambda g: w.loc[g.index].sum(), include_groups=False)
    V = df.groupby("cty").apply(lambda g: w.loc[g.index].sum(), include_groups=False)
    # Design: [1, Z_1..Z_{J-1}, C_1..C_{K-1}] with substitution coeffs
    # β_J = -(Σ_{j<J} W_j β_j)/W_J baked into columns: col_j = Z_j - (W_j/W_J)*Z_J
    n = len(df)
    cols = {}
    Z = pd.get_dummies(df["ind"]).reindex(columns=inds, fill_value=0).astype(float)
    C = pd.get_dummies(df["cty"]).reindex(columns=ctys, fill_value=0).astype(float)
    X = np.ones((n, 1))
    names = ["alpha"]
    for j in inds[:-1]:
        X = np.c_[X, Z[j].to_numpy() - (W[j] / W[inds[-1]]) * Z[inds[-1]].to_numpy()]
        names.append(f"ind:{j}")
    for k in ctys[:-1]:
        X = np.c_[X, C[k].to_numpy() - (V[k] / V[ctys[-1]]) * C[ctys[-1]].to_numpy()]
        names.append(f"cty:{k}")
    sw = np.sqrt(w.to_numpy())
    beta, *_ = np.linalg.lstsq(X * sw[:, None], df["r"].to_numpy() * sw, rcond=None)
    alpha = float(beta[0])
    b_ind = {j: float(beta[1 + i]) for i, j in enumerate(inds[:-1])}
    b_ind[inds[-1]] = -sum(W[j] * b_ind[j] for j in inds[:-1]) / W[inds[-1]]
    off = 1 + len(inds) - 1
    b_cty = {k: float(beta[off + i]) for i, k in enumerate(ctys[:-1])}
    b_cty[ctys[-1]] = -sum(V[k] * b_cty[k] for k in ctys[:-1]) / V[ctys[-1]]
    ind_s = pd.Series(b_ind, name="pure_industry")
    cty_s = pd.Series(b_cty, name="pure_country")
    fitted = alpha + df["ind"].map(ind_s) + df["cty"].map(cty_s)
    resid = (df["r"] - fitted).rename("resid")
    return {"alpha": alpha, "industry": ind_s, "country": cty_s, "resid": resid}


def _prepare_panel(
    factor: pd.Series | pd.DataFrame,
    fwd_return: pd.Series | pd.DataFrame,
) -> pd.DataFrame:
    """Coerce factor/fwd_return into a long DataFrame with MultiIndex (period, asset)."""
    # Accept either:
    # - Series with MultiIndex (period, asset)
    # - DataFrame with columns ['factor','fwd_return'] and MultiIndex
    # - Two Series aligned
    if isinstance(factor, pd.DataFrame) and "factor" in factor.columns and "fwd_return" in factor.columns:
        df = factor[["factor", "fwd_return"]].copy()
        df = df.dropna()
        return df
    # Two Series case
    if isinstance(factor, pd.Series) and isinstance(fwd_return, pd.Series):
        df = pd.DataFrame({"factor": factor, "fwd_return": fwd_return}).dropna()
        return df
    raise ValueError("factor/fwd_return must be (Series, Series) or DataFrame with factor/fwd_return cols")


def information_coefficient(
    factor: pd.Series | pd.DataFrame,
    fwd_return: pd.Series | None = None,
    *,
    method: str = "spearman",
) -> dict:
    """Period-by-period IC and summary stats.

    Parameters
    ----------
    factor : Series or DataFrame
        Factor panel. If a DataFrame with factor/fwd_return cols, fwd_return arg is ignored.
    fwd_return : Series | None
        Forward return panel aligned with factor (same MultiIndex).

    Returns
    -------
    dict with keys:
      - ic : pd.Series of per-period IC (Spearman rank correlation)
      - mean : float, mean IC
      - std : float, std of IC (ddof=1)
      - t_stat : float, mean / (std/√n)
      - hit_rate : float, share of IC with expected sign (sign of mean)
      - n_periods : int
    """
    df = _prepare_panel(factor, fwd_return) if fwd_return is not None else _prepare_panel(factor, factor)  # type: ignore
    # df should have MultiIndex with period as level 0
    if not isinstance(df.index, pd.MultiIndex):
        raise ValueError("panel must have MultiIndex (period, asset)")
    # Compute IC per period
    ics = {}
    for period, g in df.groupby(level=0):
        if len(g) < 3:
            continue
        # Spearman rank correlation
        try:
            if method == "spearman":
                ic = g["factor"].corr(g["fwd_return"], method="spearman")
            else:
                ic = g["factor"].corr(g["fwd_return"], method=method)
        except Exception:
            ic = np.nan
        if np.isfinite(ic):
            ics[period] = float(ic)
    ic_series = pd.Series(ics, name="ic").sort_index()
    if len(ic_series) == 0:
        return {"ic": ic_series, "mean": 0.0, "std": 0.0, "t_stat": 0.0, "hit_rate": 0.0, "n_periods": 0}
    mean_ic = float(ic_series.mean())
    std_ic = float(ic_series.std(ddof=1)) if len(ic_series) > 1 else 0.0
    n = len(ic_series)
    t_stat = float(mean_ic / (std_ic / np.sqrt(n))) if std_ic > 0 else 0.0
    # hit rate wrt sign of mean (if mean is 0, use positive)
    sign = 1 if mean_ic >= 0 else -1
    hit_rate = float((ic_series * sign > 0).mean())
    return {"ic": ic_series, "mean": mean_ic, "std": std_ic, "t_stat": t_stat, "hit_rate": hit_rate, "n_periods": n}


def quantile_spread(
    factor: pd.Series | pd.DataFrame,
    fwd_return: pd.Series | None = None,
    n_quantiles: int = 10,
) -> pd.DataFrame:
    """Average forward return per factor quantile (long-short spread).

    Buckets assets into n_quantiles per period by factor rank, then
    averages forward returns per bucket across time. Check monotonic
    progression and top-minus-bottom spread.

    Returns
    -------
    pd.DataFrame
        Index = quantile (1..n), columns = ['mean_fwd_return','n_obs'] plus
        per-period columns if needed. The long-short spread is
        `mean(n) - mean(1)`.
    """
    df = _prepare_panel(factor, fwd_return) if fwd_return is not None else _prepare_panel(factor, factor)  # type: ignore
    if not isinstance(df.index, pd.MultiIndex):
        raise ValueError("panel must have MultiIndex (period, asset)")
    if n_quantiles < 2:
        raise ValueError("n_quantiles must be >=2")
    # Assign quantile per period
    rows = []
    for period, g in df.groupby(level=0):
        if len(g) < n_quantiles:
            continue
        # qcut on factor rank; duplicates='drop' handles ties
        try:
            q = pd.qcut(g["factor"], q=n_quantiles, labels=False, duplicates="drop") + 1  # 1..Q
        except ValueError:
            continue
        for _, r in g.assign(quantile=q).iterrows():
            rows.append((int(r["quantile"]), float(r["fwd_return"])))
    if not rows:
        return pd.DataFrame(columns=["mean_fwd_return", "n_obs"])
    tmp = pd.DataFrame(rows, columns=["quantile", "fwd_return"])
    out = tmp.groupby("quantile")["fwd_return"].agg(["mean", "count"]).rename(columns={"mean": "mean_fwd_return", "count": "n_obs"})
    out.index.name = "quantile"
    return out.sort_index()
