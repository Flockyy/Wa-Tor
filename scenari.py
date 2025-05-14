from typing import List

class Scenario:
    def __init__(self, libelle: str):
        self.__libelle = libelle
        self.nb_lignes = 0
        self.nb_colonnes = 0 
        self.nb_requins = 0
        self.nb_proies = 0
        self.cycle_reproduction_requin = 0
        self.cycle_reproduction_proie = 0
        self.visibilite_requin = False
        self.visibilite_proie = False
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

        scenario = self.ajouter_scenario('Scenario 1')
        scenario.nb_lignes = 30
        scenario.nb_colonnes = 30
        scenario.nb_proies = 40
        scenario.nb_requins = 10
        scenario.cycle_reproduction_requin = 12
        scenario.cycle_reproduction_proie = 8
        scenario.visibilite_requin = True
        scenario.visibilite_proie = True
        scenario.vue_arriere_requin = True
        scenario.vue_arriere_proie = True
        scenario.points_vie_requin = 12
        scenario.points_par_repas_requin = 6
    
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