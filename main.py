import pygame, time

pygame.init()
width, height = 500, 500
backgroundColor = 255, 255, 255
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
penguin = pygame.image.load("sokoban.2.0.py\images\penguin.png")
penguin = pygame.transform.scale(penguin, (32,32))
box = pygame.image.load("sokoban.2.0.py\images\\box.png")
goal = pygame.image.load("sokoban.2.0.py\images\goal.JPG")
goal = pygame.transform.scale(goal, (32,32))
goal2 = goal
goal3 = goal
box = pygame.transform.scale(box, (32,32))
box2 = box
box2_hitormiss = box2.get_rect()
box2_hitormiss.x = 200
box2_hitormiss.y = 200
box3 = box
box3_hitormiss = box3.get_rect()
box3_hitormiss.x = 300
box3_hitormiss.y = 300
box_hitormiss = box.get_rect()
box_hitormiss.x = 100
box_hitormiss.y = 100
goal_hitormiss = goal.get_rect()
goal2_hitormiss = goal2.get_rect()
goal3_hitormiss = goal3.get_rect()
goal_hitormiss.x = 123
goal_hitormiss.y = 321
goal2_hitormiss.x = 213
goal2_hitormiss.y = 312
goal3_hitormiss.x = 231
goal3_hitormiss.y = 132
penguin_hitormiss = penguin.get_rect()
penguinx = 468
penguiny = 250
changex = 0
changey = 0
done = 0
speed = 10
fakeError = "Traceback (most recent call last):\n  \t File c:\\Users\Shadow\\Documents\\GitHub\\sokoban.2.0.py\\main.py, line 140, in <module>\n    \t\tclock.tick(60) \nKeyboardInterrupt"
winMessage = "You acctually win"


goals = [goal_hitormiss,goal2_hitormiss,goal3_hitormiss]
boxes = [box_hitormiss,box2_hitormiss,box3_hitormiss]
def daskdajsldkjasldjalskdjalksjdlaksjdlkajsdlkajsdlkajsdlkjasdlkjaslkdjsaldjlkasdjlasdjak():
    
    number = boxes[0].collidelist(goals)
    number2 = boxes[1].collidelist(goals)
    number3 = boxes[2].collidelist(goals)
    print("message message message", number, number2, number3)
    if number != -1 and number2 != -1 and number3 != -1:
        print(fakeError)
        exit()
def colision():
    global penguinx, penguiny
    index = penguin_hitormiss.collidelist(boxes)
    print(index)
    if index != -1:
        boxes[index].x+=changex     
        boxes[index].y+=changey
        if boxes[index].x+box.get_width() > width:
            boxes[index].x -= changex
            boxes[index].y -= changey
            penguinx-=changex
            penguiny-=changey
        if boxes[index].x < -1:
            boxes[index].x -= changex
            boxes[index].y -= changey
            penguinx-=changex
            penguiny-=changey
        if boxes[index].y+box.get_height() > height:
            boxes[index].x -= changex
            boxes[index].y -= changey
            penguinx-=changex
            penguiny-=changey
        if boxes[index].y < -1:
            boxes[index].x -= changex
            boxes[index].y -= changey
            penguinx-=changex
            penguiny-=changey
        for i in boxes:
            if boxes[index] != i:
                if boxes[index].colliderect(i):
                    boxes[index].x -= changex
                    boxes[index].y -= changey
                    penguinx-=changex
                    penguiny-=changey




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
    if penguinx+penguin.get_width() > width:
        penguinx -= changex
        penguiny -= changey
    if penguinx < -1:
        penguinx -= changex
        penguiny -= changey
    if penguiny+penguin.get_height() > height:
        penguinx -= changex
        penguiny -= changey
    if penguiny < -1:
        penguinx -= changex
        penguiny -= changey
    screen.fill(backgroundColor)
    screen.blit(goal, (goal_hitormiss.x, goal_hitormiss.y))
    screen.blit(goal2, (goal2_hitormiss.x,goal2_hitormiss.y))
    screen.blit(goal3, (goal3_hitormiss.x, goal3_hitormiss.y))
    screen.blit(penguin,(penguinx,penguiny))
    
    for x in boxes:
        screen.blit(box, (x.x, x.y))
    pygame.display.flip()
    clock.tick(60)
    penguin_hitormiss.x = penguinx
    penguin_hitormiss.y = penguiny
    colision()
    daskdajsldkjasldjalskdjalksjdlaksjdlkajsdlkajsdlkajsdlkjasdlkjaslkdjsaldjlkasdjlasdjak()



























































































































































































































