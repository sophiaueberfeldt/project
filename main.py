import sys
import time
import pygame
import background as back
from pygame.locals import QUIT

pygame.init() #Initializes pygame
pygame.font.init()

width = 800
height = 800
backgroundColor = [(130, 17, 38),(0, 0, 0), (159, 131, 111)]

from pygame.locals import(
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_w,
    K_a,
    K_s,
    K_d,
    K_SPACE,
    QUIT
)
gameFont = pygame.font.SysFont('Verdana',100)
screen = pygame.display.set_mode((width, height))

back.draw("startingScreen", screen, gameFont)
button = pygame.draw.rect(screen, (218,165,32), (495, 405, 250, 100))

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
                back.draw('trainPage', screen, gameFont)


    # time.sleep(1)
    # screen.fill(backgroundColor[1])
    # pygame.display.flip()
    # time.sleep(1)

pygame.quit() #Stops the game

