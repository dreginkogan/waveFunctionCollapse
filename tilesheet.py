import pygame

class Tilesheet:
    def __init__(self, filename, width, height, rows, cols) -> None:
        image = pygame.image.load(filename).convert()
        self.tile_table = []
        for tile_x in range(0, cols):
            line = []
            self.tile_table.append(line)
            for tile_y in range(0, rows):
                rect = [tile_x * width, tile_y  * height, width, height]
                line.append(image.subsurface(rect))

    def draw(self, screen):
        for x, row, in enumerate(self.tile_table):
            for y, tile in enumerate(row):
                screen.blit(tile, [x*72, y*72])