import argparse
from monde import Monde
from ocean import Ocean
from requin import Requin
from proie import Proie
from ocean import Coordonnees
import pygame


def main():

    def parse_args():
        """Parse les arguments de la ligne de commande."""
        parser = argparse.ArgumentParser(description="Wa-tor simulation")
        parser.add_argument(
            "--chronon",
            type=int,
            default=30,
            help="Nombre d'étapes de simulation (cycle de vie)",
        )
        parser.add_argument(
            "--hauteur", type=int, default=90, help="Nombre de lignes dans la grille"
        )
        parser.add_argument(
            "--largeur", type=int, default=60, help="Nombre de colonnes dans la grille"
        )
        parser.add_argument(
            "--proie",
            type=int,
            default=500,
            help="Nombre de proies à placer dans la grille",
        )
        parser.add_argument(
            "--requin",
            type=int,
            default=400,
            help="Nombre de requins à placer dans la grille",
        )
        parser.add_argument(
            "--fichier",
            type=str,
            help="Fichier de sortie pour les résultats de la simulation",
        )

        return parser.parse_args()

    args = parse_args()

    # Création du monde
    monde = Monde(args.hauteur, args.largeur)
    # Création des proies et requins

    proies = [Proie() for _ in range(args.proie)]
    requins = [Requin() for _ in range(args.requin)]

    # Initialisation de Pygame et création de la fenêtre
    pygame.init()
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("Simulation Wa-tor")
    clock = pygame.time.Clock()
    running = True
    chronon = 0
    
    # Placement des proies et requins dans le monde
    monde.placer_poissons(proies, requins)
    
    while running:
        
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Remplir l'écran avec une couleur
        screen.fill((0, 0, 0))

        # Limiter le nombre de frames par seconde
        clock.tick(60)

        # Afficher la grille
        for i in range(monde.nb_lignes):
            for j in range(monde.nb_colonnes):
                cell = monde.ocean.valeur_coordonnees(Coordonnees(i, j))
                if isinstance(cell, Proie):
                    pygame.draw.rect(screen, (0, 255, 0), (j * 20, i * 20, 20, 20))
                elif isinstance(cell, Requin):
                    pygame.draw.rect(screen, (255, 0, 0), (j * 20, i * 20, 20, 20))
                else:
                    pygame.draw.rect(screen, (0, 0, 255), (j * 20, i * 20, 20, 20))


        # Mettre à jour l'affichage
        pygame.display.flip()

        # Exécuter un cycle de simulation
        monde.executer_cycle()

        # Incrémenter le chronon
        chronon += 1

    pygame.quit()

if __name__ == "__main__":
    main()
