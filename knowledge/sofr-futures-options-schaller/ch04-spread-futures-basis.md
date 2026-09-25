# Chapter 4: SOFR Spread Futures and the Basis

## The Two-Dimensional STIR Universe
The introduction of SOFR futures adds a **vertical dimension** (secured vs unsecured) to the previously one-dimensional STIR universe (which only had time-period/specification differences):
- **Horizontal spreads** (same row): driven by yield curve expectations + specification differences (e.g., SR1:SR3 spread, FF:ED spread).
- **Vertical spreads** (same column): driven by the secured–unsecured basis (e.g., SR1:FF, SR3:ED spreads).
- **Diagonal spreads** (cross both): driven by both factors (e.g., SR3:FF).

CME lists inter-commodity spreads (ICS) for all edges plus the SR3:FF diagonal. Liquidity correlates with basis exposure: SR3:ED (highest basis exposure) is most liquid; SR1:SR3 (no basis) has no liquidity.

## The Secured–Unsecured Basis Model
A simplified model from Huggins & Schaller (2013): LIBOR − Repo ≈ risk-weighted capital cost, roughly:

**LIBOR − Repo ≈ 0.20 × 0.08 × g = 0.016g**

where g is the cost of equity. A 5% increase in equity cost widens the basis by ~8bp. This explains why asset swap spreads widen during banking stress.

The **SR3:ED spread** is regressed against SOFR level and 2Y JPY CCBS:

SR3:ED spread = 4.825 + 2.322 × SOFR − 0.394 × CCBS (R² = 0.67)

- Rate level (SOFR) and CCBS together explain ~67% of the spread variance.
- The CCBS captures stress in global banking (capital repatriation, flight to quality).
- Residuals exhibit mean reversion (half-life ~3.7 weeks, Sharpe ~5–8 for 5–10bp deviations).

## Three Applications
1. **Pricing spread contracts:** Use the regression to predict fair-value SR3:ED spreads under various scenarios (e.g., SOFR at 5% + CCBS at −80bp → ~45bp spread).
2. **Replacing CCBS in RV trades:** The SR3:ED spread is a cheap, liquid proxy for the CCBS when only the spread behavior (not the actual currency cash flows) is needed. The regression residual mean-reverts quickly, supporting mean-reversion trades.
3. **New RV relationship:** The two-variable regression residual offers an additional alpha source — mean-reverting with attractive Sharpe ratios (7.68 at 10bp, 4.03 at 5bp for one-week horizon).

## After the End of LIBOR
Post-June 2023, ED futures settle on fallback rates (SOFR + fixed spread), so SR3:ED no longer captures the basis. **SR1:FF becomes the cleanest instrument** for the secured–unsecured basis, as both use simple averaging (nearly identical specifications). SR1:FF may become the primary vehicle for banking-crisis exposure trades.

## Asset Swaps Post-SOFR
- **Government bonds:** LIBOR-based asset swap spread ≈ unsecured–secured basis. Switching to SOFR-based swaps **eliminates** this basis, making asset swap spreads close to zero (driven only by specialness, which is usually absent for short Treasuries).
- **Corporate bonds:** Switching to SOFR **introduces** the basis (since corporates still fund unsecured). FF-based OIS may become the preferred hedge for corporates.
- **Net effect:** SOFR for government asset swaps, FF for corporate asset swaps, with SR1:FF spreads trading the basis between the two.

**Formula:** SR3:ED spread ≈ 4.83 + 2.32 × SOFR − 0.39 × 2Y_JPY_CCBS
