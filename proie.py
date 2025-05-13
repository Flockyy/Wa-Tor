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
    def __init__(self, ocean: Ocean, cycle_reproduction: int = 8, visibilite: int = 2, vue_arriere: bool = True):
        super().__init__(ocean, cycle_reproduction, visibilite, vue_arriere)
    def __str__(self):
        return f"Proie ayant un cycle de reproduction de {self.cycle_reproduction} tours"
    def caractere_symbole(self)-> str:
        return "o"
    def _nouvelle_instance(self):
        return Proie(self._ocean, self.cycle_reproduction, self.visibilite, self.vue_arriere)
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
        set_directions_sures = set(Direction.liste_directions_melangees()) # on mélange
        set_directions_sures.remove(Direction.Aucune)
        # Mode fuite : on detecte les requins les plus proches dans chaque direction
        # et on retire leurs directions de la liste des directions sûres
        liste_orientations_requins = []
        for direction in Direction:
            if direction != Direction.Aucune:
                if (self.vue_arriere or (direction != Direction.direction_inverse(direction))):
                    coordonnees_requin = self.rechercher_poisson(coordonnees, direction, "Requin")
                    if coordonnees_requin:
                        liste_orientations_requins.append(self._ocean.calculer_orientation(coordonnees, coordonnees_requin))
        if len(liste_orientations_requins) > 0:
            liste_orientations_requins.sort(key=lambda orientation: orientation.distance)
            for orientation in liste_orientations_requins:
                for direction in orientation.directions:
                    set_directions_sures.discard(direction)
        if ((direction_choisie not in set_directions_sures) or (direction_choisie == Direction.Aucune)):
            if len(set_directions_sures) == 0:
                # Les requins se trouvent dans toutes les directions.
                # Alors on se déplace sur n'importe quelle case vide qui n'a pas de requin comme voisin
                direction_choisie = Direction.Aucune
                for direction in Direction.liste_directions_melangees():
                    coordonnees_testees = self._ocean.deplacer_coordonnees(coordonnees, direction)
                    valeur_testees = self._ocean.infos_coordonnees(coordonnees_testees)
                    if (valeur_testees is None):
                        if not self._ocean.coordonnes_jouxtent_objet(coordonnees_testees, "Requin"):
                            direction_choisie = direction
                        break
            else:
                direction_choisie = set_directions_sures.pop()

        # Si direction_choisie == Direction.Aucune
        # alors cela, signifie que quelque soit la direction, on se retrouve à côté d'un requin...
            
        # On vérifie le choix final pour s'assurer qu'on n'écrase pas d'autres poissons.
        if direction_choisie != Direction.Aucune:
            if not self._ocean.coordonnees_libres(self._ocean.deplacer_coordonnees(coordonnees, direction_choisie)):
                direction_choisie = Direction.Aucune

        self.action_deplacement(coordonnees, direction_choisie)