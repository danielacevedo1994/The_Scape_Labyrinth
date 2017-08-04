import time


segundos = 0
minutos = 0
##opcion = True
##def timer():
##    global s
##    global m
##    global opcion
##    while opcion == True:
##        print(str(m)+":"+str(s))
##        s=s+1
##        if(s>=60):
##            s=0
##            m=m+1
##
##        if s == 1:
##            opcion = False
##            
##        time.sleep(1)


def tiempo():
    global segundos
    global minutos
    segundos = int(segundos)
    if segundos == 59:
        segundos = 0
        minutos += 1
        return tiempo()
    else:
        segundos += 1
        time.sleep(1)
        return tiempo()

def Reloj():
    fuente = pygame.font.Font(None, 20)
    Reloj = str("Tiempo "+str(minutos)+":"+str(segundos))
    mensaje = fuente.render(Reloj, 1, (255, 255, 255))
    ventana.blit(mensaje, (200, 10))
