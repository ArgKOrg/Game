import pygame,sys

from pygame.locals import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((400,400))
    pygame.display.set_caption('JIGame')
    #pygame.display.toggle_fullscreen()


    while True:
       for even in pygame.event.get():
           if even.type == QUIT:
               sys.exit()

if __name__ == '__main__':
    main()
