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


running =True

while running == True:

    #in the event the user clicks the window close button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()


    screen.fill(backgroundColor[0])
    pygame.draw.rect(screen, (0,0,0), (200, 50, 200, 200)) #Draws in order
    pygame.display.flip()
    # time.sleep(1)
    # screen.fill(backgroundColor[1])
    # pygame.display.flip()
    # time.sleep(1)



pygame.quit() #Stops the game