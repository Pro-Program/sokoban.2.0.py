import pygame, time

pygame.init()
width, height = 1920, 1080
backgroundColor = 100, 0, 0

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
penguin = pygame.image.load("images/penguin.png")
penguinx = 0
penguiny = 0

while True:
    for event in pygame.event.get():
    screen.fill(backgroundColor)
    screen.blit(penguin,(penguinx,penguiny))
    pygame.display.flip()
    clock.tick(60)

