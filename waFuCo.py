import pygame

file = 'tiles.png'
image = pygame.image.load(file)

terrainDict = {
    -1: "unknown",
    0 : "water",
    1 : "grass",
    2 : "beach",
    3 : "forest"
}

class Tile:
    def __init__(self, north, east, south, west, tileSetIndex: int):
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.tileSetIndex = tileSetIndex

def printBiomes(tile:Tile, terDict:dict): # for debugging
    """
    Prints the biomes at the North, East, South, and West edges of a tile
    """
    print(f"North : {terDict[tile.north]}")
    print(f"East  : {terDict[tile.east]}")
    print(f"South : {terDict[tile.south]}")
    print(f"West  : {terDict[tile.west]}")

class displayThing:
    def __init__(self, tilesWidth, tilesHeight):
        pygame.init()
        self.tilesWidth = tilesWidth
        self.tilesHeight = tilesHeight

        self.screen = pygame.display.set_mode([tilesWidth,tilesHeight])

waterTile = Tile(0, 0, 0, 0, 0)
grassTile = Tile(1, 1, 1, 1, 1)
beachTile = Tile(2, 2, 2, 2, 2)
forestTile = Tile(3, 3, 3, 3, 3)

printBiomes(grassTile, terrainDict)




rect = image.get_rect()
print(image)

testThing = displayThing(500, 500)

screen = testThing.screen

screen.blit(image, rect)
pygame.display.update()

while True:
   for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()