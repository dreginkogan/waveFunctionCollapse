import pygame
import sys
from tilesheet import Tilesheet
import random

class WaFuCo:
    def __init__ (self, tilesWidth = 48, tilesHeight = 64, cellWidth = 6, cellHeight = 6):
    
        # move values from initialization here
        self.tilesWidth = tilesWidth
        self.tilesHeight = tilesHeight
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight

        # initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((tilesWidth*cellWidth, tilesHeight*cellHeight))
        self.clock = pygame.time.Clock()
        self.bg_color = pygame.Color('black')

        # use tile sheet
        self.tiles =  Tilesheet('tiles.png', cellWidth, cellHeight, 1, 5)

        self.tileMap = [[[1, 2] for i in range(tilesWidth)] for j in range(tilesHeight)]

    def printTileMap(self):
        for row in self.tileMap:
            print(row)

    def processVisuals(self):
        for row in range(self.tilesWidth):
            for col in range(self.tilesHeight):
                if len(self.tileMap[col][row]) == 1:
                    self.placeTile(row, col, self.tileMap[col][row][0])
                else:
                    self.placeTile(row, col, -1)
        pygame.display.flip()

    def placeTile(self, x, y, tile):
        if tile==0: # ocean
            self.screen.blit(self.tiles.get_tile(0,0), (x*self.cellWidth, y*self.cellHeight))
        elif tile==1: # grass
            self.screen.blit(self.tiles.get_tile(1,0), (x*self.cellWidth, y*self.cellHeight))
        elif tile==2: # sand
            self.screen.blit(self.tiles.get_tile(2,0), (x*self.cellWidth, y*self.cellHeight))
        else:
            self.screen.blit(self.tiles.get_tile(4,0), (x*self.cellWidth, y*self.cellHeight))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()