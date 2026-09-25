# Ch7 — Jensen's Inequality

**Source:** *Stochastic Calculus and Finance* (1997 lecture notes) — Steven
Shreve

## Statement

For a convex function φ and integrable X:

```
E[φ(X) | G] ≥ φ(E[X | G])     (conditional Jensen)
E[φ(X)] ≥ φ(E[X])             (unconditional form)
```

Proof idea: a convex function is the max of its supporting linear
functions φ(x) = max_{linear h ≤ φ} h(x); expectations pass through
linear functions, so E[φ(X)|G] ≥ h(E[X|G]) for every h ≤ φ, and taking
the max over h gives the result.

## Corollary: convex functions of martingales are submartingales

If Y_k is a martingale and φ is convex, then φ(Y_k) is a **submartingale**:

```
E[φ(Y_{k+1}) | F_k] ≥ φ(E[Y_{k+1} | F_k]) = φ(Y_k)
```

(using Jensen then the martingale property). A submartingale drifts up in
expectation — this is why prices can't be convex functions of
arbitrage-free assets without "making money."

## Optimal exercise of an American call: never early

The big result: **an American call on a non-dividend-paying stock should
never be exercised early**. For payoff g(x) = (x−K)⁺ convex with g(0) = 0:

- The discounted payoff process (1+r)^{-k} g(S_k) is a submartingale
  (convex of the discounted-stock martingale).
- Therefore for any stopping time τ, Ẽ[(1+r)^{-τ} g(S_τ)] ≤ Ẽ[(1+r)^{-n}
  g(S_n)] — waiting to expiration dominates exercising at any τ.
- Hence European value = American value for non-dividend calls, and τ = n
  (expiration) is optimal.

Intuition: the call's payoff is convex (upside unlimited, downside zero);
there is no dividend to collect, so holding to maturity is always at least
as good — money today (K) is worth more than the same K later, but the
convexity of the payoff more than compensates.

## Key takeaways

- Jensen: E[φ(X)] ≥ φ(E[X]) for convex φ — expectation and convexity
  don't commute; it's the reason convex payoffs have time value.
- Convex functions of martingales = submartingales: discounted convex
  payoffs drift up, which is why early exercise of American calls is
  suboptimal without dividends.
- Dividends (or any cash flow from holding the underlying) are what make
  early exercise valuable — that's the ch26 story.
