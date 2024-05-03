import pygame as pg
from settings import*
from folder_gestion import import_folder
# color = (80,80,80)
# couleur = pg.Color(0,0,0,a=120)
x_rect = screen_width//2 - 250
color  = ("black")
anim_frame = 0
anim_frame_speed = 0.1
run_particles = import_folder('graphics/character_2/run')
pos = (screen_width/2-32,screen_height/2 +242)
deplacement_terrain_speed = 2
deplacement_terrain = 0
deplacement_terrain_2 = 2920
delay_text = 0

def home(screen):
    global anim_frame,anim_frame_speed,run_particles,deplacement_terrain,deplacement_terrain_2,deplacement_terrain_speed,delay_text
    deplacement_terrain -= deplacement_terrain_speed
    deplacement_terrain_2 -= deplacement_terrain_speed
    delay_text+=1
    screen.blit(background_home,(0,0))
    if deplacement_terrain < -2920:
        deplacement_terrain = deplacement_terrain_2+ 2920
    if deplacement_terrain_2 < -2920:
        deplacement_terrain_2 = 2920
    screen.blit(terrain_home,(deplacement_terrain,screen_height/2))
    screen.blit(terrain_home,(deplacement_terrain_2,screen_height/2))
    anim_frame += anim_frame_speed
    if anim_frame >= len(run_particles):
        anim_frame = 0

    run_particle = run_particles[int(anim_frame)]
    screen.blit(run_particle,(pos[0],pos[1]))

    screen.blit(title_1,(screen_width-180*7,20))
    screen.blit(title_2,(screen_width-180*6,180))
    if delay_text > 100:
        screen.blit(ttp,(screen_width/2-100,450))

def menu_display(screen):
    screen.blit(background,(0,0))
    # for i in range(3):
        # screen.blit(sign,(screen_width//2 - 405/2,i*220+50))
    screen.blit(resume_txt,(screen_width//2 - 90,150))
    screen.blit(settings_txt,(screen_width//2 - 100,150+220))
    screen.blit(quit_txt,(screen_width//2 - 60,150+440))

def setting_display(screen):
    screen.blit(background,(0,0))

def select_level(screen):
    screen.fill("white")
    screen.blit(level_background,(0,0))
    for a,i in enumerate(level_positions):
        screen.blit(button_level,(i[0],i[1]))
        title_level = normal_font.render("LEVEL "+str(a+1),1,color_level[a])
        screen.blit(title_level,(i[0]+49,i[1]+24))
        title_level = normal_font.render("LEVEL "+str(a+1),1,'WHITE')
        screen.blit(title_level,(i[0]+50,i[1]+25))

    # pg.draw.rect(screen, color, pg.Rect((screen_width//4 + 450), (screen_height//4), 200, 70))
    # pg.draw.rect(screen, color, pg.Rect((screen_width//4+100), (screen_height//2 + 200), 200, 70))
    # pg.draw.rect(screen, color, pg.Rect((screen_width//4 - 150), (screen_height//4+80), 200, 70))
    # pg.draw.rect(screen, color, pg.Rect((screen_width//4 + 750), (screen_height//2 + 150), 200, 70))

# def mouse_control():
#     pass