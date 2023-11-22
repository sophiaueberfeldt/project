import sys
import time
import pygame
from pygame.locals import QUIT

pygame.init()
width, height = 800,  600
#chemSpeed= [1,1]
#Now make it a cookie

backgroundColor = [(130, 17, 38),(0, 0, 0)]

screen = pygame.display.set_mode((width, height))

while True:
    screen.fill(backgroundColor[0])
    pygame.display.flip()
    # time.sleep(1)
    # screen.fill(backgroundColor[0])
    # pygame.display.flip()
    # time.sleep(1)
