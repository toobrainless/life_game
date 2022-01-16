class Settings:
    def __init__(self):
        self.screen_width = 1206
        self.screen_height = 801
        self.bg_color = (34, 34, 34)
        self.alive_color = (102, 255, 102)
        self.block_size = 9
        self.grid_width = self.screen_width // self.block_size
        self.grid_height = self.screen_height // self.block_size
        self.start = 0
