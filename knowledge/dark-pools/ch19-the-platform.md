# Ch19 — The Platform

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 19.

## Purpose
The **Sergey Aleynikov** case (July 2009) drags HFT into the public
eye: a Goldman Sachs programmer downloads 32MB of the bank's trading
platform code on his way to a new job at Teza Capital, is arrested at
Newark airport, and is charged with industrial espionage. The chapter
also introduces the critics who turn HFT into a national controversy.

## The theft
- Aleynikov (a Russian immigrant, $400K → $1.2M offer from Teza, run by
  Misha Malyshev of Citadel fame) copies and encrypts Goldman's HFT
  code ("thisisatest"), uploads it to a server in Germany, wipes his
  bash history — but Goldman detects the 32MB transfer and the FBI
  arrests him July 3, 2009. He confesses within 11 minutes of
  interrogation: he meant to take only open-source code but grabbed
  proprietary code too. Prosecutors allege the platform "generates many
  millions of dollars of profits per year."
- The case is later overturned on appeal (Feb 2012) — but the damage to
  HFT's reputation is done.

## The critics
- **Zero Hedge**: Dan Ivandjiiski (posting as "Tyler Durden") turns
  the arrest into a sensation, speculating about Goldman's "hi-fi quant
  trading desk" — the mainstream press follows within weeks.
- **Themis Trading** (Sal Arnuk, Joe Saluzzi): their June 18, 2009
  white paper "High Frequency Trading: Red Flags and Drug Addiction"
  argues HFT's ~90% order-cancellation rate is **phantom liquidity**;
  a market event that scares the Bots could leave a vacuum. They
  compare HFT to the SOES bandits.
- **Senator Ted Kaufman** (Delaware, ex-Biden chief of staff): alarmed
  by the 2007 repeal of the uptick rule (a 1938 short-sale constraint
  that HFT lobbied to kill), he warns of systemic risk — a rogue algo
  in a feedback loop could crash the market in minutes ("the next
  LTCM meltdown will happen in a five-minute time period").
- **The SEC's concept release** (Jan 2010) documents the changes:
  average NYSE trade size 724 shares (2004) → 268 (2009); NYSE floor
  execution 10–20 sec (2005) → <1 sec (2009).
- **R.T. Leuchtkafer** (pseudonym, "firefly"): the anonymous insider's
  April 16, 2010 comment letter warns that HFT tightens spreads in
  equilibrium but *widens spreads and savages confidence* when liquidity
  is demanded; and that premium data feeds like TotalView-ITCH let HFT
  "sniff out an elephant and trade ahead of it" — front-running mutual
  fund orders legally.

## Key takeaways
- Proprietary trading code is treated as national-security-adjacent
  intellectual property — its value is the market edge, not the code
  itself.
- Cancellation ratios (~90%) are the core empirical indictment of HFT's
  liquidity-provision claim.
- Premium data feeds turn transparency into an asymmetric weapon:
  "transparency turned on its head."
