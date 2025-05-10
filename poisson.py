from abc import ABC,abstractmethod #Abstract Base Classes
from ocean import Ocean, Coordonnees, Direction

class Poisson(ABC):
    """
    Classe de base des êtres vivants sur WA-TOR.

    Args:
        cycle_reproduction (int): Nombre de cycle entre chaque reproduction
    """
    def __init__(self, cycle_reproduction: int):
        self.__cycle_reproduction = cycle_reproduction
        self.__nb_cycles_depuis_derniere_repro = 0
        self.__direction = Direction.Aucune

    @property
    def cycle_reproduction(self)-> int:
        return self.__cycle_reproduction

    @property
    def nb_cycles_depuis_derniere_repro(self)-> int:
        return self.__nb_cycles_depuis_derniere_repro
    
    @property
    def direction(self)-> Direction:
        return self.__direction
    
    @abstractmethod
    def _nouvelle_instance(self)-> any:
        pass

    @abstractmethod
    def caractere_symbole(self)-> str:
        pass

    def action_deplacement(self, coordonnees_courantes: Coordonnees, direction_choisie: Direction, ocean: Ocean):
        """Action à effectuer à chaque cycle par le poisson, en décidant de la direction de déplacement choisie.

        Cette méthode
        - met à jour la direction choisie
        - effectue le déplacement par le poisson (si la direction choisie est différente de 'Aucune')
        - et gère la reproduction s'il y a lieu.

        Args:
            coordonnees_courantes (Coordonnees): Coordonnées courantes avant déplacement.
            direction_choisie (Direction): Direction de déplacement choisie par le poisson
            ocean (Ocean): Océan dans lequel évolue le poisson.
        """
        self.__direction = direction_choisie
        if self.direction != Direction.Aucune:
            enfant = None
            if (self.__nb_cycles_depuis_derniere_repro >= self.__cycle_reproduction):
                self.__nb_cycles_depuis_derniere_repro = 0
                enfant = self._nouvelle_instance()
            ocean.effectuer_deplacement(
                coordonnees_courantes,
                ocean.deplacer_coordonnees(coordonnees_courantes, direction_choisie),
                enfant)

    def executer_cycle(self, coordonnees: Coordonnees, ocean: Ocean)-> None:
        self.__nb_cycles_depuis_derniere_repro += 1