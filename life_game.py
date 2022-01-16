import pygame
import sys

from settings import Settings
from grid import Grid


class LifeGame:
    def __init__(self):
        pygame.init()

        self.settings = Settings()

        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Life")

        self.grid = Grid(self.settings.grid_width, self.settings.grid_height)

    def draw_alive_block(self, x, y):
        alive_color = self.settings.alive_color
        block_size = self.settings.block_size
        x *= block_size
        y *= block_size

        rect = (x, y, block_size, block_size)

        pygame.draw.rect(self.screen, alive_color, rect)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)

        grid_width = self.grid.get_width()
        grid_height = self.grid.get_height()

        for x in range(grid_width):
            for y in range(grid_height):
                if self.grid.get_state(x, y):
                    self.draw_alive_block(x, y)

        pygame.display.flip()

    def check_events(self):
        """Interface

        s for start.

        r for regen grid.

        c for clear grid.

        press mouse button to create a block.

        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.unicode == "s":
                    self.settings.is_start ^= 1

                if event.unicode == "r":
                    self.grid.regen_grid()
                    self.settings.is_start = 0

                if event.unicode == "c":
                    self.grid.clear_grid()

                if event.unicode == "g":
                    self.grid.gen_picture()
                    self.settings.is_start = 0

                if event.unicode == "q":
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x, y = (event.pos[0] // self.settings.block_size), (
                        event.pos[1] // self.settings.block_size
                    )
                    self.grid.change_state(x, y)

    def run_game(self):
        self.grid.gen_picture()
        self.update_screen()

        while True:
            self.check_events()
            self.update_screen()
            if self.settings.is_start:
                self.grid.update()

            self.clock.tick(self.settings.FPS)
