# Chapter 9: Hedging Swaps and Bonds with SOFR Futures

## The Big Convergence
The transition to SOFR makes three key markets **conceptually identical** — all are ways of compounding daily SOFR into a term rate:

| Instrument | How it compounds SOFR |
|---|---|
| **SOFR futures strip** | Consecutive 3M forward segments compounded via ISDA formula |
| **SOFR-based swap** | SOFR compounded over each reset period, exchanged vs fixed rate |
| **Treasury bond** | Individual repo rate (≈ SOFR) funding coupon payments |

This convergence means each can be replicated/hedged with the others. Before SOFR, LIBOR-based swaps used a different curve for cash flows vs discounting (dual-curve world). SOFR reinstates the clean **single-curve** framework: the same SOFR curve determines both cash flows and discounting.

## Consequences of Single-Curve Framework
- **PV of floating side at inception = 100** (same compounding formula for cash flows and discount factors).
- The first floating payment is **unknown** at inception (unlike LIBOR swaps where the first payment was known) — more intuitive, and aligned with SOFR futures where all reference quarters are initially unknown.
- As SOFR values become known during the reference quarter, both the swap and the front-month future lose sensitivity at the same rate → **stable hedge ratios**.

## Hedging SOFR Swaps with SOFR Futures Strips

### Ideal IMM Swap
For a swap where reset periods align with futures reference quarters, payment dates match futures settlement, and conventions are identical:
- Hedge each forward rate R_j by selling the corresponding SR3 contract.
- The hedge ratio = (Δ PV_swap / Δ R_j) / BPV_futures.
- For a flat 1% swap, this produces ~101–102 contracts per quarterly period (slightly >100 due to money-market daycount conventions, slightly decreasing due to discount factors).

### Realistic Adjustments
1. **Money market conventions on fixed leg:** Multiply fixed coupon by 365/360.
2. **Two-day payment delay** (CME-cleared SOFR OIS): Introduce different discount factors for floating and fixed legs → PV_floating ≠ 100 at inception.
3. **Annual payment frequency:** Decompose the annual netted payment into quarterly segments aligned with futures reference quarters.
4. **Non-IMM start date:** The front-month contract is already in its reference quarter — use the known/unknown SOFR split from Chapter 2. The hedge ratio of the front-month decreases smoothly as SOFR values become known.
5. **End-date mismatch:** If the swap ends between futures reference quarters, calibrate a jump process for the gap (Chapter 2 techniques).

**Worked example:** 1Y SOFR swap (Jun 16, 2021 → Jun 16, 2022), annual payments, money-market conventions, 2-day payment delay. Hedge computed on Jun 23, 2021 (one week into first reference quarter): short 101 of each of Jun/Sep/Dec 2021 and Mar 2022 SR3 contracts — nearly identical to the simple flat-curve approximation.

## Hedging Treasuries with SOFR Futures Strips

### The Link
A Treasury's yield ≈ the SOFR futures strip rate (both compound daily secured rates into term rates). The difference (asset swap spread with SOFR as floating leg) is usually small — driven only by specialness (rare for short Treasuries) and regulatory capital effects.

**Empirical evidence:** CMT minus SOFR strip yields for 1Y and 2Y tenors, Dec 2020–Sep 2021: spreads are typically a few basis points positive, with one instance of negative spreads during Mar 2020 rate crash.

### Hedge Construction
Same approach as swap hedging: bump each reference quarter's SOFR values, observe the change in bond PV, divide by the change in futures price. The strip covers all remaining coupon payments plus any extension beyond the last coupon.

**Worked example:** 1.5% Treasury maturing Sep 30, 2021, hedged on Jan 2, 2020 with 8 SR3 contracts (Dec 19 through Sep 21). Initial hedge: −717 contracts total. A +1bp parallel shift: bond loses $17,568, futures gain $17,517 → **hedge error of 0.3%**.

### Evolution and Performance
Rehedging at each reference-quarter turn (Table 9.1):
- As contracts settle, they drop from the hedge (smooth transition, unlike ED futures).
- Lower/flatter curve → more contracts needed, more evenly distributed.
- **Mar 2020 stress test:** Until early March, hedge was nearly perfect (bond +$1.16M, futures −$1.16M). During mid-March, asset swap spreads widened (Treasury pricing temporarily influenced by corporate bond stress), creating a $328K mismatch (20% of the move). By Mar 31, the gap closed (mismatch <1%).

**Key lesson:** The hedge works when the foundation (SOFR ≈ repo rate ≈ bond funding rate) holds. During severe stress, asset swap spreads can deviate from zero, but these deviations tend to be **ephemeral**. A patient hedger can wait for convergence; an RV trader can exploit the temporary mispricing.

## Important Caveat
This approach applies to **government bonds only**. Corporate bonds involve the unsecured–secured basis — hedging them with SOFR futures would introduce basis risk. Use FF or ED futures for corporate bonds (Chapter 4).
