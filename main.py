import sys
import time
import pygame
from pygame.locals import QUIT


pygame.init() #Initializes pygame
pygame.font.init()


width = 800
height = 600
backgroundColor = [(130, 17, 38),(0, 0, 0),(159, 131, 111)]


from pygame.locals import(
   K_UP,
   K_DOWN,
   K_LEFT,
   K_RIGHT,
   K_w,
   K_a,
   K_s,
   K_d,
   QUIT
)
gameFont = pygame.font.SysFont('Verdana',100)
screen = pygame.display.set_mode((width, height))


rat1= pygame.image.load("img.png")
ratRect = rat1.get_rect()


#Title
souperRat = gameFont.render('Souper Rat', False, (218,165,32))
game = gameFont.render('Game',False, (218,165,32) )


startButton = gameFont.render('Start', False, (0,0,0))


#Start Screen (Draws in order)
screen.fill(backgroundColor[0])
screen.blit(souperRat, (200,25))
screen.blit(game, (450,150))


button = pygame.draw.rect(screen, (218,165,32), (495, 405, 250, 100))
screen.blit(startButton,(491,395))
#screen.blit(rat1,ratRect)
pygame.display.flip()


#_____________________________


#Loading Screen


def loadingScreen():  #should put in module
    
    screen.fill(backgroundColor[2])
    pygame.draw.circle(screen, (255,255,255), (400,300), 100) #change?
    pygame.display.flip()


#____________________________________________

#Training User Page

def trainPage(): #should put in module
   #Text Surfaces

    
    screen.fill(backgroundColor[1])
    #Text here
    pygame.display.flip()

#____________________________________________

running =True


while running == True:

   #in the event the user clicks the window close button
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           running = False


       #in the event the user clicks the mouse button down
       if event.type == pygame.MOUSEBUTTONDOWN:
           mouse = pygame.mouse.get_pos()
          
           #Starting button
           pygame.Rect.collidepoint(button, mouse[0],mouse[1])


           if pygame.Rect.collidepoint(button, mouse[0],mouse[1]) == True:
               trainPage()
               




   # time.sleep(1)
   # screen.fill(backgroundColor[1])
   # pygame.display.flip()
   # time.sleep(1)






pygame.quit() #Stops the game
