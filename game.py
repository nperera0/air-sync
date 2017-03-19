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
import sys, time
from random import randint

pygame.init()

white = 255,255,255
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('air-sync Test')


pygame.font.init() # showing text
myfont = pygame.font.SysFont('Comic Sans MS', 30)

#audio
pygame.mixer.init()

#pygame.mixer.music.load("01.wav")
#pygame.mixer.music.play()


ClickCount = 0

rectangle = pygame.Rect(400,300,100,100)

while True:
    gameDisplay.fill(white)

    if(ClickCount%5 != 0):
        pygame.draw.rect(gameDisplay, red,rectangle,4)

    if(ClickCount%5 == 0): # every 5 clicks show an instruction

        if(ClickCount == 0):
            textsurface = myfont.render('Click anywhere to start !', 1, (0, 0, 0))

        if(ClickCount == 5):
            textsurface = myfont.render('Task 1: Increase the value from 0 to 3 using Gesture 1',1, (0, 0, 0))

        if(ClickCount == 10):
            textsurface = myfont.render('Task 2: Decrease the value from 3 to 0 using Gesture 1', 1, (0, 0, 0))

        if(ClickCount == 15):
            textsurface = myfont.render('Task 3: Increase the value from 0 to 3 using Gesture 2',1, (0, 0, 0))

        if(ClickCount == 20):
            textsurface = myfont.render('Task 4: Decrease the value from 3 to 0 using Gesture 2', 1, (0, 0, 0))

        if(ClickCount == 25):
            textsurface = myfont.render('Task 5: Increase the value from 0 to 3 using Gesture 3',1, (0, 0, 0))

        if(ClickCount == 30):
            textsurface = myfont.render('Task 6: Decrease the value from 3 to 0 using Gesture 3', 1, (0, 0, 0))

        if(ClickCount == 35):
            textsurface = myfont.render(' Tankyou for completing the experiment !', 1, (0, 0, 0))

        gameDisplay.blit(textsurface,(25,250))
		
		            # if we are showing instructions , this will un pause the program
        if(ClickCount%5 == 0):
			ClickCount += 1;

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:

            click = rectangle.collidepoint(pygame.mouse.get_pos())

            if click == 1:
                print 'CLICKED!'
                ClickCount += 1;

                # play audio
                fileName = str(ClickCount).zfill(2)
                pygame.mixer.music.load(fileName + '.wav')
                pygame.mixer.music.play()

                if (ClickCount == 35):
                    ClickCount = 0

                rectangle = pygame.Rect(randint(0,700),randint(0,500),100,100) # NOTE: bound checks here
                pygame.display.update()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
