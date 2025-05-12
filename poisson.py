from abc import ABC,abstractmethod #Abstract Base Classes
from ocean import Ocean, Coordonnees

class Poisson(ABC):
    """
    Classe de base des êtres vivants sur WA-TOR.

    Args:
        cycle_reproduction (int): Nombre de cycle entre chaque reproduction
    """
    def __init__(self, cycle_reproduction: int):
        self.__cycle_reproduction = cycle_reproduction
        self.__nb_cycles_depuis_derniere_repro = 0

    @property
    def cycle_reproduction(self)-> int:
        return self.__cycle_reproduction

    @property
    def nb_cycles_depuis_derniere_repro(self)-> int:
        return self.__nb_cycles_depuis_derniere_repro
    
    @abstractmethod
    def _nouvelle_instance(self)-> any:
        pass

    def gestion_reproduction(self)-> any:
        if (self.__nb_cycles_depuis_derniere_repro >= self.__cycle_reproduction):
            self.__nb_cycles_depuis_derniere_repro = 0
            return self._nouvelle_instance()
        else:
            return None

    @abstractmethod
    def caractere_symbole(self)-> str:
        pass

    def executer_cycle(self, coordonnees: Coordonnees, ocean: Ocean)-> None:
        self.__nb_cycles_depuis_derniere_repro += 1