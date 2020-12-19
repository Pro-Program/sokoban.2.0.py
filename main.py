import pygame, time

pygame.init()
width, height = 500, 500
backgroundColor = 100, 0, 0

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
penguin = pygame.image.load("images/penguin.png")
penguin = pygame.transform.scale(penguin, (32,32))
penguinx = 468
penguiny = 250
changex = 0
changexyz = 0
donenot1 = 0


while not donenot1:
    for event in pygame.event.get():
        if pygame.KEYDOWN == event.type:
            if event.key == pygame.K_LEFT:
                changex -= 10
        if event.type == pygame.QUIT:
            donenot1 = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                changex = 0
    penguinx += changex
    screen.fill(backgroundColor)
    screen.blit(penguin,(penguinx,penguiny))
    pygame.display.flip()
    clock.tick(60)

