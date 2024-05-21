import pygame as pg
from settings import*
from level import*

class Enemy(pg.sprite.Sprite):
    # Classe représentant un ennemi dans le jeu, héritant de la classe Sprite de Pygame
    
    def __init__(self, pos, screen, solidity, level_type):
        super().__init__()
        # Initialisation des attributs de l'ennemi
        self.screen = screen
        self.solidity = solidity
        self.type = 'type_1'  # Type de l'ennemi, peut être modifié pour différents types d'ennemis
        self.direction = pg.math.Vector2(0, 0)  # Direction du mouvement de l'ennemi
        self.speed = 1  # Vitesse de l'ennemi
        self.sens = 1  # Sens de déplacement (1 pour droite, -1 pour gauche)

        # Chargement des assets du personnage en fonction du type de niveau
        self.character_assets(level_type)
        self.status = 'run'  # Statut initial de l'ennemi (peut être 'run', 'attack', 'death')
        self.frame = 0  # Cadre actuel de l'animation
        self.animation_speed = 0.075  # Vitesse de l'animation
        self.image = self.animations[self.status][self.frame]  # Image actuelle de l'ennemi
        self.rect = self.image.get_rect(topleft=pos)  # Rectangle de position de l'ennemi
        
        self.vie = 50  # Points de vie de l'ennemi

        self.face_direction = True  # Direction du regard de l'ennemi (True pour droite, False pour gauche)
        self.death = False  # Indicateur de mort de l'ennemi

    def character_assets(self, level_type):
        # Chargement des animations du personnage en fonction du type de niveau
        self.character_path = 'graphics/enemies/' + self.type + '/' + level_type + "/"
        self.animations = {'run': [], 'attack': [], 'death': []}

        # Chargement des fichiers d'animation pour chaque action
        for animation in self.animations.keys():
            full_path = self.character_path + animation
            self.animations[animation] = files_import(full_path)

    def animation(self):
        # Gestion de l'animation de l'ennemi
        animation = self.animations[self.status]
        self.frame += self.animation_speed
        if self.frame >= len(animation):
            self.frame = 0
            if self.status == 'death':
                self.kill()  # Supprime l'ennemi du groupe de sprites si son statut est 'death'
        
        self.image = animation[int(self.frame)]

        # Inverse l'image si l'ennemi change de direction
        if self.sens < 0:
            self.image = pg.transform.flip(self.image, True, False)

    def moove(self, world_mouvement):
        # Gestion du mouvement de l'ennemi
        if self.status == 'run':
            self.direction.x = self.sens * self.speed
            self.rect.x += self.direction.x
        # Applique le mouvement du monde (par ex. scrolling de l'écran)
        self.rect.x += world_mouvement[0]
        self.rect.y += world_mouvement[1]
   
    def update(self, world_mouvement):
        # Mise à jour de l'ennemi (animation et mouvement)
        self.animation()
        self.moove(world_mouvement)
