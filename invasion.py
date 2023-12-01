import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group



def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    bg_color = (230, 230, 230, 230)

    # Make a ship
    ship = Ship(ai_settings, screen)
    # Make a group to store bullets
    bullets = Group()

    # Start the main loop for the game
    while True:
        # Redraw the screen during each pass through the loop
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)

        # Get rid of old bullets
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        print(len(bullets))

        gf.update_screen(ai_settings, screen, ship, bullets)
        screen.fill(bg_color)
        ship.blitme()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
