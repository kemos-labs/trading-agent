# Ch16 — Natural Language Processing with RNNs and Attention

**Source:** Géron, *Hands-On Machine Learning*, Chapter 16.

## Purpose
NLP with char-RNNs, sentiment RNNs, encoder–decoders, and the
**transformer** + attention, ending with pretrained giants (GPT/BERT) and
Hugging Face.

## Char-RNN text generation (Shakespeare)
- Encode text to char ids (`TextVectorization(split="character",
  standardize="lower")`); window into (input, next-char) pairs.
- Model: Embedding → GRU(return_sequences) → Dense(softmax over vocab);
  loss = sparse categorical crossentropy. Window length bounds learnable
  patterns.
- **Generation**: feed context, sample next char from the predicted
  distribution. **Greedy decoding** repeats; **sampling** with
  `tf.random.categorical` gives diversity; **temperature** T divides the
  logits — T→0 rigid/accurate, T high creative/random.
- **Stateless vs stateful RNNs**: stateless = each window resets hidden
  state; stateful preserves state across batches/epochs (learns longer
  patterns; must process data in order, reset state between epochs).

## Sentiment analysis (word-level)
- Words → `TextVectorization` → Embedding → RNN/CNN → Dense sigmoid.
- Imbalanced data: class weights; monitor precision/recall.
- RNNs, 1D CNNs, or transformers all work; transformers generally best.

## Encoder–decoder & neural machine translation
- Encoder compresses the source sentence into a context vector; decoder
  generates the translation word by word (teacher forcing during training:
  feed the true previous word; at inference feed its own outputs).
- Sequence-to-vector + vector-to-sequence stacked; the whole source must be
  read before decoding starts (vs seq2seq single RNN).

## Attention mechanisms
- Problem: the fixed context vector is a bottleneck — long sentences lose
  information. **Attention** lets the decoder look at *all* encoder hidden
  states, weighted by learned alignment scores: each decoder step computes
  similarity (dot product) between its query and encoder keys, softmaxes
  into attention weights, and takes a weighted sum of the values.
- **Scaled dot-product attention**: `Attention(Q, K, V) =
  softmax(QKᵀ/√dₖ)V`. **Multi-head attention**: h parallel heads each with
  own Q/K/V projections, concatenated — lets the model attend to different
  relationship types.
- **Transformer**: attention-only (no recurrence); encoder = stacked
  self-attention + FFN blocks, decoder = masked (causal) self-attention +
  cross-attention to encoder. **Positional encoding** adds position info
  (since attention is permutation-invariant). Padding masks (ignore pad
  tokens) + causal masks (decoder can't see future).
- Transformer = parallelisable (unlike RNNs), no long-range memory limit.

## The transformer avalanche
- **GPT** (decoder-only, causal/masked attention, autoregressive next-token
  pretraining → fine-tune; zero-shot at GPT-2 scale). **BERT** (encoder-only,
  bidirectional, trained with **masked language modelling** 15% masked +
  **next-sentence prediction**; fine-tune per task). **T5** (all NLP as
  text-to-text). **DistilBERT** (distillation: student trained on teacher's
  soft labels — often beats training the student alone).
- Costs: training giant models needs huge capital/energy; use pretrained
  models (Hugging Face hub) + fine-tuning instead of training from scratch.
- **Hugging Face `transformers`**: `pipeline`, `AutoTokenizer` +
  `AutoModelForSequenceClassification` — pretrained SOTA in a few lines.

## Key takeaways
- Sequence modelling ladder: RNN (short) → LSTM/GRU (medium) → attention/
  transformers (long, parallelisable) → pretrained LLMs (transfer).
- Attention = learned soft lookup over all inputs; the transformer's
  building block.
- Temperature controls generation diversity; sampling beats greedy.
- Use pretrained models + fine-tuning for real NLP tasks.

## Notes
- Transformer architecture reappears in modern forecasting
  (time-series transformers) — same attention machinery.
- The causal mask trick (`tf.linalg.band_part`) is the decoder's
  no-peeking mechanism — reused in autoregressive models everywhere.
