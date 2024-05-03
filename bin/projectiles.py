import pygame as pg
from pygame.gfxdraw import*
from particles import Particle

class Fire_balls(pg.sprite.Sprite):
    def __init__(self,screen,pos,player_direction):
        super().__init__()
        self.screen = screen 
        self.bounce = 3
        self.gravity = 1
        if player_direction:
            self.speed = 14
        else:
            self.speed = -14
        self.explose = False

        self.direction = pg.math.Vector2(0,0)
        self.direction.y = 2
        
        self.image = pg.image.load('graphics/projectiles/fire_ball.png').convert_alpha()
        self.image_death = pg.image.load('graphics/projectiles/fire_ball_death.png').convert_alpha()
        self.rect = self.image.get_rect(center = (pos[0],pos[1]))

        self.explosion_particles = pg.sprite.GroupSingle()

    def animation(self):
        if self.bounce <= 0 and not(self.explose):
            image_size = self.image.get_size()
            explosion_particle = Particle((self.rect.x+image_size[0]/2,self.rect.y+image_size[1]/2+5),'explosion',0.4)
            self.explosion_particles.add(explosion_particle)
            self.explose = True
            self.image = self.image_death 
            # self.kill()
        if not(len(self.explosion_particles)) and self.explose:
            self.kill()

    def mouvement(self,world_mouvement):
        self.direction.y += (1/2)*self.gravity*2/3
        self.rect.y +=  world_mouvement[1]

        self.direction.x = world_mouvement[0]
        self.direction.x += self.speed
        self.speed /= 1.002


    def update(self,world_mouvement):
        self.animation()
        if self.bounce > 0:
            self.mouvement(world_mouvement)
        self.explosion_particles.draw(self.screen)
        self.explosion_particles.update(world_mouvement)