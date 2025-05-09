from enum import Enum

class Coordonnees:
    def __init__(self, ligne: int, colonne: int):
        self.ligne = ligne
        self.colonne = colonne
    def __str__(self):
        return f"Coordonnées = (Ligne {self.ligne} / Colonne {self.colonne})"
    def __repr__(self):
        return f"{__name__}({getattr(self)})" #TODO: Alexis: à vérifier...

Direction = Enum('Direction', [('Haut'), ('Bas'), ('Gauche'), ('Droite')])

class Ocean:
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

    def effectuer_deplacement(self,anciennes_coordonees: Coordonnees, nouvelles_coordonnees: Coordonnees, enfant: any = None)-> None:
        """Gestion du déplacement d'un poisson 

        Args:
            anciennes_coordonees (Coordonnees): _description_
            nouvelles_coordonnees (Coordonnees): _description_
            enfant (any, optional): _description_. Defaults to None.
        """
        self.grille[nouvelles_coordonnees.ligne][nouvelles_coordonnees.colonne] = self.grille[anciennes_coordonees.ligne][anciennes_coordonees.colonne]
        self.grille[anciennes_coordonees.ligne][anciennes_coordonees.colonne] = enfant

    def infos_coordonnees(self, coordonnees: Coordonnees)-> None | str:
        """Retourne les informations d'une cellule de la grille.

        Args:
            coordonnees (Coordonnees) : coordonnées de la cellule dont on veut obtenir les coordonnées

        Returns:
            None ou le nom (en chaîne de caractères) de la classe de l'objet présent dans la cellule.
        """
        if not isinstance(coordonnees, Coordonnees):
            raise TypeError("Type incorrect pour le paramètre coordonnees")

        if coordonnees.ligne < 0 or coordonnees.ligne >= self.lignes or coordonnees.colonne < 0 or coordonnees.colonne >= self.colonnes:
            raise IndexError("Coordonnées en dehors de la grille")

        contenu_cellule = self.grille[coordonnees.ligne][coordonnees.colonne]
        if self.grille[coordonnees.ligne][coordonnees.colonne] is None: #Alexis: is None ou == None ? ya une différence ?
            return None
        else:
            return type(contenu_cellule).__name__

    def valeur_coordonnees(self, coordonnees: Coordonnees):
        """Retourne la valeur d'une cellule de la grille.

        Args:
            coordonnees (Coordonnees): coordonnées de la cellule à lire.

        Returns:
            any: La valeur de la cellule.
        """
        if 0 <= coordonnees.ligne < self.lignes and 0 <= coordonnees.colonne < self.colonnes:
            return self.grille[coordonnees.ligne][coordonnees.colonne]
        else:
            raise IndexError("Position en dehors des limites de la grille.")
        
    def deplacer_coordonnees(self, coordonnees_initiales: Coordonnees, direction: Direction)-> Coordonnees:
        """Change les coordonnes en fonction de la direction.
        Args:
            coordonnees_initiales: Coordonnees
            direction (Direction): La direction dans laquelle changer la valeur.
        Returns:
            Coordonnees
        """
        nouvelles_coordonnees = Coordonnees(coordonnees_initiales.ligne, coordonnees_initiales.colonne)
        if direction == Direction.Haut:
            if nouvelles_coordonnees.ligne - 1 < 0:
                nouvelles_coordonnees.ligne = self.lignes - 1
            else:
                nouvelles_coordonnees.ligne -= 1
        elif direction == Direction.Bas:
            if nouvelles_coordonnees.ligne + 1 >= self.lignes:
                nouvelles_coordonnees.ligne = 0
            else:
                nouvelles_coordonnees.ligne += 1
        elif direction == Direction.Gauche:
            if j - 1 < 0:
                j = self.colonnes - 1
            else:
                j -= 1      
        elif direction == Direction.Droite:
            if nouvelles_coordonnees.colonne + 1 >= self.colonnes:
                nouvelles_coordonnees.colonne = 0
            else:
                nouvelles_coordonnees.colonne += 1
        else:
            raise ValueError("Direction non valide.")
        
        return nouvelles_coordonnees
        
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
