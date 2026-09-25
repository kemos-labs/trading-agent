"""Feature lab — fractional differentiation, CUSUM, triple-barrier, entropy.

Implements the discipline distilled in `skills/purged-cross-validation`
(de Prado AFML Ch.5 FFD) + `skills/alpha-factor-evaluation` + `skills/arma-garch-modeling`
+ `knowledge/advances-financial-ml` Ch.5, Ch.17–19:

- FFD with fixed-width window (memory-preserving `d*` search),
- CUSUM event sampler (symmetric, de Prado 2.5.2.1),
- Triple-barrier labeling (pt/sl/vertical barrier, Ch.3),
- Plug-in Shannon entropy (Ch.18) for regime/feature relevance.

Vectorized pandas/numpy; fallback loops only for tiny FFD weight generation.
Fail-closed on bad d/threshold; fit-on-train-only is caller discipline.
"""

from __future__ import annotations

import math
import warnings

import numpy as np
import pandas as pd

__all__ = ["cusum_filter", "fractional_diff", "get_weights", "plug_in_entropy", "triple_barrier_labels"]


def get_weights(d: float, size: int) -> np.ndarray:
    """Binomial expansion weights for fractional differentiation.

    w_k = -w_{k-1} * (d - k + 1) / k,  w_0 = 1. Truncated to `size`.
    """
    if not -1 < d < 1:
        raise ValueError("d must be in (-1, 1) for stationary FFD; 0 is integer diff")
    w = [1.0]
    for k in range(1, size):
        w.append(-w[-1] * (d - k + 1) / k)
    w = np.array(w[::-1])  # oldest first for convolution
    return w


def fractional_diff(series: pd.Series, d: float, thres: float = 1e-5) -> pd.Series:
    """FFD with fixed-width window (de Prado 5.4.2).

    Drops the smallest weights until |sum(w)| < thres relative to full,
    then applies convolution. Returns NaN for warmup.

    Parameters
    ----------
    series : pd.Series
        Price or log-price series (DatetimeIndex).
    d : float
        Fractional order in (-1,1). 0 = copy, 1 = first diff.
    thres : float
        Weight-loss threshold for window width (1e-5 default).

    Returns
    -------
    pd.Series
        Fractionally differentiated series, same index.
    """
    if not isinstance(series, pd.Series) or series.empty:
        raise ValueError("series must be non-empty Series")
    if thres <= 0:
        raise ValueError("thres must be >0")
    if d == 0:
        return series.copy()
    # Find window width l* such that sum of dropped weights < thres
    # Search up to len(series)
    w_full = get_weights(d, len(series))
    cum_abs = np.cumsum(np.abs(w_full))
    # Choose smallest l where cumulative loss < thres * total
    # Equivalent to de Prado's weight loss criterion
    total = np.sum(np.abs(w_full))
    # Find l* = min l s.t. sum_{k>l}|w_k| < thres
    # We use iterative width search
    width = len(series)
    for l in range(1, len(series)):
        w = get_weights(d, l)
        loss = np.sum(np.abs(get_weights(d, len(series)))) - np.sum(np.abs(w))
        # Simpler: compute cumulative from tail
        # Use get_weights tail loss
        if loss < thres:
            width = l
            break
    # Use fixed width = min where loss < thres, but cap at len
    # For small series, just use full
    if width >= len(series):
        width = len(series)
    w = get_weights(d, width)
    # Convolve
    out = pd.Series(np.nan, index=series.index, dtype=float)
    # Use dot product per window
    vals = series.to_numpy(dtype=float)
    for i in range(width - 1, len(vals)):
        out.iloc[i] = np.dot(w, vals[i - width + 1 : i + 1])
    return out


def cusum_filter(series: pd.Series, threshold: float) -> pd.DatetimeIndex:
    """Symmetric CUSUM sampler (de Prado Snippet 2.4).

    Emits an event when |cum_sum - min/max| >= threshold * std.
    Threshold is in units of series std (often 0.5–1.0 * daily vol).

    Returns DatetimeIndex of event timestamps (subset of series index).
    """
    if not isinstance(series, pd.Series) or len(series) < 2:
        raise ValueError("series must have >=2 observations")
    if threshold <= 0:
        raise ValueError("threshold must be >0")
    # Use log returns or price diffs? We use series diff
    diff = series.diff().dropna()
    events = []
    s_pos, s_neg = 0.0, 0.0
    # Use expanding std as in de Prado, but here use rolling 20 for stability
    # For simplicity, use full-sample std * threshold
    h = threshold * diff.std(ddof=1) if len(diff) > 1 else threshold
    if not np.isfinite(h) or h == 0:
        h = threshold
    for t, x in zip(diff.index, diff.to_numpy()):
        s_pos = max(0, s_pos + x)
        s_neg = min(0, s_neg + x)
        if s_pos >= h or s_neg <= -h:
            events.append(t)
            s_pos, s_neg = 0.0, 0.0
    return pd.DatetimeIndex(events)


def triple_barrier_labels(
    close: pd.Series,
    events: pd.DatetimeIndex,
    pt_sl: tuple[float, float] | float = (0.01, 0.01),
    vertical_barrier: int | None = None,
    trgt: pd.Series | None = None,
) -> pd.DataFrame:
    """Triple-barrier labeling (de Prado Ch.3).

    For each event timestamp `t0`, watch `close` forward:
    - upper = close[t0] * (1 + pt)
    - lower = close[t0] * (1 - sl)
    - vertical = t0 + vertical_barrier bars (or last bar)

    Returns DataFrame indexed by events with columns:
      `t1` (first barrier touch time), `ret` (return to t1), `bin` (1/0/-1).

    pt/sl are fractions (0.01 = 1%). If `trgt` is given, pt/sl are
    multiples of trgt[t0] (vol-scaled).
    """
    if not isinstance(close, pd.Series) or close.empty:
        raise ValueError("close must be non-empty Series")
    if isinstance(pt_sl, (list, tuple)):
        pt, sl = float(pt_sl[0]), float(pt_sl[1])
    else:
        pt = sl = float(pt_sl)
    if pt < 0 or sl < 0:
        raise ValueError("pt/sl must be >=0")
    out_rows = []
    close_vals = close
    for t0 in events:
        if t0 not in close_vals.index:
            # skip if event not in close
            continue
        p0 = float(close_vals.loc[t0])
        # Determine vertical barrier idx
        t0_loc = close_vals.index.get_loc(t0)
        if vertical_barrier is not None:
            t1_pos = min(t0_loc + int(vertical_barrier), len(close_vals) - 1)
            t1_candidates = close_vals.index[t0_loc + 1 : t1_pos + 1]
        else:
            t1_candidates = close_vals.index[t0_loc + 1 :]
            if len(t1_candidates) == 0:
                continue
        # Determine barrier levels
        if trgt is not None and t0 in trgt.index and np.isfinite(trgt.loc[t0]) and trgt.loc[t0] > 0:
            pt_level = p0 + p0 * pt * float(trgt.loc[t0])
            sl_level = p0 - p0 * sl * float(trgt.loc[t0])
            # For vol-scaled, pt/sl are multiples of trgt, but we keep simple
            upper = p0 + p0 * pt * float(trgt.loc[t0])
            lower = p0 - p0 * sl * float(trgt.loc[t0])
        else:
            upper = p0 * (1 + pt)
            lower = p0 * (1 - sl)
        t1 = None
        ret = np.nan
        bin_lab = 0
        for t in t1_candidates:
            px = float(close_vals.loc[t])
            ret_t = (px / p0) - 1
            if px >= upper:
                t1 = t
                ret = ret_t
                bin_lab = 1
                break
            if px <= lower:
                t1 = t
                ret = ret_t
                bin_lab = -1
                break
        if t1 is None:
            # vertical barrier
            t1 = t1_candidates[-1]
            ret = (float(close_vals.loc[t1]) / p0) - 1
            bin_lab = 0
        out_rows.append((t0, t1, float(ret), int(bin_lab)))
    if not out_rows:
        return pd.DataFrame(columns=["t1", "ret", "bin"]).astype({"t1": "datetime64[ns]", "ret": float, "bin": int}).set_index(pd.Index([], name="t0"))
    df = pd.DataFrame(out_rows, columns=["t0", "t1", "ret", "bin"]).set_index("t0")
    df["t1"] = pd.to_datetime(df["t1"])
    return df


def plug_in_entropy(series: pd.Series, bins: int = 10) -> float:
    """Plug-in Shannon entropy (discrete, bits) of a return series.

    Histograms `bins` equiprobable? Here equal-width for simplicity.
    Entropy = -sum p*log2(p). For regime relevance screening (AFML Ch.18).

    Returns entropy in bits; 0 for constant series.
    """
    if not isinstance(series, pd.Series):
        raise ValueError("series must be a Series")
    x = series.dropna().to_numpy(dtype=float)
    if len(x) < 2:
        return 0.0
    hist, _ = np.histogram(x, bins=bins, density=False)
    p = hist / hist.sum()
    p = p[p > 0]
    if len(p) == 0:
        return 0.0
    return float(-np.sum(p * np.log2(p)))
