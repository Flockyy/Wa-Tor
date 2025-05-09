#from typing import List
from ocean import Ocean, Coordonnees, Direction
from poisson import Poisson


class Proie(Poisson):
    """
    Classe Proie (descendant de Poisson, qui tente de survivre en échapant aux prédateurs)

    Args:
        cycle_reproduction (int): 8 par défaut. Nombre de cycle entre chaque reproduction.
    """
    def __init__(self, cycle_reproduction: int = 8):
        super().__init__(cycle_reproduction)
        self._age = 0
    def __str__(self):
        return f"Proie ayant un cycle de reproduction de {self.cycle_reproduction} tours"
    def caractere_symbole(self)-> str:
        return "P"
    def executer_cycle(self, coordonnees: Coordonnees, ocean: Ocean)-> None:
        self.vieillisement()
        nouvelles_coordonnees = ocean.deplacer_coordonnees(coordonnees, Direction.Haut)
        valeur = ocean.valeur_coordonnees(nouvelles_coordonnees)

        if valeur is None:
            if self.reproduction():
                ocean.grille[coordonnees.ligne][coordonnees.colonne] = Proie(self.cycle_reproduction)
                self.reinitialisation_age()
            else:
                ocean.grille[coordonnees.ligne][coordonnees.colonne] = None

            ocean.grille[nouvelles_coordonnees.ligne][nouvelles_coordonnees.colonne] = self
                
# reproduction(), vieillissement a ajouter dans poisson
