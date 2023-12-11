import pygame
import sys

pygame.init()

height = 800
width = 800

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Varpunoid")
clock = pygame.time.Clock()
FPS = 60
run = True

ax = 50
ay = 30
vx = 5
vy = 3
hit = False


# Load the image and define regla_rect before the main loop
regla = pygame.image.load("regla.bmp")
regla_rect = regla.get_rect()
regla_rect.center = (400, 795)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and regla_rect.x > 0:
        regla_rect.x -= 10
    if keys[pygame.K_RIGHT] and regla_rect.x < 700:
        regla_rect.x += 10

    screen.fill((255, 255, 255))

    if ay > height and keys[pygame.K_q]:
        ax = 50
        ay = 30
        vy = -vy

    ball = pygame.draw.circle(screen, (255, 0, 0), (ax, ay), 10)

    screen.blit(regla, regla_rect)

    ax += vx
    ay += vy

    if ball.colliderect(regla_rect):
        if not hit:
            vy = -vy - 1
            hit = True
    else:
        hit = False

    if ax <= 0 or ax >= width:
        vx = -vx
    if ay <= 0:
        vy = -vy
    


        

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
