import pygame as pg, sys
from settings import *
from level import Level
from menu import*

class Game:
    def __init__(self, screen):
        # Initialisation de l'écran et des variables de jeu
        self.screen = screen
        self.home_menu = True
        self.level_menu = False
        self.menu_activated = False
        self.key_pressed = False
        self.level_choice = 0

    def menu_settings(self):
        # Gestion des touches pour le menu
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE] and self.key_pressed == False:
            # Toggle du menu
            self.menu_activated = not self.menu_activated
            self.key_pressed = True
        elif not keys[pg.K_ESCAPE]:
            self.key_pressed = False

    def mouse_control(self, x, y, x_click, y_click, event): 
        # Gestion des événements de souris
        keys = pg.key.get_pressed()

        if self.home_menu:
            # Menu principal
            if (x_click > 0 or event.type == pg.KEYDOWN) and not(keys[pg.K_ESCAPE]):
                self.home_menu = False
                self.level_menu = True
        
        elif self.level_menu:
            for a,i in enumerate(level_positions):
                if i[0]<x<i[0]+300 and i[1]<y<i[1]+99:
                    color_level[a] = 'WHITE'
                    if x_click>0 and level_access[a] == 1:
                        self.level = Level(self.screen,a)
                        self.level_menu = False
                else:
                    color_level[a] = 'BLACK'

            if keys[pg.K_ESCAPE]:
                self.level_menu = False
                self.home_menu = True
        
        elif self.menu_activated:
            if x_click>screen_width//2 - 345/2 and x_click<screen_width//2 + 315/2 and y_click>110 and y_click<228:
                self.menu_activated = False
            if x_click>screen_width//2 - 345/2 and x_click<screen_width//2 + 315/2 and y_click>110+220 and y_click<228+220:
                self.level_menu = True
                del self.level
                pg.mixer.music.load(Home_music)
                pg.mixer.music.play(1)
                self.menu_activated = False
            if x_click>screen_width//2 - 345/2 and x_click<screen_width//2 + 315/2 and y_click>110+440 and y_click<228+440:
                pg.quit()
        
        else:
            if self.level.win == True :
                if x_click or event.type == pg.KEYDOWN:
                    del self.level
                    self.level_menu = True
                    pg.mixer.music.load(Home_music)
                    pg.mixer.music.play(1)
            elif self.level.loose_state == True:
                if (x_click>0 or event.type == pg.KEYDOWN) and not(keys[pg.K_ESCAPE]):
                    del self.level
                    self.level_menu = True
                    pg.mixer.music.load(Home_music)
                    pg.mixer.music.play(1)

    def run(self, x_mouse, y_mouse, x_click, y_click, event):
        # Boucle de jeu principale
        if self.home_menu:
            # Affichage du menu principal
            home(self.screen)
        elif self.level_menu:
            # Affichage du menu des niveaux
            select_level(self.screen)
        elif self.menu_activated:
            # Affichage du menu et gestion des touches
            menu_display(self.screen)
            self.menu_settings()
        else:
            # Exécution du niveau en cours
            self.level.run()
            self.menu_settings()
        self.mouse_control(x_mouse, y_mouse, x_click, y_click, event)
        