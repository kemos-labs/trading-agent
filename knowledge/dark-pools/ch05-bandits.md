# Ch05 — Bandits

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 5.

## Purpose
Introduces Josh Levine (the teenage programmer who will build Island)
and the **SOES bandits** — day traders who weaponized Nasdaq's Small
Order Execution System after the 1987 crash, scalping market makers who
had never been forced to honor their quotes.

## The old NYSE as a dark pool
- 1986: 18-year-old Levine runs for Russo Securities, a Staten Island
  penny-stock broker-dealer run by Shelly Maschler's associates. He sees
  the NYSE floor as chaos: hand signals, paper tickets, phone quotes,
  prices reported to the tape only *after* trades — in Levine's eyes the
  NYSE was itself a massive dark pool of insiders.
- Maschler, ex-First Jersey (Robert Brennan's penny-stock machine), is
  the streetwise counterweight who teaches Levine that Wall Street's
  powers are "straw men."

## SOES and its loophole
- Harvey Houtkin's Rushmore Securities loses $2.5M on Black Monday
  (Oct 19, 1987). Afterwards he spots a loophole in **SOES** (Small
  Order Execution System, implemented 1985 for small retail orders).
- After Black Monday's unanswered phone calls, Nasdaq makes SOES
  *mandatory* (live June 30, 1988): market makers must automatically buy
  or sell up to 1,000 shares at their posted quote, with instant,
  automated execution — they can no longer cherry-pick trades.
- Houtkin (a Baruch College-trained ex-Nasdaq plumbing student) sees the
  exploit: watch Level II quotes, catch a slow market maker still
  offering $50 while others bid $50¼, buy 1,000 shares, sell instantly —
  $250 a pop, dozens of times a day. This is pit-trading **scalping**
  turned on the market makers themselves.
- The bandits were dubbed "SOES bandits"; Houtkin had a second loophole:
  as an independent individual (his firm had imploded), he could trade
  for his own account — exactly the retail client SOES was designed for.
  Maschler just "let it rip," trading far more aggressively.

## Key takeaways
- Regulatory automation (mandatory electronic execution) that removes
  human discretion also removes human protection — the same execution
  obligation that aids retail becomes a weapon in professional hands.
- The 1987 crash is the mother of this whole revolution: forced
  automation + a visible order book (Level II) + a 1,000-share
  execution guarantee = a machine-readable edge.
- Levine's role crystallizes: he wants to *change the world through
  computers*, and Maschler gives him a lab.
