from enum import Enum
from typing import List
import random


class Coordonnees:
    """Représente des coordonnées dans une grille sous forme de ligne et colonne."""

    def __init__(self, ligne: int, colonne: int):
        """Initialise une instance de Coordonnees

        Args:
            ligne (int): Indice de la ligne
            colonne (int): Indice de la ligne
        """
        self.ligne = ligne
        self.colonne = colonne

    def __str__(self):
        """Retourne une représentation lisible de l'objet"""
        return f"Coordonnées = (Ligne {self.ligne} / Colonne {self.colonne})"

    def __repr__(self):
        """Retourne une représentation textuelle de l'objet."""
        return f"{__name__}({getattr(self)})"  # TODO: Alexis: à vérifier...


class Direction(Enum):
    """Enumération représentant les directions possibles

    Valeurs :
        - Aucune : Aucune direction
        - Haut : Vers le haut
        - Droite : Vers la droite
        - Bas : Vers le bas
        - Gauche : Vers la gauche
    """

    Aucune = 0
    Haut = 1
    Droite = 2
    Bas = 3
    Gauche = 4

    def liste_directions_melangees() -> list["Direction"]:
        """Retourne une liste des directions mélangées (incluant Aucune)

        Returns:
            list["Direction"]: Liste des directions dans un ordre aléatoire
        """
        liste_melangee = [direction for direction in Direction]
        random.shuffle(liste_melangee)
        return liste_melangee

    def direction_inverse(direction) -> "Direction":
        """Récupére la direction inverse de la direction donnée en argument

        Args:
            direction (Direction): La direction que l'on veut inverser

        Returns:
            Direction: La direction inverse ou Aucune
        """
        match direction:
            case Direction.Haut:
                return Direction.Bas
            case Direction.Bas:
                return Direction.Haut
            case Direction.Gauche:
                return Direction.Droite
            case Direction.Droite:
                return Direction.Gauche
            case _:
                return Direction.Aucune


class Orientation:
    """Représente une orientation par rapport à une cible dans l'océan

    Attributs:
        distance (int): Distance jusqu'à la cible
        directions (List[Direction]): Liste des directions à suivre pour se rendre jusqu'à la cible
    """

    # def __init__(self, distance: int = 0, directions: List[Direction] = []):
    #    self.distance = distance
    #    self.directions = directions
    #    print(f"Création Orientation : directions = {self.directions}")
    def __init__(self, distance: int = 0):
        """Initialise une nouvelle orientation

        Args:
            distance (int): Distance initial jusqu'à la cible. Par défaut: 0
        """
        self.distance = distance
        self.directions = []

    def ajouter_direction(self, direction: Direction):
        """Ajoute une direction à la liste des directions menants à la cible

        Args:
            direction (Direction): Direction à ajouter
        """
        self.directions.append(direction)


class Ocean:
    """Représentation d'un océan sous forme de grille dans laquelle vivent des poissons (requins et proies)

    Attributs:
        lignes (int): Nombre de lignes dans la grille
        colonnes (int): Nombre de colonnes dans la grille
        grille (list): Grille contenant les objets
    """

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

    # @property
    # def grille(self):
    #    return self.__grille

    def placer_proie(self, proie, coordonnees: Coordonnees):
        """Place une proie dans la grille à la position donnée.

        Args:
            proie (Proie): L'objet proie à placer.
            ligne (int): La ligne de la grille.
            colonne (int): La colonne de la grille.
        """
        if (
            0 <= coordonnees.ligne < self.__lignes
            and 0 <= coordonnees.colonne < self.__colonnes
        ):
            self.__grille[coordonnees.ligne][coordonnees.colonne] = proie
        else:
            raise IndexError("Position en dehors des limites de la grille.")

    def placer_requin(self, requin, coordonnees: Coordonnees):
        """Place un requin dans la grille à la position donnée.

        Args:
            requin (Requin): L'objet requin à placer.
            ligne (int): La ligne de la grille.
            colonne (int): La colonne de la grille.
        """
        if (
            0 <= coordonnees.ligne < self.__lignes
            and 0 <= coordonnees.colonne < self.colonnes
        ):
            self.__grille[coordonnees.ligne][coordonnees.colonne] = requin
        else:
            raise IndexError("Position en dehors des limites de la grille.")

    def effectuer_deplacement(
        self,
        anciennes_coordonees: Coordonnees,
        nouvelles_coordonnees: Coordonnees,
        enfant: any = None,
    ) -> None:
        """Gestion du déplacement d'un poisson d'une cellule à une autre. Si le déplacement s'effectue, alors le poisson à l'ancienne position
        est déplacé vers la nouvelle position. L'ancienne position est vidée sauf si le paramètre enfant est True

        Args:
            anciennes_coordonees (Coordonnees): Coordonnée de la position actuelle du poisson
            nouvelles_coordonnees (Coordonnees): Coordonnée de la nouvelle position du poisson
            enfant (any): Si True, objet à placer après le déplacement sur l'ancienne coordonnée. Par défaut None
        Returns:
            None
        """
        if (anciennes_coordonees.ligne == nouvelles_coordonnees.ligne) and (
            anciennes_coordonees.colonne == nouvelles_coordonnees.colonne
        ):
            if enfant != None:
                raise Exception(
                    "Un enfant ne pas être ajouté dans l'océan sans déplacement."
                )
        else:
            self.__grille[nouvelles_coordonnees.ligne][
                nouvelles_coordonnees.colonne
            ] = self.__grille[anciennes_coordonees.ligne][anciennes_coordonees.colonne]
            self.__grille[anciennes_coordonees.ligne][
                anciennes_coordonees.colonne
            ] = enfant

    def infos_coordonnees(self, coordonnees: Coordonnees) -> None | str:
        """Retourne les informations d'une cellule de la grille.

        Args:
            coordonnees (Coordonnees) : coordonnées de la cellule dont on veut obtenir les coordonnées

        Returns:
            None ou le nom (en chaîne de caractères) de la classe de l'objet présent dans la cellule.
        """
        if not isinstance(coordonnees, Coordonnees):
            raise TypeError("Type incorrect pour le paramètre coordonnees")

        if (
            coordonnees.ligne < 0
            or coordonnees.ligne >= self.__lignes
            or coordonnees.colonne < 0
            or coordonnees.colonne >= self.colonnes
        ):
            raise IndexError("Coordonnées en dehors de la grille")

        contenu_cellule = self.__grille[coordonnees.ligne][coordonnees.colonne]
        if (
            self.__grille[coordonnees.ligne][coordonnees.colonne] is None
        ):  # Alexis: is None ou == None ? ya une différence ?
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
        if (
            0 <= coordonnees.ligne < self.__lignes
            and 0 <= coordonnees.colonne < self.colonnes
        ):
            return self.__grille[coordonnees.ligne][coordonnees.colonne]
        else:
            raise IndexError("Position en dehors des limites de la grille.")

    def effacer_valeur(self, coordonnees: Coordonnees):
        """Efface la valeur à la position dans la grille. Permet de remplacer une entitée à des coordonnées spécifiques par None
        pour indiquer que la cellule est vide

        Args:
            coordonnees (Coordonnees): Coordonnées de la cellule à vider
        """
        self.__grille[coordonnees.ligne][coordonnees.colonne] = None

    def deplacer_coordonnees(
        self, coordonnees_initiales: Coordonnees, direction: Direction
    ) -> Coordonnees:
        """Change les coordonnes en fonction de la direction.
        Args:
            coordonnees_initiales: Coordonnees avant le déplacement
            direction (Direction): La direction dans laquelle changer la valeur.

        Returns:
            Coordonnees
        """
        nouvelles_coordonnees = Coordonnees(
            coordonnees_initiales.ligne, coordonnees_initiales.colonne
        )
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

    def calculer_orientation(
        self, coordonnees_depart: Coordonnees, coordonnees_destination: Coordonnees
    ) -> Orientation:
        """Calcul l'orientation (direction et distance) entre deux coordonées dans la grille

        Args:
            coordonnees_depart (Coordonnees): Coordonnées de d"part
            coordonnees_destination (Coordonnees): Coordonnées de destination

        Returns:
            Orientation: Objet contenant la distance totale ainsi que les directions afin d'atteindre les coordonnées de destination
        """
        distance_horizontale = abs(
            coordonnees_depart.colonne - coordonnees_destination.colonne
        )
        if distance_horizontale == 0:
            direction_horizontale = Direction.Aucune
        elif (coordonnees_depart.colonne - coordonnees_destination.colonne) > 0:
            if distance_horizontale > (self.colonnes / 2):
                distance_horizontale = self.colonnes - distance_horizontale
                direction_horizontale = Direction.Droite
            else:
                direction_horizontale = Direction.Gauche
        else:
            if distance_horizontale > (self.colonnes / 2):
                distance_horizontale = self.colonnes - distance_horizontale
                direction_horizontale = Direction.Gauche
            else:
                direction_horizontale = Direction.Droite
        distance_verticale = abs(
            coordonnees_depart.ligne - coordonnees_destination.ligne
        )
        if distance_verticale == 0:
            direction_verticale = Direction.Aucune
        elif (coordonnees_depart.ligne - coordonnees_destination.ligne) > 0:
            if distance_verticale > (self.lignes / 2):
                distance_verticale = self.lignes - distance_verticale
                direction_verticale = Direction.Bas
            else:
                direction_verticale = Direction.Haut
        else:
            if distance_verticale > (self.lignes / 2):
                distance_verticale = self.lignes - distance_verticale
                direction_verticale = Direction.Haut
            else:
                direction_verticale = Direction.Bas
        orientation = Orientation(distance=(distance_horizontale + distance_verticale))
        if direction_verticale != Direction.Aucune:
            orientation.ajouter_direction(direction_verticale)
        if direction_horizontale != Direction.Aucune:
            orientation.ajouter_direction(direction_horizontale)
        return orientation

    def coordonnees_libres(self, coordonnees: Coordonnees) -> bool:
        """Vérifie grâce aux coordonées si la case est libre (vide)

        Args:
            coordonnees (Coordonnees): Coordonnées de la case à vérifier

        Returns:
            bool: Retourne True si la case est libres, sinon False
        """
        return self.infos_coordonnees(coordonnees) is None

    def coordonnes_jouxtent_objet(
        self, coordonnees: Coordonnees, nom_classe: str
    ) -> bool:
        """Recherche la présence d'un type d'objet jouxtant les coordonnées fournies

        Args:
            coordonnees (Coordonnees): Coordonnées autour de laquelle la recherche est effectuée
            nom_classe (str): Nom de la classe recherchée

        Returns:
            bool: Retourne True si un objet dont le nom de la classe fourni est trouvé dans une cellule jouxtant celle des coordonnées fournies.
        """
        # au dessus
        coordonnees_testees = self.deplacer_coordonnees(coordonnees, Direction.Haut)
        if self.infos_coordonnees(coordonnees_testees) == nom_classe:
            return True
        # à droite
        coordonnees_testees = self.deplacer_coordonnees(coordonnees, Direction.Droite)
        if self.infos_coordonnees(coordonnees_testees) == nom_classe:
            return True
        # en bas
        coordonnees_testees = self.deplacer_coordonnees(coordonnees, Direction.Bas)
        if self.infos_coordonnees(coordonnees_testees) == nom_classe:
            return True
        # à gauche
        coordonnees_testees = self.deplacer_coordonnees(coordonnees, Direction.Gauche)
        if self.infos_coordonnees(coordonnees_testees) == nom_classe:
            return True
        return False

    def __repr__(self):
        """Retourne un représentation textuelle officielle de l'objet (utilisé pour le débogage)"""
        return f"Ocean({self.__lignes}, {self.__colonnes}, {self.__grille})"

    def __str__(self):
        """Retourne une représentation textuelle de la grille."""
        representation = ""
        for ligne in self.__grille:
            representation += (
                " | ".join([str(cellule) if cellule else " " for cellule in ligne])
                + "\n"
            )
        return representation
