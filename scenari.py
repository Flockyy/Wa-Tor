from typing import List

class Scenario:
    def __init__(self, libelle: str):
        self.__libelle = libelle
        self.commentaires = ""
        self.nb_lignes = 0
        self.nb_colonnes = 0 
        self.nb_requins = 0
        self.nb_proies = 0
        self.cycle_reproduction_requin = 0
        self.cycle_reproduction_proie = 0
        self.visibilite_requin = 1
        self.visibilite_proie = 1
        self.vue_arriere_requin = False
        self.vue_arriere_proie = False
        self.points_vie_requin = 0
        self.points_par_repas_requin = 0
    
    @property
    def libelle(self)-> str:
        return self.__libelle

class Scenari:
    def __init__(self):
        self.__liste_scenari = []

        # Scenario par défaut
        scenario = self.ajouter_scenario('Scenario par défaut')
        scenario.commentaires ='''
Un océan de 30x30 avec des valeurs par défaut.
Les requins et les proies n'ont aucune visibilité : ils ne détectent que les poissons à côté d\'eux !'''
        scenario.nb_lignes = 30
        scenario.nb_colonnes = 30
        scenario.nb_proies = 40
        scenario.nb_requins = 10
        scenario.cycle_reproduction_requin = 12
        scenario.cycle_reproduction_proie = 8
        scenario.visibilite_requin = 1
        scenario.visibilite_proie = 1
        scenario.vue_arriere_requin = True
        scenario.vue_arriere_proie = True
        scenario.points_vie_requin = 12
        scenario.points_par_repas_requin = 6

        # Scenario Chasse au fugitif
        scenario = self.ajouter_scenario('Chasse au fugitif')
        scenario.commentaires ='''
Une proie rescapée se retrouve chassée par 15 requins à la vue affûtée et à la grande endurance !
La proie saura-t-elle capable de survivre jusqu'à la mort des chasseurs ?
Durée de vie des requins : 25 chronon...'''
        scenario.nb_lignes = 30
        scenario.nb_colonnes = 30
        scenario.nb_proies = 1
        scenario.nb_requins = 15
        scenario.cycle_reproduction_requin = 26
        scenario.cycle_reproduction_proie = 26
        scenario.visibilite_requin = 15
        scenario.visibilite_proie = 1
        scenario.vue_arriere_requin = True
        scenario.vue_arriere_proie = True
        scenario.points_vie_requin = 25
        scenario.points_par_repas_requin = 6

        # Scenario Rambo
        scenario = self.ajouter_scenario('Rambo s\'évade !')
        scenario.commentaires ='''
Comme pour dans le scenario "Chasse au fugitif", une proie rescapée se retrouve chassée...
C'est contre 4 requins à la vue affûtée et à la grande endurance qu'il faudra survivre !
Mais cette fois, la proie a la vue aussi affûtée que celle des requins... Rambo saura-t-il s'en sortir ?
Durée de vie des requins : 25 chronon...'''
        scenario.nb_lignes = 30
        scenario.nb_colonnes = 30
        scenario.nb_proies = 1
        scenario.nb_requins = 4
        scenario.cycle_reproduction_requin = 26
        scenario.cycle_reproduction_proie = 26
        scenario.visibilite_requin = 15
        scenario.visibilite_proie = 15
        scenario.vue_arriere_requin = True
        scenario.vue_arriere_proie = True
        scenario.points_vie_requin = 25
        scenario.points_par_repas_requin = 6
    
        scenario = self.ajouter_scenario('Mode infinie vague')
        scenario.commentaires ='''
        '''
        scenario.nb_lignes = 60
        scenario.nb_colonnes = 90
        scenario.nb_proies = 900
        scenario.nb_requins = 100
        scenario.cycle_reproduction_requin = 12
        scenario.cycle_reproduction_proie = 4
        scenario.visibilite_requin = 2
        scenario.visibilite_proie = 2
        scenario.vue_arriere_requin = True
        scenario.vue_arriere_proie = True
        scenario.points_vie_requin = 12
        scenario.points_par_repas_requin = 1

        scenario = self.ajouter_scenario('Mode infinie brasier')
        scenario.commentaires ='''
        '''
        scenario.nb_lignes = 60
        scenario.nb_colonnes = 90
        scenario.nb_proies = 900
        scenario.nb_requins = 100
        scenario.cycle_reproduction_requin = 12
        scenario.cycle_reproduction_proie = 6
        scenario.visibilite_requin = 2
        scenario.visibilite_proie = 2
        scenario.vue_arriere_requin = True
        scenario.vue_arriere_proie = True
        scenario.points_vie_requin = 12
        scenario.points_par_repas_requin = 2
        
    @property
    def liste_scenari(self)-> list[Scenario]:
        return self.__liste_scenari
    
    def liste_libelles(self)-> list:
        return [scenario.libelle for scenario in self.__liste_scenari]
    
    def scenario(self, numero_scenario: int)-> Scenario:
        return self.liste_scenari[numero_scenario]

    def ajouter_scenario(self, libelle: str)-> Scenario:
        scenario = Scenario(libelle)
        self.__liste_scenari.append(scenario)
        return scenario