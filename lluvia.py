#%%
"""
Created on Sat May  2 17:58:31 2020

@author: Bull teacher
"""
import pygame
import numpy as np
import random


ANCHO = 540
ALTO = 650
gravedad=9.8
Tamaño=random.randrange(200,500)
print(Tamaño)
fps=60
## Adicional
puntos=np.zeros((int(Tamaño/5),2))
for i in range(int(Tamaño/5)):
    puntos[i][0]=np.random.randint(0,ANCHO)
    puntos[i][1]=np.random.randint(0,ALTO)
## Pantalla
def pantalla(screen,Tamaño,puntos):
     screen.fill((0,0,0))
     for i in range(int(Tamaño/5)):
             puntos[i][1]+=gravedad/100
             pygame.draw.circle(screen,(255,255,255),(int(puntos[i][0]),int(puntos[i][1])),2)
             if puntos[i][1]>ALTO:
                puntos[i][0]=random.randrange(ANCHO)
                puntos[i][1]=random.randrange(-30,-5)
def lluvia(screen,ANCHO,ALTO,Tamaño):
   posiciones=np.zeros((Tamaño,2))
   color=np.zeros((Tamaño,3))
   for i in range(Tamaño):
     x=random.randrange(0,ANCHO)
     y=random.randrange(0,ALTO)
     posiciones[i,0]=x
     posiciones[i,1]=y
     color[i][0]=random.randrange(0,255)
     color[i][1]=random.randrange(0,255)
     color[i][2]=random.randrange(0,255)
   return posiciones,color

def main():
    screen = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("lluvia de estrellas de colores")
    icono=pygame.image.load('C:/Users/bella/Desktop/Epython/tOBY.png')
    pygame.display.set_icon(icono)
    posicion,color=lluvia(screen,ANCHO,ALTO,Tamaño)
    corriendo=True
    clock=pygame.time.Clock()
    while corriendo:
        for eventos in pygame.event.get():
          if eventos.type == pygame.QUIT:
              corriendo=False
       
        pantalla(screen,Tamaño,puntos)
        ##screen.fill((0,0,0))
        for i in range(len(posicion)):
            posicion[i][1]+=gravedad
            R= color[i][0]
            G= color[i][1]
            B= color[i][2]
           
            pygame.draw.line(screen,(R,G,B),(posicion[i][0],posicion[i][1]),(posicion[i][0],posicion[i][1]+20))
           
            if posicion[i][1]>ALTO:
                posicion[i][0]=random.randrange(ANCHO)
                posicion[i][1]=random.randrange(-30,-5)
            
        pygame.display.flip()
        clock.tick_busy_loop(fps)
if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()

