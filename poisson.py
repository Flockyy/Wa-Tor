from abc import ABC,abstractmethod #Abstract Base Classes
from ocean import Ocean, Coordonnees, Direction

class Poisson(ABC):
    """
    Classe de base des êtres vivants sur WA-TOR.

    Args:
        cycle_reproduction (int): Nombre de cycle entre chaque reproduction
    """
    def __init__(self, cycle_reproduction: int):
        self.__cycle_reproduction = cycle_reproduction
        self.__nb_cycles_depuis_derniere_repro = 0
        self.__direction = Direction.Aucune

    @property
    def cycle_reproduction(self)-> int:
        return self.__cycle_reproduction

    @property
    def nb_cycles_depuis_derniere_repro(self)-> int:
        return self.__nb_cycles_depuis_derniere_repro
    
    @property
    def direction(self)-> Direction:
        return self.__direction
    
    @abstractmethod
    def _nouvelle_instance(self)-> any:
        pass

    @abstractmethod
    def caractere_symbole(self)-> str:
        pass

    def action_deplacement(self, coordonnees_courantes: Coordonnees, direction_choisie: Direction, ocean: Ocean):
        """Action à effectuer à chaque cycle par le poisson, en décidant de la direction de déplacement choisie.

        Cette méthode
        - met à jour la direction choisie
        - effectue le déplacement par le poisson (si la direction choisie est différente de 'Aucune')
        - et gère la reproduction s'il y a lieu.

        Args:
            coordonnees_courantes (Coordonnees): Coordonnées courantes avant déplacement.
            direction_choisie (Direction): Direction de déplacement choisie par le poisson
            ocean (Ocean): Océan dans lequel évolue le poisson.
        """
        self.__direction = direction_choisie
        if self.direction != Direction.Aucune:
            enfant = None
            if (self.__nb_cycles_depuis_derniere_repro >= self.__cycle_reproduction):
                self.__nb_cycles_depuis_derniere_repro = 0
                enfant = self._nouvelle_instance()
            ocean.effectuer_deplacement(
                coordonnees_courantes,
                ocean.deplacer_coordonnees(coordonnees_courantes, direction_choisie),
                enfant)

    def rechercher_poisson(self, ocean: Ocean, coordonnees_observation: Coordonnees, direction_observee: Direction, nom_classe_recherchee: str)-> Coordonnees | None:
        """Recherche la position du poisson le plus proche (possédant la classe recherchée) dans la direction demandée.
        La recherche est effectuée en balayant un angle 90° dans la direction demandée.

        Args:
            ocean (Ocean) : Océan dans lequel la recherche doit être faite
            coordonnees_observation (Coordonnees) : Coordonnees à partir desquelles la recherche est effectuée
            direction_observee (Direction): Direction dans laquelle la recherche est effectuée
            nom_classe_recherchee (str): Type de poisson (nom de classe) recherché.

        Returns:
            Coordonnees | None: Retourne la coordonnée du type de posson recherché le plus proche,
            ou None si la recherche n'a pas abouti.
        """

        def traiter_rang_suivant(coordonnees_precedentes: Coordonnees, distance_rang: int = 1)-> Coordonnees:
            # Si on a parcouru la moitié de la carte dans la direction demandée, on retourne None, on effectue le traitement.
            if (direction_observee in (Direction.Haut, Direction.Bas)):
                limite_profondeur = int(ocean.lignes / 2)
            else:
                limite_profondeur = int(ocean.colonnes / 2)
            if distance_rang > limite_profondeur:
                return None
            
            resultat = None;
            # longueur_rang : on observe la case du milieu du rang (celle qui est ds l'axe de la direction)
            #                 + 1 case en plus de chaque côté qui sont ajoutées au fur et à mesure qu'on s'éloigne.
            longueur_rang = 1 + (2 * distance_rang)
            # observe le rang, en partant du centre, puis en s'éloignant alternativement de chaque côté
            coordonnees_observees = ocean.deplacer_coordonnees(coordonnees_precedentes, direction_observee) # on est au milieu du rang
            if ocean.infos_coordonnees(coordonnees_observees) == nom_classe_recherchee:
                resultat = coordonnees_observees
            else:
                coordonnees_a = Coordonnees(coordonnees_observees.ligne, coordonnees_observees.colonne)
                coordonnees_b = Coordonnees(coordonnees_observees.ligne, coordonnees_observees.colonne)
                if (direction_observee in (Direction.Gauche, Direction.Droite)):
                    direction_a = Direction.Haut
                    direction_b = Direction.Bas
                else:
                    direction_a = Direction.Gauche
                    direction_b = Direction.Droite
                for position in range(int((longueur_rang - 1) / 2)):
                    coordonnees_a = ocean.deplacer_coordonnees(coordonnees_a, direction_a)
                    coordonnees_b = ocean.deplacer_coordonnees(coordonnees_b, direction_b)
                    if ocean.infos_coordonnees(coordonnees_a) == nom_classe_recherchee:
                        resultat = coordonnees_a
                        break
                    elif ocean.infos_coordonnees(coordonnees_b) == nom_classe_recherchee:
                        resultat = coordonnees_b
                        break
                if resultat == None:
                    resultat = traiter_rang_suivant(coordonnees_observees, (distance_rang + 1))
            return resultat

        if direction_observee == Direction.Aucune:
            raise Exception("La direction 'Aucune' ne peut pas être observée.")
        return traiter_rang_suivant(coordonnees_observation)
    
    def executer_cycle(self, coordonnees: Coordonnees, ocean: Ocean)-> None:
        self.__nb_cycles_depuis_derniere_repro += 1