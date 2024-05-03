import pygame as pg
from pygame import font
from win32api import GetSystemMetrics

level_1 = [
'                                                                               ',                                                                                
'                                                                               ',                                                                                   
'                                                                               ',
'                                                                               ',
'                                                                               ',
'  T                            T                                                 ',
'                                                X   XXX     E                      ',
'                                           XX            XXXXXXX                   ',
'    P       C                  E      XXX                XXXXXXX            C      ',
'XXXXXXXXXXXXXXXXX           XXXXXXX                      XXXXXXXXXXXX    XXXXX      ',
'XXXXXXXXXXXXXXXXXXXX      XXXXXXXXXX             C       XXXXXXXXXXXX    XXXXX          ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX         ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX              ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX         ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX          ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX          ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX             ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX             ',
]


level_2 = [
'                                                                                                               ',
'                                                                                                  C               ',
'                                                                                           XXXXXXXXXXXXXXX               ',
'                                          TTT                                  XXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'                     X           XXXX                                   XXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                             ',
'   T                                                        XXX     X          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXX                     ',
'                XXX                               C                            XXXXXXXXXXXXXXXXXXXX                                  ',
'                                        XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXXXXX     XXXX            XX                 ',
' C  P            E                      XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXXX       XXXX                               ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXXX     XXXXXX                                ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXX      XXXXXX                             ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXX                          ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXX               XXXXXXXXXXXXXXXXXXXXXXXXXXX                                   ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                        ',
]

level_4 = [
'                    T                                                                                                                                                                                 ',
'      XXXXX                            XX     XXX XXXXX  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXT                                                                                                                      ',
'                X                                                                                                                                                                                                                             ',
'                                 XXXX                                                                                                                                                                            ',
'                   XXXXX                                                                                              E       XX      XX                                D                                           ',
'   T                         XX                                   XXX     X                                         XXXXX     XX      XX                                                                                   ',
'                                                E      C      E                                 T                                                                                                                ',
'                         C                      XXXXXXXXXXXXXXX                 X                               E C                         XX   T  T                                                      ',
' C  P            E      XX                X     XXXXXXXXXXXXXXX                                                 XXX                                                F                                                    ',
'XXXXXXXXXX      XXX             XXXXX           XXXXXXXXXXXXXXX                              E   E       XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    ',
'XXXXXXXXXX                      XXXXX           XXXXXXXXXXXXXXX                      X      XXXXXXX     XXXXXX                                  E    E     XXX    XXXXXXXXXX                            ',
'XXXXXXXXXX                      XXXXX           XXXXXXXXXXXXXXX                             XXXXXXX     XXXXXX                                  XXXXXX            XXXXXXXXXX                             ',
'XXXXXXXXXX                      XXXXX           XXXXXXXXXXXXXXX                                         XXXXXX                                  XXXXXX            XXXXXXXXXX                               ',
'XXXXXXXXXX                      XXXXX           XXXXXXXXXXXXXXX                                         XXXXXX                                  XXXXXX            XXXXXXXXXX                              ',
'XXXXXXXXXX                      XXXXX           XXXXXXXXXXXXXXX                                         XXXXXX                                  XXXXXX            XXXXXXXXXX                                ',
'XXXXXXXXXX                      XXXXX           XXXXXXXXXXXXXXX                                         XXXXXX                                  XXXXXX            XXXXXXXXXX                                ',
'XXXXXXXXXX                      XXXXX           XXXXXXXXXXXXXXX                                         XXXXXX                                  XXXXXX            XXXXXXXXXX                                    ',
'XXXXXXXXXX                      XXXXX           XXXXXXXXXXXXXXX                                         XXXXXX                                  XXXXXX            XXXXXXXXXX                                 ',
'XXXXXXXXXX                      XXXXX           XXXXXXXXXXXXXXX                                         XXXXXX                                  XXXXXX            XXXXXXXXXX                              ',
]


# def loose_screen(size):
#     screen.blit(loose_screen,())

level_map = [level_1,level_2,level_4]

tile_size = 64
screen_width = GetSystemMetrics (0)
screen_height = GetSystemMetrics (1)

pg.init()
screen = pg.display.set_mode((screen_width,screen_height))

#Settings Menu
# sign = pg.image.load("graphics\game_display\menu\sign3.png").convert_alpha()
background = pg.image.load("graphics/game_display/menu/backround_menu2.png").convert_alpha()
background = pg.transform.scale(background,(screen_width,screen_height))

#Home Menu
background_home = pg.image.load("graphics/terrain/background_test.png")
terrain_home = pg.image.load("graphics/terrain/terrain_home.png").convert_alpha()

#Level Menu
button_level = pg.image.load('graphics/game_display/level/sign.png')
level_background = pg.image.load('graphics/terrain/images.jpeg')
level_positions = [[screen_width//4 - 150, screen_height//4+80],[screen_width//4+100, screen_height//2 + 200],[screen_width//4 + 450, screen_height//4],[screen_width//4 + 750, screen_height//2 + 150]]
color_level = ['WHITE','WHITE','WHITE','WHITE']

#Text
little_font = font.Font('font/Playa.ttf',30)
normal_font = font.Font(None,60)
title_font = font.Font('font/3Dventure.ttf',160)
death_font = font.Font('font/Death.ttf',80)

resume_txt=normal_font.render("RESUME",1,("white"))
settings_txt=normal_font.render("SETTINGS",1,("white"))
quit_txt=normal_font.render("QUIT",1,("white"))

title_1 = title_font.render("LARRY'S",1,("yellow"))
title_2 = title_font.render("ADVENTURE",1,("yellow"))

ttp =  little_font.render("TAP TO PLAY",1,("white"))

loose_txt = death_font.render("YOU LOOSE",1,("white"))

size_finish_txt = 0
pos_finish_txt = [screen_width/2,screen_height/2]

#Musique
Home_music = 'sounds/Home.mp3'
level_music = ['sounds/level_1.mp3','sounds/level_1.mp3','sounds/level_1.mp3','sounds/level_1.mp3']