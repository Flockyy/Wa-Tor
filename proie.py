#from typing import List
from ocean import Ocean, Coordonnees, Direction
from poisson import Poisson


class Proie(Poisson):
    """
    Classe Proie (descendant de Poisson, qui tente de survivre en échapant aux prédateurs)

    Args:
        ocean (Ocean) : Océan dans lequel se trouve la proie.
        cycle_reproduction (int): 8 par défaut. Nombre de cycle entre chaque reproduction.
    """
    def __init__(self, ocean: Ocean, cycle_reproduction: int = 8):
        super().__init__(ocean, cycle_reproduction)
        self._age = 0
    def __str__(self):
        return f"Proie ayant un cycle de reproduction de {self.cycle_reproduction} tours"
    def caractere_symbole(self)-> str:
        return "P"
    def _nouvelle_instance(self):
        return Proie(self._ocean, self.cycle_reproduction)
    def executer_cycle(self, coordonnees: Coordonnees)-> None:
        super().executer_cycle(coordonnees)
        # Note : pas de gestion du viellissement de la proie (selon la doc).
        #        Si on décide de la gérer, alors il faut déplacer la gestion du viuellissement de Requin vers Poisson.

        # on se déplace autant que possible en rond.
        direction_choisie = self.direction
        for _ in range(4):
            direction_choisie = Direction.tourner(direction_choisie, True, Direction.Haut)
            if self._ocean.infos_coordonnees(self._ocean.deplacer_coordonnees(coordonnees, direction_choisie)) is None:
                break
        else:
            direction_choisie = Direction.Aucune
        self.action_deplacement(coordonnees, direction_choisie)