import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    pygame.display.set_caption("Alien Invasion")
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    bg_color = (230, 230, 230, 230)

    # Make a ship
    ship = Ship(screen)

    # Start the main loop for the game
    while True:
        # Redraw the screen during each pass through the loop
        gf.check_events(ship)
        gf.update_screen(ai_settings, screen, ship)
        screen.fill(bg_color)
        ship.blitme()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # Make the most recently drawn screen visible
        pygame.display.flip()

run_game()
