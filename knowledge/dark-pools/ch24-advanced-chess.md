# Ch24 — Advanced Chess

**Source:** Scott Patterson, *Dark Pools* (2012), Chapter 24.

## Purpose
Bodek's turn from trader to whistleblower: the March 25, 2011
Princeton conference where the pieces click, his indictment of the
maker-taker/order-type machine as a rigged game, and the market's first
real reckoning with **toxic order types** — culminating in SEC scrutiny
of BATS and Direct Edge.

## The conference and the crime wave
- On his last day at Trading Machines, Bodek speaks at "Quant Trading:
  From the Flash Crash to Financial Reform." Andrei Kirilenko (CFTC)
  reveals the crash microstructure: HFT gunners trade *with* the move
  for the first ~5 seconds, flip at ~10 — on May 6 it was 2 seconds/
  4 seconds. Andresen's advice: today's traders need market
  microstructure, "the plumbing."
- The week before, Aleynikov is sentenced to 97 months (overturned Feb
  2012); SocGen's Samarth Agrawal gets 3 years for stolen HFT code.
  Bodek decides someone must expose the system.

## The rigged game
- Maker-taker is the culprit: by the late 2000s, profits on rapid
  Nasdaq trading are *negative* on spreads alone — scalpers survive
  only on rebates. Since everyone wants the rebate and it's zero-sum,
  Bodek argues the exchanges built a complex system to *pick winners*:
  speed + exotic order types. If you don't know which order to use, you
  lose nearly every time — and pay fees while others collect rebates.
- Reg NMS's mandatory market-maker presence, combined with ultra-wide
  "stub" quotes, was the crash powder (ch20). The BATS June 2011
  program letting select market makers show a *dark* better price to
  insiders is Exhibit A of two-tier pricing; BATS backs down under
  criticism.
- Justin Kane (Rainier Investment), Dec 6, 2011: "Order types are being
  created to attract predatory traders... this marketplace is set up to
  bring in the most intermediaries between the buyer and seller as
  possible." Direct Edge's "Hide Not Slide" order type comes under SEC
  scrutiny; BATS reveals an SEC enforcement inquiry into order types
  (Feb 2012) and its own IPO glitch-crashes the listing.

## Advanced Chess
- Bodek rebuilds with machine learning, targeting a 10-minute horizon
  (Renaissance-style) and leveraging his insider knowledge of the
  plumbing. His model: **man-machine integration** — Kasparov's
  "Advanced Chess" (2005 Playchess.com: humans + laptops beat
  supercomputers). Blair Hull backs him with capital in 2012.

## Key takeaways
- In a zero-sum rebate economy, the venue's order types decide winners
  — an opaque, designed-in advantage rather than skill.
- Toxic order types + mandatory presence + wide quotes = crash
  mechanics; the pieces were visible years before May 6, 2010.
- The "advanced chess" thesis: supervised human-AI teams may beat
  pure automation — a design principle for trading systems.
