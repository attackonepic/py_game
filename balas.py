import pygame
import sys

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bala.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (5, 0)

    def update(self):
        self.rect.y -= 5

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill((0, 128, 255))
        self.rect = self.image.get_rect()
        self.rect.topleft = (375, 500)

    def update(self, keys):
        # Update player position based on keys
        
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_SPACE]:
            # Fire a new bullet when the space key is pressed
            bullet = Bullet()
            all_sprites.add(bullet)

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Create player and bullet instances
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    # Update player and bullet sprites
    player.update(keys)  # Corrected line
    all_sprites.update()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate to 60 frames per second
    clock.tick(60)

