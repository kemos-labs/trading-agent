# Ch15 — Processing Sequences Using RNNs and CNNs

**Source:** Géron, *Hands-On Machine Learning*, Chapter 15.

## Purpose
Forecasting time series and processing sequences with recurrent networks
(RNNs), their limitations, and sequence-capable CNNs (WaveNet).

## Recurrent neurons & layers
- A recurrent neuron takes the input AND its own previous output:
  `ŷₜ = φ(Wₓᵀxₜ + W_ŷᵀŷₜ₋₁ + b)`. Unroll through time to view as a chain.
- A layer of recurrent neurons has weight matrices for the input (Wₓ) and
  for the previous outputs (W_ŷ), often concatenated:
  `Ŷₜ = φ([Xₜ Ŷₜ₋₁]W + b)`.
- The hidden state makes the output a function of ALL previous inputs —
  a **memory cell**; basic cells only remember ~10 steps.
- Keras: `SimpleRNN`, `LSTM`, `GRU` layers; `return_sequences=True` to
  output every step (vs just the last).

## Input/output shapes
- Sequence-to-sequence (forecast next step), sequence-to-vector
  (sentiment from a review), vector-to-sequence (image caption),
  encoder–decoder (translation: whole sentence → vector → sentence).

## Training: BPTT
- **Backpropagation through time**: unroll the net, run forward, compute
  loss (maybe on the last outputs only), backprop through the unrolled
  graph — same parameters get gradient updates at each time step, summed.

## Time-series forecasting workflow (CTA ridership)
1. Load, sort by date, clean duplicates; build **windows**
   (`tf.data` + custom `to_windows` helper) with inputs = past n steps,
   targets = next step.
2. Baselines first: naive (repeat last value), ARMA family (statsmodels)
   — then beat them with ML.
3. Simple model: `SimpleRNN`/`LSTM` on windowed data; **sequence-to-vector**
   for next-step prediction, sequence-to-sequence for multi-step.
4. Compare against classical ARMA baselines — RNNs win on nonlinear
   patterns but classical models are strong baselines.

## Two core RNN problems
1. **Unstable gradients**: vanishing (standard) / exploding (esp. RNNs) —
   fixes: recurrent dropout (dropout applied to recurrent connections),
   recurrent layer normalisation, **gradient clipping** (`clipnorm`/
   `clipvalue` in the optimizer — the direct fix for exploding gradients),
   and careful init.
2. **Limited short-term memory**: basic cells remember ~10 steps; LSTM and
   GRU remember ~10× longer:
   - **LSTM**: adds a long-term state path controlled by **gates**
     (forget gate, input gate, output gate); parameters learn what to
     remember/forget.
   - **GRU**: simplified LSTM (fewer gates/params) — comparable
     performance, cheaper.

## RNNs vs CNNs for sequences
- RNNs are natural for sequences but slow (sequential time steps) and
  short-memory. **1D CNNs** can process entire sequences in parallel and
  capture local patterns — but need many layers for long-range dependence.
- **WaveNet**: dilated causal 1D convolutions — exponentially growing
  receptive field per layer; handles tens of thousands of time steps;
  produces realistic audio/sequences. Great for very long series.
- Rule of thumb: small sequences → dense net; medium → RNN/LSTM/GRU; very
  long → WaveNet-style CNN (or transformers, ch16).

## Key takeaways
- RNN = state carried across time; train by BPTT; clip gradients.
- Use LSTM/GRU (not SimpleRNN) for real memory; recurrent dropout +
  layer norm help stability.
- For very long sequences prefer dilated-conv (WaveNet) or attention
  (ch16) over RNNs.

## Notes
- The windowing + baseline-first workflow is directly reusable for any
  financial time-series forecasting project.
- Check the arma-garch-modeling skill: ARMA baselines here complement the
  project's GARCH/ARMA skill files.
