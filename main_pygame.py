from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
import pygame_menu.font
from monde import Monde
from requin import Requin
from proie import Proie
from ocean import Ocean, Coordonnees
import argparse
from pygame._sdl2 import Window

# Color setup
FOND = (62, 70, 73)
OCEAN = (47, 47, 49)
PROIE = (34, 168, 109)
SHARK = (233, 110, 68)

# Constant setup
TAILLE_CELLULE = 8
MARGE = 2
LARGEUR = 90
HAUTEUR = 60
WINDOW_X = 1280
WINDOW_Y = 720

# Initialisation de Pygame et création de la fenêtre
pygame.init()
pygame.mixer.init()

ecran = pygame.display.set_mode((WINDOW_X, WINDOW_Y), pygame.RESIZABLE)

parser = argparse.ArgumentParser(description="Wa-tor simulation")
parser.add_argument("-fps", "--framerate", type=int, default=60, help="Frame rate")
args = parser.parse_args()
background = pygame.image.load("assets/bg.png")

def demarrer_jeu():
    """Fonction pour démarrer le jeu."""
    
    pygame.mixer.music.load("assets/music2.mp3")
    pygame.mixer.music.play(-1)

    # Initialisation des variables globales
    global police
    global pause
    global lancer
    global nb_requins
    global nb_proies
    global nb_chronons
    global plein_ecran
    global resolution
    global nb_vie_requins
    global temps_reprod_requins
    global vie_par_repas_requins
    global temps_reprod_proies
    global scenario
    
    
    if plein_ecran.get_value()[0][1]:
        ecran = pygame.display.set_mode(resolution.get_value()[0][1], pygame.FULLSCREEN)
    else:
        ecran = pygame.display.set_mode(resolution.get_value()[0][1], pygame.RESIZABLE)
        Window.from_display_module().maximize()
    
    pygame.display.set_caption("Wa-tor")
    lancer, pause = True, False
    chronon = round(nb_chronons.get_value())

    # Création du monde
    monde = Monde(
        HAUTEUR, 
        LARGEUR, 
        round(nb_requins.get_value()), 
        round(nb_proies.get_value()), 
        round(temps_reprod_requins.get_value()), 
        round(temps_reprod_proies.get_value()), 
        1, 
        1, 
        True, 
        True, 
        round(nb_vie_requins.get_value()), 
        round(vie_par_repas_requins.get_value())
    )
    
    # Boucle principale du jeu
    while lancer:
        # Gérer les événements
        for evenement in pygame.event.get():
            
            if evenement.type == pygame.QUIT:
                exit()
                
            if evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_F1:
                # Toggle fullscreen mode
                pygame.display.toggle_fullscreen()
                
            if evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_ESCAPE:
                menu.enable()
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/music.mp3")
                pygame.mixer.music.play(-1)
                return 
            
            #pause game
            if evenement.type == pygame.KEYDOWN and evenement.key == pygame.K_SPACE:
                pause = not pause
                if pause:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
        # Vérifier si le jeu est en pause
        if pause:
            continue       
        
        # Remplir l'écran avec une couleur
        ecran.fill(FOND)
        
        # Afficher la grille
        for i in range(monde.nb_lignes):
            for j in range(monde.nb_colonnes):
                cell = monde.ocean.valeur_coordonnees(Coordonnees(i, j))
                if isinstance(cell, Proie):
                    color = PROIE
                    
                elif isinstance(cell, Requin):
                    color = SHARK
                else:
                    color = OCEAN
                pygame.draw.rect(ecran, color, (j * TAILLE_CELLULE + MARGE, i * TAILLE_CELLULE + MARGE, TAILLE_CELLULE - MARGE, TAILLE_CELLULE - MARGE))
                    
        # récupérer le nombre de requins et de proies restantes
        nb_requins_restants = sum(1 for i in range(monde.nb_lignes) for j in range(monde.nb_colonnes) if isinstance(monde.ocean.valeur_coordonnees(Coordonnees(i, j)), Requin))
        nb_proies_restantes = sum(1 for i in range(monde.nb_lignes) for j in range(monde.nb_colonnes) if isinstance(monde.ocean.valeur_coordonnees(Coordonnees(i, j)), Proie))

        # Afficher le nombre de requins et de proies restantes sur pygame

        texte_requins = police.render(f"Requins restants : {nb_requins_restants}", True, (255, 255, 255))
        texte_proies = police.render(f"Proies restantes : {nb_proies_restantes}", True, (255, 255, 255))
        ecran.blit(texte_requins, (10, 10))
        ecran.blit(texte_proies, (10, 50))
        
        # Afficher le nombre de chronons restants
        texte_chronons = police.render(f"Chronons restants : {chronon}", True, (255, 255, 255))
        ecran.blit(texte_chronons, (10, 90))
        
        # Mettre à jour l'affichage
        pygame.display.flip()
        
        # Exécuter un cycle de simulation

        monde.executer_cycle()

        sleep(0.05)  # Pause pour ralentir la simulation
        
        if chronon == 0:
            lancer = False
            
        chronon -= 1

# Menu principal       
police = pygame.font.Font(None, 36)
font = pygame_menu.font.FONT_MUNRO
my_theme  = pygame_menu.themes.THEME_DARK.copy()
my_theme.widget_font = font
my_theme.widget_font_color = (255, 255, 255)

menu = pygame_menu.Menu(
    height=720,
    width=1280,
    title='Simulation Wa-tor',
    theme=my_theme
)

# Menu paramètres
menu2 = pygame_menu.Menu(
    height=720,
    width=1280,
    title='Parametres',
    theme=my_theme
)

# Menu paramètres requins
menu3 = pygame_menu.Menu(
    height=720,
    width=1280,
    title='Parametres requins',
    theme=my_theme
)

# Menu paramètres proies
menu4 = pygame_menu.Menu(
    height=720,
    width=1280,
    title='Parametres proies',
    theme=my_theme
)

# Paramètres requins et proies
nb_vie_requins = menu3.add.range_slider('Points de vie :', default=12, range_values=(1,30), increment=1, value_format=lambda x: f"{x:.0f}")
temps_reprod_requins = menu3.add.range_slider('Temps de reproduction des requins :', default=12, range_values=(1,30), increment=1, value_format=lambda x: f"{x:.0f}")
vie_par_repas_requins = menu3.add.range_slider('Point de vie par repas :', default=1, range_values=(1,30), increment=1, value_format=lambda x: f"{x:.0f}")
temps_reprod_proies = menu4.add.range_slider('Temps de reproduction des proies :', default=4, range_values=(1,30), increment=1, value_format=lambda x: f"{x:.0f}")

# Paramètres du jeu
plein_ecran = menu2.add.dropselect('Plein ecran :', [('Non', False), ('Oui', True)], default=0)
resolution = menu2.add.dropselect('Resolution :', [('1280x720', (1280, 720)), ('900x600', (900, 600)), ('1920x1080', (1920, 1080))], default=0)
scenario = menu2.add.dropselect('Scenario :', [('Mode vague', 1), ('Scenario 2', 2), ('Scenario 3', 3)], default=0)
nb_requins = menu2.add.range_slider('Nombre de requins :', default=400, range_values=(1,1000), increment=1, value_format=lambda x: f"{x:.0f}")
nb_proies = menu2.add.range_slider('Nombre de proies :', default=600, range_values=(1,1000), increment=1, value_format=lambda x: f"{x:.0f}")
nb_chronons = menu2.add.range_slider('Nombre de chronons :', default=1000, range_values=(1,10000), increment=1, value_format=lambda x: f"{x:.0f}")

# Ajout des boutons au menu
menu.add.button('Jouer', demarrer_jeu)
menu.add.button('Parametres', action=menu2)
menu2.add.button('Parametres requins', action=menu3)
menu2.add.button('Parametres proies', action=menu4)
menu.add.button('Quitter', pygame_menu.events.EXIT)
update_loading = pygame.USEREVENT + 1

# Boucle principale
lancer, pause = True, False
while lancer:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    if menu.is_enabled():
        menu.mainloop(ecran)
    
    if menu2.is_enabled():
        menu2.mainloop(ecran)
    
    pygame.display.flip()