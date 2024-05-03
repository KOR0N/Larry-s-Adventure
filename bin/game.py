import pygame as pg, sys
from settings import *
from level import Level
from menu import*
# x,y = 0,0
class Game:
    def __init__(self,screen):
        self.screen = screen
        self.home_menu = True
        self.level_menu = False
        self.menu_activated = False
        self.settings_activated = False
        self.key_pressed = False
        self.level_choice = 0

    def menu_settings(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_ESCAPE] and self.key_pressed == False:
            self.menu_activated = not self.menu_activated
            self.key_pressed = True
            self.settings_activated = False
        elif not keys[pg.K_ESCAPE]:
            self.key_pressed = False

    def mouse_control(self,x,y,x_click,y_click,event):
        keys = pg.key.get_pressed()
        if self.home_menu:
            if (x_click>0 or event.type == pg.KEYDOWN) and not(keys[pg.K_ESCAPE]):
                self.home_menu = False
                self.level_menu = True

        elif self.level_menu:
            for a,i in enumerate(level_positions):
                if i[0]<x<i[0]+300 and i[1]<y<i[1]+99:
                    color_level[a] = 'WHITE'
                    if x_click>0:
                        self.level = Level(self.screen,a)
                        self.level_menu = False

                else:
                    color_level[a] = 'BLACK'
            
            if keys[pg.K_ESCAPE]:
                self.level_menu = False
                self.home_menu = True
            # if (x>screen_width//4 + 450 and x<screen_width//4 + 450+200 and y>screen_height//4 and y<screen_height//4+70) or (x>screen_width//4+100 and x<screen_width//4+100 + 200 and y>screen_height//2 + 200 and y<screen_height//2 + 200+70) or (x>screen_width//4 - 150 and x<screen_width//4 + 50 and y>screen_height//4+80 and y<screen_height//4+150) or (x>screen_width//4 + 750 and x<screen_width//4 + 950 and y>screen_height//2 + 150 and y<screen_height//2 + 220):


        elif self.menu_activated:
            if x_click>screen_width//2 - 345/2 and x_click<screen_width//2 + 315/2 and y_click>110 and y_click<228:
                self.menu_activated = False
            if x_click>screen_width//2 - 345/2 and x_click<screen_width//2 + 315/2 and y_click>110+220 and y_click<228+220:
                self.settings_activated = True
                self.menu_activated = False
            if x_click>screen_width//2 - 345/2 and x_click<screen_width//2 + 315/2 and y_click>110+440 and y_click<228+440:
                pg.quit()
                sys.exit() #Il faudrait modifier pour faire un bouton Menu à la place
        
        elif self.settings_activated:
            pass
        
        else:
            if self.level.loose_state == True:
                    if (x_click>0 or event.type == pg.KEYDOWN) and not(keys[pg.K_ESCAPE]):
                        del self.level
                        self.level_menu = True
                        pg.mixer.music.load(Home_music)
                        pg.mixer.music.play(1)
        # x_click,y_click = 0,0

    def run(self,x_mouse,y_mouse,x_click,y_click,event):
        if self.home_menu:
            home(self.screen)
        elif self.level_menu:
            select_level(self.screen)
        elif self.menu_activated:
            menu_display(self.screen)
            self.menu_settings()
        elif self.settings_activated:
            setting_display(self.screen)
        else:
            self.level.run()
            self.menu_settings()
        self.mouse_control(x_mouse,y_mouse,x_click,y_click,event)
        