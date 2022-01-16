class Settings:
    def __init__(self):
        self.screen_width = 1050
        self.screen_height = 700
        self.bg_color = (34, 34, 34)
        self.alive_color = (102, 255, 102)
        self.block_size = 7
        self.grid_width = self.screen_width // self.block_size
        self.grid_height = self.screen_height // self.block_size
        self.is_start = 0
        self.FPS = 10
