import pygame                   #pygame library
import sys                      #systems library
from pygame.locals import *     #needed for user input

pygame.init()                   #starts pygame
screen = pygame.display.set_mode((800,600)) #creates screen object + size

#define some custom colours
red = (255,0,0)
screen.fill((255,255,255))            #sets background colour white


pygame.draw.circle(screen, red, (40,40),20)     #green circle

pygame.display.update()         #needed to update what you drew

while True:                          #loop needed for window to stay open
    for event in pygame.event.get(): #allows you to close window
        if event.type == QUIT:
            sys.exit()
