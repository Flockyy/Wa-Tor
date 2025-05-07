class Grille:
    def __init__(self, lignes: int, colonnes: int):
        """Initialise la grille avec le nombre donné de lignes et colonnes.

        Args:
            lignes (int): Nombre de ligne dans la grille.
            colonnes (int): Nombre de colonne dans la grille.
        """

        self.lignes = lignes
        self.colonnes = colonnes
        self.grille = [[None for _ in range(colonnes)] for _ in range(lignes)]

    def placer_proie(self, proie, i: int, j: int):
        """Place une proie dans la grille à la position donnée.

        Args:
            proie (Proie): L'objet proie à placer.
            i (int): La ligne de la grille.
            j (int): La colonne de la grille.
        """
        if 0 <= i < self.lignes and 0 <= j < self.colonnes:
            self.grille[i][j] = proie
        else:
            raise IndexError("Position en dehors des limites de la grille.")

    def placer_requin(self, requin, i: int, j: int):
        """Place un requin dans la grille à la position donnée.

        Args:
            requin (Requin): L'objet requin à placer.
            i (int): La ligne de la grille.
            j (int): La colonne de la grille.
        """
        if 0 <= i < self.lignes and 0 <= j < self.colonnes:
            self.grille[i][j] = requin
        else:
            raise IndexError("Position en dehors des limites de la grille.")

    def valeur_coordonnees(self, i: int, j: int):
        """Retourne la valeur d'une cellule de la grille.

        Args:
            i (int): La ligne de la cellule.
            j (int): La colonne de la cellule.

        Returns:
            object: La valeur de la cellule.
        """
        if 0 <= i < self.lignes and 0 <= j < self.colonnes:
            return self.grille[i][j]
        else:
            raise IndexError("Position en dehors des limites de la grille.")
    
    def __repr__(self):
        return f"Grille({self.lignes}, {self.colonnes}, {self.grille})"

    def __str__(self):
        """Retourne une représentation textuelle de la grille."""
        representation = ""
        for ligne in self.grille:
            representation += (
                " | ".join([str(cellule) if cellule else " " for cellule in ligne])
                + "\n"
            )
        return representation
