#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Modulos
import pygame
import sys
from cosas import *
from cosas import grid
from pygame.locals import *

grid = grid()

class Heroe(pygame.sprite.Sprite):
    def __init__(self, posx, posy, nom_heroe):
        self.imagen = pygame.image.load(nom_heroe)
        self.imagen.set_clip(pygame.Rect(0,0,32,32))
        self.parte = self.imagen.subsurface(self.imagen.get_clip())
        self.rect = self.parte.get_rect()
        self.rect.inflate_ip(-5,-10)
        self.rect.top = posy
        self.rect.left = posx
        self.frame =  0
        self.left_states = { 0: (0, 32, 32, 32), 1: (32, 32, 32, 32), 2: (64, 32, 32, 32) }
        self.right_states = { 0: (0, 64, 32, 32), 1: (32, 64, 32, 32), 2: (64, 64, 32, 32) }
        self.up_states = { 0: (0, 96, 32, 32), 1: (32, 96, 32, 32), 2: (64, 96, 32, 32) }
        self.down_states = { 0: (0, 0, 32, 32), 1: (32, 0, 32, 32), 2: (64, 0, 32, 32) }
        self.pasos = pygame.mixer.Sound("golpe.mp3")
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.imagen.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.imagen.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    def update(self, direccion):
        aux_y = int(self.rect.y/32)
        aux_x = int(self.rect.x/32)
        if direccion == 'left':
            aux_x = (int((self.rect.x/32)))-1
            self.clip(self.left_states[0])
            if self.rect.x >= 0:
                print("RETORNO " +  str(grid[aux_x][aux_y]))
                if grid[aux_x][aux_y] == 0:
                    self.rect.x -= 32
                    self.clip(self.left_states)
        if direccion == 'right':
            aux_x = (int((self.rect.x/32)))+1
            self.clip(self.right_states[0])
            if self.rect.x <= 1152:
                if grid[aux_x][aux_y] == 0:
                    self.rect.x += 32
                    self.clip(self.right_states)
        if direccion == 'up':
            aux_y = (int((self.rect.y/32)))-1
            self.clip(self.up_states[1])
            if self.rect.y >= 0:
                if grid[aux_x][aux_y] == 0:
                    self.rect.y -= 32
                    self.clip(self.up_states)
        if direccion == 'down':
            aux_y = (int((self.rect.y/32)))+1
            self.clip(self.down_states[1])
            if self.rect.y <= 1152:
                if grid[aux_x][aux_y] == 0:
                    self.rect.y += 32
                    self.clip(self.down_states)
    def colisiona_con(self, enemigo):
        print("Colision: "+str(self.rect.colliderect(enemigo.rect)))
        return self.rect.colliderect(enemigo.rect)
                    
##        if pygame.sprite.collide_rect(self, pala_jug):
##            self.speed[0] = -self.speed[0]
##            self.rect.centerx += self.speed[0] * time
##        if direccion == 'stand_left':
##            self.clip(self.left_states[0])
##        if direccion == 'stand_right':
##            self.clip(self.right_states[0])
##        if direccion == 'stand_up':
##            self.clip(self.up_states[1])
##        if direccion == 'stand_down':
##            self.clip(self.down_states[1])
        self.parte = self.imagen.subsurface(self.imagen.get_clip())
        print("x: "+str(self.rect.x/32)+"y: "+str(self.rect.y/32))
        print(grid[int(self.rect.x/32)][int(self.rect.y/32)])
    def teclado(self, event):
        if event.type == pygame.KEYDOWN:
            self.pasos.play(-1)
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
##        elif event.type == pygame.KEYUP:  
##            if event.key == pygame.K_LEFT:
##                self.update('stand_left')            
##            if event.key == pygame.K_RIGHT:
##                self.update('stand_right')
##            if event.key == pygame.K_UP:
##                self.update('stand_up')
##            if event.key == pygame.K_DOWN:
##                self.update('stand_down')
