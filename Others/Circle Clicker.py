import pygame
import random

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle Clicker")

background = pygame.image.load("res/background.jpg")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

obj = pygame.image.load("res/panda.png").convert_alpha()
obj = pygame.transform.scale(obj, (100, 100))

circle_x = 400
circle_y = 300
circle_radius = 50
score = 0


def draw_panda(x, y, radius):
    # pygame.draw.circle(screen, (0, 120, 255), (x, y), radius)
    screen.blit(obj, (x - radius, y - radius))


def draw_score(points):
    text = font.render("Score: " + str(points), True, (255, 255, 255))
    screen.blit(text, (20, 20))


def is_inside_circle(mouse_x, mouse_y, circle_x, circle_y, radius):
    dx = mouse_x - circle_x
    dy = mouse_y - circle_y
    return dx * dx + dy * dy <= radius * radius


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            if is_inside_circle(mouse_x, mouse_y, circle_x, circle_y, circle_radius):
                score = score + 1

                if circle_radius > 10:
                    circle_radius = circle_radius - 2

                circle_x = random.randint(circle_radius, WIDTH - circle_radius)
                circle_y = random.randint(circle_radius, HEIGHT - circle_radius)

            else:
                score = score - 1

    # screen.fill((30, 30, 30))
    screen.blit(background, (0, 0))
    draw_panda(circle_x, circle_y, circle_radius)

    draw_score(score)
    pygame.display.update()
    clock.tick(60)

pygame.quit()