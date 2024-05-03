import pygame as pg, sys
from settings import screen_width,screen_height,screen,Home_music
from game import Game
    
clock = pg.time.Clock()
game = Game(screen)

menu_activate = False
pg.mixer.music.load(Home_music)
pg.mixer.music.play(1)

def mouse_control(event):
    coordonnées = list(pg.mouse.get_pos())
    x=coordonnées[0]
    y=coordonnées[1]
    if event.type == pg.MOUSEBUTTONDOWN :
        if pg.mouse.get_pressed()==(1,0,0):
            x_click = x
            y_click = y
    else:
        x_click = -1
        y_click = -1
    return x,y,x_click,y_click

while True:
    for event in pg.event.get():
        x,y,x_click,y_click = mouse_control(event)
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    game.run(x,y,x_click,y_click,event)
    
    pg.display.update()
    clock.tick(60)