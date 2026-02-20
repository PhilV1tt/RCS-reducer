# Simulation d'Ondes Électromagnétiques

Simulation d'ondes électromagnétiques en 1D utilisant la méthode FDTD (Finite-Difference Time-Domain).

## Prérequis

- Python 3.x
- pip

## Installation

1. Créer et activer l'environnement virtuel :
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

2. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Simulations

Le projet contient trois simulations progressives :

| Fichier | Description |
|---------|-------------|
| `src/1.py` | Simulation FDTD de base — impulsion gaussienne à la frontière |
| `src/2.py` | Source additive au nœud 50 |
| `src/3.py` | Conditions aux limites absorbantes (ABC) |

Lancer une simulation :
```bash
python src/1.py
python src/2.py
python src/3.py
```

## Structure du projet

```
Simuondes/
├── src/        # Code source des simulations
├── tests/      # Tests unitaires
├── docs/       # Documentation
└── requirements.txt
```
