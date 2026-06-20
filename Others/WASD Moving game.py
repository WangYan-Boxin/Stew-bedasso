import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800, 600))

# red control
x1, y1 = 200, 300
ObjectSize = 20
speed1 = 0.4

# blue control
x2, y2 = 600, 300
ObjectSize = 20
speed2 = 0.4

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    #  Red moving
    if keys[pygame.K_w]:
        y1 -= speed1
    if keys[pygame.K_s]:
        y1 += speed1
    if keys[pygame.K_a]:
        x1 -= speed1
    if keys[pygame.K_d]:
        x1 += speed1

    #  Blue moving
    if keys[pygame.K_i]:
        y2 -= speed2
    if keys[pygame.K_k]:
        y2 += speed2
    if keys[pygame.K_j]:
        x2 -= speed2
    if keys[pygame.K_l]:
        x2 += speed2

# red crossing
    if x1 > 800:
        x1 = -ObjectSize
    elif x1 < -ObjectSize:
        x1 = 800
    if y1 > 600:
        y1 = -ObjectSize
    elif y1 < -ObjectSize:
        y1 = 600

# blue crossing
    if x2 > 800:
        x2 = -ObjectSize
    elif x2 < -ObjectSize:
        x2 = 800
    if y2 > 600:
        y2 = -ObjectSize
    elif y2 < -ObjectSize:
        y2 = 600


    player = pygame.Rect(x1,y1, ObjectSize, ObjectSize)
    target = pygame.Rect(x2,y2, ObjectSize, ObjectSize)
    if player.colliderect(target):
        print("collision!")

        # x1 = random.randint(0, 800 - ObjectSize)
        x2 = random.randint(0, 800 - ObjectSize)
        # y1 = random.randint(0, 600 - ObjectSize)
        y2 = random.randint(0, 600 - ObjectSize)

    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (255, 0, 0), (x1, y1, ObjectSize, ObjectSize))
    pygame.draw.rect(screen, (0, 0, 255), (x2, y2, ObjectSize, ObjectSize))
    pygame.display.update()

pygame.quit()