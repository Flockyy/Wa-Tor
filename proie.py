#from typing import List
from grille import Grille, Coordonnees, Direction
from poisson import Poisson


class Proie(Poisson):
    """
    Classe Proie (descendant de Poisson, qui tente de survivre en échapant aux prédateurs)

    Args:
        cycle_reproduction (int): 8 par défaut. Nombre de cycle entre chaque reproduction.
    """
    def __init__(self, cycle_reproduction: int = 8):
        super().__init__(cycle_reproduction)
    def __str__(self):
        return f"Proie ayant un cycle de reproduction de {self.cycle_reproduction} tours"
    def caractere_symbole(self)-> str:
        return "-"
    def executer_cycle(self, coordonnees: Coordonnees, grille: Grille)-> None:
        nouvelles_coordonnees = grille.deplacer_coordonnees(coordonnees, Direction.Haut)
        valeur = grille.valeur_coordonnees(nouvelles_coordonnees)
