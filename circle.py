import pygame,sys

from pygame.locals import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((400,400))
    WHITE = (255,255,255)
    screen.fill(WHITE)
    pygame.display.set_caption('JIGame')
    RED = (255,0,0)
    BLUE =(0,0,255)
    GREEN =(0,255,0)
    x = 20
    y = 20
    pygame.draw.circle(screen,RED,(x,y),10)
    pygame.display.update()
    #pygame.display.toggle_fullscreen()

  
    while True:
       for even in pygame.event.get():
           if even.type == QUIT:
               sys.exit()
    
       x=x+1
       pygame.draw.circle(screen,RED,(x,y),10)
       pygame.display.update()
             

if __name__ == '__main__':
    main()
