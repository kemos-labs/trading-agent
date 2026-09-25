# Ch16 — Word Embeddings for Earnings Calls and SEC Filings

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 16.

## Purpose
Dense vector representations of words that capture semantics and context — word2vec, doc2vec, and transformers (BERT) — and their use for predicting stock moves from SEC filings and earnings-call text.

## Why embeddings
- Bag-of-words (ch14) ignores word order/context: "not good" ≈ "good". Embeddings place words in a continuous vector space where *similar usage → similar vector* (distributional hypothesis), and relationships appear as vector arithmetic (king − man + woman ≈ queen).

## word2vec architectures
- **CBOW**: predict the target word from the average of its context words (fast; better for frequent words).
- **Skip-gram**: predict context words from the target (better for rare words/small data).
- Training: shallow 2-layer net; the embedding matrix is the learned representation.
- **Efficient softmax**: full softmax over a huge vocabulary is slow — use hierarchical softmax (binary tree over words), or sampling-based approximations:
  - **Noise contrastive estimation (NCE)**: binary classifier distinguishing real vs. sampled noise words.
  - **Negative sampling (NEG)**: simplified NCE; optimizes embedding quality, not language-model accuracy; ~45× faster than softmax with ~25 samples.
- **Phrase detection**: merge frequent bigrams via lift scoring / normalized PMI before training so multiword units ("new york city") get single vectors.

## Training and evaluation
- Gensim `Word2Vec(sentences, sg=1, size=300, window=5, min_count, negative=15, workers)` — fast, C-based.
- Evaluate with **analogy tests**: "Tokyo is to Japan as Paris is to __" — semantic and syntactic analogy accuracy by category.
- TensorBoard projector for visualization; t-SNE/UMAP for exploration.

## Trading application: SEC filings
- Pipeline: parse 10-K filings → extract informative sections (MD&A, risk factors) → sentence-split → n-grams → train word2vec on the corpus → represent each filing (e.g., average or weighted word vectors) → use as features to predict forward returns.
- For ~3,000 companies with price data: evaluate the filing-embedding signal with IC and long-short spreads (ch4 discipline) — the test is economic, not linguistic.

## doc2vec and beyond
- **doc2vec (PV-DM/PV-DBOW)**: learns a vector per *document* as well as per word — direct document features for sentiment/classification.
- **Transformers/BERT**: attention produces context-sensitive token representations (each token's vector depends on its sentence); fine-tune a pretrained BERT on financial text for state-of-the-art embeddings; token/CLS embeddings feed downstream models.

## Pitfalls
- Embeddings inherit corpus biases; financial corpora need finance-specific training/fine-tuning.
- Averaging word vectors loses order/syntax — okay for bag-style signals, weak for nuance.
- Leakage: train embeddings on the *past* corpus only when building point-in-time features (ch2/ch3 discipline); refit periodically.

## Key takeaways
- Embeddings encode semantics and enable transfer (pretrained vectors) — a major upgrade over BoW for text features.
- word2vec's speed tricks (NCE/negative sampling, hierarchical softmax) make large-corpus training practical.
- Text-embedding features must pass the IC/quantile economic test with point-in-time training before they earn a place in a strategy.
