import sys
import time
import pygame


from pygame.locals import QUIT


pygame.init() #Initializes pygame
width, height = 800,  600


backgroundColor = [(159, 131, 111)]


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


screen.fill(backgroundColor[0])
button = pygame.draw.rect(screen, (0,0,0), (495, 405, 250, 100)) #Draws in order
screen.blit(rat1,ratRect)
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


#CODE FOR OLD WAY OF COLOURING, DID TO PRACTICE
# def loadingScreen():
#     pygame.init()
#     width, height = 800,  600
#
#     screen = pygame.display.set_mode((width, height))
#
#     backgroundColor = [(159, 131, 111)]
#     while True:
#         screen.fill(backgroundColor[0])
#
#         pygame.display.flip()
#
#
#
# pygame.quit() #Stops the game
#
#
# loadingScreen()

