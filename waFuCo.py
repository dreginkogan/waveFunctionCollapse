import pygame

class waFuCo:
    def __init__ (self, tilesWidth, tilesHeight, cellHeight, cellWidth):
        pygame.init()

        self.screen = pygame.display.set_mode([tilesWidth*cellWidth,tilesHeight*cellHeight])
        self.clock = pygame.time.Clock()

        self.bg_color = pygame.Color('black')

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

pygame.init()

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
