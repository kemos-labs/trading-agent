"""Cross-sectional (xsec) signal construction — Phase 8 T1 µ-models lab.

Implements the tradable mechanics behind two corpus skills without the
proprietary data they assume:

- ``intermediate-momentum`` — Novy-Marx 12-7 / 6-2 formation split,
  Jegadeesh-Titman overlapping cohorts, skip-month discipline.
- ``residual-reversal`` — Da-Liu-Schaumburg residual score
  (``r - mu_hat - CF``) + within-industry (group-neutral) sorts.

Everything here is point-in-time: formation windows always end at least
``end_lag`` bars before the signal bar, and target weights are decided at
the close for next-bar execution (same discipline as ``strategies``).

Traceability: skills ``intermediate-momentum`` / ``residual-reversal``;
corpus ``drive-download-.../momentum/Is Momentum Really Momentum (2012).md``,
``.../Decomposing Short-Term Return Reversal (2011).md``,
``.../A Closer Look at the Short-Term Return Reversal (2014).md``.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def _check_panel(prices: pd.DataFrame) -> pd.DataFrame:
    if not isinstance(prices, pd.DataFrame) or prices.empty:
        raise ValueError("prices must be a non-empty DataFrame (bars x assets)")
    if prices.isna().all(axis=None):
        raise ValueError("prices is all-NaN (fail closed)")
    return prices


def formation_returns(
    prices: pd.DataFrame, start_lag: int = 12, end_lag: int = 2
) -> pd.DataFrame:
    """Log formation return ``log(P[t-end_lag]) - log(P[t-start_lag])``.

    ``formation_returns(prices, 12, 2)`` is the academic 12-2 signal;
    ``(12, 7)`` / ``(7, 2)`` give the Novy-Marx split, with the exact
    telescoping identity ``F(12,2) == F(12,7) + F(7,2)`` (log space).
    The paper labels the recent leg ``6-2``; ``(7, 2)`` is its adjacent-window
    equivalent here — the economics (intermediate leg dominates) are unchanged.
    """
    prices = _check_panel(prices)
    if not (isinstance(start_lag, int) and isinstance(end_lag, int)):
        raise ValueError("lags must be ints")
    if start_lag <= end_lag or end_lag < 1 or start_lag < 2:
        raise ValueError("need 1 <= end_lag < start_lag (skip-month discipline)")
    if (prices <= 0).any(axis=None):
        raise ValueError("prices must be positive for log formation")
    logp = np.log(prices)
    return logp.shift(end_lag) - logp.shift(start_lag)


def quantile_assign(scores: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """Cross-sectional quantile bin (1..n) per bar; NaN scores stay NaN."""
    if n < 2:
        raise ValueError("n must be >= 2")
    ranks = scores.rank(axis=1, pct=True)
    bins = np.ceil(ranks * n).clip(1, n)
    return bins.where(scores.notna())


def wml_weights(
    scores: pd.DataFrame,
    top: float = 0.1,
    bottom: float = 0.1,
    groups: pd.DataFrame | pd.Series | None = None,
) -> pd.DataFrame:
    """Winner-minus-loser target weights: long top quantile, short bottom.

    Equal-weight within each leg, dollar-neutral per bar. With ``groups``
    (industry codes aligned to ``scores``), ranks are computed *within*
    each group — the Da-Liu-Schaumburg within-industry sort — and each
    group leg is dollar-neutral on its own.
    """
    if not (0 < bottom < 1 and 0 < top < 1):
        raise ValueError("top/bottom must be fractions in (0, 1)")
    weights = pd.DataFrame(0.0, index=scores.index, columns=scores.columns)
    if groups is None:
        ranks = scores.rank(axis=1, pct=True)
        for t in scores.index:
            row = scores.loc[t].dropna()
            if row.empty:
                continue
            r = ranks.loc[t, row.index]
            longs = r[r >= 1.0 - top].index
            shorts = r[r <= bottom].index
            if len(longs):
                weights.loc[t, longs] = 0.5 / len(longs)
            if len(shorts):
                weights.loc[t, shorts] = -0.5 / len(shorts)
        return weights
    if isinstance(groups, pd.Series):
        groups = pd.DataFrame(
            np.tile(groups.values, (len(scores), 1)),
            index=scores.index,
            columns=scores.columns,
        )
    for t in scores.index:
        srow = scores.loc[t].dropna()
        if srow.empty:
            continue
        grow = groups.loc[t, srow.index]
        for _, members in srow.groupby(grow):
            r = members.rank(pct=True)
            longs = r[r >= 1.0 - top].index
            shorts = r[r <= bottom].index
            n_groups = grow.nunique()
            if len(longs):
                weights.loc[t, longs] = 0.5 / (len(longs) * n_groups)
            if len(shorts):
                weights.loc[t, shorts] = -0.5 / (len(shorts) * n_groups)
    return weights


def overlapping_weights(target: pd.DataFrame, holding: int = 1) -> pd.DataFrame:
    """Jegadeesh-Titman overlapping cohorts: mean of last ``holding`` targets.

    Decided-at-close semantics preserved: cohort formed at close ``t``
    executes from ``t+1``; with ``holding == 1`` this is a one-bar shift.
    """
    if holding < 1:
        raise ValueError("holding must be >= 1")
    cohorts = [target.shift(k, fill_value=0.0) for k in range(1, holding + 1)]
    return sum(cohorts) / holding


def residual_score(
    returns: pd.DataFrame, expected: pd.DataFrame, cf_news: pd.DataFrame
) -> pd.DataFrame:
    """Da-Liu-Schaumburg residual: ``Residual = r - mu_hat - CF``."""
    return returns - expected - cf_news
