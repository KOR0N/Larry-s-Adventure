import pygame as pg, sys
from settings import screen, Home_music, mouse
from game import Game

# Initialisation de l'horloge
clock = pg.time.Clock()

# Création de l'instance du jeu
game = Game(screen)

# Activation du menu
menu_activate = False

# Initialisation du module mixer pour la musique
pg.mixer.init()
pg.mixer.music.load(Home_music)
pg.mixer.music.play(1)

# Fonction de contrôle de la souris
def mouse_control(event):
    coordonnées = list(pg.mouse.get_pos())
    x = coordonnées[0]
    y = coordonnées[1]
    if event.type == pg.MOUSEBUTTONDOWN:
        if pg.mouse.get_pressed() == (1, 0, 0):
            return x, y, x, y
    return x, y, 0, 0

# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pg.event.get():
        # Récupération des coordonnées de la souris et des clics
        x, y, x_click, y_click = mouse_control(event)
        # Si l'événement est de type QUIT, quitter le jeu
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Exécution du jeu
    game.run(x, y, x_click, y_click, event)
    
    # Mise à jour de l'affichage
    pg.display.update()
    # Limite le nombre de frames par seconde à 60
    clock.tick(60)
