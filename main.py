import pygame, time

pygame.init()
width, height = 500, 500
backgroundColor = 100, 0, 0

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
penguin = pygame.image.load("images/penguin.png")
penguinx = 170
penguiny = 170
donenot1 = 0
while not donenot1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            donenot1 = 1
    screen.fill(backgroundColor)
    screen.blit(penguin,(penguinx,penguiny))
    pygame.display.flip()
    clock.tick(60)

