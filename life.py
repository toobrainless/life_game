import pygame

from settings import Settings
import game_functions as gf


def run_game():
    pygame.init()

    life_settings = Settings()

    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((life_settings.screen_width, life_settings.screen_height))
    pygame.display.set_caption("Life")

    grid = gf.create_random_grid(life_settings)
    gf.update_screen(life_settings, screen, grid)

    while True:
        gf.check_events(life_settings, grid)
        gf.update_screen(life_settings, screen, grid)
        if life_settings.is_start:
            grid = gf.update_grid(life_settings, grid)

        clock.tick(life_settings.FPS)


run_game()



