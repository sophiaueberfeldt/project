import sys
import time
import pygame



pygame.init()
width, height = 800,  600
chemSpeed= [1,1]
#Now make it a cookie


screen = pygame.display.set_mode((width, height))

chem= pygame.image.load("img.png")
chemRect = chem.get_rect()

while True:

    screen.blit(chem, chemRect)
    chemRect = chemRect.move(chemSpeed)

    if chemRect.left < 0 or chemRect.right > width:
        chemSpeed[0] = -chemSpeed[0]
    if chemRect.top < 0 or chemRect.bottom > height:
        chemSpeed[1] = -chemSpeed[1]

    pygame.display.flip()






