# Chapter 2: SOFR Futures

## 3M SOFR Futures (SR3)
Key difference from Eurodollar (ED) futures: ED settles to a forward-looking 3M LIBOR rate, while SR3 settles to a **compounded average of daily SOFR** over the reference quarter. This means:
- The contract month refers to the **beginning** of the reference quarter, but settlement occurs at the **end**.
- During the reference quarter, an increasing portion of the settlement rate is known → declining volatility and "stickiness" as the contract approaches expiry.
- The settlement formula uses ISDA compounding with Act/360: R = [∏(1 + SOFR_i × d_i/360) − 1] × (360/D), where d_i is calendar days per SOFR observation.

**Except for the front-month contract**, the transition from ED to SR3 is "little more than a renaming exercise."

## 3M SOFR Futures as Forward Rate Building Blocks
SR3 futures represent consecutive 3M forward segments of the secured yield curve. They can be combined into **strip rates** for longer tenors:
- Strip rate = weighted compounding of individual future-implied rates over the term.
- For the front-month contract, the reference quarter splits into known (past SOFR values) and unknown (future) portions. Solve for the unknown rate: R_unknown from the future price and known SOFR values.
- When the strip term doesn't align with reference quarters, the forward curve shape during the last reference quarter must be accounted for.

**Rolls:** Roll from second-to-third listed contracts (not front-to-back as with ED). Rolling at the end of the reference quarter is costly (the Dec-19 example: 138bp cost at end vs 4bp at beginning) because the contract decouples from market expectations.

## 1M SOFR Futures (SR1)
Modeled on Fed Funds (FF) conventions. Settles to **simple arithmetic average** of SOFR over calendar days in the delivery month (not business days). This means:
- Simple averaging ≠ compounding → introduces a convention mismatch with 3M contracts.
- The SR1:FF spread is a **clean proxy for the secured–unsecured basis** (nearly identical specifications).
- The SR1:SR3 spread depends on yield curve shape + the simple-vs-compounding convention difference, which reaches ~3bp at 5% SOFR.

## FOMC Meeting Impact
- **1M contracts:** Impact = rate change × (days post-meeting / total days in reference month). E.g., 25bp hike on May 4 affects May contract by 25 × (27/31) = 21.8bp.
- **3M contracts:** Requires recalculating the compounding formula with bumped SOFR values post-meeting.
- **Hedge ratio adjustment:** The standard 10 SR3 : 3+3 SR1 ratio must be adjusted when FOMC meetings fall off-center in the reference quarter. Two-step hedge: first immunize against the meeting jump, then immunize against the rate level.

## Process Selection for Pricing
The choice of stochastic process materially affects SR3 prices. A Vasicek + jump process simulation shows:
- Pure jump process prices are highly sensitive to Fed hike probability assumptions.
- Mean reversion parameters (mean = 1.18%, speed = 0.006 estimated from pre-SRF data) dominate pricing at low rate levels.
- Even including/excluding a few historical spikes changes the estimated speed of mean reversion from 0.002 to 0.006, shifting the simulated settlement price by ~15bp.

**Key lesson:** For pricing options on SR3 (Chapter 5), a diffusion term is necessary even if a pure jump model suffices for futures pricing alone.
