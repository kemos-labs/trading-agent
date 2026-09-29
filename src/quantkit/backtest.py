"""Two-tier strategy backtesting plus performance measurement.

Module 2 of the Phase 2 core toolkit (ROADMAP). Implements the
discipline distilled in ``skills/backtesting-framework``:

- **Tier 1, vectorized** (:func:`vectorized_backtest`): the fast first
  pass from Hilpisch PAT ch4–5 — ``position.shift(1) × returns`` with
  proportional/fixed costs. Use it to screen signals before building
  anything heavier.
- **Tier 2, bar-by-bar engine** (:class:`BacktestEngine`): a lean
  event-driven loop in the spirit of the QSTrader architecture
  (Halls-Moore ch24) — a stateful strategy callback decides target
  exposure at the close of each bar, orders execute from the *next* bar,
  proportional + flat costs are charged, exposure is capped, and an
  optional equity stop-loss halts trading. Realism the vectors can't
  give: stops, position caps, realized-cost timing.
- **Performance measurement**: annualized Sharpe (dollar-neutral rule:
  no risk-free subtraction by default), max drawdown + duration, MAR,
  and a one-call summary (Chan ch3 discipline).

The full QSTrader-style class zoo (event queue, price/order/fill
handlers, portfolio objects) is described in the skill for teams that
need it; this engine implements the same core loop for a single-asset
return stream with far less machinery.

Vectorized pandas/numpy throughout, apart from the unavoidable
bar-by-bar loop in the Tier 2 engine.
"""

from __future__ import annotations

import warnings
from typing import Callable

import numpy as np
import pandas as pd

__all__ = [
    "BacktestEngine",
    "annualized_return",
    "annualized_sharpe",
    "drawdown_duration",
    "mar_ratio",
    "max_drawdown",
    "performance_summary",
    "vectorized_backtest",
]


# ---------------------------------------------------------------------------
# Tier 1 — vectorized backtest
# ---------------------------------------------------------------------------

def vectorized_backtest(
    returns: pd.Series,
    position: pd.Series,
    *,
    ptc: float = 0.0,
    ffc: float = 0.0,
) -> pd.DataFrame:
    """Vectorized backtest of a position series against a return series.

    Applies **the** no-look-ahead discipline: the position decided at
    the close of bar ``t`` earns the return of bar ``t+1`` only
    (``position.shift(1) × returns``). Positions are held between
    signals (no resampling of the target series). Costs are charged per
    unit of position change: proportional ``ptc × |Δpos|`` plus a flat
    ``ffc`` per position change (both in return units — fractions of
    capital per bar).

    Parameters
    ----------
    returns : pd.Series
        Per-bar returns (use ``data_loader.compute_returns`` on prices),
        DatetimeIndex, any order but usually ascending.
    position : pd.Series
        Target position/exposure series (-1.0 = fully short, 0 = flat,
        +1.0 = fully long) with an identical index. NaN targets (e.g.
        rolling-window warm-up) are treated as flat (0.0).
    ptc : float, optional
        Proportional transaction cost per unit of position change
        (default 0.0).
    ffc : float, optional
        Flat cost per position change, in return units (default 0.0).

    Returns
    -------
    pd.DataFrame
        One row per bar with columns: ``exposure`` (position held
        during the bar — the shifted target), ``gross`` (pre-cost
        return), ``costs`` (per-bar cost), ``net`` (post-cost return),
        ``equity`` (compounded growth, starting at 1.0).

    Raises
    ------
    ValueError
        If ``position.index`` does not equal ``returns.index``.
    """
    if not returns.index.equals(position.index):
        raise ValueError("returns and position must share an identical index")

    returns = returns.astype(float)
    position = position.astype(float)

    if position.isna().any():
        n = int(position.isna().sum())
        warnings.warn(
            f"{n} NaN target position(s) treated as flat (0.0) — "
            "check warm-up handling"
        )
    ncalls = position.fillna(0.0)

    exposure = ncalls.shift(1).fillna(0.0)          # held during each bar
    delta = ncalls.diff().fillna(ncalls.iloc[0])    # position changes (entry from flat counts)
    change = delta.abs() > 1e-12

    gross = exposure * returns
    costs = ptc * delta.abs() + ffc * change.astype(float)
    # A NaN return (warm-up bar, e.g. pct_change) earns nothing but must
    # NOT wipe out the costs charged that bar.
    net = gross.fillna(0.0) - costs
    equity = (1.0 + net).cumprod()

    return pd.DataFrame(
        {
            "exposure": exposure,
            "gross": gross,
            "costs": costs,
            "net": net,
            "equity": equity,
        },
        index=returns.index,
    )


# ---------------------------------------------------------------------------
# Performance measurement
# ---------------------------------------------------------------------------

def annualized_return(returns: pd.Series, *, periods_per_year: int = 252) -> float:
    """Compound annual growth rate of a return series.

    ``(final_equity)^(periods / n) - 1`` where final equity compounds
    the (NaN-filled) simple returns.

    Parameters
    ----------
    returns : pd.Series
        Per-bar returns, simple (not log).
    periods_per_year : int, optional
        Bars per year for annualization (default 252, daily).

    Returns
    -------
    float
        Annualized growth rate; 0.0 for a series with no valid returns.
    """
    r = returns.dropna().astype(float)
    n = len(r)
    if n == 0:
        return 0.0
    equity = (1.0 + r).prod()
    return float(equity ** (periods_per_year / n) - 1.0)


def annualized_sharpe(
    returns: pd.Series, *, periods_per_year: int = 252, risk_free: float = 0.0
) -> float:
    """Annualized Sharpe ratio, √N_T × (mean − rf) / σ.

    Dollars-neutral default: ``risk_free = 0.0`` because self-financing
    short proceeds fund longs — subtract a risk-free rate only for
    strategies that actually borrow (see ``backtesting-framework`` skill).

    Parameters
    ----------
    returns : pd.Series
        Per-bar returns, simple.
    periods_per_year : int, optional
        Annualization factor (daily 252, hourly NYSE 1638, not 6048).
    risk_free : float, optional
        Per-bar risk-free rate to subtract (default 0.0).

    Returns
    -------
    float
        Annualized Sharpe; 0.0 when fewer than 2 valid returns or the
        sample standard deviation is zero.
    """
    r = returns.dropna().astype(float)
    if len(r) < 2:
        return 0.0
    std = r.std(ddof=1)
    if std == 0.0 or np.isnan(std):
        return 0.0
    return float((r.mean() - risk_free) / std * np.sqrt(periods_per_year))


def max_drawdown(returns: pd.Series) -> float:
    """Maximum drawdown of a return series, as a negative fraction.

    ``dd(t) = equity(t)/hwm(t) − 1`` with running high-water mark; the
    maximum drawdown is the minimum of that series (e.g. −0.20 = a 20%
    peak-to-trough decline). NaN returns are ignored.

    Parameters
    ----------
    returns : pd.Series
        Per-bar returns, simple.

    Returns
    -------
    float
        Most negative drawdown (0.0 for a never-negative equity curve).
    """
    r = returns.astype(float).fillna(0.0)
    equity = (1.0 + r).cumprod()
    hwm = equity.cummax()
    dd = equity / hwm - 1.0
    return float(dd.min())


def drawdown_duration(returns: pd.Series) -> int:
    """Longest consecutive run of bars below the high-water mark.

    Measures time underwater: the longest stretch where the equity curve
    has not yet reclaimed its previous peak (Chan's DD-duration metric).

    Parameters
    ----------
    returns : pd.Series
        Per-bar returns, simple.

    Returns
    -------
    int
        Number of consecutive bars in the longest drawdown; 0 if the
        equity curve never goes underwater.
    """
    r = returns.astype(float).fillna(0.0)
    equity = (1.0 + r).cumprod()
    underwater = equity < equity.cummax()
    if not underwater.any():
        return 0
    groups = (underwater != underwater.shift()).cumsum()
    return int(underwater.groupby(groups).sum().max())


def mar_ratio(returns: pd.Series, *, periods_per_year: int = 252) -> float:
    """MAR ratio: CAGR divided by the maximum drawdown (as a positive
    fraction).

    Leverage-relative, so it ranks strategies on efficiency of risk
    rather than raw growth.

    Parameters
    ----------
    returns : pd.Series
        Per-bar returns, simple.
    periods_per_year : int, optional
        Annualization factor (default 252).

    Returns
    -------
    float
        MAR ratio; ``inf`` when the maximum drawdown is zero.
    """
    cagr = annualized_return(returns, periods_per_year=periods_per_year)
    dd = abs(max_drawdown(returns))
    if dd == 0.0:
        return float("inf")
    return float(cagr / dd)


def performance_summary(
    returns: pd.Series, *, periods_per_year: int = 252, risk_free: float = 0.0
) -> dict[str, float]:
    """One-call performance report for a return series.

    Parameters
    ----------
    returns : pd.Series
        Per-bar returns, simple (net of costs).
    periods_per_year : int, optional
        Annualization factor (default 252).
    risk_free : float, optional
        Per-bar risk-free rate for Sharpe (default 0.0).

    Returns
    -------
    dict[str, float]
        Keys: ``total_return``, ``cagr``, ``ann_vol``, ``sharpe``,
        ``max_drawdown``, ``dd_duration``, ``mar``.
    """
    r = returns.dropna().astype(float)
    n = len(r)
    total = float((1.0 + r).prod() - 1.0) if n else 0.0
    ann_vol = float(r.std(ddof=1) * np.sqrt(periods_per_year)) if n >= 2 else 0.0
    return {
        "total_return": total,
        "cagr": annualized_return(returns, periods_per_year=periods_per_year),
        "ann_vol": ann_vol,
        "sharpe": annualized_sharpe(
            returns, periods_per_year=periods_per_year, risk_free=risk_free
        ),
        "max_drawdown": max_drawdown(returns),
        "dd_duration": float(drawdown_duration(returns)),
        "mar": mar_ratio(returns, periods_per_year=periods_per_year),
    }


# ---------------------------------------------------------------------------
# Tier 2 — bar-by-bar engine
# ---------------------------------------------------------------------------

class _State:
    """Read-only view handed to a strategy at the close of each bar.

    Only data realized up to and including the current bar is visible,
    so a strategy literally cannot peek at future returns.
    """

    __slots__ = ("bar", "timestamp", "returns", "prices", "equity", "peak")

    def __init__(self, bar, timestamp, returns, prices, equity, peak):
        self.bar = bar
        self.timestamp = timestamp
        self.returns = returns          # returns[:bar+1] (numpy view)
        self.prices = prices            # prices[:bar+1] or None
        self.equity = equity            # equity[:bar+1] (after costs)
        self.peak = peak                # running equity high-water mark


class BacktestEngine:
    """Bar-by-bar backtest engine for a single-asset return stream.

    A lean Tier-2 loop in the QSTrader spirit. At the close of each bar
    the engine calls the strategy with a read-only :class:`_State` view
    (data up to and including that bar only); the strategy returns a
    target exposure for the *next* bar, which the engine clamps to
    ``max_exposure``. Orders therefore always execute one bar late —
    the no-look-ahead rule is guaranteed by construction, not by
    caller discipline.

    Costs are charged in cash at the moment the order is placed:
    proportional ``ptc`` on the traded notional plus a flat ``ffc`` per
    position change. On an optional ``stop_loss`` breach the engine
    liquidates (charging exit costs) and halts trading for the rest of
    the run.

    Parameters
    ----------
    capital : float, optional
        Starting account equity (default 1,000,000).
    ptc : float, optional
        Proportional cost per unit of exposure traded (default 0.0).
    ffc : float, optional
        Flat cost per order, in currency units (default 0.0).
    max_exposure : float, optional
        Clamp on target exposure magnitude (default 1.0 — no leverage;
        set > 1 to allow it).
    stop_loss : float | None, optional
        Fractional equity drawdown from the running peak that triggers
        liquidation and a trading halt (default None = disabled).
    execution_cost_fn : Callable[[float, int], float] | None, optional
        Optional impact-aware cost hook ``fn(delta, bar) -> cost in
        currency`` charged *in addition* to the flat ``ptc``/``ffc``
        model. Receives the signed exposure delta and the bar index;
        must be deterministic given the state visible at that bar
        (no look-ahead). Default None = legacy flat cost only.
    """

    def __init__(
        self,
        *,
        capital: float = 1_000_000.0,
        ptc: float = 0.0,
        ffc: float = 0.0,
        max_exposure: float = 1.0,
        stop_loss: float | None = None,
        execution_cost_fn: Callable[[float, int], float] | None = None,
    ):
        if capital <= 0:
            raise ValueError("capital must be positive")
        if ptc < 0 or ffc < 0:
            raise ValueError("costs must be non-negative")
        if max_exposure <= 0:
            raise ValueError("max_exposure must be positive")
        if stop_loss is not None and not 0 < stop_loss < 1:
            raise ValueError("stop_loss must be in (0, 1)")
        self.capital = float(capital)
        self.ptc = float(ptc)
        self.ffc = float(ffc)
        self.max_exposure = float(max_exposure)
        self.stop_loss = float(stop_loss) if stop_loss is not None else None
        self.execution_cost_fn = execution_cost_fn
        self.trades: list[dict] = []
        self.stopped = False
        self.stop_bar: int | None = None

    def run(
        self,
        returns: pd.Series,
        strategy: Callable[[_State], float],
        *,
        prices: pd.Series | None = None,
    ) -> pd.DataFrame:
        """Run the engine over a return series.

        Parameters
        ----------
        returns : pd.Series
            Per-bar returns, simple; DatetimeIndex optional.
        strategy : Callable[[_State], float]
            ``strategy(state) -> target exposure`` called at the close of
            each bar. ``state`` exposes ``bar`` (int), ``timestamp``,
            ``returns``, ``prices`` (or None), ``equity``, and ``peak``
            — all sliced to include only realized history.
        prices : pd.Series | None, optional
            Optional price series with the same index as ``returns``,
            made available to the strategy for signal computation.

        Returns
        -------
        pd.DataFrame
            One row per bar: ``exposure`` (held during the bar),
            ``gross`` (exposure × return), ``cost`` (cash cost charged
            at the previous close, in currency), ``net`` (per-bar net
            return), ``equity`` (account equity after the bar).
            Engine state after the run: ``trades`` (list of order
            dicts), ``stopped`` / ``stop_bar``.
        """
        if not isinstance(returns, pd.Series) or len(returns) == 0:
            raise ValueError("returns must be a non-empty Series")
        returns = returns.astype(float)
        if prices is not None:
            if not returns.index.equals(prices.index):
                raise ValueError("prices must share returns' index")

        r = returns.to_numpy(dtype=float)
        if np.isnan(r).any():
            n_nan = int(np.isnan(r).sum())
            warnings.warn(
                f"{n_nan} NaN return(s) treated as 0.0 (no P&L, no stop "
                "effect) — check warm-up handling"
            )
            r = np.nan_to_num(r, nan=0.0)
        idx = returns.index
        p = prices.to_numpy(dtype=float) if prices is not None else None
        n = len(r)

        equity = np.empty(n + 1)
        equity[0] = self.capital
        exposure = 0.0
        peak = self.capital
        exposure_held = np.zeros(n)
        gross = np.zeros(n)
        costs = np.zeros(n)
        self.trades = []
        self.stopped = False
        self.stop_bar = None

        for i in range(n):
            # 1. Realize the return from the exposure held during bar i.
            equity[i + 1] = equity[i] * (1.0 + exposure * r[i])
            peak = max(peak, equity[i + 1])
            exposure_held[i] = exposure
            gross[i] = exposure * r[i]

            # 2. Stop check at the close of bar i.
            if (
                not self.stopped
                and self.stop_loss is not None
                and equity[i + 1] <= peak * (1.0 - self.stop_loss)
            ):
                self.stopped = True
                self.stop_bar = i

            # 3. Decide the target exposure for bar i+1 (close of bar i).
            if self.stopped:
                target = 0.0
            else:
                state = _State(
                    bar=i,
                    timestamp=idx[i],
                    returns=r[: i + 1],
                    prices=p[: i + 1] if p is not None else None,
                    equity=equity[: i + 1],
                    peak=peak,
                )
                target = float(strategy(state))
                target = float(np.clip(target, -self.max_exposure, self.max_exposure))

            # 4. Charge the order cost now, execute from the next bar.
            # On the FINAL bar there is no next bar, so the decision can
            # never be held — skip it rather than charging a dead order.
            delta = 0.0 if i == n - 1 else target - exposure
            if abs(delta) > 1e-12:
                cost = self.ptc * self.capital * abs(delta) + self.ffc
                if self.execution_cost_fn is not None:
                    cost += float(self.execution_cost_fn(delta, i))
                self.trades.append(
                    {
                        "bar": i,
                        "timestamp": idx[i],
                        "from_exposure": float(exposure),
                        "to_exposure": float(target),
                        "cost": float(cost),
                    }
                )
            else:
                cost = 0.0
            equity[i + 1] -= cost
            costs[i] = cost
            exposure = target

        net = equity[1:] / equity[:-1] - 1.0

        return pd.DataFrame(
            {
                "exposure": exposure_held,
                "gross": gross,
                "cost": costs,
                "net": net,
                "equity": equity[1:],
            },
            index=idx,
        )