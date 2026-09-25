"""Leakage-safe target positions for Phase 3 strategy research.

Signals are decisions made with information available at a bar's close. Pass
these targets to :func:`quantkit.backtest.vectorized_backtest`, which shifts
them by one bar before earning returns. Functions return zero during warm-up
rather than fabricating history.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

from quantkit.sizing import vol_target_weight

__all__ = [
    "donchian_breakout_position",
    "dual_sma_position",
    "vol_targeted_momentum_position",
]


def _valid_prices(close: pd.Series) -> pd.Series:
    if not isinstance(close, pd.Series) or close.empty:
        raise ValueError("close must be a non-empty Series")
    out = close.astype(float)
    if out.index.has_duplicates:
        raise ValueError("close index must not contain duplicates")
    if (~np.isfinite(out.dropna())).any() or (out.dropna() <= 0).any():
        raise ValueError("close must contain only finite, positive prices")
    return out


def dual_sma_position(
    close: pd.Series,
    *,
    fast: int = 9,
    slow: int = 45,
    long_only: bool = True,
) -> pd.Series:
    """Target exposure from a fast/slow simple-moving-average trend rule.

    The close-of-bar target is long when ``SMA(fast) > SMA(slow)``. It is flat
    otherwise in long-only mode, or short when the inequality reverses. Both
    averages require complete windows, so the first ``slow - 1`` targets are
    zero. Execution must occur on the next bar.
    """
    close = _valid_prices(close)
    if fast < 1 or slow < 2 or fast >= slow:
        raise ValueError("require 1 <= fast < slow")

    fast_ma = close.rolling(fast, min_periods=fast).mean()
    slow_ma = close.rolling(slow, min_periods=slow).mean()
    ready = fast_ma.notna() & slow_ma.notna()
    if long_only:
        target = (fast_ma > slow_ma).astype(float)
    else:
        target = pd.Series(
            np.where(fast_ma > slow_ma, 1.0, -1.0), index=close.index
        )
    return target.where(ready, 0.0).rename("position")


def donchian_breakout_position(
    close: pd.Series,
    *,
    entry_window: int = 50,
    exit_window: int = 20,
) -> pd.Series:
    """Long/flat Donchian breakout target with a shorter-channel exit.

    Enter after the close exceeds the *prior* ``entry_window``-bar high; exit
    after it falls below the prior ``exit_window``-bar low. Channels are
    shifted one bar explicitly, preventing the current close from defining
    the threshold it is compared with. Targets persist between events and are
    executed on the following bar by the backtester.
    """
    close = _valid_prices(close)
    if exit_window < 1 or entry_window < 2 or exit_window >= entry_window:
        raise ValueError("require 1 <= exit_window < entry_window")

    prior_high = close.rolling(entry_window, min_periods=entry_window).max().shift(1)
    prior_low = close.rolling(exit_window, min_periods=exit_window).min().shift(1)
    events = pd.Series(np.nan, index=close.index, dtype=float)
    events.loc[close > prior_high] = 1.0
    events.loc[close < prior_low] = 0.0
    return events.ffill().fillna(0.0).rename("position")


def vol_targeted_momentum_position(
    close: pd.Series,
    returns: pd.Series,
    *,
    momentum_lookback: int = 252,
    vol_lookback: int = 60,
    target_vol: float = 0.10,
    max_weight: float = 1.5,
    annualization: int = 252,
) -> pd.Series:
    """Long/flat time-series momentum scaled to a volatility target.

    The close-of-bar direction is long when the trailing price change over
    ``momentum_lookback`` bars is positive and flat otherwise. Exposure is
    ``target_vol / trailing_realized_vol``, clipped to ``max_weight``. The
    volatility estimate may include the current completed bar because the
    resulting target is held only from the next bar.
    """
    close = _valid_prices(close)
    if not isinstance(returns, pd.Series) or not close.index.equals(returns.index):
        raise ValueError("returns must be a Series sharing close's index")
    if momentum_lookback < 2:
        raise ValueError("momentum_lookback must be >= 2")

    momentum = close / close.shift(momentum_lookback) - 1.0
    direction = (momentum > 0.0).astype(float).where(momentum.notna(), 0.0)
    weight = vol_target_weight(
        returns,
        target_vol,
        lookback=vol_lookback,
        annualization=annualization,
        max_weight=max_weight,
    )
    return (direction * weight).rename("position")
