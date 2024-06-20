from waFuCo2 import WaFuCo
import time

# keep the world 2d array as 3d, so that each tile can also store additional information

# 0 - tile
# 1 - structure
# 2 - resources???
# 3 territory???

if __name__ == '__main__':
    waFuCo = WaFuCo(48, 64, 6 ,6, True)

    waFuCo.oceanBorder()
    # waFuCo.sillyTestRing(24)
    # waFuCo.prunePossibilities()
    # waFuCo.printTileMap()
    # waFuCo.randomEligibleTile()
    # waFuCo.printTileMap()

    while True:
        waFuCo.handle_events()

        count = waFuCo.countPlacedTiles()

        if count>0:
            waFuCo.prunePossibilities()
            waFuCo.randomEligibleTile()
            waFuCo.processVisuals()


