# Ch04 — Setting Up Your Business

**Source:** Ernest P. Chan, *Quantitative Trading* (2nd ed., 2021), Chapter 4.

## Retail vs proprietary trading
**Retail brokerage** (fully independent): open account, deposit cash, trade. Reg T leverage ~×2
overnight / ×4 intraday. All P&L yours. Losses not limited to deposit (brokerage can demand
"make whole" on negative equity — e.g. the 2015 Swiss-Franc unpegging).

**Proprietary firm** (semi-independent, e.g. Bright Trading): pass **FINRA Series 7**, invest your
own capital, get much higher leverage (up to 20×+ intraday/hedged). Firm may take a % of
profits; loss limited to initial investment; often training/mentoring and imposed risk rules
(e.g. no penny stocks, no overnight shorts) which are protective but limit flexibility.
**Risk: firm can piggyback your strategies with its own capital** (more market impact for you),
and bankruptcy risk of the firm (WorldCom, Refco) — accounts not SIPC-insured.

**Should you incorporate?** Yes (LLC/S-Corp) to limit personal liability — open the account
through the entity; tax pass-through; file corporate bankruptcy if needed. Works for non-US
residents (bizfilings.com, Stripe Atlas). Sole-shareholder = no lawyer needed.

**Decision factors**: capital need, strategy style (market-neutral high-leverage → prop; HFT
futures low-capital → retail), skill/experience (novices benefit from imposed restraints;
experienced traders prefer freedom).

**Retail vs prop summary** (Table 4.1):
| Issue | Retail | Prop |
|---|---|---|
| Legal req | none | Series 7 + FINRA |
| Initial capital | substantial | small |
| Leverage | Reg T (2× overnight, 4× intraday) | firm discretion (≥20×) |
| Liability | unlimited (unless LLC/S-Corp) | limited to initial investment |
| Fees | low commissions, minimal data fees | higher commissions + monthly fees |
| Brokerage bankruptcy | SIPC-insured | not insured |
| Training | none | sometimes |
| Trade-secret disclosure | little risk | piggyback risk |
| Style restrictions | none (SEC-permitted) | may restrict (e.g. overnight shorts) |
| Risk mgmt | self-imposed | firm-imposed |

Tax note: **trader tax status** can be applied for with a retail account so trading losses
offset ordinary income (greencompany.com).

## Choosing a brokerage/firm
Commission rate is only part of total transaction costs — also consider:
- **Execution speed & dark-pool access** (Liquidnet, ITG Posit, internal crossing networks):
  a large brokerage's better execution can more than offset higher commissions (REDIPlus/Sigma
  X vs IBKR anecdote — IBKR now offers smart routing & algo-execution firms like Quantitative
  Brokers for futures).
- **Product range**: futures/forex support (many retail/prop accounts disallow them).
- **API availability**: required for automated/HFT trading (Chapter 5).
- **Paper-trading accounts** (Alpaca, Interactive Brokers, Oanda) to test APIs without real
  risk; **simulator/demo accounts** replay historical quotes for debugging.
- **Firm reputation/financial strength** for prop firms (not insured): broker-dealer registered
  with an exchange, audited by SEC; check FINRA BrokerCheck for Disclosures (customer
  complaints, arbitrations, regulatory actions); elitetrader.com for member opinions.
- You can run **multiple accounts simultaneously** (retail + prop) — no noncompete usually for
  remote members; disclose "outside business activities" to FINRA; compare execution speeds and
  liquidity.

## Physical infrastructure
- **Startup**: any new PC, high-speed internet, **UPS** (avoid mid-trade power loss). Total
  initial ~$2k max; ~$100/month.
- **Real-time news feed**: Bloomberg ($2k+/mo) or cheaper Thomson Reuters / Dow Jones
  ($100–200/mo). TV (CNBC/CNN) optional — note the Mauboussin horse-handicapper study: more
  information ≠ better predictions.
- **Growth**: faster machines; **VPS with direct connections** to broker servers (speedytradingservers.com, few hundred $/month) — reduces slippage and survives household disasters; monitor via remote desktop; multiple monitors for the many trading apps.
- A million-dollar portfolio can be run on ~$2k initial + ~$100s/month operating cost.

## Summary checklist (from book)
Brokerage/firm must have: low commissions, broad instrument variety, deep liquidity access,
and **most importantly an API for real-time data + order transmission**.

## Key takeaways
- Freedom/capital protection vs leverage is the retail-vs-prop tradeoff; incorporate (LLC/S-
  Corp) to cap personal liability.
- API, paper-trading, execution quality/dark-pool access, product range, and (for prop)
  financial strength matter as much as commissions.
- Start light (PC + internet + UPS), scale to VPS as capacity/speed needs grow.
