'''
import os

def main():
	print '\n\nExperiment 1'
	os.system('python screentap.py 18 19');
	
	print '\n\nExperiment2'
	os.system('python swipe.py')
	
if __name__ == '__main__':
	main()
'''
import os
import pygame
import sys, time
from random import randint

pygame.init()

white = 255,255,255
red = (255,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('air-sync Test')


pygame.font.init() # showing text
myfont = pygame.font.SysFont('Comic Sans MS', 25)

#audio
pygame.mixer.init()

#pygame.mixer.music.load("01.wav")
#pygame.mixer.music.play()

Gesture1 = 'Circle Gesture'
Gesture2 = 'Swipe Gesture'
Gesture3 = 'Screen Tap Gesture'

ClickCount = 0

rectangle = pygame.Rect(400,300,100,100)

while True:
    gameDisplay.fill(white)
	
    #print ClickCount
	
    if((ClickCount%5 != 0) and ((ClickCount + 1) % 5 != 0)):
        pygame.draw.rect(gameDisplay, red,rectangle,4)

    if(ClickCount%5 == 0): # every 5 clicks show an instruction

        if(ClickCount == 0):
            textsurface = myfont.render('Click anywhere to start !', 1, (0, 0, 0))
            #ClickCount += 1;


        if(ClickCount == 5):
            print '\n\nExperiment 1a'
            os.system('python circle.py 4 7');
            ClickCount += 1;

      		
        if(ClickCount == 10):
            print '\n\nExperiment 1a'
            os.system('python circle.py 7 3')
            ClickCount += 1;

        if(ClickCount == 15):
            print '\n\nExperiment 2a'
            os.system('python swipe.py 4 7')
            ClickCount += 1;
	
        if(ClickCount == 20):
            print '\n\nExperiment 2b'
            os.system('python swipe.py 7 3')
            ClickCount += 1;
		
        if(ClickCount == 25):
            print '\n\nExperiment 3a'
            os.system('python screentap.py 4 7')
            ClickCount += 1;
			
        if(ClickCount == 30):
            print '\n\nExperiment 3b'
            os.system('python screentap.py 7 3')
            ClickCount += 1;

        gameDisplay.blit(textsurface,(25,250))
		
        #ClickCount += 1;
		
    if((ClickCount + 1) % 5 == 0):
        if(ClickCount == 4):
            textsurface = myfont.render(('Task 1a: Increase the value from 4 to 7 using ' + Gesture1),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen when you are ready to perform the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))
            textsurface = myfont.render(('Press enter on the other window after performing the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,350))
		
        if(ClickCount == 9):
            textsurface = myfont.render(('Task 1b: Decrease the value from 7 to 3 using '  + Gesture1),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen when you are ready to perform the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))
            textsurface = myfont.render(('Press enter on the other window after performing the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,350))
			
        if(ClickCount == 14):
            textsurface = myfont.render(('Task 2a: Increase the value from 4 to 7 using '  + Gesture2),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen when you are ready to perform the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))
            textsurface = myfont.render(('Press enter on the other window after performing the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,350))
		
        if(ClickCount == 19):
            textsurface = myfont.render(('Task 2b: Decrease the value from 7 to 3 using '  + Gesture2),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen when you are ready to perform the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))
            textsurface = myfont.render(('Press enter on the other window after performing the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,350))
		
        if(ClickCount == 24):
            textsurface = myfont.render(('Task 3a: Increase the value from 4 to 7 using '  + Gesture3),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen when you are ready to perform the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))
            textsurface = myfont.render(('Press enter on the other window after performing the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,350))

        if(ClickCount == 29):
            textsurface = myfont.render(('Task 3b: Decrease the value from 7 to 3 using '  + Gesture3),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen when you are ready to perform the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))
            textsurface = myfont.render(('Press enter on the other window after performing the gesture'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,350))
		
        if(ClickCount == 34):
            textsurface = myfont.render(' Thank you for completing the experiment :)', 1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
	

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
		    if (ClickCount in [0,4,9,14,19,24,29]):
			    ClickCount += 1
		    else: 
			    click = rectangle.collidepoint(pygame.mouse.get_pos())

			    if click == 1:
				    print 'CLICKED!'
				    ClickCount += 1;
				    print ClickCount
				    if (ClickCount == 35):
					    ClickCount = 0
				    rectangle = pygame.Rect(randint(0,700),randint(0,500),100,100) # NOTE: bound checks here
				    pygame.display.update()
					
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
