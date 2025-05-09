# filename: monde.py
# Wa-tor grid and simulation

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

    def __init__(self, nb_lignes: int, nb_colonnes: int):
        """Initialise le monde avec une grille de la taille donnée.

        Args:
            nb_lignes (int): Nombre de lignes dans la grille.
            nb_colonnes (int): Nombre de colonnes dans la grille.
        """
        self.__nb_lignes = nb_lignes
        self.__nb_colonnes = nb_colonnes
        self.ocean = Ocean(nb_lignes, nb_colonnes)
        self.__numero_chronon = 0

    @property
    def nb_lignes(self):
        return self.__nb_lignes
    
    @property
    def nb_colonnes(self):
        return self.__nb_colonnes
    
    @property
    def numero_chronon(self):
        return self.__numero_chronon

    def placer_poissons(self, proies: List[object], requins: List[object]):
        """Place une liste de proies et de requins dans la grille.
        Cette méthode place les proies et les requins dans la grille à des positions aléatoires.
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
                i, j = self._get_random_empty_cell()
            self.ocean.placer_proie(proie, coordonnees)

        # place les requins dans la grille aleatoirement
        for requin in requins:
            if not isinstance(requin, Requin):
                raise TypeError("L'objet doit être un requin")
            coordonnees = self._get_random_empty_cell()
            while self.ocean.valeur_coordonnees(coordonnees) is not None:
                i, j = self._get_random_empty_cell()
            self.ocean.placer_requin(requin, coordonnees)

    def _get_random_empty_cell(self):
        """Retourne une cellule vide aléatoire dans la grille.

        Returns:
            tuple: Coordonnées (i, j) de la cellule vide.
        """
        while True:
            ligne = random.randint(0, self.nb_lignes - 1)
            colonne = random.randint(0, self.nb_colonnes - 1)
            coordonnees = Coordonnees(ligne, colonne)
            if self.ocean.valeur_coordonnees(coordonnees) is None:
                return coordonnees
            
    def executer_cycle(self)-> None:
        """Exécution d'un cycle pour l'ensemble des poissons

        Returns:
            None
        """
        self.__numero_chronon += self.__numero_chronon
        print(f"Chronon {self.numero_chronon}")
        for ligne in range(self.nb_lignes):
            for colonne in range(self.nb_colonnes):
                coordonnees = Coordonnees(ligne, colonne)
                poisson = self.ocean.valeur_coordonnees(coordonnees)
                if isinstance(poisson, Requin):
                    poisson.executer_cycle(coordonnees, self.ocean)
        for ligne in range(self.nb_lignes):
            for colonne in range(self.nb_colonnes):
                coordonnees = Coordonnees(ligne, colonne)
                poisson = self.ocean.valeur_coordonnees(coordonnees)
                if isinstance(poisson, Proie):
                    poisson.executer_cycle(coordonnees, self.ocean)

        for ligne in range(self.nb_lignes):
            for colonne in range(self.nb_colonnes):
                coordonnees = Coordonnees(ligne, colonne)
                poisson = self.ocean.valeur_coordonnees(coordonnees)
                if poisson is None:
                    print("·", end=" ") 
                else:
                    print(poisson.caractere_symbole(), end=" ")
            print()

    def __repr__(self):
        """Retourne une représentation textuelle du monde."""
        return f"Monde({self.lignes}, {self.colonnes}, {self.ocean})"

    def __str__(self):
        """Retourne une représentation textuelle du monde."""
        return str(self.ocean)
