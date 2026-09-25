# Ch02 — Systematic Trading Rules

**Source:** Carver, *Systematic Trading*, Chapter 2.

## What makes a good trading rule
A trading rule is a systematic way of predicting price movements. Key
attributes:
1. **Built from ideas, not just data**: *ideas first* (hypothesis → rule →
   test) vs *data first* (mine patterns → rule). Carver prefers ideas first:
   no fitting required if the idea works, fewer alternatives tested, simpler
   and more intuitive rules with a story. Data first is explicit (so
   over-fitting can be controlled) and can find novel patterns (useful in
   HFT), but invites haphazard mining and narrative-fallacy rationalisation.
2. **Explainable profits**: know *why* it made money to judge if it persists.
3. **Intuitively understandable behaviour**: trust comes from predictable,
   sensible actions.
4. **As simple as possible**: few moving parts; complex data-first rules are
   less explainable and more over-fit prone.
5. **Can be systematised**: rules must be objective, generic, and have data
   available (merger arbitrage, Twitter-data strategies often fail these).

## When rules don't work
- **It never really worked**: over-fitting, look-ahead (delayed data),
  survivorship bias, underestimated costs, missed market-structure elements
  (short-selling constraints), too-brief history missing a blow-up.
- **The world changes**: relative value dies when everyone trades it; trend
  followers face synchronised exits; HFT became a pure speed arms race
  (outside this book's scope).

## Why certain rules are profitable (sources of edge)
- **Risk premia**: equities vs bonds, term premia, illiquidity premia.
  Time-varying premia → mean reversion opportunities (buying cheap premia).
- **Skew & unlikely events**: assets with same SR can differ radically in
  skew. Buying insurance = positive skew (frequent small losses, rare big
  gains); selling insurance = negative skew (frequent small gains, rare big
  losses). Negative skew strategies look great until they blow up.
- **Leverage constraints**: investors who can't borrow bid up low-SR high-
  return assets; those who *can* use leverage (safely) outperform long-run.
- **Liquidity and size**: forced/large traders pay up for liquidity → size
  and illiquidity premia.
- **When others have to trade**: central banks, tax-loss window dressing,
  hedgers → carry, seasonals. Liquidity providers earn the spread but hold
  negative skew.
- **Barriers to entry / effort**: profits may just compensate costs/effort,
  not skill.
- **Behavioural effects**: early-loss-taking profits from prospect-theory
  biases; self-fulfilling prophecies (Fibonacci etc.) work only while crowded.
- **Pure alpha**: genuine skill exists but can't be systematised.

## Classifying trading styles
- **Static vs dynamic**: static = buy & hold / rebalancing; 4th degree
  static = risk-parity rebalancing to constant expected risk. Dynamic rules
  add trading returns.
- **Skew**: the most overlooked characteristic. Warning sign: steady small
  daily gains with high hit rate ⇒ likely negative skew (hidden big losses).
- **Trading speed — Law of Active Management (Kahn 1989)**: expected SR ∝
  √(number of independent bets per year). 1 bet/yr at SR 0.15 → 4 bets/yr SR
  0.30 → 256 bets/yr SR 2.4. Assumes constant skill (false across holding
  periods — rules have a "sweet spot") and ignores costs (fast trading via
  spread bets is impossible to make profitable). Implication: **diversify —
  uncorrelated assets double your SR**.
- **Technical vs fundamental**: technical (price-only) is easier; fundamental
  effort is usually rewarded with higher returns.
- **Portfolio size**: diversification is the best source of risk-adjusted
  return; also immunises against instrument-specific bad data.
- **Leverage**: needed when an asset's natural risk is too low for your
  return target; deadly combined with negative skew (Greece 4yr/5yr trade:
  steady <1%/yr returns, then correlation broke and margin calls forced
  liquidation at the worst price).
- **Contrarians vs market followers**: mean reversion = negative skew
  (catch falling knives); trend following = positive skew (small losses,
  occasional large gains). **Crowded trades are deadly** (LTCM 1998, Quant
  Quake Aug 2007).

## Achievable Sharpe ratios (be realistic)
- Single equity ≈ 0.15; equity portfolio/index ≈ 0.20; global equities ≈
  0.25; multi-asset static portfolio ≈ 0.40 (realistic maximum for static).
- Single-instrument dynamic rule ≈ 0.40; multi-asset rules ≈ double that.
- Back-tested SR of 2.0–3.0+ on single instruments = over-fitting fantasy;
  virtually no systematic hedge fund sustains SR > 1.0 for long.
- Two dangerous "easy" paths to higher SR: (1) negative-skew strategies
  (LTCM's SR was ~4.6 before the blow-up), (2) trading faster (SR scales with
  √speed in theory but costs destroy it — one-hour holding via spread bets:
  theoretical 5.2 → −16.4 after costs).

## Notes
- Concepts defined: **Sharpe ratio** = mean return ÷ stdev of returns
  (annualised ≈ 16× daily, using 256 days); **risk** split into predictable
  (recent vol) vs unpredictable (model error, regime change); **volatility
  standardisation** — rescale each asset/rule's returns to equal expected vol
  so the same rule applies to all instruments and rule/asset returns become
  comparable (foundation of the framework in ch5+).
