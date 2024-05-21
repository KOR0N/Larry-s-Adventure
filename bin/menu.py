import pygame as pg
from settings import *

overlay = pg.Surface((screen_width, screen_height), pg.SRCALPHA)
overlay.fill((0, 0, 0, 128))  # Remplissage en noir semi-transparent


# Initialisation des variables
x_rect = screen_width // 2 - 250  # Position initiale de l'élément central sur l'axe x
color = ("black")  # Couleur par défaut
anim_frame = 0  # Cadre initial de l'animation
anim_frame_speed = 0.1  # Vitesse de l'animation
run_particles = files_import('graphics/character/run')  # Importation des images d'animation de course
pos = (screen_width / 2 - 32, screen_height / 2 + 242)  # Position initiale du personnage
deplacement_terrain_speed = 2  # Vitesse de déplacement du terrain
deplacement_terrain = 0  # Position initiale du premier segment de terrain
deplacement_terrain_2 = 2920  # Position initiale du deuxième segment de terrain
delay_text = 0  # Compteur pour le délai d'affichage du texte

# Fonction pour afficher l'écran d'accueil
def home(screen):
    global anim_frame, anim_frame_speed, run_particles, deplacement_terrain, deplacement_terrain_2, deplacement_terrain_speed, delay_text
    
    # Déplacement des segments de terrain
    deplacement_terrain -= deplacement_terrain_speed
    deplacement_terrain_2 -= deplacement_terrain_speed
    delay_text += 1
    
    # Affichage de l'arrière-plan
    screen.blit(background_home, (0, 0))
    
    # Réinitialisation des positions des segments de terrain lorsqu'ils sortent de l'écran
    if deplacement_terrain < -2920:
        deplacement_terrain = deplacement_terrain_2 + 2920
    if deplacement_terrain_2 < -2920:
        deplacement_terrain_2 = 2920
    
    # Affichage des segments de terrain
    screen.blit(terrain_home, (deplacement_terrain, screen_height / 2))
    screen.blit(terrain_home, (deplacement_terrain_2, screen_height / 2))
    
    # Mise à jour du cadre d'animation
    anim_frame += anim_frame_speed
    if anim_frame >= len(run_particles):
        anim_frame = 0

    # Affichage de l'image courante de l'animation de course
    run_particle = run_particles[int(anim_frame)]
    screen.blit(run_particle, (pos[0], pos[1]))

    # Affichage des titres
    screen.blit(title_1, (screen_width - 180 * 7, 20))
    screen.blit(title_2, (screen_width - 180 * 6, 180))
    
    # Affichage du texte avec délai
    if delay_text > 100:
        screen.blit(ttp, (screen_width / 2 - 60, 450))

# Fonction pour afficher le menu principal
def menu_display(screen):
    for i in range(3):
        screen.blit(sign_level,(screen_width // 2 - 150,100+i*250))
    screen.blit(resume_txt, (screen_width // 2 - 90, 120))  # Affichage du texte "Resume"
    screen.blit(home_txt, (screen_width // 2 - 80, 370))  # Affichage du texte "Home"
    screen.blit(quit_txt, (screen_width // 2 - 60, 620))  # Affichage du texte "Quit"

# Fonction pour afficher l'écran de sélection de niveau
def select_level(screen):
    screen.fill("white")  # Remplissage de l'écran en blanc
    screen.blit(level_background, (0, 0))  # Affichage de l'arrière-plan des niveaux
    
    # Affichage des niveaux
    for a, i in enumerate(level_positions):
        if level_access[a] == 1:
            # Si le niveau est accessible, affichage du panneau de niveau accessible
            screen.blit(sign_level, (i[0], i[1]))
            title_level = normal_font.render("LEVEL " + str(a + 1), 1, color_level[a])
            screen.blit(title_level, (i[0] + 49, i[1] + 24))
        else:
            # Si le niveau est bloqué, affichage du panneau de niveau bloqué
            screen.blit(sign_level_blocked, (i[0], i[1]))
        
        # Affichage du titre du niveau
        title_level = normal_font.render("LEVEL " + str(a + 1), 1, 'WHITE')
        screen.blit(title_level, (i[0] + 50, i[1] + 25))
