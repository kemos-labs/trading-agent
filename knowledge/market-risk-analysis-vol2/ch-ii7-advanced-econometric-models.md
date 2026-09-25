# II.7 Advanced Econometric Models

Source: Carol Alexander, *Market Risk Analysis*, Vol. II (Practical Financial
Econometrics), ch II.7.

## Core idea

OLS linear regression is the baseline ("ordinary spectacles"): plot the data
first, then run OLS, and only escalate to a more powerful model if a
relationship is evident. More advanced models (quantile regression, discrete
choice, Markov switching) see more — but fitting a Ferrari engine where a
2CV would do risks detecting spurious relationships.

## Quantile regression

OLS predicts the conditional *mean*; **quantile regression** (Koenker &
Bassett 1978) estimates any conditional quantile by minimizing an asymmetric
objective instead of residual sum of squares:

```
min sum over t of rho_tau(y_t - x_t'b),   rho_tau(u) = u*(tau - I(u<0))
```

A family of quantile regression lines gives a complete picture of the
conditional distribution of Y given X — valuable when the distribution is
non-normal and tail behavior matters (risk management). Non-linear
generalizations use **copula quantile regression**: the conditional copula
distribution (ch II.6) maps uniform quantiles to conditional quantiles of Y.

## Discrete choice models

When the dependent variable is a latent probability (default, upgrade) with
only 0/1 observations, linear regression is inappropriate. Models:
- **Probit**: P(y=1) = Phi(x'b), standard normal CDF link.
- **Logit**: P(y=1) = 1/(1+exp(-x'b)), logistic link.
- **Weibull**: P(y=1) = 1 - exp(-exp(x'b)) (complementary log-log family).

Estimated by maximum likelihood; on the same credit-default data the three
functional forms give different default probabilities — a reminder that link
choice is a model assumption.

## Markov switching models

Allow the data-generating process to switch between **regimes** (Hamilton
1989): e.g., a two-regime model with high and low volatility, where the
regime follows a (hidden) Markov chain with transition probabilities p_ij.
Applications: equities, commodities, and credit show distinct calm/turbulent
regimes; interest rates often show three regimes (declining/flat/increasing
yield-curve slope). Estimation uses maximum likelihood with the
Hamilton filter (a forward recursion over regime probabilities), which is
substantially more complex than OLS. Regime inference is probabilistic —
the filter outputs the probability of being in each regime at each date.

## Ultra-high-frequency data

Tick-by-tick data raise data-quality issues (errors, time stamps) and
motivate **autoregressive conditional duration (ACD)** models that capture
the time between trades with an autoregressive framework analogous to GARCH —
relevant for realized-volatility forecasting (variance swaps pricing).

## Key takeaways

- Plot the data; run OLS first; escalate only when the structure warrants it.
- Quantile regression estimates the full conditional distribution — use it
  for tail-focused risk analysis.
- Probit/logit/Weibull handle binary outcomes via different link functions;
  the choice matters.
- Markov switching captures regime-dependent behavior; the Hamilton filter
  gives smoothed regime probabilities and transition probabilities.

Related skills: `skills/hmm-regime-detection` (regime modeling in Python),
`skills/statistical-significance-testing`, `knowledge/market-risk-analysis-
vol1/ch-i4` (regression foundations).
