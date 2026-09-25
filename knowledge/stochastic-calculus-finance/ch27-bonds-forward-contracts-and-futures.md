# Ch27 — Bonds, Forward Contracts and Futures

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes, Part II)
— Steven Shreve

## Zero-coupon bonds

Stock dS = rS dt + σS dW under the risk-neutral measure Q (switched
already; martingale representation assumed). Accumulation factor
β(t) = e^{∫₀ᵗ r(u)du}. A zero-coupon bond maturing at T pays $1; by
risk-neutral pricing its value at t is:

```
B(t, T) = E_Q[ β(t)/β(T) | F(t) ] = E_Q[ e^{−∫ₜᵀ r(u)du} | F(t) ]
```

The bond's discounted value B(t,T)/β(t) is a Q-martingale (tower
property). Given B(t,T) dollars at t, a portfolio of stock + money market
replicates the $1 at T (completeness) — the martingale representation
gives the hedge.

## Forward contracts

A forward contract on the stock with delivery T has zero value at
inception (agreed price F(t,T) such that the contract is worth 0 now).
Solving 0 = E_Q[β(t)(S(T) − F(t,T))/β(T) | F(t)]:

```
F(t, T) = E_Q[ S(T)·β(t)/β(T) | F(t) ] = S(t)/B(t, T)
```

**Forward price = spot / bond price**: with stochastic rates the forward
price is NOT simply E_Q[S(T)] (that would be the futures price) — the
discount factor inside the expectation pulls in the interest-rate-stock
covariance.

## Futures (marking to market)

Futures are settled daily (mark-to-market), so the futures price G(t,T)
satisfies the martingale property *without* discounting:

```
G(t, T) = E_Q[ S(T) | F(t) ]
```

Key differences forward vs. futures (stochastic rates):
- Forward: F = S/B — depends on rates.
- Futures: G = E_Q[S(T)] — a martingale.
- The difference G − F = covariance between S and the discount factor
  (convexity/contingent claim adjustment). With constant r they coincide:
  F = G = e^{r(T−t)}S(t).

## Trading takeaways

- Bonds are priced as discounted Q-expectations; bond prices are
  martingales after discounting — the anchor for all interest-rate
  products.
- Forward vs. futures differ exactly by the rate-asset covariance;
  treasuries, futures on rates, and swaps all live on this distinction.
- The same framework extends to bonds as underlyings: forward bond prices,
  forward rates, and later (ch28–34) term-structure models.

## Key takeaways

- B(t,T) = E_Q[e^{−∫ₜᵀ r du}|F(t)]; discounted bond price is a
  Q-martingale; replicable via stock + money market.
- Forward price F = S(t)/B(t,T); futures price G = E_Q[S(T)] — equal only
  when rates are constant/deterministic.
- The forward-futures gap = covariance of the asset with the discount
  factor — a first real example of measure/discounting subtleties that
  drive interest-rate products.
