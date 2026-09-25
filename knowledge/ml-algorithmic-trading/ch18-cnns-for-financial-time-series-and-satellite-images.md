# Ch18 — CNNs for Financial Time Series and Satellite Images

**Source:** Stefan Jansen, *Machine Learning for Algorithmic Trading* (2nd ed., Packt 2020), Chapter 18.

## Purpose
Convolutional neural networks: the architecture for grid-like data (images and, structured as grids, time series), including transfer learning — applied to time-series classification for trading and satellite imagery for commodity signals.

## Why convolutions
- Fully connected layers explode in parameters for images (32×32×3 = 3,072 weights per unit; 640×480 → ~1M).
- CNNs assume *grid-like topology with local structure*: nearby pixels (or nearby time steps) matter more than distant ones.
- Three architectural ideas:
  - **Sparse connectivity / receptive fields**: each unit sees only a local patch.
  - **Weight sharing**: the same filter slides across the input — translation invariance and parameter economy.
  - **Downsampling (pooling)**: max/avg pooling reduces dimensionality and adds shift/scale tolerance.
- **Convolution**: filter (kernel) applied at each position; stride, padding control output size.
- Stacked conv layers learn hierarchy: edges → textures → objects (for time series: local patterns → motifs → regimes).

## CNN for time series
- Time series is a 1-D grid: arrange features as (time × features) or (window × features × channels); a 2-D grid (features × time × tickers) mirrors image structure.
- 1-D convolutions along time with multiple filters extract local temporal patterns; pooling downsamples.
- Used for: classifying price patterns, regime detection, and return prediction from multi-asset windows.
- Training: same regularization kit (dropout, BN, early stopping); validation with time-series splits.

## Transfer learning
- Pretrain on a large generic dataset (ImageNet/VGG16), replace the final classification layer(s), fine-tune.
- **Recipe**: freeze pretrained layers → train new head → unfreeze a suffix and fine-tune with a low learning rate (unfreezing early while the head is randomly initialized destroys pretrained weights with large gradients).
- Value: strong accuracy with limited data — e.g., fine-tuned VGG16/DenseNet201 on EuroSat satellite images reaches ~98% accuracy.
- **Trading relevance**: transfer learning from generic image models to satellite data (crop monitoring, oil-tanker counts, retail lots) is the practical path — you rarely have enough labeled satellite data to train from scratch.

## Object detection and segmentation (context)
- Detection: bounding boxes around objects (R-CNN, YOLO). Segmentation: pixel-level labels. Use cases: counting tankers, cars, activity levels.

## Pitfalls
- Image-style CNNs on time series can overfit; keep filters shallow for short windows.
- Satellite/alt-image labels are sparse and noisy — transfer learning and augmentation are essential.
- Same economic test as ever: CNN predictions must produce out-of-sample IC and positive costed spreads.

## Key takeaways
- Convolution + pooling encodes locality and translation invariance — the right inductive bias for grid data, including time series.
- Transfer learning makes deep vision practical with small financial datasets.
- Time series formatted as images is a legitimate, effective CNN application — validate like any other signal.
