from typing import List

class Scenario:
    def __init__(self, libelle: str):
        self.__libelle = libelle
    
    @property
    def libelle(self)-> str:
        return self.__libelle

class Scenari:
    def __init__(self):
        self.liste_scenari = []
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

        self.ajouter_scenario('Scenario 1')
        self.ajouter_scenario('Scenario 2')
        self.ajouter_scenario('Scenario 3')
    
    @property
    def liste_scenari(self)-> list[Scenario]:
        return self.__liste_scenari
    
    def ajouter_scenario(self, libelle: str)-> Scenario:
        nouveau_scenario = Scenario(libelle)
        self.__liste_scenari.append(nouveau_scenario)
        return nouveau_scenario
    
    def appliquer_scenario(numero_scenario: int)-> None:
        pass