import pygame
# Iniciar juego
pygame.init()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)
        
        # Load the bullet image
        self.image = pygame.image.load("bala.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (5, 0)

    def update(self):
        # Move the bullet upward
        self.rect.y -= 5

class Player(self):
    def movement():
        if keys[pygame.K_UP] and rect_arsenal.y > 0:
            rect_arsenal.y -= 5 
        if keys[pygame.K_DOWN] and rect_arsenal.y < height - rect_arsenal.height:
            rect_arsenal.y += 5
        if keys[pygame.K_LEFT] and rect_arsenal.x > 0:
            rect_arsenal.x -= 5
        if keys[pygame.K_RIGHT] and rect_arsenal.x < width - rect_arsenal.width:
            rect_arsenal.x += 5
        
        

    

    def collisions():
        if rect_arsenal.colliderect(rect_ucl):
            screen.blit(text_surface, text_rect)



# Configuracion de pantalla
width = 1200
height = 800
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

# Inicializar posición de los rectángulos
rect_arsenal.center = (width // 4, height // 2)
rect_ucl.center = (3 * width // 4, height // 2)

# Textos
font = pygame.font.Font(None, 36)  
text_color = (0, 0, 0)  
texto = "Arsenal have won the Champions League!"
gol = "1-0 to the Arsenal!"
# Loop del juego


bullet = Bullet()

# Create a sprite group
all_sprites = pygame.sprite.Group()
all_sprites.add(bullet)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            # Fire a new bullet when the space key is pressed
            bullet = Bullet()
            all_sprites.add(bullet)

    # Pantalla blanca
    screen.fill("white")

    # Movimiento de los rectangulos
    keys = pygame.key.get_pressed()
   

    # Ubicar los rectangulos en la pantalla
    screen.blit(arsenal, rect_arsenal)
    screen.blit(ucl, rect_ucl)
    
    # Render text
    text_surface = font.render(texto, True, text_color)
    gol_surface = font.render(gol, True, text_color)

    # Get the rect of the text surface
    text_rect = text_surface.get_rect()
    gol_rect = gol_surface.get_rect()

    

    


       
       
       
       

       
       
       
    
    # Llamar las funciones necesarias
    movement()
    collisions()

    pygame.display.flip()
    clock.tick(60)

# Salir del juego
pygame.quit()
