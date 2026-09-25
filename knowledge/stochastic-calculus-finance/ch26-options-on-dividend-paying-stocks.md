# Ch26 — Options on Dividend-Paying Stocks

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Convex payoffs: never exercise early (no dividends)

For dS = r(t)S dt + σ(t)S dB with no dividends, and a convex payoff
h(x) with h(0) = 0 (e.g. a call (x−K)⁺), the American value equals the
European value: **early exercise is never optimal**. Proof: with β(t) the
accumulation factor, S(T)/β(T) ≥ S(t)/β(t) is dominated... more precisely,
h(S(T)/β(T)) ≥ h(S(t)/β(t)) · (β(t)/β(T))? The argument: by Jensen and
convexity, h(S(T)/β(T)) ≥ h(S(t)/β(t))·(β(t)/β(T))-style inequality; hence

```
E_Q[ h(S(T))/β(T) | F(t) ] ≥ h(S(t))/β(t)
```

so the *discounted* payoff is a Q-submartingale — waiting to expiration
dominates any early exercise (matches the discrete result of ch7).

## Dividends change everything

When the stock pays dividends, early exercise can be optimal (especially
for calls just before a dividend: you capture the dividend by exercising,
or the ex-dividend drop makes the call lose value). The analysis proceeds
by replacing the stock with the "adjusted" process: treat dividends as
cash flows, so the dividend-paying stock is modeled as an asset whose
dividends fund consumption — the pricing formula uses the *ex-dividend*
dynamics.

## Dividend-adjusted pricing

- With a continuous dividend yield q: the risk-neutral dynamics become
  dS = (r − q)S dt + σS dB (the dividend is a "negative carry" on the
  drift). European option prices use the forward price F = S·e^{(r−q)(T−t)}
  in Black-Scholes (the standard dividend-adjusted BS formula).
- With discrete dividends: the stock price drops by the dividend on the
  ex-date; prices are computed on the ex-dividend process (subtract the
  present value of future dividends from spot).
- American calls: exercise just before a dividend ex-date if the dividend
  exceeds the remaining time value; American puts: exercise when deep ITM
  (the mirror logic).

## Key takeaways

- No dividends + convex payoff ⇒ American = European (Jensen/submartingale
  argument; ch7's result in continuous time).
- Dividends add early-exercise value: calls before ex-date, puts deep ITM;
  the free boundary appears again.
- Continuous-yield adjustment: drift r → r − q; price off the forward.
- Discrete dividends: strip the PV of dividends from spot before pricing.
