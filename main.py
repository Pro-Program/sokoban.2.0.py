import pygame, time

pygame.init()
width, height = 500, 500
backgroundColor = 100, 0, 0

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
penguin = pygame.image.load("sokoban.2.0.py\images\penguin.png")
penguin = pygame.transform.scale(penguin, (32,32))
penguinx = 468
penguiny = 250
changex = 0
changey = 0
done = 0
speed = 2





while not done:
    for event in pygame.event.get():
        if pygame.KEYDOWN == event.type:
            if event.key == pygame.K_LEFT:
                changex -= speed
            if event.key == pygame.K_RIGHT:
                changex += speed
            if event.key == pygame.K_UP:
                changey -= speed
            if event.key == pygame.K_DOWN:
                changey += speed
        if event.type == pygame.QUIT:
            done = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                changex = 0
            if event.key == pygame.K_RIGHT:
                changex = 0
            if event.key == pygame.K_UP:
                changey = 0
            if event.key == pygame.K_DOWN:
                changey = 0
    penguinx += changex
    penguiny += changey
    if penguinx > 500:
        penguinx = 0
        penguiny = 0
    if penguinx < -1:
        penguinx = 0
        penguiny = 0
    if penguiny > 500:
        penguinx = 0
        penguiny = 0
    if penguiny < -1:
        penguinx = 0
        penguiny = 0
    screen.fill(backgroundColor)
    screen.blit(penguin,(penguinx,penguiny))
    pygame.display.flip()
    clock.tick(60)
