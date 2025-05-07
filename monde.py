# filename: monde.py
# Wa-tor grid and simulation

import random
from typing import List
from proie import Proie
from requin import Requin
from proie import Proie
from grille import Grille


class Monde:
    """Class monde représente le monde de la simulation Wa-tor.
    Cette classe est responsable de la gestion de la grille, y compris sa taille et le
    placement de proies et de requins.
    """

    def __init__(self, lignes: int, colonnes: int):
        """Initialise le monde avec une grille de la taille donnée.

        Args:
            lignes (int): Nombre de lignes dans la grille.
            colonnes (int): Nombre de colonnes dans la grille.
        """
        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = Grille(lignes, colonnes)

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
            while self.grille.grille[i][j] is not None:
                i, j = self._get_random_empty_cell()
            self.grille.placer_proie(proie, i, j)

        # place les requins dans la grille aleatoirement
        for requin in requins:
            if not isinstance(requin, Requin):
                raise TypeError("L'objet doit être un requin")
            i, j = self._get_random_empty_cell()
            while self.grille.grille[i][j] is not None:
                i, j = self._get_random_empty_cell()
            self.grille.placer_requin(requin, i, j)

    def _get_random_empty_cell(self):
        """Retourne une cellule vide aléatoire dans la grille.

        Returns:
            tuple: Coordonnées (i, j) de la cellule vide.
        """
        while True:
            i = random.randint(0, self.lignes - 1)
            j = random.randint(0, self.colonnes - 1)
            if self.grille.grille[i][j] is None:
                return i, j

    def infos_coordonnées(self, i: int, j: int):
        """Retourne les informations d'une cellule de la grille.

        Args:
            i (int): La ligne de la cellule.
            j (int): La colonne de la cellule.

        Returns:
            tuple: symbole de la grille correspondant à la cellule.
        """
        if not isinstance(i, int) or not isinstance(j, int):
            raise TypeError("Les coordonnées doivent être des entiers")

        if i < 0 or i >= self.lignes or j < 0 or j >= self.colonnes:
            raise IndexError("Coordonnées en dehors de la grille")

        if self.grille[i][j] is None:
            return None
        elif isinstance(self.grille[i][j], Proie):
            return self.grille[i][j].symbole()
        elif isinstance(self.grille[i][j], Requin):
            return self.grille[i][j].symbole()
        else:
            raise ValueError("Type de cellule inconnu")

    def __repr__(self):
        """Retourne une représentation textuelle du monde."""
        return f"Monde({self.lignes}, {self.colonnes}, {self.grille})"

    def __str__(self):
        """Retourne une représentation textuelle du monde."""
        return str(self.grille)
