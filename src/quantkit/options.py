"""Vanilla options: BSM prices, Greeks, put-call parity, implied volatility.

Module 3 of the Phase 2 core toolkit (ROADMAP). Implements the closed
forms distilled in ``skills/options-pricing`` (Natenberg ch18, Alexander
MRA Vol. III ch III.3):

- Generalized Black-Scholes-Merton with the **carry adjustment b**, one
  formula for three markets — stock ``b = r − q``, futures/Black-76
  ``b = 0``, FX ``b = r_dom − r_for``;
- the five Greeks (delta, gamma, vega, theta, rho) with the
  ``e^{(b−r)t}`` carry factor applied to the spot-dependent rows;
- put-call parity as the no-arbitrage backbone and missing-side solver;
- implied volatility by bisection, failing closed when the market price
  is outside the achievable range.

All functions are numpy-vectorized (scipy.stats.norm) and return
floats for scalar arguments; inputs are validated and degenerate inputs
(t ≤ 0, σ ≤ 0, non-positive spot/strike) raise ``ValueError`` rather
than returning garbage. Numerical methods (tree, Monte Carlo/LSM) for
American/exotic payoffs live in the skill files, not here.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import norm

__all__ = [
    "bs_greeks",
    "bs_price",
    "call_from_put",
    "implied_vol",
    "put_call_parity",
    "put_from_call",
]

_OPTIONS = ("call", "put")


def _validate(option: str, *, times, spots, strikes, sigmas) -> None:
    if option not in _OPTIONS:
        raise ValueError(f"option must be one of {_OPTIONS}, got {option!r}")
    if np.any(spots <= 0) or np.any(strikes <= 0):
        raise ValueError("spot and strike must be strictly positive")
    if np.any(times <= 0):
        raise ValueError("time to expiry t must be > 0 (use a tree/MC for t=0)")
    if np.any(sigmas <= 0):
        raise ValueError("volatility sigma must be > 0")


def _as_float_or_array(*args):
    """Convert args to float arrays; return scalars when all were scalar."""
    out = [np.asarray(a, dtype=float) for a in args]
    scalar = all(a.ndim == 0 for a in out)
    if scalar:
        return [float(a) for a in out]
    return out


def bs_price(
    S: float | np.ndarray,
    X: float | np.ndarray,
    t: float | np.ndarray,
    r: float | np.ndarray,
    sigma: float | np.ndarray,
    b: float | np.ndarray,
    option: str = "call",
) -> float | np.ndarray:
    """Generalized Black-Scholes-Merton price of a European vanilla.

    Carry-adjustment b makes one closed form cover stocks (``b = r``,
    or ``b = r − q`` with dividend yield q), futures/Black-76
    (``b = 0``), and FX (``b = r_dom − r_for``):

    ``d1 = [ln(S/X) + (b + σ²/2)·t] / (σ·√t)``
    ``d2 = d1 − σ·√t``
    ``C = S·e^((b−r)t)·N(d1) − X·e^(−rt)·N(d2)``
    ``P = X·e^(−rt)·N(−d2) − S·e^((b−r)t)·N(−d1)``

    Parameters
    ----------
    S, X, t, r, sigma, b : float | np.ndarray
        Spot, strike, time to expiry (years, > 0), risk-free rate,
        volatility (> 0), carry rate. All broadcastable; either all
        scalar or any mix of scalars/arrays.
    option : str, optional
        ``"call"`` (default) or ``"put"``.

    Returns
    -------
    float | np.ndarray
        Model price, scalar when all inputs are scalar.

    Raises
    ------
    ValueError
        On invalid option, t ≤ 0, sigma ≤ 0, or non-positive S/X.
    """
    S, X, t, r, sigma, b = _as_float_or_array(S, X, t, r, sigma, b)
    _validate(option, times=t, spots=S, strikes=X, sigmas=sigma)
    S, X, t, r, sigma, b = map(np.asarray, (S, X, t, r, sigma, b))

    d1 = (np.log(S / X) + (b + sigma ** 2 / 2.0) * t) / (sigma * np.sqrt(t))
    d2 = d1 - sigma * np.sqrt(t)
    carry = np.exp((b - r) * t)
    disc = np.exp(-r * t)

    if option == "call":
        price = S * carry * norm.cdf(d1) - X * disc * norm.cdf(d2)
    else:
        price = X * disc * norm.cdf(-d2) - S * carry * norm.cdf(-d1)

    return float(price) if np.ndim(price) == 0 else price


def put_call_parity(
    S: float, X: float, t: float, r: float, b: float
) -> float:
    """Parity price difference ``C − P = S·e^((b−r)t) − X·e^(−rt)``.

    The no-arbitrage backbone for European options at the same
    strike/maturity: a violation of the relation means mispricing in
    one of the four legs (call, put, spot, bond).

    Parameters
    ----------
    S, X, t, r, b : float
        Spot, strike, time to expiry, rate, carry.

    Returns
    -------
    float
        The value of ``C − P`` implied by parity (for a non-dividend
        stock with ``b = r`` this is ``S − X·e^(−rT)``).
    """
    S, X, t, r, b = _as_float_or_array(S, X, t, r, b)
    out = S * np.exp((b - r) * t) - X * np.exp(-r * t)
    return float(out) if np.ndim(out) == 0 else out


def call_from_put(put: float, S: float, X: float, t: float, r: float, b: float) -> float:
    """Price the call from the put via parity (and vice versa for
    :func:`put_from_call`)."""
    return put + put_call_parity(S, X, t, r, b)


def put_from_call(call: float, S: float, X: float, t: float, r: float, b: float) -> float:
    """Price the put from the call via parity."""
    return call - put_call_parity(S, X, t, r, b)


def bs_greeks(
    S: float | np.ndarray,
    X: float | np.ndarray,
    t: float | np.ndarray,
    r: float | np.ndarray,
    sigma: float | np.ndarray,
    b: float | np.ndarray,
    option: str = "call",
) -> dict[str, float | np.ndarray]:
    """The five BSM Greeks for a European vanilla.

    Includes the carry factor ``e^((b−r)t)`` on the spot-dependent rows,
    so the same formulas serve stocks, futures (Black-76) and FX:
    delta = carry·N(d1) [call] / carry·(N(d1)−1) [put]; gamma =
    carry·φ(d1)/(S·σ·√t); vega = S·carry·φ(d1)·√t; theta (per year,
    −∂V/∂t): call ``−carry·S·φ(d1)·σ/(2√t) − (b−r)·carry·S·N(d1) −
    r·X·e^(−rt)·N(d2)``, put with flipped sign terms on the N(·) pieces;
    rho = X·t·e^(−rt)·N(d2) [call] / ``−X·t·e^(−rt)·N(−d2)`` [put].

    Parameters
    ----------
    S, X, t, r, sigma, b, option
        As in :func:`bs_price`.

    Returns
    -------
    dict[str, float | np.ndarray]
        Keys ``delta``, ``gamma``, ``vega``, ``theta``, ``rho``; greeks
        on the *price* per unit input (vega per +1.0 vol, rho per +1.0
        rate, theta per year). Scalar when all inputs are scalar.
    """
    S, X, t, r, sigma, b = _as_float_or_array(S, X, t, r, sigma, b)
    _validate(option, times=t, spots=S, strikes=X, sigmas=sigma)
    S, X, t, r, sigma, b = map(np.asarray, (S, X, t, r, sigma, b))

    sqrt_t = np.sqrt(t)
    d1 = (np.log(S / X) + (b + sigma ** 2 / 2.0) * t) / (sigma * sqrt_t)
    d2 = d1 - sigma * sqrt_t
    carry = np.exp((b - r) * t)
    disc = np.exp(-r * t)
    phi = norm.pdf(d1)

    if option == "call":
        delta = carry * norm.cdf(d1)
        theta = (
            -(carry * S * phi * sigma) / (2.0 * sqrt_t)
            - (b - r) * carry * S * norm.cdf(d1)
            - r * X * disc * norm.cdf(d2)
        )
        rho = X * t * disc * norm.cdf(d2)
    else:
        delta = carry * (norm.cdf(d1) - 1.0)
        theta = (
            -(carry * S * phi * sigma) / (2.0 * sqrt_t)
            + (b - r) * carry * S * norm.cdf(-d1)
            + r * X * disc * norm.cdf(-d2)
        )
        rho = -X * t * disc * norm.cdf(-d2)

    gamma = carry * phi / (S * sigma * sqrt_t)
    vega = S * carry * phi * sqrt_t

    greeks = {"delta": delta, "gamma": gamma, "vega": vega, "theta": theta, "rho": rho}
    if all(np.ndim(v) == 0 for v in greeks.values()):
        return {k: float(v) for k, v in greeks.items()}
    return greeks


def implied_vol(
    market_price: float,
    S: float,
    X: float,
    t: float,
    r: float,
    b: float,
    option: str = "call",
    *,
    lo: float = 1e-4,
    hi: float = 5.0,
    tol: float = 1e-8,
) -> float:
    """Implied volatility by bisection: the σ making the model price
    equal the market price.

    Vega is strictly positive, so price is monotone in σ and bisection
    is safe (Natenberg ch18; ``options-pricing`` skill). Fails closed:
    a market price outside the achievable band raises ``ValueError`` —
    e.g. a call priced above the discounted forward ``S·e^((b−r)t)``,
    or below the intrinsic floor.

    Parameters
    ----------
    market_price : float
        Observed option price (> 0).
    S, X, t, r, b, option
        As in :func:`bs_price`.
    lo, hi : float, optional
        Initial volatility bracket (default 1e-4…5.0); ``hi`` expands
        ×2 automatically while the upper price is too low.
    tol : float, optional
        Width of the final bracket in vol units (default 1e-8).

    Returns
    -------
    float
        Implied volatility.

    Raises
    ------
    ValueError
        If the market price is not achievable by any σ in the
        (expanded) bracket.
    """
    if market_price <= 0:
        raise ValueError("market_price must be positive")
    if lo >= hi:
        raise ValueError("lo must be < hi")

    floor = 0.0
    max_spot = S * np.exp((b - r) * t)
    if market_price > max_spot and option == "call":
        raise ValueError(
            f"call price {market_price:.6g} exceeds the discounted forward "
            f"{max_spot:.6g} — unachievable"
        )
    # Put floor: intrinsic bound X·e^(−rt) − S·e^((b−r)t), floored at 0.
    put_floor = X * np.exp(-r * t) - max_spot
    if option == "put" and market_price < max(0.0, put_floor):
        raise ValueError(
            f"put price {market_price:.6g} below the intrinsic floor "
            f"{max(0.0, put_floor):.6g} — unachievable"
        )
    del floor

    while bs_price(S, X, t, r, hi, b, option) < market_price and hi < 1e4:
        hi *= 2.0
    if bs_price(S, X, t, r, hi, b, option) < market_price:
        raise ValueError("market price exceeds the model price at the bracket ceiling")

    for _ in range(200):  # 200 bisections ≈ 1e-8 on a 1e4-wide bracket
        mid = 0.5 * (lo + hi)
        if bs_price(S, X, t, r, mid, b, option) > market_price:
            hi = mid
        else:
            lo = mid
        if hi - lo < tol:
            break
    return 0.5 * (lo + hi)