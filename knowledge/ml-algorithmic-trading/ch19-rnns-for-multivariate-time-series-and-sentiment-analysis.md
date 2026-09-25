# Ch19 — RNNs for Multivariate Time Series and Sentiment Analysis

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 19.

## Purpose
Recurrent neural networks for sequential data: hidden-state memory, LSTM/GRU gating, and applications to univariate/multivariate return prediction and text sentiment.

## How RNNs work
- FFNNs treat samples as iid (no memory); CNNs only see local neighborhoods. RNNs propagate a **hidden state** h_t = f(W_hh·h_{t−1} + W_hx·x_t), so each output depends on the whole past — parameter sharing across a deep unrolled graph.
- **Sequence mappings**: one-to-one (FF), one-to-many (captioning), many-to-one (sentiment), many-to-many (translation, multistep forecasting).
- **Backpropagation through time (BPTT)**: unroll the graph and backprop across all time steps — expensive and inherently sequential (no parallelization across steps).

## Gating: LSTM and GRU
- Vanilla RNNs suffer vanishing gradients on long sequences. 
- **LSTM**: cell state c_t (long-term memory) regulated by input, forget, and output gates; learn which information to write, keep, and read.
- **GRU**: simplified — update and reset gates only; fewer parameters, comparable performance; the practical default for many tasks.
- Bidirectional RNNs process the sequence both ways (context from future and past) — good for classification where the whole document is available.

## Financial applications
- **Univariate/multivariate return prediction**: reshape to (n_samples × window_size × n_series); use LSTM layers (+ dropout, recurrent_dropout), Dense head; classify direction (sigmoid + binary cross-entropy) or regress returns (linear + MSE).
- **Macro multivariate forecasting**: e.g., consumer sentiment + industrial production (FRED) with a small LSTM (12 units) + dense layers, MAE loss — a nonlinear alternative to VAR (ch9). Stationarize and min-max scale inputs.
- **Sentiment analysis**: RNN over word embeddings (ch16) — either trained or pretrained embeddings → LSTM → sentiment probability; bidirectional + attention improve accuracy.
- Evaluation: test AUC / accuracy and, for trading, IC and quintile spreads.

## Practical lessons from the book's examples
- Stacked LSTMs with dropout beat shallow ones; early stopping on validation; small data → small networks (a single LSTM layer sufficed for the macro set).
- For return *prediction*: regression on returns gave an average weekly IC of 3.3 with top/bottom quintile spread ~20bp — modest but significant, which is the realistic bar.
- Embeddings for text must be trained/selected point-in-time to avoid leakage.

## Pitfalls
- RNNs are slow to train (BPTT, sequential); GPU helps; prefer GRU when data is small.
- Financial noise + memory models = high overfitting risk; keep capacity low and validate with time-series splits.
- Teacher forcing and output-recurrence variants reduce capacity — usually not what you want for returns (returns are near unpredictable from their own lags).

## Key takeaways
- RNNs add memory — the right inductive bias for sequences where context matters across long horizons.
- LSTM/GRU solve the vanishing-gradient problem; GRU is a leaner default.
- On noisy financial data, expect modest IC — the honest benchmark for whether memory helps at all.
