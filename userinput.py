import pygame,sys

from pygame.locals import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((400,400))
    WHITE = (255,255,255)
    BLACK =(0,0,0)
    screen.fill(BLACK)
    pygame.display.set_caption('JIGame')
    RED = (255,0,0)
    BLUE =(0,0,255)
    GREEN =(0,255,0)
    x = 20
    y = 20
    pygame.draw.rect(screen,BLACK,(0,0,400,300))
    pygame.draw.circle(screen,RED,(x,y),10)
    pygame.display.update()
    #pygame.display.toggle_fullscreen()

  
    while True:
       for even in pygame.event.get():
           if even.type == QUIT:
               sys.exit()
           if even.type == KEYDOWN:
               if even.key == K_LEFT:
                   x-=1
               elif even.key == K_RIGHT:
                   x+=1
               if even.key == K_UP:
                   y-=1
               elif even.key == K_DOWN:
                   y+=1  
       pygame.draw.rect(screen,BLACK,(0,0,400,300))
       pygame.draw.circle(screen,RED,(x,y),10)
       pygame.display.update()
             

if __name__ == '__main__':
    main()
