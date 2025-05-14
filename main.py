# filename: main.py
import os
from time import sleep
import sys
from monde import Monde
import argparse
from proie import Proie
from requin import Requin
from ocean import Coordonnees
from scenari import Scenari, Scenario

MODE_DEBUG = False  # ça marche pas. (getattr(sys, 'gettrace', None) is not None)

def demander_choix_menu(liste_choix: list) -> int:
    """
    Fonction qui affiche un menu et demande à l'utilisateur de faire un choix.

    Args:
        liste_choix (list): Liste des choix possibles.

    Returns:
        int: L'index du choix fait par l'utilisateur.
    """
    while True:
        print("Faites un choix...")
        for numero_choix in range(len(liste_choix)):
            print(f"{numero_choix + 1} : {liste_choix[numero_choix]}")
        choix = input("Votre choix : ")
        if choix.isnumeric():
            valeur_numerique = int(choix)
            if 1 <= valeur_numerique <= len(liste_choix):
                return valeur_numerique - 1
        print("Numéro non reconnu.")
    
def parse_args():
    """Parse les arguments de la ligne de commande."""
    parser = argparse.ArgumentParser(description="Wa-tor simulation")
    parser.add_argument(
        "--menu",
        type=str,
        default="OUI",
        help="Afficher le menu (OUI ou NON)"
    )
    parser.add_argument(
        "--auto",
        type=str,
        default="NON",
        help="Automatiser la simulation (OUI ou NON)"
    )
    parser.add_argument(
        "--chronon",
        type=int,
        default=30,
        help="Nombre d'étapes de simulation si activation paramètre --auto=OUI (cycle de vie)"
    )
    parser.add_argument(
        "--hauteur",
        type=int,
        default=(10 if MODE_DEBUG else 30),
        help="Nombre de lignes dans la grille"
    )
    parser.add_argument(
        "--largeur",
        type=int,
        default=(10 if MODE_DEBUG else 30),
        help="Nombre de colonnes dans la grille"
    )
    parser.add_argument(
        "--nb-proie",
        type=int,
        default=(1 if MODE_DEBUG else 40),
        help="Nombre de proies à placer dans la grille"
    )
    parser.add_argument(
        "--nb-requin",
        type=int,
        default=(0 if MODE_DEBUG else 10),
        help="Nombre de requins à placer dans la grille"
    )
    #parser.add_argument(
    #    "--fichier",
    #    type=str,
    #    help="Fichier de sortie pour les résultats de la simulation",
    #)
    parser.add_argument(
        "--cycle-reproduction-requin",
        type=int,
        default=(12 if MODE_DEBUG else 12),
        help="Nombre de cycles entre chaque reproduction des requins"
    )
    parser.add_argument(
        "--cycle-reproduction-proie",
        type=int,
        default=(8 if MODE_DEBUG else 8),
        help="Nombre de cycles entre chaque reproduction des proies"
    )
    parser.add_argument(
        "--visibilite-requin",
        type=int,
        default=1,
        help="Distance en cellules pour la vision des requins"
    )
    parser.add_argument(
        "--visibilite-proie",
        type=int,
        default=1,
        help="Distance en cellules pour la vision des proies"
    )
    parser.add_argument(
        "--vue_arriere-requin",
        type=str,
        help="Capacité des requins à détecter les proies à distance derrière eux"
    )
    parser.add_argument(
        "--vue_arriere-proie",
        type=str,
        default=("OUI" if MODE_DEBUG else "OUI"),
        help="Capacité des proies à détecter les requins à distance derrière eux"
    )
    parser.add_argument(
        "--points-de-vie-requin",
        type=int,
        default=(12 if MODE_DEBUG else 12),
        help="Points de vie du requin (réduit de 1 à chaque cycle)"
    )
    parser.add_argument(
        "--points-par-repas-requin",
        type=int,
        default=(6 if MODE_DEBUG else 6),
        help="Points de recharge par proie mangée"
    )
    return parser.parse_args()

def lancer(
        automatique: bool, nb_cycles: int,
        hauteur: int, largeur: int,
        nb_requin: int, nb_proie: int,
        cycle_reproduction_requin: int, cycle_reproduction_proie: int,
        visibilite_requin: int, visibilite_proie: int,
        vue_arriere_requin: bool, vue_arriere_proie: bool,
        points_de_vie_requin: int, points_par_repas_requin: int):
    monde = Monde(hauteur, largeur,
                  nb_requin, nb_proie,
                  cycle_reproduction_requin, cycle_reproduction_proie,
                  visibilite_requin, visibilite_proie,
                  vue_arriere_requin, vue_arriere_proie,
                  points_de_vie_requin, points_par_repas_requin)
    if automatique:
        cnt = 0
        while cnt < nb_cycles:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Cycle {cnt + 1}/{nb_cycles}")
            monde.executer_cycle()
            for ligne in range(hauteur):
                for colonne in range(nb_cycles):
                    if (
                        monde.ocean.valeur_coordonnees(Coordonnees(ligne, colonne))
                        == None
                    ):
                        print("·", end=" ")
                    else:
                        print(
                            monde.ocean.valeur_coordonnees(
                                Coordonnees(ligne, colonne)
                            ).caractere_symbole(),
                            end=" ",
                        )
                print()
            cnt += 1
            sleep(0.1)
    else:
        cnt = 0
        while True:
            if MODE_DEBUG:
                print("En debug...")
            else:
                os.system("cls" if os.name == "nt" else "clear")
            monde.executer_cycle()
            print(f"Cycle {cnt + 1}")
            for ligne in range(hauteur):
                for colonne in range(largeur):
                    if (
                        monde.ocean.valeur_coordonnees(Coordonnees(ligne, colonne))
                        == None
                    ):
                        print("·", end=" ")
                    else:
                        print(
                            monde.ocean.valeur_coordonnees(
                                Coordonnees(ligne, colonne)
                            ).caractere_symbole(),
                            end=" ",
                        )
                print()
            cnt += 1
            if (
                input(
                    "Entrez Q pour quitter ou n'importe quelle autre touche pour continuer..."
                ).lower()
                == "q"
            ):
                break

    ## Sauvegarde des résultats dans un fichier
    #if args.fichier:
    #    with open(args.fichier, "w") as f:
    #        for i in range(args.hauteur):
    #            for j in range(args.largeur):
    #                if isinstance(monde.ocean.grille[i][j], Proie):
    #                    f.write("P ")
    #                elif isinstance(monde.ocean.grille[i][j], Requin):
    #                    f.write("R ")
    #                else:
    #                    f.write(". ")
    #            f.write("\n")
    #else:
    #    print("Aucun fichier de sortie spécifié.")

    print("Simulation terminée.")

def selection_scenario(scenario: Scenario)-> None:
    print(f"Scenario sélectionné : {scenario.libelle}")
    print("Commentaires :")
    print(scenario.commentaires)
    print("")
    liste_choix = ["Lancer le scenario", "Revenir au menu principal"]
    choix = demander_choix_menu(liste_choix)
    if choix == 0:
        lancer(
            False, 0,
            scenario.nb_lignes, scenario.nb_colonnes,
            scenario.nb_requins, scenario.nb_proies,
            scenario.cycle_reproduction_requin, scenario.cycle_reproduction_proie,
            scenario.visibilite_requin, scenario.visibilite_proie,
            scenario.vue_arriere_requin, scenario.vue_arriere_proie,
            scenario.points_vie_requin, scenario.points_par_repas_requin)
    else:
        return

def main():
    args = parse_args()
    if (args.menu == "OUI"):
        scenari = Scenari()
        print("Bienvenue dans WA-TOR !")
        while True:
            print("Choisissez un scenario :")
            liste_libelles = scenari.liste_libelles()
            liste_libelles.append("Quitter le programme")
            choix = demander_choix_menu(liste_libelles)
            if choix == (len(liste_libelles) - 1):
                break
            else:
                selection_scenario(scenario = scenari.scenario(choix))
    else:
        lancer(
            True, args.chronon,
            args.hauteur, args.largeur,
            args.nb_requin, args.nb_proie,
            args.cycle_reproduction_requin, args.cycle_reproduction_proie,
            args.visibilite_requin, args.visibilite_proie,
            (args.vue_arriere_requin == "OUI"), (args.vue_arriere_proie == "OUI"),
            args.points_de_vie_requin, args.points_par_repas_requin)

if __name__ == "__main__":
    main()