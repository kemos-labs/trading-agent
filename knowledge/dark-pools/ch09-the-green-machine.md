# Ch09 — The Green Machine

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 9.

## Purpose
The regulatory reckoning that created the modern market: the 1996
Justice Department/SEC actions against Nasdaq market makers and the
**Order-Handling Rules** that gave birth to the ECN — legitimizing
Island and opening Nasdaq to computer-driven competition.

## The case against Nasdaq
- July 17, 1996: the DOJ settles with 24 major Nasdaq firms (Lehman,
  Goldman, Bear Stearns, Morgan Stanley, Smith Barney, PaineWebber,
  etc.) for inflating spreads — the largest antitrust settlement in
  history at the time (~$1B total with follow-ons), built on the
  Christie–Schultz odd-eighth findings and Leo Wang's tape evidence.
- Aug 7, 1996: the SEC report finds mass price-fixing and the practice
  of **backing away** — dealers not honoring quotes for traders they
  preferred to avoid. The NASD had made pursuing SOES bandits an
  "enforcement priority" while ignoring dealer abuses.

## The Order-Handling Rules
- The SEC's new rules forced Nasdaq to display *competing* quotes (from
  firms like Datek) alongside market-maker quotes on its national
  system — retail-sized orders could no longer be hidden or dodged.
- They also created the **ECN** (electronic communications network):
  anyone with technology could build a hub that matches trades
  internally or sends quotes to Nasdaq. Bids/offers that don't match
  internally appear beside dealer quotes.
- Instinet — the "**Green Machine**" (quotes visible only on its
  proprietary green-screen terminals) — met the ECN qualifications, so
  its secret institutional quotes were forced into the open. Island
  qualified too, legitimizing Levine's pool.

## Levine vs. Nasdaq at the SEC (Oct 23, 1996)
- Levine argues Nasdaq should simply automate like Island: execute all
  matching SelectNet orders instantly. He dismantles Nasdaq's
  "the market will crash" objections point by point — telling the SEC
  that Nasdaq's warnings were "smoke."
- He wins over SEC staffer Mark Tellini; the rules go live Jan 20, 1997
  (a ten-day delay from the initial January 10 target date).
- Levine's architecture lesson: Island used **distributed computing** —
  spread across many cheap Dell hard drives, massively scalable,
  swap-a-broken-box redundancy — versus Nasdaq's centralized Sun
  mainframes in Trumbull, CT, which were exposed to systemwide crashes.
  Simple, scalable, blazing fast beat big and fragile.

## Key takeaways
- Regulation that *forces* transparency (quotes into the open, ECN
  status) is what let upstarts compete with entrenched dealers.
- Robust systems design (distributed > centralized) is a competitive
  edge, not an engineering footnote.
- The regulator's pen, not just technology, restructured the market.
