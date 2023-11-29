import pygame

# Iniciar juego
pygame.init()
# Configuracion de pantalla
width = 800
height = 500
# Definir pantalla
screen = pygame.display.set_mode((width, height))
# Titulo
pygame.display.set_caption("Aburrido en clase")

# Crear reloj
clock = pygame.time.Clock()
running = True

# Cargar imagenes
arsenal = pygame.image.load("arsenal.png")
ucl = pygame.image.load("ucl.png")
saka = pygame.image.load("saka.png")
# convertir imagenes a rectangulos
rect_arsenal = arsenal.get_rect()
rect_ucl = ucl.get_rect()
rect_saka = saka.get_rect()

# Inicializar posición de los rectángulos
rect_arsenal.center = (width // 4, height // 2)
rect_ucl.center = (3 * width // 4, height // 2)
rect_saka.topleft = (5, 0)

font = pygame.font.Font(None, 36)  
text_color = (0, 0, 0)  

texto = "Arsenal have won the Champions League!"

# Loop del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pantalla blanca
    screen.fill("white")

    # Movimiento de los rectangulos
    keys = pygame.key.get_pressed()
    
    # Render text
    text_surface = font.render(texto, True, text_color)

    # Get the rect of the text surface
    text_rect = text_surface.get_rect()

    if keys[pygame.K_UP] and rect_arsenal.y > 0:
        rect_arsenal.y -= 5 
    if keys[pygame.K_DOWN] and rect_arsenal.y < height - rect_arsenal.height:
        rect_arsenal.y += 5
    if keys[pygame.K_LEFT] and rect_arsenal.x > 0:
        rect_arsenal.x -= 5
    if keys[pygame.K_RIGHT] and rect_arsenal.x < width - rect_arsenal.width:
        rect_arsenal.x += 5
    if keys[pygame.K_SPACE]:
        screen.blit(saka, rect_saka)


    # Ubicar los rectangulos en la pantalla
    screen.blit(arsenal, rect_arsenal)
    screen.blit(ucl, rect_ucl)

    if rect_arsenal.colliderect(rect_ucl):
        screen.blit(text_surface, text_rect)

    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
