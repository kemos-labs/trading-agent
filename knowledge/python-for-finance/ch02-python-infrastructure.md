# Chapter 2 — Python Infrastructure

## Core idea
Reproducible, production-grade Python environments: conda for package and
environment management, Docker for containerization, and cloud instances
(DigitalOcean droplets) for deployment.

## conda
- **Package manager**: `conda install numpy` etc.; the `nomkl` metapackage
  avoids Intel MKL auto-installs.
- **Virtual environment manager**: isolated environments per project —
  `conda create -n <env> python=3.7`, `conda activate <env>`. Environments
  fix package versions, so a project stays reproducible.
- Miniconda (minimal installer) is recommended over full Anaconda.

## Docker
- **Images** are read-only templates; **containers** are running instances.
- A Dockerfile can build an Ubuntu + Python image with all dependencies;
  the container then runs the analytics stack anywhere Docker runs.
- Solves the "works on my machine" problem for deployment.

## Cloud instances (DigitalOcean droplets)
- Spin up Linux VMs for always-on services (e.g., a live trading server).
- **RSA public/private keys** for passwordless SSH: generate a keypair, add
  the public key to the droplet, connect with the private key.
- **Jupyter Notebook configuration file** (`.jupyter/jupyter_notebook_config.py`)
  to set host/port/token for remote access.
- **Installation scripts**: a script to install Python + Jupyter on the
  droplet, and an orchestration script to create the droplet and push the
  setup — infrastructure as code, Bash-style.

## Why it matters
- Every quant project needs a reproducible environment: conda pins the Python
  stack, Docker pins the OS layer, the cloud provides always-on compute.
- The book's later live-trading chapters (ch16) deploy exactly this way.

## Pitfalls
- MKL and license issues: use `nomkl` where needed.
- Environment drift: always record versions (`conda list --export`) rather
  than a bare `requirements.txt`.
- Cloud cost/lock-in: droplets are cheap but must be secured (SSH keys, not
  passwords; firewall rules).

## Bottom line
The infrastructure layer of the book's stack: conda → Docker → cloud. This
mirrors `knowledge/python-algorithmic-trading/ch02`, which covers the same
four-layer stack — the ideas are standard for Python quant work.
