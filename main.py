import sys
import time
import pygame
from pygame.locals import QUIT

pygame.init() #Initializes pygame
pygame.font.init()

print(pygame.font.get_fonts())

width = 800
height = 600
backgroundColor = [(130, 17, 38),(0, 0, 0)]

gameFont = pygame.font.SysFont('Verdana',100)
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

rat1= pygame.image.load("img.png")
ratRect = rat1.get_rect()

souperRat = gameFont.render('Souper Rat', False, (0, 0, 0))
game = gameFont.render('Game',False, (0, 0, 0) )

screen.fill(backgroundColor[0])
screen.blit(souperRat, (200,25))
screen.blit(game, (450,150))
button = pygame.draw.rect(screen, (0,0,0), (495, 405, 250, 100)) #Draws in order
#screen.blit(rat1,ratRect)
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