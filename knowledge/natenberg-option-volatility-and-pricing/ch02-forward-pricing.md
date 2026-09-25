# Chapter 2 — Forward Pricing

Source: Natenberg, *Option Volatility and Pricing*, 2nd ed. (2015)

## Core principle

A forward contract defers the costs and benefits of ownership, it does
not eliminate them. The fair forward price reflects them:

    forward price = cash price + costs of buying now − benefits of buying now

Basis = cash price − forward price (usually negative in contango).

## Forward price formulas (simple interest convention)

- **Physical commodities** (C = cash price, r = interest rate, t = time,
  s = annual storage, i = annual insurance):
  `F = C × (1 + r·t) + (s + i)·t`
  Costs are always positive, so futures > cash in a normal/contango
  market. If cash > futures, the market is *backwardated*; the premium
  users pay for immediate access is the **convenience yield**. You can
  infer it from quoted cash vs. futures: e.g. with F = 77.40, r = 8%,
  s + i = 3.60/yr, t = 3 mo, fair cash = 77.40/1.02 − 0.90 = 74.98; a
  quoted cash price of 76.25 implies convenience yield ≈ $1.25/unit.
- **Stock** (aggregating dividends D, ignoring interest on them):
  `F = S × (1 + r·t) − D`
  Example: S = 67.00, r = 6%, t = 8/12, D = 0.66 →
  F = 67 × 1.04 − 0.66 = **69.02**. Exact version discounts each
  dividend's future value separately.
- **Bonds/notes**: same as stock, treating coupons as dividends.
- **FX**: with S = spot domestic-per-foreign, r_d domestic, r_f foreign:
  `F = S × (1 + r_d·t) / (1 + r_f·t)`. Interest-rate differentials
  (carry) determine the forward premium/discount.
- **Futures options**: the forward price of the underlying futures is
  simply its quoted futures price — no extra computation (one reason
  futures options are easier to evaluate than stock options).

## Arbitrage and implied values

- **Cash-and-carry arbitrage**: buy cash, sell futures (or sell forward,
  buy stock), carry to maturity. If 8-mo forward trades at 69.50 vs fair
  69.02, sell the forward, buy stock: locked profit 0.48 per unit,
  insensitive to spot/futures moves (both legs fixed). Residual risks:
  interest-rate changes on borrowed funds, dividend uncertainty (uncut vs
  announced).
- **Implied values**: given F, solve the pricing equation for the missing
  input — *implied spot*, *implied interest rate*, *implied dividend*
  (D = S·(1 + r·t) − F). Implied values = the market's consensus estimate
  of an input; recurring theme throughout the book (cf. implied vol).

## Dividend mechanics (US conventions)

- Declared date → record date (must own on this date) → payable date.
- Settlement is T+3; a buyer must purchase 3 business days before record
  date to get the dividend. Ex-dividend date = 2 business days before
  record date: quotes drop by the dividend amount that morning.
- Dividend *date* accuracy matters most when payment falls near contract
  maturity — a small date error can shift derivative value significantly.

## Short sales and the arbitrage band

- Shorting = borrowing stock, selling it; lender holds proceeds and pays
  the **short-stock rebate** r_s (less than the full **long rate** r_l
  when the stock is hard to borrow; ~0 in a squeeze).
  Borrowing costs: `r_bc = r_l − r_s`.
- Repricing the short-side arbitrage with the short rate creates a
  **no-arbitrage band**. Example: forward at 68.75. With r_l = 6% the
  fair price is 69.02 (buy-forward arbitrage works if F < 69.02, i.e.,
  selling stock you own nets 0.27). With r_s = 4% the short-sale fair
  price is 68.13 — shorting stock to buy the cheap forward loses 0.62.
  Only forward prices < 68.13 or > 69.02 allow arbitrage.
- **Options always use the long rate**: they are created, not
  deliverable, so no borrowing constraint applies to shorting an option.

## Key takeaways

1. Forward price = spot + net carry cost; every derivative on a stock
   ultimately keys off this forward value.
2. Shorting frictions (rebate < long rate) widen the no-arbitrage
   bounds — an arbitrage model must use the correct financing rate per
   leg.
