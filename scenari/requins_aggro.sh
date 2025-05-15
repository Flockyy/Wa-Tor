#!/bin/sh

# Requin très peu nombreux mais très agressifs:  
export AUTO=NON
export CHRONON=100
export HAUTEUR=30
export LARGEUR=30
export NB_PROIE=100
export NB_REQUINS=3
export CYCLE_REPRODUCTION_REQUIN=10
export CYCLE_REPRODUCTION_PROIE=8
export VISIBILITE_REQUIN=15
export VISIBILITE_PROIE=1
export VUE_ARRIERE_REQUIN=OUI
export VUE_ARRIERE_PROIE=OUI
export POINTS_DE_VIE_REQUIN=15
export POINTS_PAR_REPAS=10

./lancement_scenario.sh
