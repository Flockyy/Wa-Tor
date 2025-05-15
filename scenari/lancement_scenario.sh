#!/bin/sh

echo $CHRONON

SIMULATION="/Users/alexis/dev/simplon/Wa-Tor/.venv/bin/python \
/Users/alexis/dev/simplon/Wa-Tor/main.py \
--auto=$AUTO \
--chronon=$CHRONON \
--hauteur=$HAUTEUR \
--largeur=$LARGEUR \
--nb-proie=$NB_PROIE \
--nb-requin=$NB_REQUINS \
--cycle-reproduction-requin=$CYCLE_REPRODUCTION_REQUIN \
--cycle-reproduction-proie=$CYCLE_REPRODUCTION_PROIE \
--visibilite-requin=$VISIBILITE_REQUIN \
--visibilite-proie=$VISIBILITE_PROIE \
--vue_arriere-requin=$VUE_ARRIERE_REQUIN \
--vue_arriere-proie=$VUE_ARRIERE_PROIE \
--points-de-vie-requin=$POINTS_DE_VIE_REQUIN \
--points-par-repas-requin=$POINTS_PAR_REPAS"

echo $SIMULATION
read -p "Appuyez sur une touche pour lancer..." -n1 -s
$SIMULATION