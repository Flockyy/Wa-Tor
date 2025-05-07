#from typing import
from grille import Grille, Coordonnees
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
        return "O"
    def mange(self)-> None:
        self.__points_energie += self.__points_par_repas
    def executer_cycle(self, x: int, y: int, grille: Grille)-> None:
        nouvelles_coordonnees = grille.deplacer_coordonnees(x, y, "haut")
        valeur_emplacement = grille.valeur_coordonnees(nouvelles_coordonnees)
        
        if (valeur_emplacement == None) or (valeur_emplacement.__name__ == 'Proie'):
            grille.deplacer_valeur(Coordonnees(x, y), nouvelles_coordonnees)
