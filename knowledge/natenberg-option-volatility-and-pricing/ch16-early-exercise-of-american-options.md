# Chapter 16 — Early Exercise of American Options

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## When early exercise matters

Early exercise requires an *advantage to holding the underlying*:
dividends (stock) or interest on cash flows. With no dividends/interest,
**American = European**. Options on futures under futures-type
settlement have effectively no early-exercise value (no cash flows).

## Arbitrage boundaries

- **American option ≥ intrinsic value** (else buy option, hedge, and
  exercise immediately for riskless profit: call — buy 90 call @9.90,
  sell stock @100, exercise → +0.10).
- **European call ≥ max(0, PV(F − X))**: futures stock-type → (F−X)/
  (1+rt) (F=1167, X=1100, r=4%, ½yr → 65.69 < intrinsic 67). Stock →
  max(0, S − X/(1+rt) − D): an OTM 50 call (S=49.50, X=50, r=4%,
  t=½, D=0) still has boundary 0.48 — buy call, sell stock, exercise at
  expiry: ≥0.08 certain.
- **European put ≥ max(0, PV(X − F))**: stock → X/(1+rt) − S + D.
- **American ≥ max(intrinsic, European boundary)** — the "at least"
  qualifier from ch. 15: American 45 call (S=49.50, D=1.30) boundary =
  max(4.50, 4.08) = 4.50.
- Upper bounds: American put ≤ X, European put ≤ PV(X); American call ≤
  S, European stock call ≤ S − D.
- Lower boundaries move over time: futures (stock-type) boundary rises
  toward intrinsic (→ positive theta for a European ITM option).

## Early exercise of calls on stock

`Call = intrinsic + volatility value + interest value − dividend value`.

- Exercise when **dividend > volatility + interest** (interest = cost of
  carrying X, X·r·t; volatility ≈ companion put price). Example:
  S=100, t=1 mo, r=6%, D=0.75 (in 15 d), 90 put = 0.20: 0.75 > 0.20 +
  90×0.06/12 = 0.65 → candidate (gain 0.10).
- **Only optimal day = the day before the ex-dividend date.** Each day
  you sacrifice vol + interest for nothing; if no dividend, never
  exercise a call early.

## Early exercise of puts on stock

`Put = intrinsic + volatility + dividend − interest`.

- Exercise when **interest > volatility + dividend**. Example: S=100,
  t=2 mo, r=6%, D=0.40, 120 call = 0.55: 120×0.06/6 = 1.20 > 0.55+0.40
  → candidate (gain 0.25).
- No single optimal day; blackout period before the dividend where
  interest < dividend loss: **D / daily interest** days (0.40/0.02 =
  20 days — no knowledgeable trader exercises a put within 20 days of
  the dividend). Common choice: exercise on the dividend payment day.
- Short stock lowers the effective rate → calls more likely exercised
  early, puts less (supports the avoid-short-stock rule).

## Futures options (stock-type settlement)

- Exercise when **interest on intrinsic > volatility value** (companion
  OTM option price): F=100, X=80, t=3 mo, r=8%, 80 put = 0.15 →
  (100−80)×0.08×3/12 = 0.40 > 0.15 ✓.
- *Immediate* candidate needs daily interest > daily theta: 0.0044 vs
  0.0046 → not yet; exercise in ~4 days (the **fugit**).
- Compare with the third choice — selling the option + trading the
  underlying = exercising; exercise only if the market price = parity
  (usually the case for illiquid deep-ITM options).
- **Protective value**: exercising the 90 call ≡ selling the 90 put at
  0.30 (0.10 better than market); buying the companion OTM option
  restores the protection.

## Pricing Americans

- Black-Scholes is European. Approximations: *pseudo-American* (max of
  value-at-ex-div and value-with-S−D); raised-to-parity for puts/futures.
- **Cox-Ross-Rubinstein (binomial, 1979)** — algorithm, best for
  dividend-paying stocks; **Barone-Adesi-Whaley (quadratic, 1987)** —
  faster, treats cash flows as interest (best for no-dividend).
  Optimal exercise: value = parity **and** Δ = 100.
- American−European premium: grows as the option deepens ITM; shrinks at
  higher vol. Stock 90 call premium → dividend − carry cost
  (1.00 − 90×0.06×22/365 ≈ 0.67); 110 put → interest after ex-div
  (110×0.06×21/365 ≈ 0.38). Futures (stock-type) premium grows
  *unboundedly* in the money: (110−90)×0.08×3/12 = 0.40.
- American synthetics: companion deltas can sum > 100 → conversions,
  boxes, rolls aren't exactly delta neutral.
- **American box** (100/110, 24 d, r=6%, D=0.60 in 9 d): European value
  9.96; early-exercise cases raise it — both puts 9.985, both calls
  9.986, one leg 10.23–10.30, call+put (stock ≈105, low vol) **10.568**.

## Early exercise strategies & risk

- **Dividend play**: sell deep-ITM calls + buy stock before ex-div;
  break even if assigned, profit ≈ dividend if not. Assignment
  probability ∝ open interest & market sophistication.
- **Interest play**: sell stock + sell deep-ITM puts; earn interest on
  proceeds while puts stay unexercised. Works on futures (stock-type)
  too, earning interest on intrinsic.
- Market makers may quote deep-ITM spreads at exact parity (5.00) to
  harvest dividend plays from either side.
- Assignment risk: if you'd exercise it, expect assignment; early
  assignment of deep-ITM shorts can create cash squeezes. Getting
  assigned when exercise *wasn't* rational = an unexpected gift.

## Key takeaways

1. Calls: exercise only the day before ex-div; puts: exercise when
   interest on X beats volatility + dividends (never inside the
   dividend blackout).
2. American ≥ European ≥ their lower arbitrage boundaries; use CRR/BAW
   for Americans, BS for Europeans; differences matter most for deep-ITM
   dividend-paying stocks.
3. Early exercise is a right — trade the strategies that exploit
   others' failure to exercise (dividend/interest plays) and respect
   assignment risk on deep-ITM shorts.
