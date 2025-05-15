from abc import ABC,abstractmethod #Abstract Base Classes
from ocean import Ocean, Coordonnees, Direction

class Poisson(ABC):
    """
    Classe de base des êtres vivants sur WA-TOR.

    Args:
        cycle_reproduction (int): Nombre de cycle entre chaque reproduction
    """
    def __init__(self, ocean: Ocean, cycle_reproduction: int, visibilite: int, vue_arriere: bool):
        """Initialise un être vivant avec ses paramètres

        Args:
            ocean (Ocean): Représentation de l'océan 
            cycle_reproduction (int): Nombre de cycle entre chaque reproduction
            visibilite (int): Distance maximale que l'être vivant peut voir autour de lui
            vue_arriere (bool): Si True, le poisson peut voir derrière lui
        """
        self._ocean = ocean
        self.__cycle_reproduction = cycle_reproduction
        self.__nb_cycles_depuis_derniere_repro = 0
        self.__visibilite = visibilite
        self.__vue_arriere = vue_arriere
        self.__direction = Direction.Aucune

    @property
    def cycle_reproduction(self)-> int:
        return self.__cycle_reproduction

    @property
    def nb_cycles_depuis_derniere_repro(self)-> int:
        return self.__nb_cycles_depuis_derniere_repro
    
    @property
    def visibilite(self)-> int:
        return self.__visibilite
    
    @property
    def vue_arriere(self)-> bool:
        return self.__vue_arriere
    
    @property
    def direction(self)-> Direction:
        return self.__direction
    
    @abstractmethod
    def _nouvelle_instance(self)-> any:
        pass

    @abstractmethod
    def caractere_symbole(self)-> str:
        pass

    def action_deplacement(self, coordonnees_courantes: Coordonnees, direction_choisie: Direction):
        """Action à effectuer à chaque cycle par le poisson, en décidant de la direction de déplacement choisie.

        Cette méthode
        - met à jour la direction choisie
        - effectue le déplacement par le poisson (si la direction choisie est différente de 'Aucune')
        - et gère la reproduction s'il y a lieu.

        Args:
            coordonnees_courantes (Coordonnees): Coordonnées courantes avant déplacement.
            direction_choisie (Direction): Direction de déplacement choisie par le poisson
        """
        self.__direction = direction_choisie
        if self.direction != Direction.Aucune:
            enfant = None
            if (self.__nb_cycles_depuis_derniere_repro >= self.__cycle_reproduction):
                self.__nb_cycles_depuis_derniere_repro = 0
                enfant = self._nouvelle_instance()
            self._ocean.effectuer_deplacement(
                coordonnees_courantes,
                self._ocean.deplacer_coordonnees(coordonnees_courantes, direction_choisie),
                enfant)

    def rechercher_poisson(self, coordonnees_observation: Coordonnees, direction_observee: Direction, nom_classe_recherchee: str)-> Coordonnees | None:
        """Recherche la position du poisson le plus proche (possédant la classe recherchée) dans la direction demandée.
        La recherche est effectuée en balayant un angle 90° dans la direction demandée.

        Args:
            coordonnees_observation (Coordonnees) : Coordonnees à partir desquelles la recherche est effectuée
            direction_observee (Direction): Direction dans laquelle la recherche est effectuée
            nom_classe_recherchee (str): Type de poisson (nom de classe) recherché.

        Returns:
            Coordonnees | None: Retourne la coordonnée du type de posson recherché le plus proche,
            ou None si la recherche n'a pas abouti.
        """

        def traiter_rang_suivant(coordonnees_precedentes: Coordonnees, distance_rang: int = 1)-> Coordonnees:
            """Recherche dans un rang successif la présence d’un élément correspondant à la classe recherchée,
            en suivant une direction d’observation donnée.

            Observe la case située juste devant dans la direction choisie, puis élargit son champ de vision en observant 
            les cases sur le côté au fur et à mesure que la distance augmente. Si aucun élément recherché n’est trouvé, elle appelle 
            le rang suivant jusqu’à atteindre une limite.

            Args:
                coordonnees_precedentes (Coordonnees) : Coordonnees précendentes 
                distance_rang (int): Distance à laquelle le rang est observé. Incrémente à chaque appel

            Returns:
                Coordonnees | None: : Retourne la première case contenant la class recherchée
                ou None si la recherche n'a pas abouti
            """

            # Si on a parcouru la moitié de la carte dans la direction demandée, ou qu'on a atteint la limite de la vision,
            # alors on retourne None, sinon on effectue le traitement.
            if (direction_observee in (Direction.Haut, Direction.Bas)):
                limite_profondeur = min(int(self._ocean.lignes / 2), self.visibilite)
            else:
                limite_profondeur = min(int(self._ocean.colonnes / 2), self.visibilite)
            if distance_rang > limite_profondeur:
                return None
            
            resultat = None;
            # longueur_rang : on observe la case du milieu du rang (celle qui est ds l'axe de la direction)
            #                 + 1 case en plus de chaque côté qui sont ajoutées au fur et à mesure qu'on s'éloigne.
            longueur_rang = 1 + (2 * distance_rang)
            # observe le rang, en partant du centre, puis en s'éloignant alternativement de chaque côté
            coordonnees_observees = self._ocean.deplacer_coordonnees(coordonnees_precedentes, direction_observee) # on est au milieu du rang
            if self._ocean.infos_coordonnees(coordonnees_observees) == nom_classe_recherchee:
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
                    coordonnees_a = self._ocean.deplacer_coordonnees(coordonnees_a, direction_a)
                    coordonnees_b = self._ocean.deplacer_coordonnees(coordonnees_b, direction_b)
                    if self._ocean.infos_coordonnees(coordonnees_a) == nom_classe_recherchee:
                        resultat = coordonnees_a
                        break
                    elif self._ocean.infos_coordonnees(coordonnees_b) == nom_classe_recherchee:
                        resultat = coordonnees_b
                        break
                if resultat == None:
                    resultat = traiter_rang_suivant(coordonnees_observees, (distance_rang + 1))
            return resultat

        if direction_observee == Direction.Aucune:
            raise Exception("La direction 'Aucune' ne peut pas être observée.")
        return traiter_rang_suivant(coordonnees_observation)
    
    def executer_cycle(self, coordonnees: Coordonnees)-> None:
        """Execute un tour de cycle pour les poissons:
        Déplacement, alimentation (pour les requins), vieillissement et reproduction si les conditions sont remplies.

        Args:
            coordonnees (Coordonnees): Position actuelle du poisson sur la grille
        """
        self.__nb_cycles_depuis_derniere_repro += 1