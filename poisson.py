from ocean import Ocean, Coordonnees

class Poisson:
    """
    Classe de base des êtres vivants sur WA-TOR.

    Args:
        cycle_reproduction (int): Nombre de cycle entre chaque reproduction
    """
    def __init__(self, cycle_reproduction: int):
        self.__cycle_reproduction = cycle_reproduction
    @property
    def cycle_reproduction(self)-> int:
        return self.__cycle_reproduction
    def caractere_symbole(self)-> str:
        pass
    def executer_cycle(self, coordonnees: Coordonnees, ocean: Ocean)-> None:
        pass