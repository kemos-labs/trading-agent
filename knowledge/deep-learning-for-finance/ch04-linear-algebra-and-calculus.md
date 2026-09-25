# Ch04 — Linear Algebra and Calculus

**Source:** Sofien Kaabar, *Deep Learning for Finance* (O'Reilly, 2024), Chapter 4.

## Purpose
Provides the math foundation for deep learning: vectors and matrices,
the operations that manipulate them, and the calculus (derivatives and
gradients) that powers model training.

## Vectors and matrices
- A **scalar** is a single number; a **vector** is an ordered list
  (an n×1 column or 1×n row); a **matrix** is a 2-D grid of numbers.
  In ML, data is a matrix: rows = observations, columns = features.
- **Matrix multiplication** (A·B) requires A's columns to equal B's
  rows; the result's entry [i,j] is the dot product of A's row i with
  B's column j. Order matters: A·B ≠ B·A in general.
- **Transpose** Aᵀ flips rows and columns; the **identity matrix** I
  is the multiplicative neutral element (A·I = A); **inverse** A⁻¹
  satisfies A·A⁻¹ = I and exists only for square non-singular matrices.
- The **determinant** det(A) signals invertibility: det ≠ 0 means
  invertible. Solving linear systems Ax = b (e.g., ordinary least
  squares via the normal equation x = (AᵀA)⁻¹Aᵀb) is the workhorse of
  linear models.

## Derivatives
- The **derivative** measures instantaneous rate of change — the slope
  of a function at a point. In ML, it tells you which direction and how
  much to adjust a parameter to reduce a loss.
- Key rules: power rule d(xⁿ)/dx = n·xⁿ⁻¹; chain rule
  d(f(g(x)))/dx = f'(g(x))·g'(x) — the chain rule is what makes
  backpropagation through layered networks possible.
- **Partial derivatives** treat one variable at a time (others held
  constant); the **gradient** ∇f stacks all partial derivatives into a
  vector pointing in the direction of steepest ascent. Gradient
  descent steps against it to minimize a loss.

## Why this matters for deep learning
- A neural network is a composition of matrix multiplications
  (weights × activations) and nonlinear activation functions; training
  is gradient descent on the loss with respect to every weight.
- The chain rule lets the error at the output layer flow back through
  each layer — this is *backpropagation*, the core learning algorithm.
- Matrix shapes must align (broadcasting aside) — shape errors are the
  most common bug in hand-written training loops.

## Key takeaways
- Know how to compute matrix products and gradients by hand at least
  once; frameworks (NumPy, TensorFlow) automate them but you must
  understand shapes and semantics.
- Gradient descent needs a learning rate: too high diverges, too low
  crawls. The gradient only points downhill locally — non-convex loss
  surfaces (the norm in deep learning) have many local minima.
