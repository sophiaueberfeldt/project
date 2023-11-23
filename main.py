import sys
import time
import pygame
from pygame.locals import QUIT

pygame.init() #Initializes pygame
width, height = 800,  600

backgroundColor = [(130, 17, 38),(0, 0, 0)]

screen = pygame.display.set_mode((width, height))

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

screen.fill(backgroundColor[0])
button = pygame.draw.rect(screen, (0,0,0), (495, 405, 250, 100)) #Draws in order
pygame.display.flip()

running =True

while running == True:


    #in the event the user clicks the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            pygame.Rect.collidepoint(button, mouse[0],mouse[1])

            if pygame.Rect.collidepoint(button, mouse[0],mouse[1]) == True:
                screen.fill(backgroundColor[1])
                pygame.display.flip()


    # time.sleep(1)
    # screen.fill(backgroundColor[1])
    # pygame.display.flip()
    # time.sleep(1)



pygame.quit() #Stops the game