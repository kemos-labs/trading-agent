# Ch13 — Some Wrinkles of Option Markets

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 13.

## Purpose
Practical market quirks that break textbook assumptions: expiration pin risk, sticky strikes, and the currency-band "rubber tree" phenomena.

## Expiration pin risk
- **Pin risk** = the uncertainty at expiration about option assignment: the lag between option-market close and notification of exercise/assignment leaves short options with a contingent claim whose resolution is unknown.
- **Rule**: put-call parity does NOT hold for non-cash-settled listed options (European and American) because of pin risk — a textbook conversion (short call, long put, long underlying, all at the money at the close) is not riskless: the trader doesn't know whether to exercise the puts or whether the calls will be assigned.
- Worst case: news after the close (e.g., a scandal) moves the expected open through the strike — the trader can be assigned on calls AND be wrong on puts.
- Pure conversions/reversals exist only where the underlying is a cash-settled future expiring with the option (Eurodollars, S&P 500 quarterly).

## Sticky strikes
- **Sticky strikes**: large open interest at a strike alters market behavior near expiration — the strike "sticks" (dealers hedge deltas around it, pinning price). Magnified by concentration of long/short interest.

## The currency band ("rubber tree")
- For currencies in bands (ERM), the forward can trade "unfettered" while spot is at the band edge: what looks like extreme interest-rate volatility is the currency's volatility translated into rate terms.
- The "absent barrier": the reflecting/absorbing barrier is an optical illusion — spot is a synthetic of spot + forward points, so freezing S does not freeze F; markets snap through bands with a vengeance (hysteresis).

## Practical lessons
- Delta-hedging around expiration requires anticipating pin and sticky-strike dynamics, not just model deltas.
- Scenario analysis around the strike at expiration beats theoretical parity relationships.
- Exotic books must be monitored for "pin" at barriers too (P/L swing at the trigger).

## Key takeaways
- Market mechanics (assignment uncertainty, open-interest concentration) create real risks that continuous-time models ignore.
- Parity relationships hold only under cash-settled, synchronized instruments.
- Expiration handling is a craft: information arriving after the close makes the last hours a game of conditional probabilities.
