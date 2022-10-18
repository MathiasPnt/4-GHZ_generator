# Numerical simulations of on-chip generation of 4-partite GHZ states

[![DOI](https://zenodo.org/badge/550971860.svg)](https://zenodo.org/badge/latestdoi/550971860)

Numerical simulations based on a phenomenological model of an experimental apparatus using the linear optical circuit framework Perceval. This code is used in a scientific project that demonstrate a high fidelity preparation of path-encoded 4-qubit GHZ states on a tunable glass photonic chip.

# Key Features

* reconstruct the density matrix from measured indistinguishability (M) and multiphoton component (g2)
* easily adaptable to any optical circuit


# Installation

Perceval requires:

* Python 3.9 or above

This script requires a specific fork of the package Perceval to run. We recommend installing it with `pip`:

```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install git+https://github.com/MathiasPnt/Perceval.git@imperfect_sps
```



