# Ch13 — Naive Bayes

**Source:** Grus, *Data Science from Scratch*, Chapter 13.

## Purpose
A probabilistic classifier built directly on Bayes's theorem (ch6), used
here for a spam filter. "Naive" because it assumes all word events are
independent given the class.

## The model
- Events: S = "spam", B = "contains word bitcoin". Bayes's theorem:
  `P(S|B) = P(B|S)·P(S) / P(B)`.
- With a uniform prior `P(S) = P(¬S) = 0.5`, this simplifies to
  `P(S|B) = P(B|S) / (P(B|S) + P(B|¬S))`.
- Worked example: 50% of spam contains "bitcoin", 1% of ham does ⇒
  `0.5/(0.5+0.01) = 98%` chance a bitcoin message is spam.

## The naive assumption
- For a vocabulary of words w₁…wₙ with events Xᵢ = "message contains wᵢ":
  **assume Xᵢ independent conditional on the class**:
  `P(X₁=x₁,…,Xₙ=xₙ|S) = ∏ P(Xᵢ=xᵢ|S)`.
- Obviously false (bitcoin and rolex co-occur only in scams), yet the model
  works well in practice — that's why it's called naive.

## Practical details
- **Compute in log space** to avoid underflow when multiplying hundreds of
  tiny probabilities:
  `P(S|X) = exp(Σ log P(Xᵢ|S))` vs ham, then normalise. `log(ab)=log a+log b`.
- **Smoothing (pseudocount k)**: if a word never appeared in training spam,
  a raw fraction gives `P(data|S) = 0`, which would zero out the whole spam
  probability for any message containing it. Fix with Laplace-style
  smoothing:
  `P(Xᵢ|S) = (k + #spams containing wᵢ) / (2k + #spams)`
  and likewise for ham. (k=1: "data" in 0/98 spams ⇒ 1/100 = 0.01, not 0.)
- **Tokenisation**: lowercase, extract `[a-z0-9']+` with regex, and use a
  **set** of distinct words per message (presence/absence, not counts, for
  the book's simple version).
- **Classifier state**: token→spam-count and token→ham-count dicts plus
  message counts; train by counting; classify by scoring each token.

## Results / behaviour
- Trained on ~100 labelled messages, the filter classifies well, but:
  - spam/ham probabilities hover near 50% when few informative tokens are
    present (weak signal);
  - classification errors are dominated by *long messages* (many tokens)
    that contain one strong spam token — a genuinely useful observation for
    tuning.
- **Practical point**: a message is classified by comparing spam score vs
  ham score (log-likelihood ratio), not by thresholding a single p.

## Key takeaways
- Naive Bayes = multiply word likelihoods under each class, in log space,
  with pseudocount smoothing so unseen words don't zero out scores.
- Independence assumptions that are wrong can still yield good classifiers.
- Failure mode to remember: single strong features can overwhelm the rest in
  long inputs — check per-token contributions.

## Notes
- The `Message` NamedTuple + counting dictionaries pattern is a compact
  template for any event-counting classifier.
- Connects forward: this is a generative model; ch21's topic modelling and
  ch23's recommender reuse the same probability/conditional-independence
  machinery.
