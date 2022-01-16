import sys
import pygame
import random


def create_random_grid(life_settings):
    grid_width = life_settings.grid_width
    grid_height = life_settings.grid_height
    grid = []
    for x in range(grid_width):
        row = []
        for y in range(grid_height):
            row.append(random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1]))

        grid.append(row)

    return grid


def regen_grid(life_settings, grid):
    grid_width = life_settings.grid_width
    grid_height = life_settings.grid_height

    for x in range(grid_width):
        for y in range(grid_height):
            grid[x][y] = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])


def clear_grid(life_settings, grid):
    grid_width = life_settings.grid_width
    grid_height = life_settings.grid_height

    for x in range(grid_width):
        for y in range(grid_height):
            grid[x][y] = 0


def draw_alive_block(life_settings, screen, x, y):
    alive_color = life_settings.alive_color
    block_size = life_settings.block_size
    x *= block_size
    y *= block_size

    rect = (x, y, block_size, block_size)

    pygame.draw.rect(screen, alive_color, rect)


def get_neighbours(life_settings, x, y):
    gw = life_settings.grid_width
    gh = life_settings.grid_height

    return [((x + gw - 1) % gw, (y + gh - 1) % gh), (x, (y + gh - 1) % gh), ((x + gw + 1) % gw, (y + gh - 1) % gh),
            ((x + gw - 1) % gw, y),                                        ((x + gw + 1) % gw, y),
            ((x + gw - 1) % gw, (y + gh + 1) % gh), (x, (y + gh + 1) % gh), ((x + gw + 1) % gw, (y + gh + 1) % gh)]


def update_cell(life_settings, x, y, grid):
    neighbours = get_neighbours(life_settings, x, y)

    live_neighbors = 0
    for neigh in neighbours:
        live_neighbors += grid[neigh[0]][neigh[1]]

    if grid[x][y]:
        if live_neighbors == 2 or live_neighbors == 3:
            return 1
        else:
            return 0
    else:
        if live_neighbors == 3:
            return 1
        else:
            return 0


def update_grid(life_settings, grid):
    grid_width = life_settings.grid_width
    grid_height = life_settings.grid_height

    new_grid = []

    for x in range(grid_width):
        row = []
        for y in range(grid_height):
            row.append(update_cell(life_settings, x, y, grid))

        new_grid.append(row)

    return new_grid


def check_events(life_settings, grid):
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
            if event.unicode == 's':
                life_settings.is_start ^= 1

            if event.unicode == 'r':
                regen_grid(life_settings, grid)

            if event.unicode == 'c':
                clear_grid(life_settings, grid)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = (event.pos[0] // life_settings.block_size), (event.pos[1] // life_settings.block_size)
                grid[x][y] ^= 1

                print(event.pos[0], event.pos[1])
                print(x, y)


def update_screen(life_settings, screen, grid):
    screen.fill(life_settings.bg_color)

    # grid = create_random_grid(life_settings)

    grid_width = life_settings.grid_width
    grid_height = life_settings.grid_height

    for x in range(grid_width):
        for y in range(grid_height):
            if grid[x][y]:
                draw_alive_block(life_settings, screen, x, y)

    # grid = update_grid(life_settings, grid)

    pygame.display.flip()


