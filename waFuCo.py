terrainDict = {
    0 : "water",
    1 : "grass",
    2 : "beach",
    3 : "forest"
}

class Tile:
    def __init__(self, biome):
        self.biome = biome

def printBiomes(tile:Tile, terDict:dict): # for debugging
    """
    Prints the biomes at the North, East, South, and West edges of a tile
    """
    print(f"North : {terDict[tile.north]}")
    print(f"East  : {terDict[tile.east]}")
    print(f"South : {terDict[tile.south]}")
    print(f"West  : {terDict[tile.west]}")

testTile = Tile(1, 1, 1, 1)

printBiomes(testTile, terrainDict)