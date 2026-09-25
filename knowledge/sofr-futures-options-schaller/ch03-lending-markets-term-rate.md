# Chapter 3: SOFR Lending Markets and the Term Rate

## The Core Tension
The transition to SOFR encounters resistance in cash loan markets because:
1. Borrowers want to know interest payments **in advance** (LIBOR-style), not in arrears.
2. Even with in-arrears, the payment date is too tight (same day the last SOFR is published).
3. Legacy systems are built around simple averaging, not compounding.

## Simple Averaging vs Daily Compounding
The economically correct approach is compounding (ISDA formula), which equals the settlement formula for 3M SOFR futures. Simple averaging is a relic of system limitations. At low rates, the difference is negligible (~0.1bp at 100bp SOFR), but it grows substantially with rates: a 1-year loan at constant 500bp SOFR earns 513bp compounded vs 500bp simple — a 13bp gap. Rising rates will drive adoption of compounding.

**Supporting features introduced:**
- Fed publishes SOFR simple averages for 30/90/180-day periods and a SOFR index (base 1.0 on April 2, 2018) implementing daily compounding.
- Lookback/lockout conventions extend the notification period for in-arrears loans (e.g., use SOFR from 2 days ago), at the cost of increasing hedge mismatch with futures.

## The SOFR Term Rate
The CME Term SOFR (1M, 3M, 6M, 12M tenors) is calculated via a **model** — specifically a pure jump process (Heitfield & Park 2019) — fitted to prices of the first 13 1M and first 5 3M SOFR futures contracts. The model assumes SOFR only changes at FOMC meeting dates and is constant otherwise.

**Calculation process:**
1. Aggregate futures data via 14 × 30-minute observation intervals from 7 a.m.–2 p.m. CT, using VWAP and random snapshot bid-ask.
2. Fit a stepwise overnight forward rate curve with jumps at FOMC dates.
3. Compound the fitted curve using the ISDA formula to produce term rates.

## Criticism of CME Term Rate
- **Pure jump process** ignores diffusion, mean reversion, momentum, and all non-FOMC volatility — a strong assumption given historical SOFR spikes.
- **The pure jump process is unsuitable for option pricing**, forcing traders to use two different models (jump-only for the term rate, jump-diffusion for options), creating inconsistencies.
- **Over-identification:** The optimization uses more futures contracts than parameters, so no futures are repriced exactly — the fitted curve is global and non-local.
- **External futures influence:** A 3M term rate can depend on futures whose reference periods extend well beyond the term horizon.
- **The penalty function** (λ = 1/#FOMC meetings/year ≈ 0.33) smooths the curve but may impart a systematic upward bias of ~0.5bp on term rates.

## Two Resolution Scenarios
1. **Term rate fades:** High hedging costs (multiple bp vs ~1bp for direct futures hedging) incentivize borrowers to adopt in-arrears structures, making the term rate superfluous.
2. **Term rate persists:** Regulators allow a secondary market for term-rate derivatives, reducing hedging costs and locking in the term rate's permanence. Currently, interdealer trading is prohibited, keeping hedging costs artificially high.

**Key insight:** The term rate is a compromise product — it allows "in-advance" LIBOR-style lending but cannot be cheaply hedged because it is model-derived rather than directly linked to traded instruments.
