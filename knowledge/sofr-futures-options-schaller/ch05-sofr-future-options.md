# Chapter 5: SOFR Future Options

## The Metamorphosis Problem
Before the reference period starts, options on SOFR futures have a **forward term rate** as underlying — standard options analyzable via familiar methods. Once the reference period begins, the future's aggregative function ends, and the option suddenly becomes a **path-dependent Asian option** (arithmetic average of daily SOFR values). This is the central challenge: the migration from LIBOR to SOFR forced the entire money-market options complex from standard to exotic instruments.

## Options on 3M SOFR Futures (SR3)
**Specifications:** American style, $25/bp, last trading day = Friday before 3rd Wednesday of contract month (i.e., **before** the reference quarter begins). This avoids the metamorphosis — options on 3M contracts are always standard.

**Product suite:** Quarterly standards (nearest 16 months), serial standards (nearest 4 months), 1–5Y mid-curve options, 3M/6M/9M mid-curve options, weekly mid-curve options. Strikes: 6.25bp intervals near ATM for first quarterlies, 12.5bp or 25bp otherwise.

**Key limitation:** Options end trading before the reference quarter starts, so **no options on 3M futures exist during the period when a cap/floor's value is being determined.** This is "healing a wound by amputation" — the pricing problem is avoided by removing the hedging instrument.

## Realized Volatility Analysis
Using SOFR future prices, one can extract the **realized volatility curve** for consecutive 3M forward periods of the secured rate — a milestone, since repo market liquidity was previously concentrated only on overnight tenors.

Key observations from 2018–2021 data:
- Realized volatility peaked during the 2019 rate-cutting cycle (up to 92bp at the front end).
- Volatility curves are generally upward-sloping (uncertainty increases with forward horizon).
- The **Sharpe ratio is highest around the 9M forward point** — consistent with Burghardt (2011) and Ilmanen (1995) for unsecured rates.
- Post-SRF (Aug 2021+), realized SOFR volatility is structurally lower than pre-SRF.

## Implied vs Realized Volatility
If the current implied volatility curve is extreme relative to historical realized curves, it's a candidate for:
1. **Level trade:** Sell options and delta-hedge to capture implied minus realized vol.
2. **Slope trade:** Sell steep implied curve (e.g., 12M) and buy flat realized curve (e.g., 6M), delta-hedging both.

## SOFR vs ED Future Options
Realized vol of ED futures typically exceeds realized vol of SOFR futures — explained by the LIBOR-repo spread widening more when rates rise. This creates **spread trading opportunities**: sell ED vol / buy SOFR vol when the SOFR:ED implied vol ratio is elevated.

## Options on 1M SOFR Futures (SR1)
**Key difference:** Both the 1M future and its options end trading on the last business day of the contract month — meaning options **do** undergo the metamorphosis into exotic Asian options during their lives.

**Consequences:**
- A complete strip of options exists for hedging caps/floors (unlike 3M options).
- But no pricing model exists for American-type arithmetic-average Asian options.
- Product suite is limited: nearest 4 months only, narrower strike range.

## Pricing Model Road Map
1. **Process selection:** Mixed jump-diffusion (with drift) — captures both FOMC jumps and non-policy volatility. Pure jump models give zero value for OTM calls (mispricing risk).
2. **Pricing framework:** Fusai & Meucci (2008) for geometric Asian options under Lévy processes; extend to arithmetic via moments/approximations.
3. **American exercise:** No closed-form; numerical methods (LSM, trees) required.

**Critical insight:** The diffusion term is far more important for option pricing than for futures pricing. A trader using pure jump models for futures will misprice options by ignoring non-policy volatility.
