import pygame as pg
from settings import*
from level import*
from folder_gestion import import_folder

class Enemy(pg.sprite.Sprite):

    def __init__(self, pos, screen, solidity):
        super().__init__()
        
        self.screen = screen
        self.solidity = solidity
        self.type = 'type_1'
        self.direction = pg.math.Vector2(0,0)
        self.speed = 1
        self.sens = 1

        self.character_assets()
        self.status = 'run'
        self.frame = 0
        self.animation_speed = 0.075
        self.image = self.animations[self.status][self.frame]
        self.rect = self.image.get_rect(topleft=pos)
        
        self.vie = 50

        self.face_direction = True
        self.death = False

    def character_assets(self):
        self.character_path = 'graphics/enemies/'+self.type+'/'
        self.animations = {'run':[],'attack':[],'death':{}}

        for animation in self.animations.keys():
            full_path = self.character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animation(self):
        animation = self.animations[self.status]
        self.frame += self.animation_speed
        if self.frame >= len(animation):
            self.frame = 0
            if self.status == 'death':
                self.kill()
        
        self.image = animation[int(self.frame)]

        if self.sens < 0 :
            self.image = pg.transform.flip(self.image,True,False)


    def moove(self,world_mouvement):
        if self.status == 'run':
            self.direction.x = self.sens * self.speed
            self.rect.x += self.direction.x
        self.rect.x +=world_mouvement[0]
        self.rect.y += world_mouvement[1]
            
   
    def update(self,world_mouvement):
        self.animation()
        self.moove(world_mouvement)