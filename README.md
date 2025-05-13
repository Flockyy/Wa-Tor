# 🌊 Wa-Tor – Simulateur de monde aquatique

Wa-Tor est une simulation d’écosystème dans un environnement aquatique. Le monde est représenté par une grille torique où vivent deux types d'agents : les poissons 🐟 et les requins 🦈. Chaque agent suit des règles de reproduction, de déplacement et de survie, simulant une dynamique de population.

## 🔧 Requirements

Ce projet nécessite Python 3.7 ou plus récent. Pour installer les dépendances :

```bash
pip install -r requirements.txt
``` 

# ⚙️ Arguments disponibles
Le programme peut être exécuté avec les arguments suivants :



# ▶️ Exemple d'utilisation
Exécution simple, affichage en ligne de commande avec les paramètres par défaut :
```bash
python main.py 
``` 
Simulation avec des paramètres personnalisés :
```bash
python main.py --auto oui --hauteur 20 --largeur 30 --chronon 50 --proie 40 --requin 10
```

Exécution avec interface en pygame :
```bash
python main_pygame.py 
``` 

# 📁 Structure suggérée du projet
```plaintext
Wa-Tor/
├── main.py                # Script principal pour exécuter la simulation en ligne de commande
├── main_pygame.py         # Script principal pour exécuter la simulation avec interface pygame
├── requirements.txt       # Fichier listant les dépendances nécessaires
├── README.md              # Documentation du projet
├── src/                   # Dossier contenant le code source
│   ├── __init__.py        # Fichier d'initialisation du package
│   ├── simulation.py      # Module contenant la logique de simulation
│   ├── agents.py          # Module définissant les classes pour les poissons et les requins
│   └── utils.py           # Module utilitaire pour des fonctions auxiliaires
├── tests/                 # Dossier contenant les tests unitaires
│   ├── __init__.py        # Fichier d'initialisation des tests
│   ├── test_simulation.py # Tests pour la logique de simulation
│   └── test_agents.py     # Tests pour les classes des agents
└── assets/                # Dossier pour les ressources (images, sons, etc.)
    └── sprites/           # Dossier pour les sprites utilisés dans pygame
```
