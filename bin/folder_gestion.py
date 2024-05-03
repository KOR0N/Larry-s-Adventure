from os import listdir
import pygame as pg

def import_folder(path):
    animation_list = []
    for image_name in listdir(path):
        image = pg.image.load(path+'/'+image_name).convert_alpha()
        animation_list.append(image)

    return animation_list