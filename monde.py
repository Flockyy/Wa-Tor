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
            i, j = self._get_random_empty_cell()
            while self.ocean.grille[i][j] is not None:
                i, j = self._get_random_empty_cell()
            self.ocean.placer_proie(proie, i, j)

        # place les requins dans la grille aleatoirement
        for requin in requins:
            if not isinstance(requin, Requin):
                raise TypeError("L'objet doit être un requin")
            i, j = self._get_random_empty_cell()
            while self.ocean.grille[i][j] is not None:
                i, j = self._get_random_empty_cell()
            self.ocean.placer_requin(requin, i, j)

    def _get_random_empty_cell(self):
        """Retourne une cellule vide aléatoire dans la grille.

        Returns:
            tuple: Coordonnées (i, j) de la cellule vide.
        """
        while True:
            i = random.randint(0, self.nb_lignes - 1)
            j = random.randint(0, self.nb_colonnes - 1)
            if self.ocean.grille[i][j] is None:
                return i, j
            
    def executer_cycle(self)-> None:
        """Exécution d'un cycle pour l'ensemble des poissons

        Returns:
            None
        """
        self.__numero_chronon += 1
        print(f"Chronon {self.numero_chronon}")
        for ligne in range(self.nb_lignes):
            for colonne in range(self.nb_colonnes):
                if isinstance(self.ocean.grille[ligne][colonne], Requin):
                    self.ocean.grille[ligne][colonne].executer_cycle(Coordonnees(ligne, colonne), self.ocean)
        for ligne in range(self.nb_lignes):
            for colonne in range(self.nb_colonnes):
                if isinstance(self.ocean.grille[ligne][colonne], Proie):
                    self.ocean.grille[ligne][colonne].executer_cycle(Coordonnees(ligne, colonne), self.ocean)
        # debut modifs temporaires à ne pas récupérer
        for ligne in range(self.nb_lignes):
            for colonne in range(self.nb_colonnes):
                    valeur_cellule = self.ocean.valeur_coordonnees(Coordonnees(ligne, colonne))
                    if valeur_cellule == None:
                        print("·", end=" ") 
                    else:
                        print(valeur_cellule.caractere_symbole(), end=" ")
            print()
        # fin modifs temporaires à ne pas récupérer

    def __repr__(self):
        """Retourne une représentation textuelle du monde."""
        return f"Monde({self.lignes}, {self.colonnes}, {self.ocean})"

    def __str__(self):
        """Retourne une représentation textuelle du monde."""
        return str(self.ocean)
