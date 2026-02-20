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
| `src/1.py` | Basic FDTD — Gaussian pulse at boundary |
| `src/2.py` | Additive source at node 50 |
| `src/3.py` | Absorbing Boundary Conditions (ABC) |

Run a simulation:
```bash
python src/1.py
```

## Project Structure

```
rcs-optimizer/
├── src/        # Simulation source code
├── tests/      # Unit tests
├── docs/       # Documentation
└── requirements.txt
```

## Roadmap

- [x] 1D FDTD EM wave simulation
- [ ] Genetic algorithm for shape optimization
- [ ] RCS computation
- [ ] 2D/3D extension
