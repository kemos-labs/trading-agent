# Ch21 — Natural Language Processing

**Source:** Grus, *Data Science from Scratch*, Chapter 21.

## Purpose
Language as data: from word clouds and n-grams to **word embeddings
(word2vec)** and a **character-level RNN** for text generation.

## Text basics
- **Word clouds**: pretty but useless as analysis (position is arbitrary).
  Better: plot each word at meaningful coordinates (e.g. job-posting
  frequency vs résumé frequency) so position encodes information.
- **n-grams**: contiguous sequences of n tokens; 2-grams (bigrams) capture
  local context. `bigrams(sentence)` pairs each word with its successor;
  counts reveal phrases ("data science").
- **Language modelling with n-grams**: `P(w | previous words)` estimated
  from counts (e.g. bigram model `P(wᵢ|wᵢ₋₁)`); use **smoothing** so unseen
  n-grams don't get zero probability. The book's generator samples words by
  their conditional distribution to produce plausible text.

## Word embeddings (word2vec, skip-gram)
- **Goal**: a dense vector per word such that similar words (same context)
  have similar vectors; the `TextEmbedding` layer stores a vector per
  vocabulary word.
- **Skip-gram training**: for each word, predict its nearby context words
  (the two to the left and right). Input = word id; target = one-hot of the
  context word; model = `Embedding → Linear → softmax/CrossEntropy`.
- Training on a few sentences yields 5-D embeddings where "boat"↔"car",
  "extremely"↔"quite" are most similar by **cosine similarity**; adjectives
  cluster, nouns cluster. Even tiny data shows the effect.
- **CBOW variant** (exercise): sum the embeddings of context words to
  predict the middle word — harder to train than skip-gram on small data.
- Inspecting: project embeddings with PCA (ch10) to a 2-D scatter and see
  clusters.

## Recurrent neural networks
- **Problem**: sentences vary in length and word order matters ("dog bites
  man" ≠ "man bites dog"); a fixed-size network can't see order.
- **SimpleRNN**: keeps a hidden state updated by each input:
  `output[h] = tanh(dot(w[h], input) + dot(u[h], hidden) + b[h])`;
  the output becomes the new hidden state. Two weight matrices: w for input,
  u for previous hidden state.
- **Why simple RNNs are inadequate**: the entire hidden state is overwritten
  each step and always used — hard to learn long-range dependencies.
  Production uses **LSTM/GRU** with gating (the book ships an LSTM on GitHub).
- **Character-level RNN example**: train on a text corpus (e.g. band names),
  feed characters one at a time, sample from the output distribution each
  step to *generate* new plausible text — a classic generative demo.

## Key takeaways
- n-gram counts + smoothing give simple, workable language models.
- Word embeddings learn similarity from context (distributional semantics);
  cosine similarity is the natural metric.
- RNNs handle sequences via a hidden state, but gated variants (LSTM/GRU)
  are required for real long-range dependencies.
- Tokenise with `re.findall("[a-z]+|[.]", text.lower())` for a quick
  pipeline.

## Notes
- Reuses the ch19 framework: `Embedding`/`Linear` layers, `SoftmaxCrossEntropy`,
  cosine similarity from ch4, PCA from ch10.
- Word2vec in production = gensim; RNNs in production = PyTorch (ch27).
