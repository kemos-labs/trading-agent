"""Tests for quantkit.options (stdlib unittest — no pytest in venv).

Reference values are hand-computed from the BSM closed forms:
S=X=$100, t=1y, sigma=20% => d1 = (0 + (r-0r + 0.02))/0.2 and the
textbook ATM call of ~$10.45 at r=5%. Run:
    .venv/bin/python -m unittest discover -s tests -v
"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import numpy as np

from quantkit import options as opt


class TestBsPrice(unittest.TestCase):
    def test_atm_call_reference(self):
        # Classic textbook case: S=X=100, t=1, r=5%, sigma=20%, b=r -> C ~ 10.45.
        C = opt.bs_price(100, 100, 1.0, 0.05, 0.20, 0.05, option="call")
        self.assertAlmostEqual(C, 10.45, places=2)

    def test_zero_rates_symmetric_atm(self):
        # S=X=100, t=1, r=0, sigma=0.2: C = 100*(N(0.1) - N(-0.1)) = 7.9656.
        C = opt.bs_price(100, 100, 1.0, 0.0, 0.20, 0.0, option="call")
        P = opt.bs_price(100, 100, 1.0, 0.0, 0.20, 0.0, option="put")
        self.assertAlmostEqual(C, 7.9656, places=3)
        self.assertAlmostEqual(P, C, places=9)  # symmetry at r=0, b=r

    def test_put_call_parity_holds(self):
        # b=r => C - P = S - X*exp(-rT)
        C = opt.bs_price(100, 100, 1.0, 0.05, 0.20, 0.05, option="call")
        P = opt.bs_price(100, 100, 1.0, 0.05, 0.20, 0.05, option="put")
        self.assertAlmostEqual(
            C - P, 100.0 - 100.0 * math.exp(-0.05), places=9
        )

    def test_black76_futures(self):
        # b=0 (Black-76): same price as zero-rate stock case for ATM future.
        C = opt.bs_price(100, 100, 1.0, 0.0, 0.20, 0.0, option="call")
        self.assertAlmostEqual(C, 7.9656, places=3)

    def test_vectorized_prices(self):
        S = np.array([90.0, 100.0, 110.0])
        out = opt.bs_price(S, 100, 1.0, 0.05, 0.20, 0.05)
        self.assertEqual(out.shape, (3,))
        # Deep ITM call > S - Xe^-rT (lower bound); ITM call also exceeds
        # the intrinsic-style bound S - Xe^-rT for the higher spot.
        self.assertGreater(out[0], 90.0 - 100.0 * math.exp(-0.05))
        self.assertGreater(out[2], 110.0 - 100.0 * math.exp(-0.05))
        self.assertLess(out[2], 110.0)

    def test_scalar_broadcast_with_array(self):
        out = opt.bs_price(100, np.array([95.0, 100.0, 105.0]), 1.0, 0.05, 0.20, 0.05)
        self.assertEqual(out.shape, (3,))

    def test_invalid_inputs_raise(self):
        with self.assertRaises(ValueError):
            opt.bs_price(0, 100, 1.0, 0.05, 0.20, 0.05)
        with self.assertRaises(ValueError):
            opt.bs_price(100, 0, 1.0, 0.05, 0.20, 0.05)
        with self.assertRaises(ValueError):
            opt.bs_price(100, 100, 0.0, 0.05, 0.20, 0.05)
        with self.assertRaises(ValueError):
            opt.bs_price(100, 100, 1.0, 0.05, 0.0, 0.05)
        with self.assertRaises(ValueError):
            opt.bs_price(100, 100, 1.0, 0.05, 0.2, 0.05, option="straddle")


class TestPutCallParity(unittest.TestCase):
    def test_parity_value_stock(self):
        # b=r => C - P = S - Xe^-rT
        self.assertAlmostEqual(
            opt.put_call_parity(100, 100, 1.0, 0.05, 0.05),
            100.0 - 100.0 * math.exp(-0.05),
            places=10,
        )

    def test_parity_value_futures(self):
        # b=0 => C - P = F*e^-rT - X*e^-rT (equals zero for ATM future)
        self.assertAlmostEqual(
            opt.put_call_parity(100, 100, 1.0, 0.05, 0.0), 0.0, places=10
        )

    def test_derive_missing_side(self):
        C = opt.bs_price(105, 100, 0.5, 0.03, 0.25, 0.03, option="call")
        P = opt.put_from_call(C, 105, 100, 0.5, 0.03, 0.03)
        self.assertAlmostEqual(
            P, opt.bs_price(105, 100, 0.5, 0.03, 0.25, 0.03, option="put"), places=9
        )
        self.assertAlmostEqual(
            opt.call_from_put(P, 105, 100, 0.5, 0.03, 0.03), C, places=9
        )


class TestGreeks(unittest.TestCase):
    def test_atm_delta(self):
        g = opt.bs_greeks(100, 100, 1.0, 0.05, 0.20, 0.05)
        # d1 = (0.05 + 0.02)/0.2 = 0.35 -> N(0.35) = 0.6368
        self.assertAlmostEqual(g["delta"], 0.6368, places=3)
        self.assertAlmostEqual(g["delta"] - 1.0, -0.3632, places=3)

    def test_put_delta(self):
        from scipy.stats import norm
        g = opt.bs_greeks(100, 100, 1.0, 0.05, 0.20, 0.05, option="put")
        # b=r -> carry factor 1; delta = N(d1) - 1 with d1 = 0.35.
        self.assertAlmostEqual(g["delta"], norm.cdf(0.35) - 1.0, places=9)

    def test_atm_vega_gamma(self):
        g = opt.bs_greeks(100, 100, 1.0, 0.05, 0.20, 0.05)
        # phi(0.35) = 0.37524; vega = S*phi*sqrt(t) = 37.52; gamma = phi/(S*sigma) = 0.01876
        self.assertAlmostEqual(g["vega"], 37.52, places=1)
        self.assertAlmostEqual(g["gamma"], 0.01876, places=4)

    def test_rho_call(self):
        g = opt.bs_greeks(100, 100, 1.0, 0.05, 0.20, 0.05)
        # X*t*e^-rT*N(d2) with d2 = 0.15, N(0.15) = 0.5596, e^-0.05 = 0.95123
        self.assertAlmostEqual(g["rho"], 100.0 * math.exp(-0.05) * 0.5596, places=2)

    def test_finite_difference_crosscheck(self):
        h = 1.0  # 1% of S=100
        S, X, t, r, sigma, b = 105.0, 100.0, 0.5, 0.03, 0.25, 0.03
        g = opt.bs_greeks(S, X, t, r, sigma, b)
        v_up = opt.bs_price(S + h, X, t, r, sigma, b)
        v_dn = opt.bs_price(S - h, X, t, r, sigma, b)
        v_c = opt.bs_price(S, X, t, r, sigma, b)
        self.assertAlmostEqual(g["delta"], (v_up - v_dn) / (2 * h), places=3)  # FD error ~ gamma*h/2
        self.assertAlmostEqual(g["gamma"], (v_up - 2 * v_c + v_dn) / h ** 2, places=4)

        dr = 1e-4
        # Stock convention: b = r - q with q = 0, so perturbing r must
        # perturb b along with it (rho = dV/dr holding the market setup).
        v_r_up = opt.bs_price(S, X, t, r + dr, sigma, b + dr)
        v_r_dn = opt.bs_price(S, X, t, r - dr, sigma, b - dr)
        self.assertAlmostEqual(g["rho"], (v_r_up - v_r_dn) / (2 * dr), places=3)

    def test_theta_sign_is_negative_for_long_call(self):
        g = opt.bs_greeks(100, 100, 1.0, 0.05, 0.20, 0.05)
        self.assertLess(g["theta"], 0.0)

    def test_carries_for_futures(self):
        # b=0 (futures): d1 = (b + sigma^2/2)t / (sigma sqrt(t)) = 0.1,
        # delta = e^-rT*N(d1).
        g = opt.bs_greeks(100, 100, 1.0, 0.05, 0.20, 0.0)
        from scipy.stats import norm
        self.assertAlmostEqual(
            g["delta"], math.exp(-0.05) * float(norm.cdf(0.1)), places=6
        )


class TestImpliedVol(unittest.TestCase):
    def test_round_trip(self):
        S, X, t, r, b = 100.0, 105.0, 0.25, 0.02, 0.02
        for sigma in (0.1, 0.25, 0.6):
            price = opt.bs_price(S, X, t, r, sigma, b)
            iv = opt.implied_vol(price, S, X, t, r, b)
            self.assertAlmostEqual(iv, sigma, places=6)

    def test_put_round_trip(self):
        S, X, t, r, b = 95.0, 100.0, 0.5, 0.03, 0.03
        price = opt.bs_price(S, X, t, r, 0.4, b, option="put")
        iv = opt.implied_vol(price, S, X, t, r, b, option="put")
        self.assertAlmostEqual(iv, 0.4, places=6)

    def test_unachievable_call_price_raises(self):
        # Call price above the discounted forward is impossible.
        with self.assertRaises(ValueError):
            opt.implied_vol(110.0, 100, 90.0, 1.0, 0.0, 0.0)

    def test_unachievable_put_price_raises(self):
        # Put price below the intrinsic floor is impossible.
        with self.assertRaises(ValueError):
            opt.implied_vol(0.01, 100, 150.0, 1.0, 0.0, 0.0, option="put")

    def test_nonpositive_price_raises(self):
        with self.assertRaises(ValueError):
            opt.implied_vol(-1.0, 100, 100, 1.0, 0.05, 0.05)


if __name__ == "__main__":
    unittest.main()