# Options Pricing (Consolidated)

## name
Vanilla options pricing & hedging toolkit: Black-Scholes-Merton closed
forms, put-call parity, the Greeks, implied volatility, and the numerical
methods (binomial tree, Monte Carlo / LSM) for everything closed forms
can't reach.

## description
The one-stop skill for pricing and risk-managing plain-vanilla options.
Starts with the BSM model (closed-form call/put, the carry adjustment b
that makes one formula cover stocks, futures and FX), put-call parity as
the no-arbitrage backbone, and the Greeks (delta, gamma, vega, theta,
rho) with their formulas. Then implied volatility by root-finding, and
when to switch to numerical methods — binomial tree (CRR) for
European/American vanillas, Monte Carlo / Least-Squares Monte Carlo for
path-dependent and multi-asset payoffs. Consolidates
`skills/binomial-tree-pricing` and `skills/monte-carlo-option-pricing`
into one decision tree; read those skills for the full vectorized code.

## when to use it
- You need a fast, auditable reference price for a European/American
  call or put (sanity-check market quotes, arbitrage screens, mark-to-
  model).
- You are hedging and need deltas/gammas/vegas — either closed-form (BSM
  underlyings) or numerical (MC/tree for anything else).
- You need implied volatility from a market price (the vol that makes
  the model price equal the quote) for vol surfaces, relative-value
  screens, or VaR inputs.
- Payoff is exotic/path-dependent/multi-asset or needs early exercise in
  high dimensions → Monte Carlo/LSM; moderate-dimension American →
  tree/finite differences.
- Teaching/auditing: the binomial tree is the discrete proof that
  price = E_Q[discounted payoff] and delta = hedge.

## the method

### 1. Black-Scholes-Merton (European, closed form)
Underlying follows GBM; the correctly hedged position breaks even (PDE).
Solution for a European call on a non-dividend stock:

```
d1 = [ln(S/X) + (b + σ²/2)·t] / (σ·√t)
d2 = d1 − σ·√t
C  = S·e^((b−r)t)·N(d1) − X·e^(−rt)·N(d2)
P  = X·e^(−rt)·N(−d2) − S·e^((b−r)t)·N(−d1)
```

**Carry adjustment b** — one formula, three markets: stock b = r
(dividend yield q: b = r − q); futures b = 0; FX b = r_dom − r_for.
The model family differs only in the forward and settlement.

```python
from math import log, sqrt, exp
from scipy.stats import norm

def bs_price(S, X, t, r, sigma, b, option='call'):
    """Generalized BSM (Black '76 for futures via b=0)."""
    d1 = (log(S / X) + (b + sigma**2 / 2) * t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
    if option == 'call':
        return S * exp((b - r) * t) * norm.cdf(d1) - X * exp(-r * t) * norm.cdf(d2)
    return X * exp(-r * t) * norm.cdf(-d2) - S * exp((b - r) * t) * norm.cdf(-d1)
```

### 2. Put-call parity (no-arbitrage backbone)
`C − P = S·e^((b−r)t) − X·e^(−rt)` (European, same strike/maturity).
Violations → arbitrage; also prices the missing side and derives lower
bounds. For non-dividend stock (b = r): `C − P = S − X·e^(−rT)`.

### 3. Greeks
| Greek | Meaning | BSM formula (non-dividend stock) |
|---|---|---|
| Delta | ∂V/∂S | call: N(d1); put: N(d1)−1 |
| Gamma | ∂²V/∂S² | φ(d1) / (S·σ·√t) |
| Vega | ∂V/∂σ | S·φ(d1)·√t |
| Theta | −∂V/∂t | call: −S·φ(d1)·σ/(2√t) − r·X·e^(−rt)·N(d2) |
| Rho | ∂V/∂r | X·t·e^(−rt)·N(d2) (call) |

φ = standard normal pdf. (Put theta flips the second term's sign;
theta = decay of volatility value + spot-to-forward drift + changing
present value of the strike.) For futures/FX (b ≠ r) multiply the
delta/gamma/vega rows by the carry factor e^((b−r)t) — the table
above is the non-dividend-stock (b = r) special case. **Value Greeks are additive across a portfolio;
position Greeks are not** — to neutralize a book, solve the linear system
in value-Greek space, then delta-hedge with the underlying (which has
zero vega/gamma).

Hedge-ratio interpretation: delta = N(d1) > N(d2) = ITM probability, so
an at-the-forward call has Δ > 0.5 and its companion put < −0.5.

### 4. Implied volatility (root-finding)
Find σ such that model price = market price. Bisection is robust; or
Newton with vega as the derivative (vega > 0, so monotone in σ):

```python
def implied_vol(market_price, S, X, t, r, b, option='call',
                lo=1e-4, hi=5.0, tol=1e-6):
    while hi - lo > tol:
        mid = (lo + hi) / 2
        p = bs_price(S, X, t, r, mid, b, option)
        if p > market_price: hi = mid
        else:                lo = mid
    return (lo + hi) / 2
```

Volatility is the only unobservable input — the IV surface (smile/skew
by moneyness and term) is where real relative value lives.

### 5. Numerical methods (when closed forms fail)
- **Binomial tree (CRR)**: u = e^(σ√Δt), d = 1/u, p̃ =
  (e^((r−q)Δt) − d)/(u − d); backward induction with
  max(continuation, intrinsic) at every node for Americans. Converges to
  BSM as N → ∞. Full vectorized code in
  `skills/binomial-tree-pricing/SKILL.md`.
- **Monte Carlo**: simulate risk-neutral paths (log-Euler with the
  −0.5σ² drift), average discounted payoffs; variance reduction via
  antithetic variates + moment matching; **American valuation by LSM**
  (regress continuation value on polynomial basis of in-the-money
  paths). Full code in `skills/monte-carlo-option-pricing/SKILL.md`.
- **Multi-asset**: Cholesky-decompose the covariance for correlated
  paths (`skills/correlated-scenario-simulation`).
- **Finite-difference Greeks**: bump the input, re-price with the same
  random numbers (common random numbers cut noise):
  `Δ ≈ (V(S+h) − V(S−h)) / 2h`.

Decision rule: European + closed form exists → BSM. American vanilla →
tree or finite differences (low dimension). Path-dependent, exotic,
high-dimensional, or multi-asset → Monte Carlo/LSM.

## known pitfalls
- **b vs r confusion**: use b (carry) in d1/d2 and the forward term,
  r only for discounting — mixing them misprices futures/FX options.
- **Degenerate tree**: if e^((r−q)Δt) falls outside [d, u], p̃ ∉ [0,1]
  and tree prices are meaningless — check the no-arbitrage condition.
- **American = max at EVERY node**, not just maturity — forgetting early
  exercise silently returns the European price.
- **Missing the −0.5σ² drift** in Monte Carlo biases every path.
- **IV root-finding edge cases**: deep-OTM and very short-dated options
  have tiny vega (flat price-vs-σ) — widen tolerances, guard against
  non-convergence, and never report IV for price outside [0, intrinsic-
  adjusted bounds].
- **Price-vs-model sanity**: BSM assumes constant σ and r; real markets
  have a vol smile — a single "the" IV only exists per strike/tenor.
- **Greeks near expiry**: gamma and vega blow up for ATM options as t→0;
  numerically differentiate with care (choose h ~ 1% of S, not machine
  epsilon).

## source
Natenberg, *Option Volatility and Pricing*, 2nd ed., ch18 (BSM formula,
40% rule, Greeks); Alexander, *Market Risk Analysis* Vol. III, ch III.3
(risk-neutral valuation, put-call parity, value vs position Greeks);
Shreve, *Stochastic Calculus and Finance* ch1–5 (tree); Hilpisch,
*Python for Finance* 2ed ch12, ch18–19 (MC/LSM). Consolidates the
existing `skills/binomial-tree-pricing`, `skills/monte-carlo-option-
pricing` skills; knowledge notes in `knowledge/natenberg-option-
volatility-and-pricing/ch18` and `knowledge/market-risk-analysis-vol3/
ch-iii3-options`.
