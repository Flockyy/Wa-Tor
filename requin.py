#from typing import
from poisson import Poisson

class Requin(Poisson):
    """
    Classe Requin (descendant de Poisson, est un prédateur qui doit manger des poissons pour survivre)

    Args:
        cycle_reproduction (int): 12 par défaut. Nombre de cycle entre chaque reproduction.
        points_energie (int): 6 par défaut. Nombre de cycles possibles sans manger.
    """
    def __init__(self, cycle_reproduction: int = 12, points_energie: int = 6):
        super().__init__(cycle_reproduction)
        self.__points_energie = points_energie
    def __str__(self):
        return f"Requin ayant un cycle de reproduction de {self.cycle_reproduction} tours et {self.points_energie} tours de vie"
    @property
    def points_energie(self)-> int:
        return self.__points_energie
    def symbole()-> str:
        return "O"