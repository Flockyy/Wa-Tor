from enum import Enum
from typing import List

class Coordonnees:
    def __init__(self, ligne: int, colonne: int):
        self.ligne = ligne
        self.colonne = colonne
    def __str__(self):
        return f"Coordonnées = (Ligne {self.ligne} / Colonne {self.colonne})"
    def __repr__(self):
        return f"{__name__}({getattr(self)})" #TODO: Alexis: à vérifier...

class Direction(Enum):
    Aucune = 0
    Haut = 1
    Droite = 2
    Bas = 3
    Gauche = 4
    def tourner(direction_depart, sens_horaire: bool, direction_par_defaut = Aucune):
        if direction_depart == Direction.Aucune:
            return direction_par_defaut
        else:  #TODO: Alexis: Trouver le moyen de passer par les valeurs ordinales, ce doit être forcément possible !
            if sens_horaire:
                if direction_depart == Direction.Haut:
                    return Direction.Droite
                elif direction_depart == Direction.Droite:
                    return Direction.Bas
                elif direction_depart == Direction.Bas:
                    return Direction.Gauche
                else:
                    return Direction.Haut
            else:
                if direction_depart == Direction.Haut:
                    return Direction.Gauche
                elif direction_depart == Direction.Gauche:
                    return Direction.Bas
                elif direction_depart == Direction.Bas:
                    return Direction.Droite
                else:
                    return Direction.Haut

class Orientation():
    #def __init__(self, distance: int = 0, directions: List[Direction] = []):
    #    self.distance = distance
    #    self.directions = directions
    #    print(f"Création Orientation : directions = {self.directions}")
    def __init__(self, distance: int = 0):
        self.distance = distance
        self.directions = []
    def ajouter_direction(self,direction: Direction):
        self.directions.append(direction)

class Ocean:
    def __init__(self, lignes: int, colonnes: int):
        """Initialise la grille avec le nombre donné de lignes et colonnes.

        Args:
            lignes (int): Nombre de ligne dans la grille.
            colonnes (int): Nombre de colonne dans la grille.
        """

        self.__lignes = lignes
        self.__colonnes = colonnes
        self.__grille = [[None for _ in range(colonnes)] for _ in range(lignes)]

    @property
    def lignes(self):
        return self.__lignes
    
    @property
    def colonnes(self):
        return self.__colonnes

    @property
    def grille(self):
        return self.__grille

    def placer_proie(self, proie, coordonnees: Coordonnees):
        """Place une proie dans la grille à la position donnée.

        Args:
            proie (Proie): L'objet proie à placer.
            i (int): La ligne de la grille.
            j (int): La colonne de la grille.
        """
        if 0 <= coordonnees.ligne < self.__lignes and 0 <= coordonnees.colonne < self.__colonnes:
            self.__grille[coordonnees.ligne][coordonnees.colonne] = proie
        else:
            raise IndexError("Position en dehors des limites de la grille.")

    def placer_requin(self, requin, coordonnees: Coordonnees):
        """Place un requin dans la grille à la position donnée.

        Args:
            requin (Requin): L'objet requin à placer.
            i (int): La ligne de la grille.
            j (int): La colonne de la grille.
        """
        if 0 <= coordonnees.ligne < self.__lignes and 0 <= coordonnees.colonne < self.colonnes:
            self.__grille[coordonnees.ligne][coordonnees.colonne] = requin
        else:
            raise IndexError("Position en dehors des limites de la grille.")

    def effectuer_deplacement(self,anciennes_coordonees: Coordonnees, nouvelles_coordonnees: Coordonnees, enfant: any = None)-> None:
        """Gestion du déplacement d'un poisson 

        Args:
            anciennes_coordonees (Coordonnees): _description_
            nouvelles_coordonnees (Coordonnees): _description_
            enfant (any, optional): _description_. Defaults to None.
        """
        if ((anciennes_coordonees.ligne == nouvelles_coordonnees.ligne) and (anciennes_coordonees.colonne == nouvelles_coordonnees.colonne)):
            if (enfant != None):
                raise Exception("Un enfant ne pas être ajouté dans l'océan sans déplacement.")
        else:
            self.__grille[nouvelles_coordonnees.ligne][nouvelles_coordonnees.colonne] = self.__grille[anciennes_coordonees.ligne][anciennes_coordonees.colonne]
            self.__grille[anciennes_coordonees.ligne][anciennes_coordonees.colonne] = enfant

    def infos_coordonnees(self, coordonnees: Coordonnees)-> None | str:
        """Retourne les informations d'une cellule de la grille.

        Args:
            coordonnees (Coordonnees) : coordonnées de la cellule dont on veut obtenir les coordonnées

        Returns:
            None ou le nom (en chaîne de caractères) de la classe de l'objet présent dans la cellule.
        """
        if not isinstance(coordonnees, Coordonnees):
            raise TypeError("Type incorrect pour le paramètre coordonnees")

        if coordonnees.ligne < 0 or coordonnees.ligne >= self.__lignes or coordonnees.colonne < 0 or coordonnees.colonne >= self.colonnes:
            raise IndexError("Coordonnées en dehors de la grille")

        contenu_cellule = self.__grille[coordonnees.ligne][coordonnees.colonne]
        if self.__grille[coordonnees.ligne][coordonnees.colonne] is None: #Alexis: is None ou == None ? ya une différence ?
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
        if 0 <= coordonnees.ligne < self.__lignes and 0 <= coordonnees.colonne < self.colonnes:
            return self.__grille[coordonnees.ligne][coordonnees.colonne]
        else:
            raise IndexError("Position en dehors des limites de la grille.")
    
    def effacer_valeur(self, coordonnees: Coordonnees):
        self.grille[coordonnees.ligne][coordonnees.colonne] = None
        
    def deplacer_coordonnees(self, coordonnees_initiales: Coordonnees, direction: Direction)-> Coordonnees:
        """Change les coordonnes en fonction de la direction.
        Args:
            coordonnees_initiales: Coordonnees
            direction (Direction): La direction dans laquelle changer la valeur.
        Returns:
            Coordonnees
        """
        nouvelles_coordonnees = Coordonnees(coordonnees_initiales.ligne, coordonnees_initiales.colonne)
        if direction == Direction.Aucune:
            return nouvelles_coordonnees
        else:
            if direction == Direction.Haut:
                if nouvelles_coordonnees.ligne - 1 < 0:
                    nouvelles_coordonnees.ligne = self.__lignes - 1
                else:
                    nouvelles_coordonnees.ligne -= 1

            elif direction == Direction.Bas:
                if nouvelles_coordonnees.ligne + 1 >= self.__lignes:
                    nouvelles_coordonnees.ligne = 0
                else:
                    nouvelles_coordonnees.ligne += 1

            elif direction == Direction.Gauche:
                if nouvelles_coordonnees.colonne - 1 < 0:
                    nouvelles_coordonnees.colonne = self.__colonnes - 1
                else:
                    nouvelles_coordonnees.colonne -= 1     
                    
            elif direction == Direction.Droite:
                if nouvelles_coordonnees.colonne + 1 >= self.__colonnes:
                    nouvelles_coordonnees.colonne = 0
                else:
                    nouvelles_coordonnees.colonne += 1
            else:
                raise ValueError("Direction non valide.")
            
            return nouvelles_coordonnees
        
    def calculer_orientation(self, coordonnees_depart: Coordonnees, coordonnees_destination: Coordonnees)-> Orientation:
        distance_horizontale = abs(coordonnees_depart.colonne - coordonnees_destination.colonne)
        if (distance_horizontale == 0):
            direction_horizontale = Direction.Aucune
        elif ((coordonnees_depart.colonne - coordonnees_destination.colonne) > 0):
            if (distance_horizontale > (self.colonnes /2)):
                distance_horizontale = self.colonnes - distance_horizontale
                direction_horizontale = Direction.Droite
            else:
                direction_horizontale = Direction.Gauche
        else:
            if (distance_horizontale > (self.colonnes /2)):
                distance_horizontale = self.colonnes - distance_horizontale
                direction_horizontale = Direction.Gauche
            else:
                direction_horizontale = Direction.Droite
        distance_verticale = abs(coordonnees_depart.ligne - coordonnees_destination.ligne)
        if (distance_verticale == 0):
            direction_verticale = Direction.Aucune
        elif ((coordonnees_depart.ligne - coordonnees_destination.ligne) > 0):
            if (distance_verticale > (self.lignes /2)):
                distance_verticale = self.lignes - distance_verticale
                direction_verticale = Direction.Bas
            else:
                direction_verticale = Direction.Haut
        else:
            if (distance_verticale > (self.lignes /2)):
                distance_verticale = self.lignes - distance_verticale
                direction_verticale = Direction.Haut
            else:
                direction_verticale = Direction.Bas
        orientation = Orientation(distance = (distance_horizontale + distance_verticale))
        if direction_verticale != Direction.Aucune:
            orientation.ajouter_direction(direction_verticale)
        if direction_horizontale != Direction.Aucune:
            orientation.ajouter_direction(direction_horizontale)
        return orientation
        
    def __repr__(self):
        return f"Grille({self.__lignes}, {self.__colonnes}, {self.__grille})"

    def __str__(self):
        """Retourne une représentation textuelle de la grille."""
        representation = ""
        for ligne in self.__grille:
            representation += (
                " | ".join([str(cellule) if cellule else " " for cellule in ligne])
                + "\n"
            )
        return representation
