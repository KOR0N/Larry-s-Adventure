import pygame as pg
from pygame import font,mixer
from win32api import GetSystemMetrics
from os import listdir

def files_import(path):
    animation_list = []
    for image_name in listdir(path):
        image = pg.image.load(path+'/'+image_name).convert_alpha()
        animation_list.append(image)

    return animation_list

level_1 = [
'                                                                                                                                                                        D                      ',                                                                                
'                                                                                                                                                                                              ',                                                                                   
'                                                                                                                                                                                              ',
'                                                              T                                   T  T                 T                                                                       ',
'                                                                                                                                                                   F                           ',
'  T                            T                                                                                                         T  T                     XXXXXXXXXX    ',
'                                                X   XXX     E                                               XX        C                                      C    XXXXXXXXXX    ',
'                                           XX            XXXXXXX                         XXX     XXXXXXE          EXXXXXXX     XXXX                        XXX    XXXXXXXXXX    ',
'    P       C                  E      XXX                XXXXXXX            C     XXX    XXX     XXXXXXXXXXXXXXXXXXXXXXXXX     XXXX                XXX            XXXXXXXXXX    ',
'XXXXXXXXXXXXXXXXX           XXXXXXX                      XXXXXXXXXXXX    XXXXX    XXX            XXXXXXXXXXXXXXXXXXXXXXXXX              XXXXXXX    XXX            XXXXXXXXXX    ',
'XXXXXXXXXXXXXXXXXXXX      XXXXXXXXXX             C       XXXXXXXXXXXX    XXXXX                   XXXXXXXXXXXXXXXXXXXXXXXXX              XXXXXXX                   XXXXXXXXXX    ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX                   XXXXXXXXXXXXXXXXXXXXXXXXX                                        XXXXXXXXXX    ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX                   XXXXXXXXXXXXXXXXXXXXXXXXX                                        XXXXXXXXXX    ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX                   XXXXXXXXXXXXXXXXXXXXXXXXX                                        XXXXXXXXXX    ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX                   XXXXXXXXXXXXXXXXXXXXXXXXX                                        XXXXXXXXXX    ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX                   XXXXXXXXXXXXXXXXXXXXXXXXX                                        XXXXXXXXXX    ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX                   XXXXXXXXXXXXXXXXXXXXXXXXX                                        XXXXXXXXXX    ',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXXXX                   XXXXXXXXXXXXXXXXXXXXXXXXX                                        XXXXXXXXXX    ',
]


level_2 = [
'                                                                                                               ',
'                                                                                               E  C    E          ',
'                                                                                    E      XXXXXXXXXXXXXXX                                                              D                    ',
'                                          TTT                                  XXXXXXXXXXXXXXXXXXXXXXXXXXX                                                                             ',
'                     X           XXXX                                   XXX    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                                   XXX                                  ',
'   T                                                        XXX     X          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX    XXX                             E                                    ',
'                XXX                           E    C                           XXXXXXXXXXXXXXXXXXXX                                            XXXXX     XXX       F                       ',
'                                        XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXXXXX     XXXX            XX               XXX              XXX      XXXXXXXXXX                        ',
' C  P            E                      XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXXX       XXXX                       E     XXX              XXX      XXXXXXXXXX                      ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXXX     XXXXXX                      XXX                     XXX      XXXXXXXXXX                          ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXX      XXXXXX    E       E         XXX                     XXX      XXXXXXXXXX          ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXXXXXXXXXXXXXX   XXXXXXXXXXXXXXXXXXXXXXXXXXX                            XXX      XXXXXXXXXX             ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                       XXXX               XXXXXXXXXXXXXXXXXXXXXXXXXXX                            XXX      XXXXXXXXXX                      ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                                        XXXXXXXXXXXXXXXXXXXXXXXXXXXXX                            XXX      XXXXXXXXXX       ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                                V       XXXXXXXXXXXXXXXXXXXXXXXXXXXXX                            XXX      XXXXXXXXXX       ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                            XXX      XXXXXXXXXX       ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                            XXX      XXXXXXXXXX       ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                            XXX      XXXXXXXXXX       ',
'XXXXXXXXXX    XXXXXXX    XX     XXXXX   XXXXXXXXXXXXXXXX                      XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX                            XXX      XXXXXXXXXX       ',
]


level_3 = [
'       V            T                          C                                                                                                                                                       ',
'      XXXXX                            XX     XXX       XXX                                                        T                                                                                                                      ',
'                X                 C                                                                                                                                                                                                           ',
'                                 XXXX           T       T                                                                                                                                                       ',
'                   XXXXX                                                                                              E       XX      XX                                D                                           ',
'   T                         XX  T                                XXX     X                             T           XXXXX     XX      XX                                                                                   ',
'                                                E      C      E                                T                    XXXXX                                                                                        ',
'                         C                      XXXXXXXXXXXXXXX                 X                               E C                         XX   T  T                                                      ',
'    P   C        E      XX       E        X     XXXXXXXXXXXXXXX                                                 XXX                                                F                                                    ',
'XXXXXXXXXX      XXX             XXXXX           XXXXXXXXXXXXXXX                              E   E       XXXX                                              XXC    XXXXXXXXXX    ',
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

level_4 = [
'                                                                                                                                  T                                            ',
'                                              E                                                                                                                                ',
'                                  C     XX    XXXX      XX                                  T                                              EC                                  ',
'                                 XXXX                                           C E                                                      XXXX            T              D      ',
'                                   T                                           XXXXX                                              XX                                           ',
'   T                         XX                              T                 XXXXX                                         T                    X                            ',
'                                                                         XX                XXXX                                        E                                       ',
'                                              XXX       XX       XXX     XX                XXXX      X     X      C                  XXX                 XXX       F           ',
'    P          XXXX     XXX     XXXXX         XXX      XXXE E E EXXXX                                            XXX      E    E                         XXX      XXXXXXXXXX   ',
'XXXXXXXXXX     XXXX             XXXXX                  XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
'XXXXXXXXXX                               XX            XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
'XXXXXXXXXX               E                             XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
'XXXXXXXXXX     XXXX     XXX     XXXXX                  XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
'XXXXXXXXXX     XXXX             XXXXX                  XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
'XXXXXXXXXX     XXXX             XXXXX                  XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
'XXXXXXXXXX     XXXX             XXXXX                  XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
'XXXXXXXXXX     XXXX             XXXXX                  XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
'XXXXXXXXXX     XXXX             XXXXX                  XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
'XXXXXXXXXX     XXXX             XXXXX                  XXXXXXXXXXXXXX                                                    XXXXXXXX                                 XXXXXXXXXX   ',
]

# def loose_screen(size):
#     screen.blit(loose_screen,())
tile_size = 64
screen_width = GetSystemMetrics (0)
screen_height = GetSystemMetrics (1)
pg.init()
screen = pg.display.set_mode((screen_width,screen_height))

mouse = pg.image.load('graphics/game_display/Cursor.png').convert_alpha()
cursor = pg.cursors.Cursor((0,0),mouse)
pg.mouse.set_cursor(cursor)

level_map = [level_1,level_2,level_3,level_4]
level_type = ['sky','sky','lava','lava']
level_access = [1,0,0,0]

#Settings Menu
# sign = pg.image.load("graphics\game_display\menu\sign3.png").convert_alpha()
background = pg.image.load("graphics/game_display/menu/backround_menu2.png").convert_alpha()
background = pg.transform.scale(background,(screen_width,screen_height))

#Home Menu
background_home = pg.image.load("graphics/terrain/sky/background.png")
terrain_home = pg.image.load("graphics/terrain/terrain_home.png").convert_alpha()

#Level Menu
sign_level = pg.image.load('graphics/game_display/level/sign.png')
sign_level_blocked = pg.image.load('graphics/game_display/level/sign_blocked.png')
level_background = pg.image.load('graphics/terrain/images.jpeg')
level_positions = [[screen_width//4 - 150, screen_height//4+80],[screen_width//4+100, screen_height//2 + 200],[screen_width//4 + 450, screen_height//4],[screen_width//4 + 750, screen_height//2 + 150]]
color_level = ['WHITE','WHITE','WHITE','WHITE']

#Text
little_font = font.Font('font/Playa.ttf',30)
normal_font = font.Font(None,60)
title_font = font.Font('font/3Dventure.ttf',160)
death_font = font.Font('font/Death.ttf',80)

resume_txt=normal_font.render("RESUME",1,("white"))
home_txt=normal_font.render("HOME",1,("white"))
quit_txt=normal_font.render("QUIT",1,("white"))

title_1 = title_font.render("LARRY'S",1,("yellow"))
title_2 = title_font.render("ADVENTURE",1,("yellow"))

ttp =  little_font.render("TAP TO PLAY",1,("white"))


#Music
Home_music = 'sounds/Home.mp3'
level_music = ['sounds/level_1.mp3','sounds/level_2.mp3','sounds/level_3.mp3','sounds/level_4.mp3']
game_over_sound = pg.mixer.Sound('sounds/game_over.mp3')
win_sound = pg.mixer.Sound('sounds/win.mp3')