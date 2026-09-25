# Ch15 — Topic Modeling: Summarizing Financial News

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 15.

## Purpose
Beyond sentiment: discovering the *subjects* in a corpus via topic models (LDA and friends), then using topic exposure as features for event-driven and cross-sectional trading signals.

## Topic models in one line
A generative model that assumes each document is a mixture of a small number of topics, and each topic is a distribution over words — so documents and words get mapped into a shared latent topic space.

## LDA (Latent Dirichlet Allocation)
- Generative story: per document, draw a topic distribution θ_d ~ Dirichlet(α); per word, pick topic z ~ θ_d, then a word w ~ φ_z ~ Dirichlet(β).
- Inference (Gibbs sampling / variational EM) recovers: topic-word distributions φ (what each topic is about) and document-topic weights θ (each document's topic mix).
- **Preprocessing matters**: tokenize, remove stop words, TF-IDF weighting or counts; choose k topics by coherence/hold-out perplexity (coherence preferred — human-interpretable topics).
- Output: a dense, low-dimensional document representation (topic weights) — a *feature matrix* for ML.

## Variants and adjacent methods
- **NMF** (non-negative matrix factorization): factorizes the term-document matrix into W·H with non-negativity — sparse, parts-based topics, often cleaner than LDA for news.
- **LSA** (latent semantic analysis): truncated SVD of TF-IDF matrix; fast, but components less interpretable.
- Dynamic topic models: topics evolve over time (useful for regime/theme drift).
- **Embedding-based**: sentence/word embeddings (ch16) + clustering as a modern alternative for topic discovery.

## Applying topics to trading
- **Event monitoring**: track topic intensity for a theme (e.g., "supply chain", "regulation") across news; spikes signal events.
- **Cross-sectional features**: document-topic weights per firm per period → aggregate (e.g., mean topic weight in a window) → rank and evaluate with IC/quantile spreads (ch4).
- **Sector/thematic tilt**: topic exposures can identify firms exposed to a theme before the market prices it (e.g., AI adoption in filings).
- **Risk/regime features**: topic mix of the news flow correlates with market regimes (cf. `hmm-regime-detection`).

## Evaluation
- Topic quality: interpretability (coherence score) — not just likelihood.
- Economic value: does the topic feature predict returns with stability and monotonic quantile spreads?
- Avoid leakage: topics trained on the full corpus leak future documents into the past — refit or use expanding-window topic models for point-in-time features.

## Key takeaways
- Topic modeling turns an unstructured corpus into interpretable, low-dimensional features — the bridge from raw text to tabular ML.
- NMF and LDA are complementary; NMF is often easier to interpret for news.
- As with all text features, the economic test (IC, spreads, walk-forward) and point-in-time training are decisive.
