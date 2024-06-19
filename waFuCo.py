import pygame
import sys
from tilesheet import Tilesheet
import random

class WaFuCo:
    def __init__ (self):
        pygame.init()

        #self.screen = pygame.display.set_mode([tilesWidth*cellWidth,tilesHeight*cellHeight])
        self.screen = pygame.display.set_mode((48*6, 64*6))
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color('black')

        self.tiles =  Tilesheet('tiles.png', 6, 6, 1, 5)
        self.tileMap = [[-1 for i in range(64)] for j in range(48)]
        
        self.possibilitiesMap = [[[0, 1, 2] for i in range(64)] for j in range(48)]

    def oceanBorder(self, margin, tilesWidth, tilesHeight):
        
        # top line
        for i in range(margin):
            for x in range(tilesWidth):
                self.tileMap[x][i] = 0

        #left line
        for y in range(tilesHeight):
            for i in range(margin):
                self.tileMap[i][y] = 0

        #bot line
        for i in range(margin):
            for x in range(tilesWidth):
                self.tileMap[x][63-i] = 0

        #right line
        for y in range(tilesHeight):
            for i in range(margin):
                self.tileMap[47-i][y] = 0

    def prunePossibilities(self):
        for y in range(1, 63): # a lot of hardcoded values here
            for x in range(1, 47):
                    if self.tileMap[x-1][y] == 0 or self.tileMap[x][y+1] == 0 or self.tileMap[x][y-1] == 0 or self.tileMap[x+1][y] == 0:
                        if 1 in self.possibilitiesMap[x][y]: # remove the grass posibility
                            self.possibilitiesMap[x][y].remove(1)
                    if self.tileMap[x-1][y] == 1 or self.tileMap[x][y+1] == 1 or self.tileMap[x][y-1] == 1 or self.tileMap[x+1][y] == 1:
                        if 0 in self.possibilitiesMap[x][y]:
                            self.possibilitiesMap[x][y].remove(0)


    def collapse(self): # must make it do the random thing

        smallestPossib = 3
        eligible = []

        for y in range(1, 63): # a lot of hardcoded values here
            for x in range(1, 47):
                if len(self.possibilitiesMap[x][y]) < smallestPossib:
                    smallestPossib = len(self.possibilitiesMap[x][y])

        if smallestPossib == 1:
            for y in range(1, 63): # a lot of hardcoded values here
                for x in range(1, 47):
                    if len(self.possibilitiesMap[x][y]) == 1:
                        self.tileMap[x][y] = self.possibilitiesMap[x][y][0]
        else:
            for y in range(1, 63): # a lot of hardcoded values here
                for x in range(1, 47):
                    if len(self.possibilitiesMap[x][y]) == smallestPossib and self.tileMap[x][y] == -1: # do not replace existing tiles
                        eligible.insert(0, (x, y))

            if len(eligible)>1: # 
                (i, j) = eligible[random.randint(0, len(eligible)-1)]
            else:
                (i, j) = (0,0)

            self.tileMap[i][j] = self.possibilitiesMap[i][j][random.randint(0, len(self.possibilitiesMap[i][j])-1)]
                    # wai whwere do x and y come from


    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def vomit(self): #randomize
        for y in range(64): # has to be better way of writing this
            for x in range(48):
                self.tileMap[x][y] = random.randint(0, 2) # ignore forest
            
    def update(self):
        pass

    def draw(self):
        self.screen.fill(self.bg_color)
        for y in range(64):
            for x in range(48):
                tileStatus = self.tileMap[x][y]
                if tileStatus == 0:
                    self.screen.blit(self.tiles.get_tile(0,0), (x*6, y*6))
                elif tileStatus == 1:
                    self.screen.blit(self.tiles.get_tile(1,0), (x*6, y*6)) # ignore forest for now
                elif tileStatus == 2:
                    self.screen.blit(self.tiles.get_tile(2,0), (x*6, y*6))
                elif tileStatus == -1:
                    self.screen.blit(self.tiles.get_tile(4,0), (x*6, y*6))
        pygame.display.flip()



    

# file = 'tiles.png'
# sprites = pygame.image.load(file)

# tilesWidth = 255
# tilesHeight = 130

# tileHeightPixels = 5
# tileWidthPixels = 5

# screen = pygame.display

# terrainDict = {
#     -1: "unknown",
#     0 : "water",
#     1 : "grass",
#     2 : "beach",
#     3 : "forest"
# }

# tileMap = [[0]*int(tilesWidth/tileHeightPixels)]*int(tilesHeight/tileHeightPixels)

# class Cell: # each section on the screen
    
#     def __init__(self, coords:tuple):
#         x, y = self.coords

#     def checkOptions():
#         pass

# class Tile: # the things from the tilemap

#     def __init__(self, edgeBiomes, index):
#         self.north = edgeBiomes[0]
#         self.east = edgeBiomes[1]
#         self.south = edgeBiomes[2]
#         self.west = edgeBiomes[3]
#         self.index = index

#         self.possibilities = len(terrainDict) - 1
#         self.collapsed = False # essentially if possibilities equals 1

#     def checkStatus():
#         pass
        

# def printBiomes(tile:Tile, terDict:dict): # for debugging
#     """
#     Prints the biomes at the North, East, South, and West edges of a tile
#     """
#     print(f"North : {terDict[tile.north]}")
#     print(f"East  : {terDict[tile.east]}")
#     print(f"South : {terDict[tile.south]}")
#     print(f"West  : {terDict[tile.west]}")

# # class displayThing:
# #     def __init__(self, tilesWidth, tilesHeight):
# #         pygame.init()
# #         self.tilesWidth = tilesWidth
# #         self.tilesHeight = tilesHeight

# #         self.screen = pygame.display.set_mode([tilesWidth,tilesHeight])

# waterTile = Tile([0, 0, 0, 0], 0)
# grassTile = Tile([1, 1, 1, 1], 1)
# beachTile = Tile([2, 2, 2, 2], 2)
# forestTile = Tile([3, 3, 3, 3], 3)

# # printBiomes(grassTile, terrainDict)


# rect = sprites.get_rect()


# print(sprites)

# screen.blit(sprites, rect)
# pygame.display.update()
