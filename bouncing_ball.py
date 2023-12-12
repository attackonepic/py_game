import pygame

pygame.init()

width = 800
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Bouncing ball")
FPS = 60
clock = pygame.time.Clock()
run = True

regla = pygame.image.load("regla.bmp")
regla2 = pygame.image.load("regla.bmp")
regla_rect = regla.get_rect()
regla2_rect = regla2.get_rect()
regla_rect.center = (400, 595)
regla2_rect.center = (400, 10)

ax = 50
ay = 50
vx = 5
vy = 3
hit = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    screen.fill("white")

    ball = pygame.draw.circle(screen, (255, 0, 0), (ax, ay), 10)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and regla_rect.x > 0:
        regla_rect.x -= 5
    if keys[pygame.K_RIGHT] and regla_rect.x < 720:
        regla_rect.x += 5

    if regla2_rect.x < ball.x and regla2_rect.x < 720:
        regla2_rect.x += 5
    elif regla2_rect.x > ball.x and regla2_rect.x > 0:
        regla2_rect.x -= 5

    ax += vx
    ay += vy

    if ball.colliderect(regla_rect) or ball.colliderect(regla2_rect):
        if not hit:
            vy = -vy - 2
            hit = True 

    else:
        hit = False
    
    screen.blit(regla, regla_rect)
    screen.blit(regla2, regla2_rect)
    
    if ax <= 0 or ax >= width:
        vx = -vx
    
    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()