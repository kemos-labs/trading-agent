"""Position sizing: Kelly, fractional Kelly, and Carver vol targeting.

Module 4 of the Phase 2 core toolkit (ROADMAP). Implements the sizing
discipline distilled in ``skills/kelly-position-sizing`` (Sinclair,
*Volatility Trading* ch8) and ``skills/volatility-targeted-position-
sizing`` (Carver, *Systematic Trading* ch5/9/10):

- **Kelly**: continuous ``f* = m/σ²`` from a return history and the
  discrete Bernoulli form ``f* = p − q/b``; output is a *fraction of
  capital* to stake. Use fractional Kelly (multiply by 0.25–0.5) —
  full Kelly over-bets on estimated edges.
- **Vol targeting (robust proxy)**: when edge estimates are too noisy
  for Kelly, hold ``target_vol / realized_vol`` weights, re-estimating
  vol on a rolling window and clipping leverage.
- **Carver pipeline**: forecast (−20…+20) → subsystem position in whole
  blocks via the volatility scalar, sized so every instrument/rule
  contributes equal expected risk at a fixed percentage-vol target.

Fail-closed rules from the skills: never divide by zero or negative
variance, keep intermediate values fractional (round only at the final
target position), and never size from simulated data.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

__all__ = [
    "carver_position",
    "cash_vol_target",
    "discrete_kelly",
    "instrument_value_volatility",
    "kelly_fraction",
    "subsystem_position",
    "vol_target_weight",
    "volatility_scalar",
]


def kelly_fraction(returns: pd.Series, *, fraction: float = 1.0) -> float:
    """Continuous Kelly fraction ``f* = m / σ²`` of capital to stake.

    ``m`` and ``σ²`` are the sample mean and variance of the per-trade
    or per-period returns. With ``fraction < 1`` this is fractional
    Kelly (recommended range 0.25–0.5): growth drops mildly, tail risk
    and estimation-error damage fall sharply. Zero or negative variance
    (flat/no-trade history) returns 0.0 rather than dividing by zero.

    Parameters
    ----------
    returns : pd.Series
        Per-trade (or per-period) strategy returns, simple.
    fraction : float, optional
        Fractional-Kelly multiplier (default 1.0 = full Kelly).

    Returns
    -------
    float
        Fraction of capital; may exceed 1.0 for very high edge, so the
        caller should cap leverage before use.
    """
    if fraction <= 0:
        raise ValueError("fraction must be positive")
    r = returns.dropna().astype(float)
    n = len(r)
    if n < 2:
        return 0.0
    var = r.var(ddof=1)
    if var <= 0 or np.isnan(var):
        return 0.0
    return float(r.mean() / var * fraction)


def discrete_kelly(p: float, b: float) -> float:
    """Discrete Kelly for a Bernoulli bet: ``f* = (b·p − q) / b = p − q/b``.

    For win probability ``p``, loss probability ``q = 1 − p``, and
    payoff odds ``b`` (net gain per unit staked, e.g. 1.0 = win doubles
    the stake). Negative results mean the bet is losing in expectation
    — the correct Kelly is "no bet" (stake 0), not a negative stake.

    Parameters
    ----------
    p : float
        Win probability, in (0, 1).
    b : float
        Net payoff odds, > 0.

    Returns
    -------
    float
        Fraction of capital to stake; ≤ 0 means the bet has no edge.
    """
    if not 0 < p < 1:
        raise ValueError("p must be in (0, 1)")
    if b <= 0:
        raise ValueError("b (payoff odds) must be positive")
    return float(p - (1.0 - p) / b)


def vol_target_weight(
    returns: pd.Series,
    target_vol: float,
    *,
    lookback: int = 60,
    annualization: int = 252,
    max_weight: float = 3.0,
) -> pd.Series:
    """Rolling volatility-target weight: ``target_vol / realized_vol``.

    The robust Kelly proxy from ``kelly-position-sizing``: only the
    variance must be estimated, not the mean, so it survives noisy edge
    estimates. Realized vol is the rolling sample std of returns
    annualized by ``√annualization``; weights are clipped at
    ``max_weight`` (leverage cap) and 0 where vol is not yet measured
    (insufficient history / NaN returns).

    Parameters
    ----------
    returns : pd.Series
        Per-period strategy/asset returns, simple.
    target_vol : float
        Desired annualized volatility (e.g. 0.10 = 10%).
    lookback : int, optional
        Rolling window for the volatility estimate (default 60).
    annualization : int, optional
        Periods per year (default 252).
    max_weight : float, optional
        Upper clip on the weight (default 3.0).

    Returns
    -------
    pd.Series
        Weight series aligned with ``returns``; 0.0 in the warm-up
        window (and where returns are NaN).
    """
    if target_vol <= 0:
        raise ValueError("target_vol must be positive")
    if lookback < 2:
        raise ValueError("lookback must be >= 2")
    rv = returns.astype(float).rolling(lookback).std(ddof=1) * np.sqrt(annualization)
    with np.errstate(divide="ignore", invalid="ignore"):
        w = target_vol / rv
    return w.clip(upper=max_weight).fillna(0.0)


def cash_vol_target(capital: float, annual_vol_target: float, *, periods: int = 256) -> float:
    """Daily cash volatility budget: ``capital × target / √periods``.

    Carver's daily cash vol target: the per-bar P&L standard deviation
    consistent with an annualized % volatility target on trading
    capital. Carver uses √256 ≈ 16 as "the number of trading days in a
    year"; pass ``periods=252`` for the calendar-year convention.

    Parameters
    ----------
    capital : float
        Trading capital.
    annual_vol_target : float
        Annualized volatility target as a fraction (e.g. 0.20 = 20%).
    periods : int, optional
        Trading periods per year for the daily budget (default 256).

    Returns
    -------
    float
        Daily cash volatility target.
    """
    if capital <= 0 or annual_vol_target <= 0 or periods <= 0:
        raise ValueError("capital, annual_vol_target and periods must be positive")
    return float(capital * annual_vol_target / np.sqrt(periods))


def instrument_value_volatility(
    price_vol: float, block_value: float, *, fx: float = 1.0
) -> float:
    """Per-block daily P&L volatility of one instrument in account
    currency.

    ``block_value × price_vol × fx`` — how much one unit ("block": 1
    share, 1 futures contract, £1/point) loses/gains per 1% price move,
    converted into account currency via the FX rate.

    Parameters
    ----------
    price_vol : float
        Expected daily std of % returns (fraction, e.g. 0.02 = 2%).
    block_value : float
        Currency exposure per unit block.
    fx : float, optional
        Instrument currency → account currency rate (default 1.0).

    Returns
    -------
    float
        Daily P&L volatility per block, account currency.
    """
    if price_vol < 0 or block_value < 0 or fx <= 0:
        raise ValueError("price_vol/block_value must be >= 0 and fx > 0")
    return float(block_value * price_vol * fx)


def volatility_scalar(cash_vol_target: float, inv_vol: float) -> float:
    """Position (in blocks) consistent with a constant forecast of +10.

    ``cash_vol_target / inv_vol``: the scalar that equalizes expected
    risk across instruments/rules. Carver's volatility scalar is the
    position whose per-bar P&L vol equals the cash target.

    Parameters
    ----------
    cash_vol_target : float
        Daily cash volatility target (see :func:`cash_vol_target`).
    inv_vol : float
        Per-block daily P&L volatility (see
        :func:`instrument_value_volatility`).

    Returns
    -------
    float
        Volatility scalar in blocks; fractional values are correct and
        must not be rounded at this stage.
    """
    if inv_vol <= 0:
        raise ValueError("instrument value volatility must be positive (low-vol instruments are untradeable)")
    return float(cash_vol_target / inv_vol)


def subsystem_position(scalar: float, forecast: float, *, cap: float = 20.0) -> float:
    """Subsystem position from a forecast: ``scalar × forecast / 10``.

    Forecasts are scaled −20…+20 with expected |·| = 10 (Carver's
    convention, also produced by combined-forecast rules); the position
    caps at ``±cap`` (default 20, i.e. 2× the constant-forecast-10
    position).

    Parameters
    ----------
    scalar : float
        Volatility scalar (see :func:`volatility_scalar`).
    forecast : float
        Signal strength in −20…+20 units; values outside are clipped.
    cap : float, optional
        Forecast magnitude cap (default 20).

    Returns
    -------
    float
        Position in blocks (fractional until the final position is
        rounded by the caller).
    """
    if cap <= 0:
        raise ValueError("cap must be positive")
    f = float(np.clip(forecast, -abs(cap), abs(cap)))
    return float(scalar * f / 10.0)


def carver_position(
    capital: float,
    annual_vol_target: float,
    price_vol: float,
    block_value: float,
    forecast: float,
    *,
    fx: float = 1.0,
    periods: int = 256,
    cap: float = 20.0,
    round_blocks: bool = False,
) -> float:
    """End-to-end Carver position: capital + target + instrument → blocks.

    One-call version of the pipeline (:func:`cash_vol_target` →
    :func:`instrument_value_volatility` → :func:`volatility_scalar` →
    :func:`subsystem_position`). Size the position so the instrument
    contributes ``annual_vol_target`` of expected risk at the current
    forecast.

    Parameters
    ----------
    capital : float
        Trading capital (account currency).
    annual_vol_target : float
        Annualized % vol target (fraction).
    price_vol : float
        Instrument's expected daily %-return vol (fraction).
    block_value : float
        Currency exposure per block.
    forecast : float
        Signal in −20…+20 units.
    fx : float, optional
        Instrument → account FX rate (default 1.0).
    periods : int, optional
        Trading days per year (default 256, Carver's √256).
    cap : float, optional
        Forecast magnitude cap (default 20).
    round_blocks : bool, optional
        Round to whole blocks (default False — round only at the final
        trading position, never intermediate values).

    Returns
    -------
    float
        Position in blocks (fractional unless ``round_blocks``).
    """
    budget = cash_vol_target(capital, annual_vol_target, periods=periods)
    ivv = instrument_value_volatility(price_vol, block_value, fx=fx)
    scalar = volatility_scalar(budget, ivv)
    pos = subsystem_position(scalar, forecast, cap=cap)
    return float(round(pos)) if round_blocks else pos