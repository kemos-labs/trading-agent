# Ch2 — Python Infrastructure

**Source:** *Python for Algorithmic Trading: From Idea to Cloud Deployment* —
Yves Hilpisch (O'Reilly, 2021)

## The deployment problem

Python deployment is hard because: the interpreter ships only the standard
library; hundreds of optional packages must be installed separately;
building non-standard packages is OS/dependency-sensitive; version
consistency and upgrades are tedious; one package change can break others;
migrating Python versions amplifies everything. Four technology layers
solve it:

1. **Package manager** (pip, conda): install/update/remove packages, keep
   versions consistent. Conda also resolves non-Python binary deps
   (e.g. MKL).
2. **Virtual environment manager** (virtualenv, conda env): run multiple
   Python installations in parallel without conflict (e.g. py2.7 and py3.8
   side by side, or test new package versions risk-free).
3. **Containers** (Docker): a complete file system (code, runtime, system
   tools, packages) that runs identically on any host — build a
   Ubuntu+Python image once, deploy it unchanged to the cloud.
4. **Cloud instances** (virtual servers): pay for actual usage hours,
   available in minutes, meet the high-availability/security/performance
   needs of financial deployment.

## conda basics

- Miniconda = minimal Python distribution bundling conda (package +
  environment manager). Install via the shell installer script, then:
  `conda install <pkg>`, `conda update --all`, `conda search`.
- The `nomkl` metapackage avoids auto-installing the Intel MKL build
  (`conda install numpy nomkl`) — relevant on machines without MKL
  licensing/optimization.
- Environment management: `conda create -n py38 python=3.8`,
  `conda activate py38`, `conda env export > environment.yml` (reproducible
  environments), `conda env remove -n <env>`.

## Docker workflow

- `docker run -ti -h <host> -p <port>:<port> ubuntu:latest /bin/bash`
  starts an interactive Ubuntu container with port mapping (bind a host
  port into the container — essential for sockets/Jupyter in ch7).
- Pattern: base OS image → apt-get update/install (gcc, wget) → install
  Miniconda → install Python packages → commit or build via Dockerfile.
- Containers solve "works on my machine": the same image is deployed to
  the cloud with no changes.

## Cloud instances

- DigitalOcean droplets (or similar) are spun up in ~1 minute; you're
  billed per hour of usage — cheap, elastic, agile.
- **RSA public/private keys** authenticate SSH without passwords:
  generate a keypair locally, paste the public key into the provider, SSH
  with the private key.
- **Jupyter Notebook config**: generate with `jupyter notebook
  --generate-config`, set a password hash, edit the config file; Jupyter
  Lab is the extended, browser-based suite used throughout the book.
- Orchestrate setup with install scripts (apt + Miniconda + packages) so a
  fresh droplet becomes a working trading host deterministically.

## Key takeaways

- Use conda for packages/environments, Docker for reproducible images,
  cloud instances for always-on, scalable deployment — the four-layer
  stack (manager, env, container, cloud).
- Reproducible environments (`conda env export`) and scripted provisioning
  turn one-off setup into repeatable infrastructure.
- Port mapping in containers and RSA-key SSH are the two mechanics that
  make remote Jupyter/socket deployments work.
- Plan for operational risk (availability, security, performance) from the
  start — the reason professional infrastructure is a deployment
  requirement, not an option.
