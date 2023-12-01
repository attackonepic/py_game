import pygame
import sys

pygame.init()
pygame.display.set_caption("Aburrido en clase")
screen = pygame.display.set_mode((800, 600))

#megaman = pygame.image.load("images/megaman.png")
#megaman_rect = megaman.get_rect()

while True:
    bg_color = (0, 0, 225)
    screen.fill(bg_color)

    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            print(event.type)
        
        if event.type == pygame.QUIT:
            sys.exit()

    # Set the Megaman's initial position to the center of the screen
 #   megaman_rect.centerx = screen.get_rect().centerx
  #  megaman_rect.centery = screen.get_rect().centery

    # Draw Megaman at its current location (which is centered)
   # screen.blit(megaman, megaman_rect)

    
        

    pygame.display.flip()
