'''
import pygame                   #pygame library
import sys                      #systems library
from pygame.locals import *     #needed for user input
from random import randint

pygame.init()                   #starts pygame
screen = pygame.display.set_mode((800,600)) #creates screen object + size

#define some custom colours
red = (255,0,0)
screen.fill((255,255,255))            #sets background colour white




pygame.display.update()         #needed to update what you drew

while True:                          #loop needed for window to stay open
    for event in pygame.event.get(): #allows you to close window
        print(event)
        if event.type == QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            x, y = event.pos
            print( 'x cord :' + str(x) + ' y cord :' + str(y))
            pygame.draw.circle(screen, red, (x,y),30)     #red circle
            pygame.display.update()
            # pygame.draw.circle(screen, red, (randint(0,800),randint(0,600)),20)     #red circle
'''

import pygame
import sys
from random import randint

pygame.init()

white = 255,255,255
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('air-sync Test')

rectangle = pygame.Rect(400,300,100,100)

while True:
    gameDisplay.fill(white)

    pygame.draw.rect(gameDisplay, red,rectangle,4)

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = rectangle.collidepoint(pygame.mouse.get_pos())

            if click == 1:
                print 'CLICKED!'
                rectangle = pygame.Rect(randint(0,700),randint(0,500),100,100) # NOTE: boun checks here
                pygame.display.update()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
