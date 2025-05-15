#from typing import List
from ocean import Ocean, Coordonnees, Direction
from poisson import Poisson



class Proie(Poisson):
    """
    Classe Proie (descendant de Poisson, qui tente de survivre en échapant aux prédateurs)

    Args:
        ocean (Ocean) : Océan dans lequel se trouve la proie.
        cycle_reproduction (int): 8 par défaut. Nombre de cycle entre chaque reproduction.
    """
    def __init__(self, ocean: Ocean, cycle_reproduction: int = 8, visibilite: int = 2, vue_arriere: bool = True):
        """Initialise une instance de poisson avec ses paramètres.

        Args:
            ocean (Ocean): _description_
            cycle_reproduction (int, optional): _description_. Defaults to 8.
            visibilite (int, optional): _description_. Defaults to 2.
            vue_arriere (bool, optional): _description_. Defaults to True.
        """
        super().__init__(ocean, cycle_reproduction, visibilite, vue_arriere)

    def __str__(self) -> str:
        """Retourne une représentation textuelle de l'objet Proie

        Returns:
            str: Description indiquant le cycle de reproduction des proies
        """
        return f"Proie ayant un cycle de reproduction de {self.cycle_reproduction} tours"
    def caractere_symbole(self)-> str:
        """Retourne le caractère représentant une proie

        Returns:
            str: Le caractère utilisé pour identifier la proie
        """
        return "o"
    def _nouvelle_instance(self):
        """Crée une nouvelle instance de la class proie avec les mêmes paramètres. Cette méthode est utilisée
        lors de la reproduction pour génèrer un nouvel individu

        Returns:
            Proie: Une nouvelle instance de proie avec les mêmes paramètres

        """
        return Proie(self._ocean, self.cycle_reproduction, self.visibilite, self.vue_arriere)
    def executer_cycle(self, coordonnees: Coordonnees)-> None:
        """Execute un cycle de vie pour la proie à une position donnée

        Args:
            coordonnees (Coordonnees): Position actuelle de la proie sur la grille
            
        Returns:
            None
        """
        super().executer_cycle(coordonnees)
        # Note : pas de gestion du viellissement de la proie (selon la doc).
        #        Si on décide de la gérer, alors il faut déplacer la gestion du viuellissement de Requin vers Poisson.

        # recherche direction souhaitée
        direction_choisie = self.direction
        liste_directions = []
        liste_directions.extend(Direction.liste_directions_melangees()) # on mélange
        liste_directions.remove(Direction.Aucune)
        # Mode fuite : on detecte les requins les plus proches dans chaque direction
        # et on retire leurs directions de la liste des directions sûres
        liste_orientations_requins = []
        for direction in Direction:
            if direction != Direction.Aucune:
                if (self.vue_arriere or (direction != Direction.direction_inverse(direction_choisie))):
                    coordonnees_requin = self.rechercher_poisson(coordonnees, direction, "Requin")
                    if coordonnees_requin:
                        liste_orientations_requins.append(self._ocean.calculer_orientation(coordonnees, coordonnees_requin))
        if len(liste_orientations_requins) > 0:
            liste_orientations_requins.sort(key=lambda orientation: orientation.distance)
            for orientation in liste_orientations_requins:
                for direction in orientation.directions:
                    if direction in liste_directions:
                        liste_directions.remove(direction)
        # on teste tous les choix possibles en priorisant les directions sans requins (s'il y en a).
        # Si l'ancienne direction est sûre, on la teste en premier
        if (direction_choisie in liste_directions):
            liste_directions.remove(direction_choisie)
            liste_directions.insert(0,direction_choisie)
        direction_choisie = Direction.Aucune
        # on ajoute à la fin les directions manquantes (qui ont été virées à cause des requins)
        for direction in Direction.liste_directions_melangees():
            if ((direction != Direction.Aucune) and (direction not in liste_directions)):
                liste_directions.append(direction)
        for direction in liste_directions:
            if self._ocean.coordonnees_libres(self._ocean.deplacer_coordonnees(coordonnees, direction)):
                coordonnees_testees = self._ocean.deplacer_coordonnees(coordonnees, direction)
                if self._ocean.coordonnees_libres(coordonnees_testees):
                    if self.visibilite == 1:
                        direction_choisie = direction # mode miro : si un requin se trouve juste à côté, la proie ne le voit pas.
                        break 
                    else:
                        if not self._ocean.coordonnes_jouxtent_objet(coordonnees_testees, "Requin"):
                            direction_choisie = direction
                            break

        # Si direction_choisie == Direction.Aucune
        # alors cela signifie que la proie est complètement entourée,
        # ou que quelque soit la direction, on se retrouve à côté d'un requin...

        self.action_deplacement(coordonnees, direction_choisie)