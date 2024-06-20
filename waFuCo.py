import pygame
import sys
from tilesheet import Tilesheet
import random

class WaFuCo:
    def __init__ (self, tilesWidth = 48, tilesHeight = 64, cellWidth = 6, cellHeight = 6, doGrassPreference = False):
    
        # move values from initialization here
        self.tilesWidth = tilesWidth
        self.tilesHeight = tilesHeight
        self.cellWidth = cellWidth
        self.cellHeight = cellHeight
        self.doGrassPreference = doGrassPreference

        # used to know when to stop
        self.tilesRemaining = tilesWidth*tilesHeight

        # initialize pygame
        pygame.init()
        self.screen = pygame.display.set_mode((tilesWidth*cellWidth, tilesHeight*cellHeight))
        self.clock = pygame.time.Clock()
        self.bg_color = pygame.Color('black')

        # use tile sheet
        self.tiles =  Tilesheet('tiles.png', cellWidth, cellHeight, 1, 5)

        self.tileMap = [[[0, 1, 2] for i in range(tilesWidth)] for j in range(tilesHeight)]

    def oceanBorder(self): # creates border of ocean
        for x in range(self.tilesWidth): # top
            self.tileMap[0][x] = [0]

        for y in range(self.tilesHeight): # left
            self.tileMap[y][0] = [0]

        for x in range(self.tilesWidth): # bottom
            self.tileMap[self.tilesHeight-1][x] = [0]

        for y in range(self.tilesHeight): # right
            self.tileMap[y][self.tilesWidth-1] = [0]

    def sillyTestRing(self, distance = 2): # just for debug!! to test if sand spawns in
        for y in range(distance, self.tilesHeight-distance):
            for x in range(distance, self.tilesWidth-distance):
                self.tileMap[y][x] = [1]

    def prunePossibilities(self):
        for y in range(1, self.tilesHeight-1): # just ignoring margin stuff for now
            for x in range(1, self.tilesWidth-1):

                if len(self.tileMap[y][x])!= 1:
                    # ocean, remove grass
                    if self.tileMap[y][x-1] == [0] or self.tileMap[y+1][x] == [0] or self.tileMap[y-1][x] == [0] or self.tileMap[y][x+1] == [0]:
                        if 1 in self.tileMap[y][x]: # remove the grass posibility
                            self.tileMap[y][x].remove(1)

                    # grass, remove ocean
                    if self.tileMap[y][x-1] == [1] or self.tileMap[y+1][x] == [1] or self.tileMap[y-1][x] == [1] or self.tileMap[y][x+1] == [1]:
                        if 0 in self.tileMap[y][x]: # remove the ocean posibility
                            self.tileMap[y][x].remove(0)

    def randomEligibleTile(self): # the lowest possibility somehow becomes 2 when it isnt?? the black spaces are places where it is 3 but the program ignores bc its looking for 2s
        eligible = [] # eligible tiles
        lowestPoss = 3 

        for y in range(self.tilesHeight):
            for x in range(self.tilesWidth):
                if len(self.tileMap[y][x]) > 1 and len(self.tileMap[y][x])<lowestPoss: # ignores placed ones, tiles with only one poss are functionally placed
                    lowestPoss = len(self.tileMap[y][x])

        for y in range(self.tilesHeight):
            for x in range(self.tilesWidth):
                if len(self.tileMap[y][x]) == lowestPoss:
                    eligible.insert(0, (x, y)) # insert coordinates into pool to choose from

        if lowestPoss > 1 and len(eligible)>0:
            # make the choice
            (xi, yi) = eligible[random.randint(0, len(eligible)-1)] # chooses coordinates

            if self.doGrassPreference and 1 in self.tileMap[yi][xi] == True:
                self.tileMap[yi][xi].insert(0, 1)

            self.tileMap[yi][xi] = [self.tileMap[yi][xi][random.randint(0,len(self.tileMap[yi][xi])-1)]]


    def printTileMap(self):
        print()
        for row in self.tileMap:
            print(row)
            print()

    def processVisuals(self):
        for row in range(self.tilesWidth): # i def need to fix the row and col stuff later
            for col in range(self.tilesHeight):
                if len(self.tileMap[col][row]) == 1:
                    self.placeTile(row, col, self.tileMap[col][row][0])
                else:
                    self.placeTile(row, col, -1)
        pygame.display.flip()

    def countPlacedTiles(self): # used to know when to terminate
        count = self.tilesHeight*self.tilesWidth
        for y in range(self.tilesHeight):
            for x in range(self.tilesWidth):
                if len(self.tileMap[y][x]) == 1:
                    count-=1

        return count

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