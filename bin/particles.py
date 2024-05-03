import pygame as pg
from folder_gestion import import_folder

class Particle(pg.sprite.Sprite):
	def __init__(self,pos,type,animation_speed):
		super().__init__()
		self.frame_index = 0
		self.animation_speed = animation_speed
		if type == 'jump':
			self.frames = import_folder('graphics\character\particles\jump')
		if type == 'land':
			self.frames = import_folder('graphics\character\particles\land')
		if type == 'explosion':
			self.frames = import_folder('graphics\projectiles\explosion')
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center = (pos[0],pos[1]-5))

	def animation(self):
		self.frame_index += self.animation_speed
		if self.frame_index >= len(self.frames):
			self.kill()
		else:
			self.image = self.frames[int(self.frame_index)]

	def update(self,mouvement):
		self.animation()
		self.rect.x += mouvement[0]
		self.rect.y += mouvement[1]

