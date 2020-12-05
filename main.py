import pygame, time

pygame.init()
width, height = 800, 600
dvdLogoSpeed = [1, 1]
backgroundColor = 100, 0, 0

screen = pygame.display.set_mode((width, height))


while True:
    screen.fill(backgroundColor)

    pygame.display.flip()
    time.sleep(10 / 1000)
