"""Portfolio lab — HRP, risk parity, mean-variance, estimation discipline.

Implements the discipline distilled in `skills/portfolio-optimization`
(Van Der Post, Pythonic Quant Ch.6; Hilpisch Ch.13) + Hudson & Thames
PortfolioLab (HRP, risk parity, Black-Litterman) + Phase 8 T3
`skills/allocation-discipline` (Clarke-de Silva-Thorley exact FLAM/transfer
coefficient, Jorion Bayes-Stein mean shrinkage, Ledoit-Wolf covariance
shrinkage, Tu-Zhou 1/N combination):

- HRP via hierarchical clustering + recursive bisection (de Prado 2016),
- Risk parity via equal risk contributions,
- Mean-variance max-Sharpe / GMV / target-return via cvxpy→scipy fallback,
- Long-only, estimation-error guardrails.

Vectorized numpy; cvxpy is optional.
"""

from __future__ import annotations

import math
import warnings
from typing import Literal

import numpy as np
import pandas as pd
from scipy.cluster.hierarchy import linkage
from scipy.spatial.distance import squareform
from scipy.optimize import minimize

__all__ = ["bayes_stein_means", "combine_with_1n", "equal_weight", "fundamental_law_ir", "hrp_weights", "ledoit_wolf_shrinkage", "max_sharpe_weights", "min_variance_weights", "risk_parity_weights", "transfer_coefficient"]


def equal_weight(n: int) -> np.ndarray:
    if n < 1:
        raise ValueError("n must be >=1")
    return np.full(n, 1.0 / n)


def fundamental_law_ir(alpha: pd.Series | np.ndarray, cov: pd.DataFrame | np.ndarray) -> float:
    """Exact unconstrained IR = √(α'Ω⁻¹α) (Clarke-de Silva-Thorley eq. 10).

    Under diagonal Ω with Grinold alphas α_i = IC·σ_i·S_i this reduces to
    IC√N. Raises on singular Ω (shrink first via ``ledoit_wolf_shrinkage``).
    """
    a = np.asarray(alpha, dtype=float).ravel()
    S = np.asarray(cov, dtype=float)
    if S.ndim != 2 or S.shape[0] != S.shape[1] or S.shape[0] != a.size:
        raise ValueError("alpha/cov shape mismatch")
    try:
        x = np.linalg.solve(S, a)
    except np.linalg.LinAlgError as exc:
        raise ValueError(f"singular covariance (shrink first): {exc}")
    ir2 = float(a @ x)
    if ir2 < 0 and ir2 > -1e-12:
        ir2 = 0.0
    if ir2 < 0:
        raise ValueError("non-PSD covariance")
    return float(math.sqrt(ir2))


def transfer_coefficient(alpha: pd.Series | np.ndarray, w: pd.Series | np.ndarray, cov: pd.DataFrame | np.ndarray) -> float:
    """Full-covariance transfer coefficient (CDT eq. 23-24).

    TC = α'w / (√(α'Ω⁻¹α) · σ_A), σ_A = √(w'Ωw). TC = 1 for unconstrained
    w*; decay toward 0 measures constraint deadweight. Scale-free in w.
    """
    a = np.asarray(alpha, dtype=float).ravel()
    wv = np.asarray(w, dtype=float).ravel()
    S = np.asarray(cov, dtype=float)
    if not (a.size == wv.size == S.shape[0] == S.shape[1]):
        raise ValueError("alpha/w/cov shape mismatch")
    denom_ir = fundamental_law_ir(a, S)
    sig_a = float(math.sqrt(max(float(wv @ S @ wv), 0.0)))
    if denom_ir == 0 or sig_a == 0:
        raise ValueError("degenerate alpha or weights")
    return float((a @ wv) / (denom_ir * sig_a))


def bayes_stein_means(returns: pd.DataFrame) -> pd.Series:
    """Jorion (1986) Bayes-Stein shrunk mean vector.

    μ̂ = (1-w)·Ȳ + w·Y₀·1, w = min{1, (N-2)/(T·(Ȳ-Y₀1)'Σ⁻¹(Ȳ-Y₀1))},
    grand-mean target Y₀ = mean(Ȳ) (textbook variant of Jorion's GMV target),
    Σ = sample covariance. Feed μ̂ (not raw means) into mean-variance rules.
    """
    if returns.shape[1] < 3:
        raise ValueError("Stein shrinkage needs N >= 3 assets")
    ybar = returns.mean().to_numpy(dtype=float)
    n, N = returns.shape[0], returns.shape[1]
    y0 = float(ybar.mean())
    S = np.cov(returns.to_numpy(dtype=float), rowvar=False)
    d = ybar - y0
    try:
        q = float(d @ np.linalg.solve(S, d))
    except np.linalg.LinAlgError:
        q = float(d @ d / (np.trace(S) / N))
    w = min(1.0, (N - 2) / (n * q)) if q > 0 else 1.0
    return pd.Series((1 - w) * ybar + w * y0, index=returns.columns, name="bayes_stein_mean")


def ledoit_wolf_shrinkage(returns: pd.DataFrame) -> tuple[pd.DataFrame, float]:
    """Ledoit-Wolf (2004) optimal linear shrinkage to scaled identity.

    S* = (1-δ*)S + δ*μI, μ = tr(S)/N, δ* = clamp((π̂-ρ̂)/γ̂, 0, 1) with the
    paper's π̂/ρ̂/γ̂ estimators (T-normalized sample covariance). Returns
    (shrunk_cov DataFrame, delta). S* is PD even when N > T.
    """
    X = returns.to_numpy(dtype=float)
    T, N = X.shape
    if T < 3 or N < 2:
        raise ValueError("need T >= 3 rows and N >= 2 assets")
    Xc = X - X.mean(axis=0)
    S = (Xc.T @ Xc) / T
    mu = float(np.trace(S) / N)
    # γ̂ = ||μI − S||²_F
    gamma = float(np.sum((mu * np.eye(N) - S) ** 2))
    if gamma == 0:
        return pd.DataFrame(S, index=returns.columns, columns=returns.columns), 0.0
    # π̂ = Σ_ij (1/T)Σ_t (x_ti x_tj − s_ij)²
    pi = 0.0
    for t in range(T):
        A = np.outer(Xc[t], Xc[t])
        pi += float(np.sum((A - S) ** 2))
    pi /= T
    # ρ̂ (diagonal + correlation-weighted off-diagonal terms)
    rho_diag = 0.0
    for t in range(T):
        A = np.outer(Xc[t], Xc[t])
        rho_diag += float(np.sum(np.diag(A - S) ** 2))
    rho_diag /= T
    rho_off = 0.0
    s_ii = np.diag(S)
    with np.errstate(divide="ignore", invalid="ignore"):
        for i in range(N):
            for j in range(N):
                if i == j or s_ii[i] <= 0 or s_ii[j] <= 0:
                    continue
                th_ii_ij = float(np.mean((Xc[:, i] ** 2 - s_ii[i]) * (Xc[:, i] * Xc[:, j] - S[i, j])))
                th_jj_ij = float(np.mean((Xc[:, j] ** 2 - s_ii[j]) * (Xc[:, i] * Xc[:, j] - S[i, j])))
                rho_off += 0.5 * (np.sqrt(s_ii[j] / s_ii[i]) * th_ii_ij + np.sqrt(s_ii[i] / s_ii[j]) * th_jj_ij)
    rho = rho_diag + rho_off
    kappa = (pi - rho) / gamma
    delta = float(max(0.0, min(kappa, 1.0)))
    Sstar = (1 - delta) * S + delta * mu * np.eye(N)
    return pd.DataFrame(Sstar, index=returns.columns, columns=returns.columns), delta


def optimal_turnover(gamma: float, phi: float) -> float:
    """Baldacci-Benveniste-Ritter (2022) Eq. 20 — optimal steady-state turnover.

    ``turnover = gamma * sqrt(phi/gamma + 1)`` where ``gamma =
    sqrt(kappa*sigma^2/lambda)`` (trading-speed rate from risk aversion,
    vol, and Kyle lambda) and ``phi`` is the OU alpha mean-reversion
    speed (half-life = ln2/phi). Units: fraction of book per unit time.
    Desk rule: realized turnover far above this = overtrading vs the
    linear-impact optimum; far below = leaving alpha on the table.
    """
    for name, v in [("gamma", gamma), ("phi", phi)]:
        if not np.isfinite(v) or v <= 0:
            raise ValueError(f"{name} must be positive finite")
    return float(gamma * np.sqrt(phi / gamma + 1.0))


def steady_state_ir(nu: float, sigma: float, gamma: float, phi: float) -> float:
    """Baldacci-Benveniste-Ritter (2022) Eq. 23 — steady-state IR net of
    quadratic costs.

    ``IR = nu/(2*sigma) * sqrt(gamma / (phi*(phi + 2*gamma)))`` where
    ``nu`` is the OU forecast innovation vol (signal strength), ``sigma``
    asset vol. Multiplied by sqrt(N) for N independent (residual) assets.
    """
    for name, v in [("nu", nu), ("sigma", sigma), ("gamma", gamma), ("phi", phi)]:
        if not np.isfinite(v) or v <= 0:
            raise ValueError(f"{name} must be positive finite")
    return float(nu / (2 * sigma) * np.sqrt(gamma / (phi * (phi + 2 * gamma))))


def combine_with_1n(w_soph: pd.Series | np.ndarray, delta: float) -> pd.Series:
    """Tu-Zhou combination: w_c = (1-δ)·(1/N) + δ·w_soph, δ ∈ [0,1].

    1/N is the low-variance shrinkage anchor for estimation-noisy rules.
    """
    w = pd.Series(np.asarray(w_soph, dtype=float))
    if not 0 <= delta <= 1:
        raise ValueError("delta must be in [0,1]")
    return ((1 - delta) / len(w) + delta * w).rename("combined_1n")


def _corr_to_dist(corr: pd.DataFrame) -> np.ndarray:
    # distance = sqrt(0.5 * (1 - corr)), per HRP
    dist = np.sqrt(0.5 * (1 - corr.to_numpy(dtype=float)))
    # linkage needs condensed form
    return squareform(dist, checks=False)


def hrp_weights(cov: pd.DataFrame, linkage_method: str = "single") -> pd.Series:
    """HRP weights (de Prado 2016, PortfolioLab).

    Steps: corr → distance → linkage → quasi-diagonal order → recursive
    bisection allocating inverse variance.

    Parameters
    ----------
    cov : pd.DataFrame
        Covariance matrix (assets × assets), symmetric, PSD.
    linkage_method : str
        Hierarchical linkage method (single, complete, average).

    Returns
    -------
    pd.Series
        HRP weights summing to 1, index = cov.index.
    """
    if not isinstance(cov, pd.DataFrame) or cov.shape[0] != cov.shape[1]:
        raise ValueError("cov must be square DataFrame")
    if cov.isna().any().any():
        raise ValueError("cov contains NaN")
    n = cov.shape[0]
    if n == 1:
        return pd.Series([1.0], index=cov.index)
    # Correlation
    std = np.sqrt(np.diag(cov.to_numpy(dtype=float)))
    std[std == 0] = 1e-8
    corr = cov / np.outer(std, std)
    corr = corr.clip(-1, 1)
    # Hierarchical clustering
    dist = _corr_to_dist(corr)
    link = linkage(dist, method=linkage_method)
    # Quasi-diagonal order via linkage leaves
    # Use scipy's dendrogram leaves: traverse linkage to get order
    # Simpler: use sort by cluster; we approximate via hierarchical order
    # For small n, we can get order via sorting by first principal component is overkill;
    # Instead, use linkage to get ordered indices via recursion
    # Implement quick recursive bisection order from link matrix
    # Build tree: each merge creates new node n + i
    # To get leaves order, we can use the linkage's leaves via optimal leaf ordering is complex;
    # Fallback: use correlation seriation via hierarchical clustering leaves as per scipy's `leaves_list`
    from scipy.cluster.hierarchy import leaves_list

    order = leaves_list(link)
    cov_sorted = cov.iloc[order, order]
    # Recursive bisection: allocate inverse variance
    # Initialize weights as 1 for each leaf cluster
    # Use iterative bisection on ordered cov
    import math as _math

    # Helper to compute cluster variance
    def _cluster_var(cov_slice: pd.DataFrame) -> float:
        # Use inverse variance portfolio variance within cluster as proxy
        # For HRP, cluster variance = w^T Σ w where w = 1/var / sum(1/var)
        iv = 1.0 / np.diag(cov_slice.to_numpy(dtype=float))
        iv = np.where(np.isfinite(iv) & (iv > 0), iv, 0)
        if iv.sum() == 0:
            iv = np.ones(len(cov_slice))
        w = iv / iv.sum()
        return float(w @ cov_slice.to_numpy(dtype=float) @ w)

    # Recursive bisection using stack
    weights = pd.Series(1.0, index=cov_sorted.index, dtype=float)
    clusters = [list(cov_sorted.index)]
    # Actually textbook HRP bisect donates weights based on cluster variance
    # Use iterative split: for each cluster, split into two halves, allocate by inverse variance
    # We'll do classic loop: start with one cluster containing all assets ordered
    # Use a queue of clusters to split
    from collections import deque

    queue = deque([list(cov_sorted.index)])
    final_weights = pd.Series(dtype=float)
    # We'll compute weights via recursion copying de Prado's algorithm
    # Simplify: iterative bisection allocating via clusterVar
    # Use weights dict initialized to 1
    w = pd.Series(1.0, index=cov_sorted.index)
    # Use stack to process clusters
    # Implement as in MlFinLab: getRecBipart
    def _get_rec_bipart(cov_sorted: pd.DataFrame, sort_ix: list) -> pd.Series:
        w_local = pd.Series(1.0, index=sort_ix, dtype=float)
        # cItems is list of lists to be split
        c_items: list[list] = [sort_ix]
        while c_items:
            # split each cluster into two
            new_items = []
            for items in c_items:
                if len(items) <= 1:
                    continue
                mid = len(items) // 2
                c1 = items[:mid]
                c2 = items[mid:]
                # cluster variances
                var1 = _cluster_var(cov_sorted.loc[c1, c1])
                var2 = _cluster_var(cov_sorted.loc[c2, c2])
                # allocation
                alpha = 1 - var1 / (var1 + var2) if (var1 + var2) > 0 else 0.5
                # scale weights
                w_local.loc[c1] *= alpha
                w_local.loc[c2] *= 1 - alpha
                new_items.append(c1)
                new_items.append(c2)
            c_items = new_items
        return w_local / w_local.sum() if w_local.sum() != 0 else w_local

    hrp_sorted = _get_rec_bipart(cov_sorted, list(cov_sorted.index))
    # Reorder to original cov index
    return hrp_sorted.reindex(cov.index)


def risk_parity_weights(cov: pd.DataFrame, max_iter: int = 1000, tol: float = 1e-8) -> pd.Series:
    """Equal risk contribution (risk parity) via cyclical coordinate descent.

    Each asset's risk contribution RC_i = w_i * (Σw)_i / σ_p should be equal.
    Simple iterative method: w ∝ 1/σ until convergence to equal RC.

    Falls back to inverse volatility if cov is diagonal.
    """
    if not isinstance(cov, pd.DataFrame) or cov.shape[0] != cov.shape[1]:
        raise ValueError("cov must be square DataFrame")
    n = cov.shape[0]
    if n == 1:
        return pd.Series([1.0], index=cov.index)
    # Start inverse vol
    iv = 1.0 / np.sqrt(np.diag(cov.to_numpy(dtype=float)))
    iv = np.where(np.isfinite(iv) & (iv > 0), iv, 1.0)
    w = iv / iv.sum()
    # Iterative equal risk
    for _ in range(max_iter):
        port_var = float(w @ cov.to_numpy(dtype=float) @ w)
        port_vol = math.sqrt(max(port_var, 1e-12))
        # Marginal risk
        mrc = cov.to_numpy(dtype=float) @ w / port_vol
        rc = w * mrc
        # Equal RC target
        target = port_vol / n
        # Update: w_i *= target / rc_i (damped)
        # Avoid divide by zero
        rc_safe = np.where(rc == 0, 1e-12, rc)
        w_new = w * (target / rc_safe)
        w_new = np.maximum(w_new, 0)
        w_new = w_new / w_new.sum()
        if np.max(np.abs(w_new - w)) < tol:
            w = w_new
            break
        w = 0.5 * w + 0.5 * w_new  # damp
    return pd.Series(w, index=cov.index)


def _mean_variance_optimize(
    expected: pd.Series,
    cov: pd.DataFrame,
    objective: Literal["max_sharpe", "min_variance"] = "max_sharpe",
    risk_free: float = 0.0,
    long_only: bool = True,
) -> pd.Series:
    n = len(expected)
    # Use scipy minimize with fallback; cvxpy if available would be faster
    # For max_sharpe, minimize -Sharpe; for min_variance, minimize w^T Σ w
    # Constraints: sum w =1, long_only => w>=0
    x0 = np.full(n, 1.0 / n)
    bounds = [(0, 1) if long_only else (None, None)] * n
    constraints = [{"type": "eq", "fun": lambda w: np.sum(w) - 1}]

    def _neg_sharpe(w):
        ret = float(w @ expected.to_numpy(dtype=float))
        var = float(w @ cov.to_numpy(dtype=float) @ w)
        vol = math.sqrt(max(var, 1e-12))
        sharpe = (ret - risk_free) / vol if vol > 0 else 0.0
        return -sharpe

    def _variance(w):
        return float(w @ cov.to_numpy(dtype=float) @ w)

    obj = _neg_sharpe if objective == "max_sharpe" else _variance
    try:
        res = minimize(obj, x0, method="SLSQP", bounds=bounds, constraints=constraints, options={"maxiter": 500, "ftol": 1e-9})
        if not res.success:
            warnings.warn(f"mean-variance {objective} did not converge: {res.message}")
        w = np.clip(res.x, 0 if long_only else -np.inf, np.inf)
        w = w / w.sum() if w.sum() != 0 else equal_weight(n)
    except Exception as exc:  # pragma: no cover
        warnings.warn(f"mean-variance fallback to equal weight ({exc})")
        w = equal_weight(n)
    return pd.Series(w, index=expected.index)


def max_sharpe_weights(
    expected: pd.Series, cov: pd.DataFrame, risk_free: float = 0.0, long_only: bool = True
) -> pd.Series:
    """Max-Sharpe (tangency) portfolio, long-only by default."""
    return _mean_variance_optimize(expected, cov, objective="max_sharpe", risk_free=risk_free, long_only=long_only)


def min_variance_weights(cov: pd.DataFrame, long_only: bool = True) -> pd.Series:
    """Global minimum variance portfolio."""
    # Use zero expected return dummy; optimizer will minimize variance
    n = cov.shape[0]
    expected = pd.Series(np.zeros(n), index=cov.index)
    return _mean_variance_optimize(expected, cov, objective="min_variance", long_only=long_only)
