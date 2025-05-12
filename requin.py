#from typing import
from ocean import Ocean, Coordonnees, Direction
from poisson import Poisson


class Requin(Poisson):
    """
    Classe Requin (descendant de Poisson, est un prédateur qui doit manger des poissons pour survivre)

    Args:
        cycle_reproduction (int): 12 par défaut. Nombre de cycle entre chaque reproduction.
        points_total_vie (int): 6 par défaut. Nombre de chronons possibles sans manger. Points de vie de départ.
        points_par_repas (int): 3 par défaut. Nombre de chronons ajoutés aux points de vie lors d'un repas. 
    """
    def __init__(self, cycle_reproduction: int = 12, points_total_vie: int = 12, points_par_repas: int = 6):
        super().__init__(cycle_reproduction)
        self.__points_energie = points_total_vie
        self.__point_total_vie = points_total_vie
        self.__points_par_repas = points_par_repas
    def __str__(self):
        return f"Requin ayant un cycle de reproduction de {self.cycle_reproduction} tours et {self.points_energie} tours de vie"
    @property
    def points_energie(self)-> int:
        return self.__points_energie
    
    def caractere_symbole(self)-> str:
        return "R"
    
    def _nouvelle_instance(self):
        return Requin(self.cycle_reproduction, self.points_energie, self.__points_par_repas)

    def executer_cycle(self, coordonnees: Coordonnees, ocean: Ocean)-> None:
        super().executer_cycle(coordonnees, ocean)
        self.__points_energie -= 1

        if self.__points_energie == 0:
            ocean.effacer_valeur(coordonnees)
        
        else:
            direction_choisie = Direction.Aucune
            liste_directions = []

            if self.points_energie < self.__point_total_vie:
                liste_orientations = []
                # Mode morfal : le requin détecte pour chaque directions quelle est la proie la plus proche...
                for direction in Direction:
                    if direction != Direction.Aucune:
                        coordonnees_proie = self.rechercher_poisson(ocean, coordonnees, direction, "Proie")
                        if coordonnees_proie != None:
                            #... il calcule alors le chemin le plus court pour la choper...
                            liste_orientations.append(ocean.calculer_orientation(coordonnees, coordonnees_proie))
                if len(liste_orientations) > 0:
                    # Il déduit les directions possibles triées par diner le plus proche...
                    liste_orientations.sort(key=lambda orientation: orientation.distance)
                    for orientation in liste_orientations:
                        for direction in orientation.directions:
                            if not (direction in liste_directions):
                                liste_directions.append(direction)

            # on ajoute en dernier la direction du cycle précédent (nage en ligne droite par défaut)
            liste_directions.append(self.direction)

            for direction in liste_directions:
                if (ocean.infos_coordonnees(ocean.deplacer_coordonnees(coordonnees, direction)) != "Requin"):
                    if ocean.infos_coordonnees(ocean.deplacer_coordonnees(coordonnees, direction_choisie)) == "Proie":
                        if self.points_energie < self.__point_total_vie:
                            direction_choisie = direction
                            break
                    else:
                        direction_choisie = direction
                        break

            # et si les requins se bousculent, alors on prend la première direction possible si il a faim
            if direction_choisie == Direction.Aucune:
                for direction in Direction:
                    valeur_destination = ocean.infos_coordonnees(ocean.deplacer_coordonnees(coordonnees, direction))
                    if not((valeur_destination == "Requin") or ((valeur_destination == "Proie") and (self.points_energie >= self.__point_total_vie))):
                        direction_choisie = direction
                        break
                    
            # On applique le choix final...
            if (ocean.infos_coordonnees(ocean.deplacer_coordonnees(coordonnees, direction_choisie)) == "Proie"):            
                self.__points_energie += self.__points_par_repas
            self.action_deplacement(coordonnees, direction_choisie, ocean)




