# Ch15 — Understanding Strategy Risk

**Source:** Marcos López de Prado, *Advances in Financial Machine
Learning* (Wiley, 2018), Chapter 15.

## Purpose
Models strategies as binomial bet processes (profit/stop-loss exits)
to derive the trade-off between precision, betting frequency, and
payoffs — and to compute the *probability of strategy failure*.

## Symmetric payouts
- n IID bets/year, win π with probability p, lose −π with 1−p.
- E[X] = π(2p−1); V[X] = 4π²p(1−p); the annualized Sharpe is
  θ(p,n) = (2p−1)√n / (2√(p(1−p))) — π cancels: with symmetric
  payouts, Sharpe depends only on precision and frequency.
- This is the economic basis of HFT: p barely above 0.5 + very large n
  → high Sharpe. Example: p = 0.55 requires ~396 bets/year for
  SR = 2. Sharpe rewards *precision* (avoiding false positives), not
  raw accuracy — negatives aren't directly punished, but too many
  negatives shrink n.
- Inverse: p = ½ + SR/(2√(SR²+n)) — explicit precision↔frequency
  trade-off.

## Asymmetric payouts
- Win π⁺ with probability p, lose −π⁻ with 1−p. Then the Sharpe becomes
  θ = (p·π⁺ − (1−p)·π⁻)/√(p(1−p))·(π⁺+π⁻)/... — payouts no longer
  cancel, and there is a minimum probability of success:
  p_min = π⁻/(π⁺+π⁻) below which even a perfect classifier loses.
- **The asymmetric payoff dilemma** (Easley et al.): market makers win
  small (the spread) and lose big (adverse selection); a tiny edge can
  be a huge loss if the loss state is larger than the win state.
- Strategies must be evaluated by *expected profit*, not hit rate: a
  90%-hit strategy with rare huge losses (negative skew) can be
  ruinous.

## Probability of strategy failure
- Given a series of bet outcomes {π_t}: estimate π⁻ = E[π|π≤0],
  π⁺ = E[π|π>0], annual frequency n = T/y, then bootstrap:
  1. For i = 1..I: draw ⌊n·k⌋ samples with replacement (k = investor
     assessment horizon, e.g., 2 years).
  2. From each bootstrap draw, estimate the realized precision
     p̂_i (share of positive outcomes) and derive the Sharpe.
  3. **P[strategy fails] = fraction of bootstrap iterations where the
     strategy's Sharpe (or cumulative profit) is negative** — the
     probability that the strategy underperforms over the assessment
     window despite its historical average.
- This is strategy risk (will this strategy make money?) — distinct
  from portfolio risk (volatility of the underlying book).

## Key takeaways
- With symmetric payouts, Sharpe = f(precision, frequency) only —
  increase n to monetize tiny edges (HFT logic).
- With asymmetric payouts, respect p_min = π⁻/(π⁺+π⁻); market-making
  payoffs demand precision far above 50%.
- Report the probability of strategy failure (bootstrap of bet
  outcomes) — it answers the question investors actually ask.
