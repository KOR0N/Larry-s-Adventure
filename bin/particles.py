import pygame as pg
from settings import files_import

class Particle(pg.sprite.Sprite):
    def __init__(self, pos, type, animation_speed):
        super().__init__()

        # Initialisation de l'index de l'image et de la vitesse d'animation
        self.frame_index = 0
        self.animation_speed = animation_speed

        # Chargement des images appropriées en fonction du type de particule
        if type == 'jump':
            self.frames = files_import('graphics\character\particles\jump')
        elif type == 'land':
            self.frames = files_import('graphics\character\particles\land')
        elif type == 'explosion':
            self.frames = files_import('graphics\projectiles\explosion')

        # Définition de l'image initiale et de son rectangle
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center=(pos[0], pos[1] - 5))

    def animation(self):
        # Animation : incrémentation de l'index de l'image
        self.frame_index += self.animation_speed

        # Vérification si l'index dépasse la longueur des images
        if self.frame_index >= len(self.frames):
            # Si oui, supprimer la particule
            self.kill()
        else:
            # Sinon, mettre à jour l'image
            self.image = self.frames[int(self.frame_index)]

    def update(self, movement):
        # Appel de la méthode d'animation
        self.animation()

        # Mise à jour de la position de la particule en fonction du mouvement
        self.rect.x += movement[0]
        self.rect.y += movement[1]
