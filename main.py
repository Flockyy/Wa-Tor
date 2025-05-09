# filename: main.py

from monde import Monde
import argparse
from proie import Proie
from requin import Requin


def main():

    def parse_args():
        """Parse les arguments de la ligne de commande."""
        parser = argparse.ArgumentParser(description="Wa-tor simulation")
        parser.add_argument(
            "--auto", 
            type=str, 
            default="NON",
            help="Automatiser la simulation (OUI ou NON)"
        )
        parser.add_argument(
            "--chronon",
            type=int,
            default=10,
            help="Nombre d'étapes de simulation (cycle de vie)",
        )
        parser.add_argument(
            "--hauteur", 
            type=int, 
            default=10, 
            help="Nombre de lignes dans la grille"
        )
        parser.add_argument(
            "--largeur", 
            type=int, 
            default=10, 
            help="Nombre de colonnes dans la grille"
        )
        parser.add_argument(
            "--proie",
            type=int,
            default=5,
            help="Nombre de proies à placer dans la grille",
        )
        parser.add_argument(
            "--requin",
            type=int,
            default=5,
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
    proie = [Proie() for _ in range(args.proie)]
    requins = [Requin() for _ in range(args.requin)]

    # Placement des poissons et requins dans la grille
    monde.placer_poissons(proie, requins)
    
    if args.auto.lower() == "oui":
        cnt = 0
        while cnt < args.chronon:
            print(f"Cycle {cnt + 1}/{args.chronon}")
            monde.executer_cycle()
            cnt += 1
    else:
        while True:
            monde.executer_cycle()
            if input("Entrez Q pour quitter ou n'importe quelle autre touche pour continuer...").lower() == "q":
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
