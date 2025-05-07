from proie import Proie
from requin import Requin
from monde import Monde
import pygame, random, argparse, sys

# Color setup
BACKGROUND = ( 62,  70,  73)
OCEAN      = ( 47,  47,  49)
FISH       = ( 34, 168, 109)
SHARK      = (233, 110,  68)

# Constant setup
CELLSIZE = 8
MARGIN = 2
WIDTH = 90
HEIGHT = 60
WINDOW_X = 900
WINDOW_Y = 600

def draw_grid(screen, monde):
    """Draw the grid on the screen."""
    for i in range(monde.lignes):
        for j in range(monde.colonnes):
            color = OCEAN
            if isinstance(monde.grille.grille[i][j], Proie):
                color = FISH
            elif isinstance(monde.grille.grille[i][j], Requin):
                color = SHARK

            pygame.draw.rect(
                screen,
                color,
                [
                    j * (CELLSIZE + MARGIN),
                    i * (CELLSIZE + MARGIN),
                    CELLSIZE,
                    CELLSIZE,
                ],
            )

def parse_args():
    
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Wa-tor simulation")
    parser.add_argument(
        "--hauteur", type=int, default=10, help="Nombre de lignes dans la grille"
    )
    parser.add_argument(
        "--largeur", type=int, default=10, help="Nombre de colonnes dans la grille"
    )
    parser.add_argument(
        "--chronon", type=int, default=10, help="Nombre d'étapes de simulation"
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
    return parser.parse_args()

def main(args):
    """Main function to run the simulation."""
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_X, WINDOW_Y))
    pygame.display.set_caption("Wa-tor Simulation")

    # Create the world
    monde = Monde(args.hauteur, args.largeur)
    proies = [Proie() for _ in range(args.proie)]
    requins = [Requin() for _ in range(args.requin)]
    monde.placer_poissons(proies, requins)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BACKGROUND)
        draw_grid(screen, monde)
        pygame.display.flip()

        # Simulation step
        monde.simuler()

        # Delay for visualization
        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    args = parse_args()
    main(args)