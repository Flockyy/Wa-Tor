# 🌊 Wa-Tor – Simulateur de monde aquatique

Wa-Tor est une simulation d’écosystème dans un environnement aquatique. Le monde est représenté par une grille torique où vivent deux types d'agents : les poissons 🐟 et les requins 🦈. Chaque agent suit des règles de reproduction, de déplacement et de survie, simulant une dynamique de population.

## 🔧 Requirements

Ce projet nécessite Python 3.7 ou plus récent. Pour installer les dépendances :

```bash
pip install -r requirements.txt
``` 

# ⚙️ Arguments disponibles
Le programme peut être exécuté avec les arguments suivants :
```plaintext
--auto [oui/non]          # Active ou désactive le mode automatique
--hauteur [int]           # Définit la hauteur de la grille
--largeur [int]           # Définit la largeur de la grille
--chronon [int]           # Nombre de cycles de simulation
--proie [int]             # Nombre initial de poissons
--requin [int]            # Nombre initial de requins
--fps [int]               # Images par seconde pour l'affichage pygame
```



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

# 📁 Structure du projet
```plaintext
Wa-Tor/
├── main.py                # Script principal pour exécuter la simulation en ligne de commande
├── main_pygame.py         # Script principal pour exécuter la simulation avec interface pygame
├── requirements.txt       # Fichier listant les dépendances nécessaires
├── README.md              # Documentation du projet
├── monde.py               # Module définissant la logique de simulation
├── ocean.py               # Module définissant la grille du jeu
├── poisson                # Module parent de proie et requins définissant leur logiques communes
├── proie.py               # Module définissant la classe proie
├── requin.py              # Module définissant la classe requin
├── tests/                 # Dossier contenant les tests unitaires
│   ├── __init__.py        # Fichier d'initialisation des tests
│   ├── test_monde.py      # Tests pour la logique de simulation
│   ├── test_ocean.py      # Tests pour la logique de la grille
│   ├── test_poisson.py    # Tests pour les classes des poissons
│   ├── test_proie.py      # Tests pour les classes des proies
│   └── test_requin.py     # Tests pour les classes des requins
└── assets/                # Dossier pour les ressources (images, sons, etc.)
    └── sprites/           # Dossier pour les sprites utilisés dans pygame
```
