# Ch17 — Binary Options: European Style

**Source:** Nassim N. Taleb, *Dynamic Hedging: Managing Vanilla and Exotic Options* (Wiley, 1997), Chapter 17.

## Purpose
European binary (bet/digital) options: pricing, hedging via call spreads, the delta paradox, and why the "easy to price, hard to hedge" product is the best training ground.

## European binaries
- **Binary option**: pays a single fixed sum or zero — a discontinuous (digital) payoff; opposite of the continuous ramp payoff.
- **European binary**: bet on the asset being above/below a level *at expiration*; American bets are "if touched" (ch18). European binaries have one strike; a European double bet = sum of two independent bets.

## The delta paradox
- **Delta ≠ probability of exercise**: the delta integrates the *payoff*, the binary price integrates only the *frequency* (probability mass). For a skewed/lognormal distribution the delta shifts (lognormal drift) while the binary value reflects the shifted probability.
- Binary cash call = e^(−r·t)·N(d₂); binary forward call = N(d₂); vanilla call = S·N(d₁) − K·e^(−rt)·N(d₂); delta = N(d₁). The delta of a put for one strike equals the price of the binary call at that strike (and vice versa) — the "binary paradox."

## Hedging a binary: it's a call spread
- Near expiration the binary's price profile becomes a near-vertical step at the strike — imitated by a *very narrow call spread* (long K, short K+ε). The binary is a call spread in disguise: long gamma below the long leg, short gamma above the short leg, a risk reversal in between.
- Mixed convexity: OTM the binary is long gamma (risking little to make much); ITM it is short gamma (earning theta). Exactly at the money it acts like a future.
- Because it is short gamma and earning theta ITM (and the reverse OTM), the "risk reversal" structure facilitates hedging with a few skewed instruments; barriers are best hedged with narrow spreads sized to compound the skew.

## Pricing via risk-neutral integration
- Bet price = ∫ f(x)p(x)dx over the in-the-money region under the risk-neutral measure; skew on one side is compensated by shifting the distribution so no side gets a free expected return ("fair dice" argument, Module B).
- The Dirac delta: gamma of a binary near expiration is a spike (like δ(t)); useful intuition for the "pin" and for barrier deltas.

## Key takeaways
- Binaries are the elementary building block of exotics — every bet and most structures contain one.
- They are hedged as narrow vertical spreads, not with raw delta — delta/gamma explode near the strike.
- Binaries are a superb training ground for book management: they expose every misunderstanding about Greeks and payoffs.
