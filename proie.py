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
    def _nouvelle_instance(self):
        return Proie(self.cycle_reproduction)
    def executer_cycle(self, coordonnees: Coordonnees, ocean: Ocean)-> None:
        super().executer_cycle(coordonnees, ocean)
        nouvelles_coordonnees = ocean.deplacer_coordonnees(coordonnees, Direction.Haut)
        valeur = ocean.infos_coordonnees(nouvelles_coordonnees)

        if valeur is None:
            ocean.effectuer_deplacement(coordonnees, nouvelles_coordonnees, self.gestion_reproduction())
                
# reproduction(), vieillissement a ajouter dans poisson
