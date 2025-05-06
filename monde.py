# filename: monde.py
# Wa-tor grid and simulation

import random
from typing import List

class Monde:
    """Class monde représente le monde de la simulation Wa-tor.
    Cette classe est responsable de la gestion de la grille, y compris sa taille et le
    placement de poissons et de requins.
    """
    def __init__(self, lignes: int, cols: int):
        """Initialise la grille avec le nombre donnée de lignes et colonnes.
        
        Args:
            lignes (int): Nombre de ligne dans la grille.
            cols (int): Nombre de colonne dans la grille.
        """
        self.lignes = lignes
        self.cols = cols
        self.grille = [[None for _ in range(cols)] for _ in range(lignes)]
    
    def place_fishes(self, poissons: List[object]):
        """Place une liste de poissons dans la grille.
        
        Args:
            poissons (list): Liste d'objets poisson à placer dans la grille.
        """
        for poisson in poissons:
            placed = False
            while not placed:
                row = random.randint(0, self.lignes - 1)
                col = random.randint(0, self.cols - 1)
                if self.grille[row][col] is None:
                    self.grille[row][col] = poisson
                    placed = True
    
    def place_sharks(self, requins: List[object]):
        """Place une liste de requins dans la grille.
        
        Args:
            requins (list): Liste d'objets requin à placer dans la grille.
        """
        for requin in requins:
            placed = False
            while not placed:
                row = random.randint(0, self.rows - 1)
                col = random.randint(0, self.cols - 1)
                if self.grille[row][col] is None:
                    self.grille[row][col] = requin
                    placed = True
                    
    def update(self):
        """Met à jour la grille en déplaçant les poissons et les requins."""
        for i in range(self.lignes):
            for j in range(self.cols):
                if self.grille[i][j] is not None:
                    self.grille[i][j].move(self.grille, i, j)
                    # Si le poisson ou le requin est mort, le retirer de la grille
                    if self.grille[i][j].is_dead():
                        self.grille[i][j] = None

        self.update_fishes()
        self.update_sharks()
    
    def update_fishes(self):
        """Met à jour les poissons dans la grille."""

        pass

    def update_sharks(self):
        """Met à jour les requins dans la grille."""
        
        pass
        
    def __str__(self):
        """Return une représentation string de la grille."""
        grille_str = ""
        for ligne in self.grille:
            grille_str += " ".join(str(cell) if cell else "." for cell in ligne) + "\n"
        return grille_str
    

