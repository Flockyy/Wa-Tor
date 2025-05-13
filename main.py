# filename: main.py
import os
from time import sleep
import sys
from monde import Monde
import argparse
from proie import Proie
from requin import Requin
from ocean import Coordonnees

MODE_DEBUG = False  # (getattr(sys, 'gettrace', None) is not None)


def main():

    def parse_args():
        """Parse les arguments de la ligne de commande."""
        parser = argparse.ArgumentParser(description="Wa-tor simulation")
        parser.add_argument(
            "--auto",
            type=str,
            default="NON",
            help="Automatiser la simulation (OUI ou NON)",
        )
        parser.add_argument(
            "--chronon",
            type=int,
            default=30,
            help="Nombre d'étapes de simulation (cycle de vie)",
        )
        parser.add_argument(
            "--hauteur",
            type=int,
            default=(10 if MODE_DEBUG else 30),
            help="Nombre de lignes dans la grille",
        )
        parser.add_argument(
            "--largeur",
            type=int,
            default=(10 if MODE_DEBUG else 30),
            help="Nombre de colonnes dans la grille",
        )
        parser.add_argument(
            "--proie",
            type=int,
            default=(3 if MODE_DEBUG else 30),
            help="Nombre de proies à placer dans la grille",
        )
        parser.add_argument(
            "--requin",
            type=int,
            default=(1 if MODE_DEBUG else 10),
            help="Nombre de requins à placer dans la grille",
        )
        parser.add_argument(
            "--fichier",
            type=str,
            help="Fichier de sortie pour les résultats de la simulation",
        )

        return parser.parse_args()

    args = parse_args()

    # Instanciation de la grille
    monde = Monde(args.hauteur, args.largeur)

    # Instanciation des poissons et requins
    proie = [Proie(monde.ocean) for _ in range(args.proie)]
    requins = [Requin(monde.ocean) for _ in range(args.requin)]

    # Placement des poissons et requins dans la grille
    monde.placer_poissons(proie, requins)

    if args.auto.lower() == "oui":
        cnt = 0
        while cnt < args.chronon:
            os.system("cls" if os.name == "nt" else "clear")
            print(f"Cycle {cnt + 1}/{args.chronon}")
            monde.executer_cycle()
            for ligne in range(args.hauteur):
                for colonne in range(args.largeur):
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
            sleep(1)
    else:
        cnt = 0
        while True:
            if MODE_DEBUG:
                print("En debug...")
            else:
                os.system("cls" if os.name == "nt" else "clear")
            monde.executer_cycle()
            print(f"Cycle {cnt + 1}")
            for ligne in range(args.hauteur):
                for colonne in range(args.largeur):
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

    # Sauvegarde des résultats dans un fichier
    if args.fichier:
        with open(args.fichier, "w") as f:
            for i in range(args.hauteur):
                for j in range(args.largeur):
                    if isinstance(monde.ocean.grille[i][j], Proie):
                        f.write("P ")
                    elif isinstance(monde.ocean.grille[i][j], Requin):
                        f.write("R ")
                    else:
                        f.write(". ")
                f.write("\n")
    else:
        print("Aucun fichier de sortie spécifié.")

    print("Simulation terminée.")


if __name__ == "__main__":
    main()
