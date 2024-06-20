from waFuCo2 import WaFuCo
import time

if __name__ == '__main__':
    waFuCo = WaFuCo(64, 96, 6 ,6)

    waFuCo.oceanBorder()
    # waFuCo.sillyTestRing(16)
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
        else:
            print("doney with the funny")

