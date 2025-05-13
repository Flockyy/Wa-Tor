#from typing import List
import random
from ocean import Ocean, Coordonnees, Direction
from poisson import Poisson



class Proie(Poisson):
    """
    Classe Proie (descendant de Poisson, qui tente de survivre en échapant aux prédateurs)

    Args:
        ocean (Ocean) : Océan dans lequel se trouve la proie.
        cycle_reproduction (int): 8 par défaut. Nombre de cycle entre chaque reproduction.
    """
    def __init__(self, ocean: Ocean, cycle_reproduction: int = 8, visibilite: int = 2):
        super().__init__(ocean, cycle_reproduction, visibilite)
    def __str__(self):
        return f"Proie ayant un cycle de reproduction de {self.cycle_reproduction} tours"
    def caractere_symbole(self)-> str:
        return "o"
    def _nouvelle_instance(self):
        return Proie(self._ocean, self.cycle_reproduction, self.visibilite)
    def executer_cycle(self, coordonnees: Coordonnees)-> None:
        super().executer_cycle(coordonnees)
        # Note : pas de gestion du viellissement de la proie (selon la doc).
        #        Si on décide de la gérer, alors il faut déplacer la gestion du viuellissement de Requin vers Poisson.

        ## on se déplace autant que possible en rond.
        #direction_choisie = self.direction
        #for _ in range(4):
        #    direction_choisie = Direction.tourner(direction_choisie, True, Direction.Haut)
        #    if self._ocean.infos_coordonnees(self._ocean.deplacer_coordonnees(coordonnees, direction_choisie)) is None:
        #        break
        #else:
        #    direction_choisie = Direction.Aucune
        #self.action_deplacement(coordonnees, direction_choisie)

        # recherche direction souhaitée
        direction_choisie = self.direction

        # Mode fuite : on detecte les requins les plus proches dans chaque direction
        liste_directions_requins = []
        liste_orientations_requins = []
        for direction in Direction:
            if direction != Direction.Aucune:
                coordonnees_requin = self.rechercher_poisson(coordonnees, direction, "Requin")
                if coordonnees_requin:
                    liste_orientations_requins.append(self._ocean.calculer_orientation(coordonnees, coordonnees_requin))
        if len(liste_orientations_requins) > 0:
            liste_orientations_requins.sort(key=lambda orientation: orientation.distance)
            for orientation in liste_orientations_requins:
                for direction in orientation.directions:
                    if not (direction in liste_directions_requins):
                        liste_directions_requins.append(direction)
        if ((direction_choisie in liste_directions_requins) or (direction_choisie == Direction.Aucune)):
            liste_directions_sures = []
            for direction in Direction.liste_directions_melangees():
                if direction != Direction.Aucune:
                    if direction not in liste_directions_requins:
                        liste_directions_sures.append(direction)
            # Aiucune direction n'est sûre...
            # On se déplace sur n'importe quelle case vide
            # TODO: Alexis: il faudrait une boucle intermédiaire pour vérifier si un requin est à côté de la case choisie !
            if len(liste_directions_sures) > 0:
                for direction in liste_directions_sures:
                    valeur_destination = self._ocean.infos_coordonnees(self._ocean.deplacer_coordonnees(coordonnees, direction))

                    if (valeur_destination is None):
                        direction_choisie = direction
                        break
                    else:
                        direction_choisie = Direction.Aucune
            else:
                direction_choisie = random.choice(list(Direction))
        self.action_deplacement(coordonnees, direction_choisie)