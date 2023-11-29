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
# convertir imagenes a rectangulos
rect_arsenal = arsenal.get_rect()
rect_ucl = ucl.get_rect()


# Loop del juego
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    # posicion de los rectangulos
    rect_arsenal.center = (width // 4, height // 2)
    rect_ucl.center = (3 * width // 4, height // 2)
    
    # movimiento de los rectangulos
    keys = pygame.key.get_pressed()

   # Pantalla blanca
    screen.fill("white")

    # Movimiento de los rectangulos
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        rect_arsenal.y -= 5  # Adjust the speed as needed

    # Ubicar los rectangulos en la pantalla
    screen.blit(arsenal, rect_arsenal)
    screen.blit(ucl, rect_ucl)

    pygame.display.flip()
    clock.tick(60)
 


# Salir del juego
pygame.quit()