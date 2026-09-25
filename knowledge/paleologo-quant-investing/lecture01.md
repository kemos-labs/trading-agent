# Paleologo, FINC-B8420 Quantitative Investing — Lecture 1 (distilled)

Source: `FINC_B8420_1_simple.pdf` (Columbia, 43 slides). Course spine for the
whole Phase 8 corpus program. Own-words distillation; no slide text quoted.

## The quant business in one slide

Quant firms differ by holding horizon and capacity, not by mystique: market
makers (microseconds, spread + rebates), stat-arb pods (days–weeks, crowded
short-horizon signals), factor managers (months–years, slow scalable premia),
and multi-strategy platforms renting infrastructure to pods. Every one of them
runs the same pipeline — data → expected-return model → risk model →
transaction-cost model → optimizer → execution → attribution — and competes on
how honestly each block is measured. Guest speakers and five homework
backtests plus an original out-of-sample final project enforce the hands-on
rule: nothing counts until it survives unseen data net of costs.

## The organizing equation

Before the trade, three models define the opportunity set: expected returns
(signals across assets and horizons), a risk model (portfolio volatility and
systematic exposures), and a transaction-cost model (spread, impact, fees,
capacity). During the trade the optimizer balances them in a single objective
— forecast return against risk and trading cost (return minus risk-aversion
times variance minus cost of trading away from the current portfolio). The
lecture's key line: the optimizer is a decision rule, not a math exercise —
constraints are where judgment about funding, liquidity, and mandate limits
lives. After the trade, realized P&L becomes new information: which signals
worked, whether sizing added value, whether realized costs match the model,
and how risk and leverage should evolve.

## Factors as portfolios, not labels

The standard style boxes (value, momentum, size, quality, low-volatility,
carry) are long–short portfolios with microstructure footprints, not abstract
attributes. A persistent premium needs an economic mechanism, and the lecture
insists on naming who is on the other side: liquidity demand, funding or flow
constraints, risk-bearing for bad-state exposure, or a genuine informational
edge. Cochrane's dictum quoted in the slides — there is no alpha, only beta
you understand and beta you don't — becomes the research filter for the whole
paper corpus: every abnormalreturns/momentum/anomaly note must answer which
mechanism it claims before it earns a skill.

## Efficiency is about implementation, not just information

Predictability alone never guarantees profit. The lecture separates the return
forecast from the feasible position: risk (outcome uncertainty), liquidity
(size, horizon, cost), and funding (margin, capital) can each break the
forecast-to-position path. The Palm–3Com carve-out is the canonical exhibit —
a visible valuation identity survived because only 5% of Palm floated and the
short leg was prohibitively expensive to borrow. Same logic covers
index-reconstitution flow: predictable benchmark demand is an opportunity only
for whoever can warehouse the liquidity, market, and cancellation risk first.

## Data families and what they feed

Four data families map to pipeline blocks: prices and volume (regular or
order-level microstructure), security characteristics (cross-sectional
descriptors), macro/market time series (regime and risk inputs), and
unstructured records (text, audio, multimodal). Raw observations must be
point-in-time aligned and cleaned before they become model inputs — the same
fit-on-train-only discipline the repo already enforces for FFD, triple-barrier,
and purged CV.

## Why this lecture anchors Phase 8

The course outline (portfolio basics → µ models → Σ models + costs →
optimization → attribution) gives the 634-note corpus a filing spine the
folder names alone lack: momentum/anomalies/abnormalreturns → µ; marketimpact/
returnproperties → Σ + costs; portfolioconstruction/universalportfolios →
optimization; trendfollowing/derivatives/yield → overlays. Every Phase 8 work
item must name its spine block, and every promoted skill must state the
claimed mechanism (risk, liquidity, funding, flow, information) per the
no-alpha-without-a-counterparty rule.
