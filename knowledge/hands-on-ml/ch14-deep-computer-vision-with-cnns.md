# Ch14 — Deep Computer Vision Using CNNs

**Source:** Géron, *Hands-On Machine Learning*, Chapter 14.

## Purpose
Convolutional neural networks: the vision workhorse, from the visual
cortex to ConvNets, and object detection/segmentation.

## Why CNNs
- Fully connected nets on images explode in parameters (100×100 image ×
  1000 neurons = 10M connections in layer one) and don't share features
  across locations. CNNs use **partially connected layers + weight sharing**
  — few parameters, translation invariance.

## Convolutional layers
- Each neuron connects only to its **receptive field** in the previous
  layer; the same **filter** (kernel, a small weight image) is shared by
  all neurons in a feature map → detects a pattern anywhere in the input.
- **Zero padding** preserves spatial size; **stride** > 1 downsamples.
- One filter = one **feature map**; a layer stacks many filters (3D output:
  height × width × num_filters). Neurons in a feature map share weights +
  bias; different maps use different filters.
- Filter values are **learned** during training (usually small odd sizes
  like 3×3, plus 1×1 convs).
- Keras: `tf.keras.layers.Conv2D(filters, kernel_size, padding="same",
  activation="relu")`; also Conv1D (sequences), Conv3D, SeparableConv2D,
  DepthwiseConv2D.

## Pooling layers
- Downsample each feature map: **max pooling** (max over a window — the
  common choice; sharpens) or average pooling; stride = pool size;
  reduces computation and gives some translation invariance.
- `MaxPool2D(pool_size=2)`; global average pooling before the head is a
  common architectural pattern.

## Modern CNN architectures
- **LeNet-5** (1998): conv → pool → conv → pool → dense; digit
  recognition.
- **AlexNet** (2012): deeper, ReLU, dropout, data augmentation — the
  ImageNet breakthrough. **GoogLeNet**: inception modules (parallel conv
  branches + 1×1 bottlenecks). **VGGNet**: simple deep stacks of 3×3.
- **ResNet** (2015): **skip connections** `y = f(x) + x` — lets gradients
  flow through deep stacks, enabling hundreds of layers. **SENet**:
  channel attention. **Xception**: depthwise-separable convs.
- **Transfer learning** (the practical default): take a pretrained
  backbone (on ImageNet), freeze or fine-tune lower layers, replace the
  head. `tf.keras.applications.ResNet50V2(weights="imagenet", ...)`.
- **Pretrained models for feature extraction**: truncate the head; use
  `keras.utils.image_dataset_from_directory` + augmentation + fine-tuning
  with a low learning rate.

## Object detection & segmentation
- **Classification** = whole image → class. **Object detection** =
  bounding boxes around multiple objects. **Semantic segmentation** = class
  per pixel. **Instance segmentation** = per-pixel + per-instance.
- Detection approaches: sliding windows + classifier; **YOLO** (single
  pass, grid of boxes — fast, popular); **SSD**; region-based (R-CNN
  family). Keras CV (keras_cv) has YOLOv8, RetinaNet, etc.
- Segmentation: **FCNs** (fully convolutional), **U-Net** (encoder-decoder
  with skip connections — the standard for medical imaging).

## Key takeaways
- CNN = conv layers (learned filters, shared weights) + pooling
  (downsample) + dense head; parameters drop by orders of magnitude.
- Use pretrained backbones + transfer learning before training from
  scratch.
- Depth works when you add skip connections (ResNet).

## Notes
- CNN building blocks (convolutions, pooling, receptive fields) also apply
  to time series: 1D convs / WaveNet (ch15) for long sequences.
- "Convolution" in deep learning is technically cross-correlation — the
  convention doesn't change learning.
