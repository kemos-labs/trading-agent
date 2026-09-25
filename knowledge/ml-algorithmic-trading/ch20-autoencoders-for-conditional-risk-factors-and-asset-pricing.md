# Ch20 — Autoencoders for Conditional Risk Factors and Asset Pricing

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 20.

## Purpose
Autoencoders — neural nets trained to reconstruct their input — as unsupervised feature extractors: nonlinear dimensionality reduction, denoising, and the Gu-Kelly-Xiu conditional autoencoder that learns *data-driven risk factors conditioned on asset characteristics*.

## Autoencoder basics
- Encoder h = f(x) compresses input; decoder g(h) reconstructs; the hidden layer h is the learned code/representation.
- Trained to minimize reconstruction loss (e.g., MSE) with constraints that prevent copying the identity function.
- **Undercomplete** (bottleneck < input): lossy compression → learns the most salient structure; with linear activations it recovers the PCA subspace — so autoencoders are *nonlinear PCA*.
- **Overcomplete + regularization** (L1 sparsity penalty on the code): sparse encodings select informative features.
- **Denoising autoencoders**: train on corrupted inputs (add noise), reconstruct clean originals — forces learning of the true data-generating structure; the basis of generative models.
- Variants: convolutional autoencoders for images/grid data (conv encoder + upsampling decoder); variational autoencoders (VAE) — probabilistic, sample from latent space → generative.

## Applications in finance
- **Dimensionality reduction / features**: compress many raw features into a dense code feeding a supervised model; t-SNE on the code shows cluster structure.
- **Risk factors**: PCA-style factor extraction (ch13) generalized nonlinearly.
- **Denoising** noisy financial data before modeling.

## Conditional autoencoder for asset pricing (GKX 2019)
- Gu, Kelly & Xiu treat risk factors as *latent* (unobservable) drivers of return covariance; asset characteristics (size, value, momentum, …) are proxies for *time-varying* exposures to those factors.
- Architecture: an encoder maps asset *characteristics* → factor loadings (conditional betas); a decoder maps loadings × latent factors → predicted returns.
- The autoencoder is trained to predict returns with the latent-factor structure as an intermediate bottleneck — "conditional" because loadings depend on observable characteristics, giving a nonlinear, data-driven factor model.
- Related: **IPCA** (Kelly, Pruitt & Su) — linear latent-factor model with characteristic-instrumented loadings; the linear relative of the GKX autoencoder.
- Result: assets with similar characteristics share factor exposure; predicted returns from the model can drive long-short portfolios.

## Pitfalls
- Autoencoders can overfit and learn noise — undercomplete/bottleneck capacity and regularization matter.
- Latent factors have no inherent economic meaning — interpret via loadings and downstream performance.
- Same validation discipline: the extracted factors/features must improve out-of-sample prediction (walk-forward), not just reconstruction.

## Key takeaways
- Autoencoders = nonlinear PCA + denoising + generative groundwork in one framework.
- The GKX conditional autoencoder is a modern, ML-native factor model: latent factors with characteristic-conditioned loadings.
- Evaluate any learned representation by its downstream economic value (IC, spreads, costed backtest).
