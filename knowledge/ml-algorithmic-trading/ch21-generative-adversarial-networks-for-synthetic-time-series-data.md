# Ch21 — Generative Adversarial Networks for Synthetic Time-Series Data

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 21.

## Purpose
GANs — generator vs. discriminator adversarial training — as generative models, and the TimeGAN adaptation that produces *synthetic financial time series* for data augmentation and backtesting.

## Generative vs. discriminative
- Discriminative: learn p(y|X) — classification/regression (the rest of the book).
- Generative: learn the joint p(y, X) or the data distribution p_data — can *sample new data*. GANs are the most prominent deep generative approach.

## GAN mechanics
- **Generator** G maps random noise z → fake samples; **discriminator** D classifies real vs. fake.
- Adversarial game: G tries to fool D; D tries to catch G. Equilibrium: G produces samples D can't distinguish from real.
- Objective: min_G max_D V(D,G) = E[log D(x)] + E[log(1 − D(G(z)))] — a zero-sum game; training alternates between updating D and G.
- **Training instability**: the game may not converge; both nets must be kept balanced (this is the classic GAN difficulty).

## Architecture zoo
- **DCGAN** (deep convolutional GAN): CNN-based generator/discriminator — the stable baseline for images.
- Conditional GANs: condition both nets on labels/context (e.g., asset class, regime) → targeted generation.
- **WGAN** (Wasserstein): critic + gradient penalty — better convergence and mode coverage.
- Time-series GANs: generator/discriminator built on RNNs (GRU/LSTM) so sequences are generated step by step.

## TimeGAN (Yoon, Jarrett, van der Schaar, NeurIPS 2019)
- Designed specifically for temporal data; the book's worked example.
- Components:
  1. **Embedder + Recovery** (autoencoder, ch20): map real series to a latent space and back — training phase 1.
  2. **Supervisor**: a model that learns the *temporal dynamics* — given the embedding at step t, predict step t+1 (supervised training phase 2) — this is what makes sequences coherent rather than point-wise fake.
  3. **Generator + Discriminator**: adversarial game in the latent space (phases 3a/3b).
- Output: synthetic time series with realistic autocorrelation, distributions, and dynamics — e.g., synthetic price series for a given asset's statistical profile.

## Financial use cases
- **Data augmentation**: generate more training samples when history is short (de Prado's point that limited history drives backtest overfitting — see `advances-financial-ml` ch13).
- **Stress/scenario generation**: sample alternative price paths for robust strategy evaluation.
- **Backtesting**: test strategies on synthetic paths as a robustness check alongside real data.
- Semi-supervised learning and model-based RL environments (ch22).

## Pitfalls
- Synthetic ≠ real: GANs may miss rare events, fat tails, and structural breaks — verify moments and autocorrelation of generated series against the real ones.
- Mode collapse: generator produces only a few patterns — watch diversity.
- Leakage if synthetic data is mixed with real data naively in validation.

## Key takeaways
- GANs learn distributions, not just boundaries — enabling sample generation, augmentation, and scenario analysis.
- TimeGAN's supervised step is what yields temporally coherent synthetic series.
- Synthetic data is a complement to — never a substitute for — honest real-data backtesting.
