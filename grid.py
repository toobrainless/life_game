import random


def is_in_rect(x, y, x1, y1, x2, y2):
    if x1 <= x <= x2 and y1 <= y <= y2:
        return 1
    else:
        return 0


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

    def gen_picture(self):
        for x in range(self.width):
            for y in range(self.height):
                if is_in_rect(x, y, 10, 25, 20, 75):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 20, 65, 40, 75):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 50, 40, 60, 75):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 50, 25, 60, 35):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 70, 25, 80, 75):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 80, 25, 100, 35):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 80, 45, 90, 55):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 110, 25, 120, 75):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 120, 25, 140, 35):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 120, 65, 140, 75):
                    self.grid[x][y] = random.choice([0, 0, 1])
                elif is_in_rect(x, y, 120, 45, 130, 55):
                    self.grid[x][y] = random.choice([0, 0, 1])
                else:
                    self.grid[x][y] = 0

                # if y <= 24 or y >= 75:
                #     self.grid[x][y] = 1
                #
                # if x <= 24 or x >= 125:
                #     self.grid[x][y] = 1

    def change_state(self, x, y):
        self.grid[x][y] ^= 1

    def get_state(self, x, y):
        return self.grid[x][y]

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height
