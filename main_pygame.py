from time import sleep
import pygame
import pygame_menu
from pygame_menu import themes
from monde import Monde
from requin import Requin
from proie import Proie
from ocean import Ocean, Coordonnees

pygame.init()
ecran = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
    
def demarrer_jeu():
    """Fonction pour démarrer le jeu."""
    global nb_requins
    global nb_proies
    global nb_chronons
    global plein_ecran
    global resolution
    global nb_vie_requins
    global temps_reprod_requins
    global vie_par_repas_requins
    global temps_reprod_proies
    
    
    # Initialisation de Pygame et création de la fenêtre
    if plein_ecran.get_value()[0][1]:
        ecran = pygame.display.set_mode(resolution.get_value()[0][1], pygame.FULLSCREEN)
    else:
        ecran = pygame.display.set_mode(resolution.get_value()[0][1], pygame.RESIZABLE)
    
    pygame.display.set_caption("Simulation Wa-tor")
    lancer = True
    horloge = pygame.time.Clock()
    chronon = round(nb_chronons.get_value())
    # Création du monde
    monde = Monde(60, 90)
    
    # Création des proies et requins
    proies = [Proie(monde.ocean, cycle_reproduction=round(temps_reprod_proies.get_value())) for _ in range(round(nb_proies.get_value()))]
    requins = [Requin(monde.ocean, cycle_reproduction=round(temps_reprod_requins.get_value()), points_total_vie=round(nb_vie_requins.get_value()), points_par_repas=round(vie_par_repas_requins.get_value())) for _ in range(round(nb_requins.get_value()))]
    
    # Placement des proies et requins dans le monde
    monde.placer_poissons(proies, requins) 
    
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
                return
        
        # Remplir l'écran avec une couleur
        ecran.fill((0, 0, 0))
        
        # Afficher la grille
        for i in range(monde.nb_lignes):
            for j in range(monde.nb_colonnes):
                cell = monde.ocean.valeur_coordonnees(Coordonnees(i, j))
                if isinstance(cell, Proie):
                    pygame.draw.rect(ecran, (0, 255, 0), (j * 10, i * 10, 10, 10))
                elif isinstance(cell, Requin):
                    pygame.draw.rect(ecran, (255, 0, 0), (j * 10, i * 10, 10, 10))
        
                    
        # récupérer le nombre de requins et de proies restantes
        nb_requins_restants = sum(1 for i in range(monde.nb_lignes) for j in range(monde.nb_colonnes) if isinstance(monde.ocean.valeur_coordonnees(Coordonnees(i, j)), Requin))
        nb_proies_restantes = sum(1 for i in range(monde.nb_lignes) for j in range(monde.nb_colonnes) if isinstance(monde.ocean.valeur_coordonnees(Coordonnees(i, j)), Proie))

        # Afficher le nombre de requins et de proies restantes sur pygame
        police = pygame.font.Font(None, 36)
        texte_requins = police.render(f"Requins restants : {nb_requins_restants}", True, (255, 255, 255))
        texte_proies = police.render(f"Proies restantes : {nb_proies_restantes}", True, (255, 255, 255))
        ecran.blit(texte_requins, (10, 10))
        ecran.blit(texte_proies, (10, 50))
        
        # Afficher le nombre de chronons restants
        texte_chronons = police.render(f"Chronons restants : {chronon}", True, (255, 255, 255))
        ecran.blit(texte_chronons, (10, 90))
        
        # Mettre à jour l'affichage
        pygame.display.flip()
        
        # Limiter le nombre de frames par seconde
        horloge.tick(60)
        
        # Exécuter un cycle de simulation

        monde.executer_cycle()

        sleep(0.05)  # Pause pour ralentir la simulation
        
        if chronon == 0:
            lancer = False
            
        chronon -= 1

        
# Menu principal         
menu = pygame_menu.Menu(
    height=720,
    width=1280,
    title='Simulation Wa-tor',
    theme=themes.THEME_DARK
)

# Menu paramètres
menu2 = pygame_menu.Menu(
    height=720,
    width=1280,
    title='Paramètres',
    theme=themes.THEME_DARK
)

# Menu paramètres requins
menu3 = pygame_menu.Menu(
    height=720,
    width=1280,
    title='Paramètres requins',
    theme=themes.THEME_DARK
)

# Menu paramètres proies
menu4 = pygame_menu.Menu(
    height=720,
    width=1280,
    title='Paramètres proies',
    theme=themes.THEME_DARK
)

# Paramètres requins et proies
nb_vie_requins = menu3.add.range_slider('Points de vie :', default=12, range_values=(1,30), increment=1, value_format= lambda x: f"{x:.0f}")
temps_reprod_requins = menu3.add.range_slider('Temps de reproduction des requins :', default=12, range_values=(1,30), increment=1, value_format= lambda x: f"{x:.0f}")
vie_par_repas_requins = menu3.add.range_slider('Point de vie par repas :', default=1, range_values=(1,30), increment=1, value_format= lambda x: f"{x:.0f}")
temps_reprod_proies = menu4.add.range_slider('Temps de reproduction des proies :', default=4, range_values=(1,30), increment=1, value_format= lambda x: f"{x:.0f}")

# Paramètres du jeu
plein_ecran = menu.add.selector('Mode plein écran :', [('OUI', True), ('NON', False)], default=True)
resolution = menu.add.selector('Résolution :', [('1280x720', (1280, 720)), ('1920x1080', (1920, 1080))], default=0)
nb_requins = menu.add.range_slider('Nombre de requins :', default=400, range_values=(1,1000), increment=1, value_format= lambda x: f"{x:.0f}")
nb_proies = menu.add.range_slider('Nombre de proies :', default=600, range_values=(1,1000), increment=1, value_format= lambda x: f"{x:.0f}")
nb_chronons = menu.add.range_slider('Nombre de chronons :', default=1000, range_values=(1,10000), increment=1, value_format= lambda x: f"{x:.0f}")

# Ajout des boutons au menu
menu.add.button('Jouer', demarrer_jeu)
menu.add.button('Paramètres', action=menu2)
menu2.add.button('Paramètres requins', action=menu3)
menu2.add.button('Paramètres proies', action=menu4)
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
        menu.mainloop(ecran)
    
    if menu2.is_enabled():
        menu2.mainloop(ecran)
            
    pygame.display.flip()