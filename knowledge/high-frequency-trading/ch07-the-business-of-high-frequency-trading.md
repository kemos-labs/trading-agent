# Ch07 — The Business of High-Frequency Trading

**Source:** Irene Aldridge, *High-Frequency Trading* (2nd ed., 2013), Chapter 7.

## Purpose
The economics of running an HFT operation: it is mostly a *technology*
business, with an unusual cost profile and development pipeline.

## Key processes
- HFT's value proposition: tick-by-tick processing and high capital
  turnover. The development process: concept → **back-test** (two
  years of tick data; out-of-sample validation) → **paper trading**
  (fully programmed, no orders; a month of clean reconciliation with
  the back-test) → low-capital **production** → scale.
- A successful HFT system takes ~36 months to develop (three years to
  become consistently profitable).
- Man-hour allocation (steady state): coding of trading/risk
  infrastructure 40%, system testing 20%, quant model development 15%,
  risk management 10%, compliance 10%, run-time monitoring 5%.
  Start-ups are data/programming-heavy; steady state is
  monitoring/compliance-heavy. The Knight Capital failure (2012,
  ~$10M/min) is the cautionary tale for testing/compliance.

## Economics
- **Cost curves are inverted vs. traditional trading**: HFT spends
  heavily up front, then near-zero marginal cost; traditional desks
  have constant staffing costs.
- **Transaction costs scale inversely with size**: retail pays ~0.05%
  per leg ($20 per $40k notional) vs. institutional ~0.0005%
  ($3–5 per $1M). Leverage (1:9 typical) multiplies gains and losses.
- **Fee model**: HFT is "alternative investment" — institutional
  investors want 1–3 year auditable track records at 8–12% p.a.;
  typical HFT compensation is **1-and-30** (1% management, 30%
  performance above high-water mark) vs. classic 2-and-20.
- **Leverage viability** hinges on Sharpe and max drawdown; because
  the HFT Sharpe is leverage-invariant, leverage L scales return
  linearly: `E[R_annualized]×L / σ[R_annualized]×L = same Sharpe`.

## Markets suitable for HFT
- Automated execution is a prerequisite: equities most (50%+ algo),
  then futures/options; OTC markets (FX retail, some bonds) are less
  suitable without electronic dealing.

## Key takeaways
- HFT businesses sell **technology and process**, not trading genius —
  the moat is the development pipeline and infrastructure, not a
  signal.
- The back-test→paper→production ladder with reconciliation at each
  step is the discipline that prevents Knight-scale disasters.
- Small capital is the worst position to be in: costs per unit notional
  are highest exactly when capacity is smallest — size up or use
  leverage deliberately.
