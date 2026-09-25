# Ch17 — Autoencoders, GANs, and Diffusion Models

**Source:** Géron, *Hands-On Machine Learning*, Chapter 17.

## Purpose
Three generative/unsupervised families: autoencoders (learn compact latent
codes), GANs (adversarial generation), diffusion models (denoise-to-
generate).

## Autoencoders
- Learn to **copy inputs to outputs** under constraints, forcing efficient
  latent representations: encoder → **coding** (latent) → decoder;
  reconstruction loss (MSE) penalises output ≠ input.
- **Undercomplete** autoencoder (coding dim < input dim) can't trivially
  copy — learns the most important features.
- **Linear undercomplete AE with MSE = PCA** (no activations) — a great
  sanity-check link to ch8.
- **Stacked (deep) autoencoders**: symmetric encoder/decoder (784 → 100 →
  30 → 100 → 784); sandwich architecture. Careful: too powerful an encoder
  memorises arbitrary codings without learning useful representations.
- **Denoising autoencoder**: corrupt input with noise, train to recover the
  clean input — learns robust features. **Sparse AE**: sparsity penalty on
  codings (more units active rarely). **Contractive AE**: penalise
  sensitivity of codings to input.
- **Uses**: dimensionality reduction/visualisation, feature extraction,
  unsupervised pretraining (then fine-tune with labels), anomaly detection
  (high reconstruction error ⇒ anomaly), and as generative models (sample
  from the latent space).

## GANs (generative adversarial networks)
- Two competing nets: **generator** (noise → fake data) vs
  **discriminator** (real vs fake). Adversarial training: the generator
  learns to fool the discriminator; the discriminator gets sharper.
  (Criminal-vs-police analogy.)
- **Training loop**: sample real images + generator fakes; train
  discriminator to classify them; train generator to fool the
  discriminator; repeat. Discriminator loss = binary crossentropy on real
  vs fake; generator's gradient flows through the discriminator.
- **Notorious instability**:
  - **Mode collapse**: generator finds one image that fools the
    discriminator and repeats it;
  - **Non-convergence**: discriminator gets too good / oscillates;
  - vanishing gradients early on.
  - **Mitigations**: label smoothing, noise in labels, batch norm in both
    nets, larger discriminator, train generator more/less often, track
    diversity (not just loss) to spot collapse.
- Uses: super-resolution, colourisation, image editing, data augmentation,
  style transfer (StyleGAN), time-series generation.
- GAN evaluation is hard (no clean loss) — use Fréchet Inception Distance
  (FID) or human studies.

## Diffusion models (DDPM)
- **Forward process**: gradually add Gaussian noise to an image until it's
  pure noise (known schedule). **Training**: learn to denoise one small
  step (predict the noise added at each level).
- **Generation**: start from pure Gaussian noise; repeatedly apply the
  model to remove a little noise until a clean image emerges.
- Since 2021: more diverse + higher quality than GANs, **much easier to
  train** (stable objective), but **much slower at inference** (many
  denoising steps).
- This is the tech behind text-to-image models (e.g. Stable Diffusion);
  conditioning (text embeddings) guides generation.

## Key takeaways
- Autoencoder = constrained copying; the constraint is what creates value;
  great for pretraining/features/anomaly detection.
- GAN = generator/discriminator minimax game — powerful but finicky
  (mode collapse); treat training instability as the norm.
- Diffusion = learn to denoise, then generate by iterative denoising —
  stable training, slower sampling; the current SOTA family.

## Notes
- All three are unsupervised latent-representation learners — the
  "learn normal, generate new" theme connects to anomaly detection (ch9).
- For quant work: autoencoders for factor extraction/anomaly detection and
  GANs/diffusion for synthetic market-data generation are the practical
  entry points.
