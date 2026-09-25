# Ch27 — Floor Versus Automated Trading Systems

**Source:** Larry Harris, *Trading and Exchanges* (2003), Chapter 27.

## Purpose
The comparative economics of open-outcry floors and electronic
systems: audit trails, fairness, capacity, and negotiation.

## What automation improves
1. **Audit trails**: electronic systems record every order and fill
   perfectly; floors rely on manual records and human honesty. Trade
   misreporting (like Eli's spread discrepancy) is impossible in a
   clean automated system.
2. **Fair access**: floors favor whoever can see/hear first — floor
   traders see the whole market before off-floor traders get data
   (2s) and route orders (5s+); physical size, voice, and position in
   the pit are advantages. Automation removes these (replacing them
   with keyboard speed and co-location — a different inequality).
3. **Capacity/scalability**: oral auctions break down when too many
   traders participate (designated "fast markets" where best-price
   execution isn't guaranteed); electronic systems scale to massive
   message rates and enforce price/time priority automatically.
4. **Distributed access**: traders can work from desks with their
   data, phones, and colleagues — impossible on a floor.
5. **Negotiation speed**: while a shout may beat a keystroke, the
   full trade cycle (entry + record keeping + reporting) is faster
   electronically.

## What floors still offer
- **Personal relationships and trust** — brokers who know their
  clients' needs; negotiation nuance (size, timing, partial fills)
  that rigid systems encode poorly.
- **Discretion in order handling** (e.g., "not-held" orders worked by
  judgment).
- Some argue floors are cheaper for complex negotiations; but the
  trend has been decisively toward automation because its audit
  integrity and capacity benefits are structural.

## The trade-off
- Automation trades away human discretion and flexibility for
  **integrity, speed, capacity, and fairness of rules**.
- Fairness is relative: both systems create access advantages —
  floors favor the physically present, automation favors the
  technically equipped.

## Key takeaways
- The audit trail is the killer feature: automated markets are
  provably fair *in process*, even when participants are not.
- When converting a market to electronic, expect the 
  rent distribution to shift from floor intermediaries to
  technology/co-location — the access inequality moves, it doesn't
  vanish.
- For execution design, automation's deterministic priority rules are
  the reason algorithmic strategies are viable at all.
