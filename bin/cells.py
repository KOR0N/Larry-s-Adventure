import pygame as pg

class Cell(pg.sprite.Sprite):
    def __init__(self, pos, type, solidity, level_type):
        super().__init__()

        # Charge l'image appropriée pour le type de cellule
        if type == 'C':
            self.image = pg.image.load("graphics/terrain/crate.png")
        elif type == 'T':
            self.image = pg.image.load("graphics/terrain/" + level_type + "/tree/sapin.png")
        elif type == 'D':
            self.image = pg.image.load("graphics/terrain/donjon_end.png")
        else:
            self.image = pg.image.load("graphics/terrain/" + level_type + "/Block " + type + ".png")

        # Définir le rectangle de la cellule pour la positionner
        self.rect = self.image.get_rect(topleft=pos)
        
        # Définir si la cellule est solide ou non
        self.solidity = solidity
        
    def update(self, screen, mouvement):
        # Met à jour la position de la cellule en fonction du mouvement de la caméra
        self.rect.x += mouvement[0]
        self.rect.y += mouvement[1]
