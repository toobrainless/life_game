import random


class Grid:
    def __init__(self, grid_width, grid_height):
        self.width = grid_width
        self.height = grid_height

        self.grid = [[0] * self.height for _ in range(self.width)]

    def regen_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = random.choice([0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

    def clear_grid(self):
        for x in range(self.width):
            for y in range(self.height):
                self.grid[x][y] = 0

    def get_neighbours(self, x, y):
        gw = self.width
        gh = self.height

        return [
            ((x - 1) % gw, (y - 1) % gh),
            (x, (y - 1) % gh),
            ((x + 1) % gw, (y - 1) % gh),
            ((x - 1) % gw, y),
            ((x + gw + 1) % gw, y),
            ((x - 1) % gw, (y + 1) % gh),
            (x, (y + 1) % gh),
            ((x + 1) % gw, (y + 1) % gh),
        ]

    def update_cell(self, x, y):
        neighbours = self.get_neighbours(x, y)

        live_neighbors = 0
        for neigh in neighbours:
            live_neighbors += self.grid[neigh[0]][neigh[1]]

        if self.grid[x][y]:
            return 1 if live_neighbors == 2 or live_neighbors == 3 else 0
        else:
            return 1 if live_neighbors == 3 else 0

    def update(self):
        new_grid = []

        for x in range(self.width):
            row = []
            for y in range(self.height):
                row.append(self.update_cell(x, y))

            new_grid.append(row)

        self.grid = new_grid

    def change_state(self, x, y):
        self.grid[x][y] ^= 1

    def get_state(self, x, y):
        return self.grid[x][y]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
