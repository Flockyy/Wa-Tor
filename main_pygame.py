from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
from monde import Monde
from requin import Requin
from proie import Proie
from ocean import Ocean, Coordonnees

pygame.init()
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

def set_parameters(nb_requins, nb_proies, nb_chronons, resolution, plein_ecran):
    """Fonction pour définir les paramètres de la simulation."""
    # Ici vous pouvez utiliser les paramètres pour initialiser votre simulation
    print(f"Nombre de requins: {nb_requins}")
    print(f"Nombre de proies: {nb_proies}")
    print(f"Nombre de chronons: {nb_chronons}")
    print(f"Résolution: {resolution}")
    print(f"Plein écran: {plein_ecran}")
    
def start_game(nb_requins, nb_proies, nb_chronons, resolution, plein_ecran):
    """Fonction pour démarrer le jeu."""
    
    # Initialisation de Pygame et création de la fenêtre
    if plein_ecran:
        pygame.display.set_mode(resolution, pygame.FULLSCREEN)
    else:
        pygame.display.set_mode(resolution, pygame.RESIZABLE)
    
    pygame.display.set_caption("Simulation Wa-tor")
    running = True
    clock = pygame.time.Clock()
    chronon = 0
    # Création du monde
    monde = Monde(90, 60)
    # Création des proies et requins
    proies = [Proie(monde.ocean) for _ in range(nb_proies)]
    requins = [Requin(monde.ocean) for _ in range(nb_requins)]
    # Placement des proies et requins dans le monde
    
    monde.placer_poissons(proies, requins) 
    while running:
        # Gérer les événements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # Check for the fullscreen toggle event
            if event.type == pygame.KEYDOWN and event.key == pygame.K_F1:
                # Toggle fullscreen mode
                pygame.display.toggle_fullscreen()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                menu.enable()
                return
        
        # Remplir l'écran avec une couleur
        screen.fill((0, 0, 0))
        
        # Afficher la grille
        for i in range(monde.nb_lignes):
            for j in range(monde.nb_colonnes):
                cell = monde.ocean.valeur_coordonnees(Coordonnees(i, j))
                if isinstance(cell, Proie):
                    pygame.draw.rect(screen, (0, 255, 0), (j * 20, i * 20, 20, 20))
                elif isinstance(cell, Requin):
                    pygame.draw.rect(screen, (255, 0, 0), (j * 20, i * 20, 20, 20))
        
        # Mettre à jour l'affichage
        pygame.display.flip()
        
        # Limiter le nombre de frames par seconde
        clock.tick(60)
        
        # Exécuter un cycle de simulation

        monde.executer_cycle()

        sleep(0.05)  # Pause pour ralentir la simulation
            
menu = pygame_menu.Menu(
    height=720,
    width=1280,
    title='Simulation Wa-tor',
    theme=themes.THEME_DARK
)

plein_ecran = menu.add.selector('Mode plein écran :', [('OUI', True), ('NON', False)], default=1)
resolution = menu.add.selector('Résolution :', [('1280x720', (1280, 720)), ('1920x1080', (1920, 1080))], default=0)
nb_requins = menu.add.range_slider('Nombre de requins :', default=400, range_values=(1,1000), increment=1, value_format= lambda x: f"{x:.0f}")
nb_proies = menu.add.range_slider('Nombre de proies :', default=600, range_values=(1,1000), increment=1, value_format= lambda x: f"{x:.0f}")
nb_chronons = menu.add.range_slider('Nombre de chronons :', default=10, range_values=(1,10000), increment=1, value_format= lambda x: f"{x:.0f}")

menu.add.button('Jouer', start_game, nb_requins.get_value(), nb_proies.get_value(), nb_chronons.get_value(), resolution.get_value()[0][1], plein_ecran.get_value())
menu.add.button('Quitter', pygame_menu.events.EXIT)

update_loading = pygame.USEREVENT + 1

while True:
    
    pygame.time.Clock().tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if menu.is_enabled():
        menu.mainloop(screen)
            
    pygame.display.flip()