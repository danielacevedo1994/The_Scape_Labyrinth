#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Modulos
import pygame
import sys
from pygame.locals import *
from cosas import *
from Heroe import *
from reloj import *
milseg = 0
segundos = 0
minutos = 0
# Variables
WIDTH = 1152
HEIGHT = 1152
##Funciones Principal
def main():
    ventana = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Prueba2")
    trans = False
    salir = True
    opcion = False
    muro = cosas(0, trans)
    piso = cosas(1, trans)
    trans = True
    play = cosas(2, trans)
    reloj = pygame.time.Clock()
    player = Heroe(32,32, "heroe2.png")
    opcion = False
    global timepo_jugado
    fuente = pygame.font.Font(None, 20)
    enemigo = Heroe (32, 128, "heroe.png")
####    pygame.mixer.music.load("fondo.mp3")
##    pygame.mixer.music.play(-1)
##    hilo = threading.Thread(target = tiempo, args = ())
##    hilo.start()
    while salir == True:
        for event in pygame.event.get():
            if event.type==QUIT:
                salir = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                if pos[0]>=80 and pos[0]<=275 and pos[1]>=320 and pos[1]<=400:
                    opcion = True
        if opcion == False:
            play.rect.y = 320
            play.rect.x = 80
            ventana.blit(play.image, play.rect)
        else:
##            pygame.mixer.music.stop()
            global milseg
            global segundos
            global minutos
            milseg = int(milseg)
            if milseg == 20:
                milseg = 0
                segundos += 1
            if segundos == 59:
                segundos = 0
                minutos += 1
            else:
                milseg += 1
            Reloj = str("Tiempo "+str(minutos)+":"+str(segundos))
            print(Reloj)
            mensaje = fuente.render(Reloj, 1, (255, 255, 255))
            mapa(muro, piso, ventana)
            player.teclado(event)
            enemigo.teclado(event)
            ventana.blit(mensaje, (0, 0))
            ventana.blit(player.parte,player.rect)
            ventana.blit(enemigo.parte,enemigo.rect)
            player.colisiona_con(enemigo)
            reloj.tick(20)
        pygame.display.flip()
    pygame.quit()

if __name__=='__main__':
    pygame.init()
    main()
    
