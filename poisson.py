from ocean import Ocean, Coordonnees

class Poisson:
    """
    Classe de base des êtres vivants sur WA-TOR.

    Args:
        cycle_reproduction (int): Nombre de cycle entre chaque reproduction
    """
    def __init__(self, cycle_reproduction: int):
        self.__cycle_reproduction = cycle_reproduction
        self._age = 0
    @property
    def cycle_reproduction(self)-> int:
        return self.__cycle_reproduction
    
    def vieillisement(self) -> None:
        self._age += 1

    def reproduction(self) -> bool:
        return self._age >= self.__cycle_reproduction
    
    def _nouvelle_instance(self)-> any:
        pass

    def gestion_reproduction(self)-> any:
        if self.reproduction():
            self.reinitialisation_age()
            return self._nouvelle_instance()
        else:
            return None
    
    def reinitialisation_age(self) -> None:
        self._age = 0

    def caractere_symbole(self)-> str:
        pass
    def executer_cycle(self, coordonnees: Coordonnees, ocean: Ocean)-> None:
        pass