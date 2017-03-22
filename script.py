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

GestureList = ['Circle Gesture','Swipe Gesture', 'Screen Tap Gesture']
fileList = ['circle.py','swipe.py','screentap.py']
GestureCount = 0
CurrentGesture = GestureList[GestureCount];


ClickCount = 0

rectangle = pygame.Rect(400,300,100,100)

while True:
    gameDisplay.fill(white)
	
    #print ClickCount
	
    if((ClickCount%5 != 0) and ((ClickCount + 1) % 5 != 0)):
        pygame.draw.rect(gameDisplay, red,rectangle,4)

    if(ClickCount%5 == 0): # every 5 clicks show an instruction

        if(ClickCount == 0 and GestureCount == 0 ):
            textsurface = myfont.render('Click anywhere to start !', 1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            #ClickCount += 1;


        if(ClickCount == 5):
            print '\n\nExperiment '  + str(CurrentGesture)
            os.system('python ' + fileList[GestureCount] + ' 1 5');
            ClickCount += 1;

      		
        if(ClickCount == 10):
            print '\n\nExperiment '+ str(CurrentGesture)
            os.system('python ' + fileList[GestureCount] + ' 5 3')
            ClickCount += 1;

        if(ClickCount == 15):
            print '\n\nExperiment '+ str(CurrentGesture)
            os.system('python ' + fileList[GestureCount] + ' 3 9')
            ClickCount += 1;
	
        if(ClickCount == 20):
            print '\n\nExperiment '+ str(CurrentGesture)
            os.system('python ' + fileList[GestureCount] + ' 9 13')
            ClickCount += 1;
		
        if(ClickCount == 25):
            print '\n\nExperiment ' + str(CurrentGesture)
            os.system('python ' + fileList[GestureCount] + ' 13 5')
            ClickCount += 1;
			
        if(ClickCount == 30):
            print '\n\nExperiment '+ str(CurrentGesture)
            if (GestureCount <= 3) :
                os.system('python ' + fileList[GestureCount -1] + ' 5 1')
                if(GestureCount < 3):
                   ClickCount = 0
                else:
				   ClickCount += 1
            else:
				ClickCount +=1
				

        #ClickCount += 1;
	

    if((ClickCount + 1) % 5 == 0):
        if(ClickCount == 4):
            textsurface = myfont.render(('Task 1: Increase the value from 1 to 5 using ' + CurrentGesture),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen to start'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))

        if(ClickCount == 9):
            textsurface = myfont.render(('Task 2: Decrease the value from 5 to 3 using '  + CurrentGesture),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen to start'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))
			
        if(ClickCount == 14):
            textsurface = myfont.render(('Task 3: Increase the value from 3 to 9 using '  + CurrentGesture),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen to start'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))

        if(ClickCount == 19):
            textsurface = myfont.render(('Task 4: Increase the value from 9 to 13 using '  + CurrentGesture),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen to start'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))
		
        if(ClickCount == 24):
            textsurface = myfont.render(('Task 5: Decrease the value from 13 to 5 using '  + CurrentGesture),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen to start'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))

        if(ClickCount == 29):
            textsurface = myfont.render(('Task 6: Decrease the value from 5 to 1 using '  + CurrentGesture),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
            textsurface = myfont.render(('Click on this screen to start'),1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,300))

        if(GestureCount == 3):
            textsurface = myfont.render(' Thank you for completing the experiment :)', 1, (0, 0, 0))
            gameDisplay.blit(textsurface,(25,250))
	

    for event in pygame.event.get():

        if event.type == pygame.MOUSEBUTTONDOWN:
		    if (ClickCount in [0,4,9,14,19,24,29]):
			    if(ClickCount == 29):
			        GestureCount += 1
			        print GestureCount
			        print ClickCount
			        if GestureCount <= 2:
			            CurrentGesture = GestureList[GestureCount]
			    ClickCount += 1
			   
		    else: 
			    click = rectangle.collidepoint(pygame.mouse.get_pos())

			    if click == 1:
				    #print 'CLICKED!'
				    ClickCount += 1;
				    #print ClickCount
				    #if (ClickCount == 35):
					#    ClickCount = 0
				    rectangle = pygame.Rect(randint(0,700),randint(0,500),100,100) # NOTE: bound checks here
				    pygame.display.update()
					
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
