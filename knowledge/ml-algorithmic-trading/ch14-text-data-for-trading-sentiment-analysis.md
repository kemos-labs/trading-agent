# Ch14 — Text Data for Trading: Sentiment Analysis

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 14.

## Purpose
The NLP workhorse applied to markets: turning news, tweets, and filings into sentiment features — from bag-of-words and dictionaries to ML classifiers — and validating that sentiment actually predicts returns.

## Text data for trading
- Sources: news wires, social media (Twitter), earnings calls/transcripts, SEC filings, analyst reports.
- **Why it works**: language conveys information not yet priced in; aggregate sentiment can be a leading indicator (e.g., post-earnings drift, event-driven moves).
- Key design choice: *event* vs. *continuous* sentiment — align text to asset and timestamp, respecting publication time (lookahead discipline from ch2/ch3).

## Text preprocessing pipeline
- Lowercase, remove punctuation/stop words, tokenize.
- **Stemming/lemmatization** to merge inflections.
- N-grams (1-2-3) to capture phrases ("beat estimates", "missed guidance").
- **Dictionary-based sentiment**: count matches in lexicons (Loughran-McDonald for finance — words like "loss", "risk" have financial valence distinct from general lexicons like AFINN/VADER).

## Bag-of-words representations
- Count vectors → **TF-IDF**: weight term frequency by inverse document frequency; tfidf(t,d) = tf·log(N/df_t). Reduces common-word dominance, highlights discriminative terms.
- Document-term matrix as features for linear classifiers (logistic regression is a strong, interpretable baseline).
- **Beyond BoW**: word embeddings (ch16) capture context; transformers/BERT fine-tuning for state-of-the-art.

## Classification and evaluation
- Target: document-level sentiment label (positive/negative) or forward-return-based labels.
- Models: logistic regression/SVM on TF-IDF as baseline; validate with stratified splits (class imbalance is common — use AUC/F1).
- **The finance-specific test**: does predicted sentiment → returns? Rank stocks by sentiment score and evaluate IC and long-short spreads (ch4 methodology) — text models live or die by this economic test, not accuracy.

## Pitfalls
- **Event-driven leakage**: sentiment from an article published at time t can only be used at t+1; timestamps must be the publication time, not crawl time.
- **Lookahead in labels**: forward returns must be measured *after* the text's availability.
- Domain mismatch: general lexicons misclassify financial language; use finance-specific dictionaries and domain-tuned models.
- Sparse, noisy, adversarial content (spam/trolls) — filter and aggregate carefully.

## Key takeaways
- Sentiment analysis is a feature-engineering layer: the output must survive the IC/quantile test to matter.
- TF-IDF + linear models is a strong, fast, auditable baseline before deep NLP.
- Timestamp integrity and domain lexicons are where sentiment strategies are won or lost.
