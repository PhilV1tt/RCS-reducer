# RCS Optimizer

Optimization of radar cross-section (RCS) using a genetic algorithm (GA) and 1D electromagnetic wave simulation via the FDTD (Finite-Difference Time-Domain) method.

**Goal:** find the optimal shape to minimize incident radar waves.

## Prerequisites

- Python 3.x
- pip

## Installation

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Simulations

The project contains three progressive FDTD simulations:

| File | Description |
|------|-------------|
| `src/fdtd_basic.py` | Basic FDTD — Gaussian pulse at boundary |
| `src/fdtd_source.py` | Additive source at node 50 |
| `src/fdtd_abc.py` | Absorbing Boundary Conditions (ABC) |

Run a simulation:
```bash
python src/fdtd_basic.py
```

## Project Structure

```
rcs-optimizer/
├── src/
│   ├── fdtd_basic.py    # FDTD de base
│   ├── fdtd_source.py   # Source additive
│   └── fdtd_abc.py      # Conditions absorbantes (ABC)
├── tests/
├── docs/
├── requirements.txt
└── .venv/
```

## Roadmap

- [x] 1D FDTD EM wave simulation
- [ ] Genetic algorithm for shape optimization
- [ ] RCS computation
- [ ] 2D/3D extension
