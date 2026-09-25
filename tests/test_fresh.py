"""Tests for quantkit.fresh — mocked transports, no network, no keys."""

import json
import unittest

import pandas as pd

from quantkit.fresh import (
    QuotaLedger,
    fetch_alphavantage_daily,
    fetch_finnhub_quote,
    fetch_massive_aggs,
    load_terminal_keys,
    normalize_massive,
    pull_symbol,
)


def _massive_payload():
    return {"status": "OK", "results": [
        {"t": 1756785600000, "o": 637.5, "h": 640.49, "l": 634.92, "c": 640.27, "v": 81983545},
        {"t": 1756872000000, "o": 642.67, "h": 644.21, "l": 640.46, "c": 643.74, "v": 70820898},
    ]}


class TestKeys(unittest.TestCase):
    def test_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            load_terminal_keys("/nonexistent-xyz/.env")
    def test_parse(self):
        import tempfile, os
        with tempfile.NamedTemporaryFile("w", suffix=".env", delete=False) as f:
            f.write("# comment\nMASSIVE_API_KEY=abc123\nEMPTY=\n")
            p = f.name
        try:
            k = load_terminal_keys(p)
            self.assertEqual(k["MASSIVE_API_KEY"], "abc123")
        finally:
            os.unlink(p)


class TestLedger(unittest.TestCase):
    def test_budget_gate(self):
        import tempfile
        with tempfile.TemporaryDirectory() as d:
            L = QuotaLedger(f"{d}/q.json")
            self.assertTrue(L.allows("massive", 200))
            for _ in range(170):
                L.record("massive")
            self.assertFalse(L.allows("massive", 200))  # 170 >= 200*0.85
            self.assertTrue(L.allows("massive", 200, headroom=1.0))
            L2 = QuotaLedger(f"{d}/q.json")  # persists
            self.assertEqual(L2.used("massive"), 170)


class TestNormalize(unittest.TestCase):
    def test_massive_ok(self):
        df = normalize_massive(_massive_payload())
        self.assertEqual(len(df), 2)
        self.assertAlmostEqual(df["close"].iloc[-1], 643.74)
        self.assertTrue((df["low"] <= df["close"]).all())
    def test_massive_bad(self):
        with self.assertRaises(ValueError):
            normalize_massive({"status": "ERROR"})
        with self.assertRaises(ValueError):
            normalize_massive({"status": "OK", "results": []})
    def test_massive_delayed_ok(self):
        p = _massive_payload(); p["status"] = "DELAYED"  # free tier flag
        self.assertEqual(len(normalize_massive(p)), 2)


class TestChain(unittest.TestCase):
    def _ledger(self):
        import tempfile
        d = tempfile.mkdtemp()
        return QuotaLedger(f"{d}/q.json"), d

    def test_massive_first(self):
        L, d = self._ledger()
        calls = []
        df = fetch_massive_aggs("SPY", "2025-09-01", "2025-09-02",
                                {"MASSIVE_API_KEY": "x"}, L, cache_dir=d,
                                http_get=lambda u: calls.append(u) or _massive_payload(),
                                sleep=lambda s: None)
        self.assertEqual(len(df), 2)
        self.assertEqual(L.used("massive"), 1)

    def test_failover_to_av(self):
        import json
        from pathlib import Path
        L, d = self._ledger()
        import quantkit.fresh as F
        # pre-seed AV cache so no network happens
        av = {"Time Series (Daily)": {
            "2025-09-05": {"1. open": "640", "2. high": "645", "3. low": "639",
                           "4. close": "644", "5. volume": "70000000"}}}
        Path(d, "av_SPY_compact.json").write_text(json.dumps(av))
        orig = F.fetch_massive_aggs
        F.fetch_massive_aggs = lambda *a, **k: (_ for _ in ()).throw(ValueError("down"))
        try:
            df, prov = pull_symbol("SPY", "2025-09-01", "2025-09-05",
                                   {"ALPHA_VANTAGE_API_KEY": "x"}, L, cache_dir=d)
            self.assertEqual(prov, "alphavantage")
            self.assertAlmostEqual(df["close"].iloc[-1], 644.0)
        finally:
            F.fetch_massive_aggs = orig

    def test_all_fail_closed(self):
        L, d = self._ledger()
        with self.assertRaises(ValueError):
            pull_symbol("SPY", "2025-09-01", "2025-09-05", {}, L, cache_dir=d)

    def test_finnhub_quote(self):
        L, d = self._ledger()
        q = fetch_finnhub_quote("SPY", {"FINNHUB_API_KEY": "x"}, L,
                                http_get=lambda u: {"c": 771.35, "pc": 767.18, "t": 1790366400})
        self.assertAlmostEqual(q["last"], 771.35)
        with self.assertRaises(ValueError):
            fetch_finnhub_quote("SPY", {"FINNHUB_API_KEY": "x"}, L,
                                http_get=lambda u: {"c": 0})


if __name__ == "__main__":
    unittest.main()
