
def draw():

    if loadingScreen == True:
        screen.fill(backgroundColor[2])
        pygame.draw.circle(screen, (255,255,255), (400,400), 125)
        pygame.display.flip()