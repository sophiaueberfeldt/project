#This module will be used to draw the scenes

import sys
import time
import pygame
import background as back
from pygame.locals import QUIT

def room1(surface, image):


    image = str(image)

    room1 = pygame.image.load(image)
    roomRect = room1.get_rect()

    surface.blit(room1, roomRect)

    pygame.display.flip()


def draw(scene, surface, font):
    backgroundColor = [(130, 17, 38),(0, 0, 0), (159, 131, 111)]
    gameFont = pygame.font.SysFont('Verdana',100)
    gameFont2 = pygame.font.SysFont('Verdana',40)
    gameFont3 = pygame.font.SysFont('Verdana',20)
    gameFont4 = pygame.font.SysFont('Verdana',17)

    drawscene= str(scene)

    if drawscene == 'startingScreen':
        rat1= pygame.image.load("img_1.png")
        ratRect = rat1.get_rect()

        #Title
        souperRat = font.render('Souper Rat', False, (218,165,32))
        game = font.render('Game',False, (218,165,32) )


        startButton = font.render('Start', False, (0,0,0))


        #Start Screen (Draws in order)
        surface.fill(backgroundColor[0])
        surface.blit(souperRat, (200,25))
        surface.blit(game, (450,150))


        button = pygame.draw.rect(surface, (218,165,32), (495, 405, 250, 100))
        surface.blit(startButton,(491,395))
        surface.blit(rat1,ratRect)
        pygame.display.flip()


    if drawscene == 'loadingScreen':
        surface.fill(backgroundColor[2])
        pygame.draw.circle(surface, (255,255,255), (400,400), 125)
        pygame.display.flip()


    if drawscene == 'trainPage':
        tutorial = font.render('Tutorial',False, (218,218,218) )
        welcome = gameFont2.render('Welcome to the Souper Rat Game!',False, (0,200,32) )
        explain = gameFont4.render('The rats, Basil and Pip, famous soup chefs, lost the ingredients for their new recipe.',False, (218,218,218) )
        explain2 = gameFont3.render('Together they must brave the restaurant to find the lost ingredients.',False, (218,218,218) )
        controls1 = gameFont3.render('Use the keys W,A,S,D to move Basil',False, (218,218,218) )
        controls2 = gameFont3.render('Use the Arrow Keys to move Pip.',False, (218,218,218) )
        french = gameFont2.render('Bon Jeu!',False, (0,200,32) )


        surface.fill(backgroundColor[1])
        surface.blit(tutorial, (200,75))
        surface.blit(welcome, (65,200))
        surface.blit(explain, (30,270))
        surface.blit(explain2, (65,300))
        surface.blit(controls1, (220,330))
        surface.blit(controls2, (230,360))
        surface.blit(french, (300,400))


        pygame.display.flip()

    if drawscene == 'kitchen':
        room1= pygame.image.load("new size backroom.png")
        roomRect = room1.get_rect()
        surface.blit(room1,roomRect)
        pygame.display.flip()

    if drawscene == 'outside':
        room2= pygame.image.load("room.png")
        roomRect = room2.get_rect()
        surface.blit(room2,roomRect)
        pygame.display.flip()

