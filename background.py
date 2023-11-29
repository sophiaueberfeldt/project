#This module will be used to draw the scenes

import sys
import time
import pygame
import background as back
from pygame.locals import QUIT

def draw(scene):

    pygame.init() #Initializes pygame
    pygame.font.init()

    width = 800
    height = 800
    backgroundColor = [(130, 17, 38),(0, 0, 0), (159, 131, 111)]


    gameFont = pygame.font.SysFont('Verdana',100)
    screen = pygame.display.set_mode((width, height))

    drawscene= str(scene)

    if drawscene == 'startingScreen':
        rat1= pygame.image.load("img_1.png")
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
        screen.blit(rat1,ratRect)
        pygame.display.flip()


    if drawscene == 'loadingScreen':
        screen.fill(backgroundColor[2])
        pygame.draw.circle(screen, (255,255,255), (400,400), 125)
        pygame.display.flip()


    if drawscene == 'trainPage':


        screen.fill(backgroundColor[1])
        pygame.display.flip()


    if drawscene == 'kitchen':
        room1= pygame.image.load("new size backroom.png")
        roomRect = room1.get_rect()
        screen.blit(room1,roomRect)
        pygame.display.flip()

