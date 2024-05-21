import pygame as pg
from pygame.gfxdraw import*
from particles import Particle  # Importe la classe Particle depuis le module particles.py

class Fire_balls(pg.sprite.Sprite):
    def __init__(self, screen, pos, player_direction, speed_mult):
        super().__init__()

        # Initialisation des attributs de la balle de feu
        self.screen = screen
        self.bounce = 3
        self.gravity = 1
        
        # Définition de la vitesse en fonction de la direction du joueur
        if player_direction:
            self.speed = 8 * speed_mult
        else:
            self.speed = -8 * speed_mult
        
        # Initialisation de l'état de l'explosion
        self.explose = False

        # Initialisation du vecteur de direction et de la position
        self.direction = pg.math.Vector2(0, 0)
        self.direction.y = 2
        
        # Chargement des images de la balle de feu et de son explosion
        self.image = pg.image.load('graphics/projectiles/fire_ball.png').convert_alpha()
        self.image_death = pg.image.load('graphics/projectiles/fire_ball_death.png').convert_alpha()
        self.rect = self.image.get_rect(center=(pos[0], pos[1]))

        # Groupe pour les particules d'explosion
        self.explosion_particles = pg.sprite.GroupSingle()

    def animation(self):
        # Animation de l'explosion de la balle de feu
        if self.bounce <= 0 and not(self.explose):
            image_size = self.image.get_size()
            explosion_particle = Particle((self.rect.x + image_size[0] / 2, self.rect.y + image_size[1] / 2 + 5), 'explosion', 0.4)
            self.explosion_particles.add(explosion_particle)
            self.explose = True
            self.image = self.image_death
        if not(len(self.explosion_particles)) and self.explose:
            self.kill()

    def mouvement(self, world_mouvement):
        # Mouvement de la balle de feu
        self.direction.y += (1 / 2) * self.gravity
        self.rect.y += world_mouvement[1]

        self.direction.x = world_mouvement[0]
        self.direction.x += self.speed
        self.speed /= 1.002

    def update(self, world_mouvement):
        # Mise à jour de la balle de feu
        self.animation()
        if self.bounce > 0:
            self.mouvement(world_mouvement)
        self.explosion_particles.draw(self.screen)
        self.explosion_particles.update(world_mouvement)
