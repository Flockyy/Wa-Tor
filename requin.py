#from typing import
from ocean import Ocean, Coordonnees, Direction
from poisson import Poisson


class Requin(Poisson):
    """
    Classe Requin (descendant de Poisson, est un prédateur qui doit manger des poissons pour survivre)

    Args:
        cycle_reproduction (int): 12 par défaut. Nombre de cycle entre chaque reproduction.
        points_energie (int): 6 par défaut. Nombre de chronons possibles sans manger. Points de vie de départ.
        points_par_repas (int): 3 par défaut. Nombre de chronons ajoutés aux points de vie lors d'un repas. 
    """
    def __init__(self, cycle_reproduction: int = 12, points_energie: int = 6, points_par_repas: int = 3):
        super().__init__(cycle_reproduction)
        self.__points_energie = points_energie
        self.__points_par_repas = points_par_repas
    def __str__(self):
        return f"Requin ayant un cycle de reproduction de {self.cycle_reproduction} tours et {self.points_energie} tours de vie"
    @property
    def points_energie(self)-> int:
        return self.__points_energie
    def caractere_symbole(self)-> str:
        return "R"
    def _nouvelle_instance(self):
        return Requin(self.cycle_reproduction, self.points_energie, self.__points_par_repas)
    def mange(self)-> None:
        self.__points_energie += self.__points_par_repas
    def executer_cycle(self, coordonnees: Coordonnees, ocean: Ocean)-> None:
        super().executer_cycle(coordonnees, ocean)
        self.__points_energie -= 1
        if self.__points_energie == 0:
            ocean.effacer_valeur(coordonnees)
        else:
            # on avance bêtement vers le haut
            if ocean.infos_coordonnees(ocean.deplacer_coordonnees(coordonnees, Direction.Haut)) is None:
                self.action_deplacement(coordonnees, Direction.Haut, ocean)
