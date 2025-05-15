import random
from typing import List
from proie import Proie
from requin import Requin
from proie import Proie
from ocean import Ocean, Coordonnees


class Monde:
    """Class monde représente le monde de la simulation Wa-tor.
    Cette classe est responsable de la gestion de la grille, y compris sa taille et le
    placement de proies et de requins.
    """

    def __init__(
        self,
        nb_lignes: int,
        nb_colonnes: int,
        nb_requins: int,
        nb_proies: int,
        cycle_reproduction_requin: int,
        cycle_reproduction_proie: int,
        visibilite_requin: int,
        visibilite_proie: int,
        vue_arriere_requin: bool,
        vue_arriere_proie: bool,
        points_vie_requin: int,
        points_par_repas_requin: int,
    ):
        """Initialise le monde avec une grille de la taille donnée.

        Args:
            nb_lignes (int): Nombre de lignes dans la grille.
            nb_colonnes (int): Nombre de colonnes dans la grille.
        """
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes
        self.__nb_requins = nb_requins
        self.__nb_proies = nb_proies
        self.__cycle_reproduction_requin = cycle_reproduction_requin
        self.__cycle_reproduction_proie = cycle_reproduction_proie
        self.__visibilite_requin = visibilite_requin
        self.__visibilite_proie = visibilite_proie
        self.__vue_arriere_requin = vue_arriere_requin
        self.__vue_arriere_proie = vue_arriere_proie
        self.__points_vie_requin = points_vie_requin
        self.__points_par_repas_requin = points_par_repas_requin
        self.__ocean = Ocean(nb_lignes, nb_colonnes)
        self.__numero_chronon = 0
        proie = [
            Proie(
                self.ocean,
                self.__cycle_reproduction_proie,
                self.__visibilite_proie,
                self.__vue_arriere_proie,
            )
            for _ in range(self.__nb_proies)
        ]
        requins = [
            Requin(
                self.ocean,
                self.__cycle_reproduction_requin,
                self.__visibilite_requin,
                self.__vue_arriere_requin,
                self.__points_vie_requin,
                self.__points_par_repas_requin,
            )
            for _ in range(self.__nb_requins)
        ]
        self.placer_poissons_aleatoirement(proie, requins)

    @property
    def nb_lignes(self):
        return self.__nb_lignes

    @property
    def nb_colonnes(self):
        return self.__nb_colonnes

    @property
    def numero_chronon(self):
        return self.__numero_chronon

    @property
    def ocean(self) -> Ocean:
        return self.__ocean

    def placer_poissons_aleatoirement(
        self, proies: List[object], requins: List[object]
    ):
        """Place une liste de proies et de requins dans la grille.
        Cette méthode place les proies et les requins dans la grille à des positions aléatoires.
        Si une position est déjà occupée, une nouvelle position est tirée jusqu'à trouver une cellule vide.

        Args:
            proies (List[object]): Liste d'objets de type Proie à placer dans la grille.
            requins (List[object]): Liste d'objets de type Requin à placer dans la grille.
        """
        if not isinstance(proies, list):
            raise TypeError("Les proies doivent être une liste")
        if not isinstance(requins, list):
            raise TypeError("Les requins doivent être une liste")

        # place les proies et les requins dans la grille aleatoirement
        for proie in proies:
            if not isinstance(proie, Proie):
                raise TypeError("L'objet doit être une proie")
            coordonnees = self._get_random_empty_cell()
            while self.ocean.valeur_coordonnees(coordonnees) is not None:
                coordonnees = self._get_random_empty_cell()
            self.ocean.placer_proie(proie, coordonnees)

        # place les requins dans la grille aleatoirement
        for requin in requins:
            if not isinstance(requin, Requin):
                raise TypeError("L'objet doit être un requin")
            coordonnees = self._get_random_empty_cell()
            while self.ocean.valeur_coordonnees(coordonnees) is not None:
                coordonnees = self._get_random_empty_cell()
            self.ocean.placer_requin(requin, coordonnees)

    def _get_random_empty_cell(self) -> tuple:
        """Génère des coordonnées aléatoires jusqu'à trouver une cellule vide (non occupée) dans la grille de l'océan.

        Returns:
            tuple: Coordonnées (i, j) de la cellule vide.
        """
        while True:
            ligne = random.randint(0, self.nb_lignes - 1)
            colonne = random.randint(0, self.nb_colonnes - 1)
            coordonnees = Coordonnees(ligne, colonne)
            if self.ocean.valeur_coordonnees(coordonnees) is None:
                return coordonnees

    def executer_cycle(self) -> None:
        """Exécution d'un cycle pour l'ensemble des poissons.
        Le cycle se déroule en deux phases:
        1. Les requins sont traités en premier, dans l’ordre de parcours de la grille. Ils peuvent se déplacer, se reproduire ou manger une proie.
        2. Les proies survivantes (ou nouvelles) sont ensuite traitées.

        Returns:
            None
        """
        liste_poissons = []  # on récupère dans l'ordre les requins puis les proies…
        for ligne in range(self.nb_lignes):
            for colonne in range(self.nb_colonnes):
                coordonnees = Coordonnees(ligne, colonne)
                poisson = self.ocean.valeur_coordonnees(coordonnees)
                if isinstance(poisson, Requin):
                    liste_poissons.append(
                        {"instance": poisson, "coordonnes": Coordonnees(ligne, colonne)}
                    )
        for poisson in liste_poissons:
            poisson["instance"].executer_cycle(poisson["coordonnes"])
        liste_poissons = (
            []
        )  # les requins ont peut-être mangé... on passe la main aux proies survivantes.
        for ligne in range(self.nb_lignes):
            for colonne in range(self.nb_colonnes):
                coordonnees = Coordonnees(ligne, colonne)
                poisson = self.ocean.valeur_coordonnees(coordonnees)
                if isinstance(poisson, Proie):
                    liste_poissons.append(
                        {"instance": poisson, "coordonnes": Coordonnees(ligne, colonne)}
                    )
        for poisson in liste_poissons:
            poisson["instance"].executer_cycle(poisson["coordonnes"])

    # def liste_scenarii

    def __repr__(self):
        """Retourne une représentation textuelle du monde."""
        return f"Monde({self.lignes}, {self.colonnes}, {self.ocean})"

    def __str__(self):
        """Retourne une représentation textuelle du monde."""
        return str(self.ocean)
