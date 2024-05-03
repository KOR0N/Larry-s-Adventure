import pygame as pg

class Cell(pg.sprite.Sprite):
    def __init__(self, pos, type, solidity):
        super().__init__()
        if type == 't':
            self.image = pg.image.load("graphics/terrain/Block.png")
        elif type == 'tr':
            self.image= pg.image.load("graphics/terrain/Block tr.png")
        elif type == 'tl':
            self.image= pg.image.load("graphics/terrain/Block tl.png")
        elif type == 'r':
            self.image= pg.image.load("graphics/terrain/Block r.png")
        elif type == 'l':
            self.image= pg.image.load("graphics/terrain/Block l.png")
        elif type == 'c':
            self.image= pg.image.load("graphics/terrain/crate.png")
        elif type == 'T':
            self.image= pg.image.load("graphics/terrain/tree/sapin.png")
        elif type == 'D':
            self.image= pg.image.load("graphics/terrain/donjon_end.png")
        else:
            self.image = pg.image.load("graphics/terrain/Block b.png")
        # self.screen.blit(self.image,pos)
        # self.image = pg.Surface((size,size))
        # self.image.fill((50,50,50))
        # if solidity:
        self.rect = self.image.get_rect(topleft = pos)
        self.solidity = solidity
        # else:
        #     self.rect_x = pos[0]
        #     self.rect.y = pos[1]

    def update(self,screen,mouvement):
        self.rect.x += mouvement[0]
        self.rect.y += mouvement[1]
        # screen.blit(self.image,(self.rect.x,self.rect.y))