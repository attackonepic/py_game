import pygame

class Ship():
    def __init__(self, screen):
        """Initialize the ship and set its starting position"""
        # Load the ship image and get its rect
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()
        self.screen = screen  # Assign the screen attribute

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
