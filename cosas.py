#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Modulos
import pygame
from pygame.locals import *
from reloj import *
def grid():

    grid = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1],
        [1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,1,1,0,0,0,1,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
        [1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1],
        [1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,1,1,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,1],
        [1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
        [1,0,1,1,0,1,1,1,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,1,1,1,0,1,1,0,1],
        [1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,0,0,0,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,1,0,0,0,0,0,0,0,1],
        [1,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
        [1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1],
        [1,0,1,1,0,1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,1],
        [1,1,1,1,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,1,1,1,1,0,1,1,0,1,1,0,1],
        [1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1],
        [1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1],
        [1,0,0,0,0,1,1,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    return grid

imagenes = ["brick_brown0.png", "brick_dark0.png", "play.png"]
matriz = grid()
class cosas(pygame.sprite.Sprite):
    def __init__(self, index, trans):
        pygame.sprite.Sprite.__init__(self)
        index = int(index)
        self.image = load_image(imagenes[index], trans)
        self.rect=self.image.get_rect()
        
def load_image(filename, transparent = False):
    try: image =pygame.image.load(filename)
    except pygame.error, message:
        raise SystemExit, message
    image =image.convert()
    if transparent:
        color = image.get_at((0,0))
        image.set_colorkey(color, RLEACCEL)
    return image
def mapa(muro, piso, ventana):
    for fila in range(36):
        for columna in range(36):
            if matriz[fila][columna] == 1:
                muro.rect.y = 32*columna
                muro.rect.x = 32*fila
                ventana.blit(muro.image, muro.rect)
    for fila in range(36):
        for columna in range(36):
            if matriz[fila][columna] == 0:
                piso.rect.y = 32*columna
                piso.rect.x = 32*fila
                ventana.blit(piso.image, piso.rect)

