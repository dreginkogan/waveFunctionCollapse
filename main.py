from waFuCo import WaFuCo
import time

# keep the world 2d array as 3d, so that each tile can also store additional information

# 0 - tile
# 1 - structure
# 2 - resources???
# 3 territory???

if __name__ == '__main__':
    waFuCo = WaFuCo(128, 128, 6 ,6, True)

    waFuCo.oceanBorder()
    waFuCo.grassVomit(5, 2)


    numClean = 8
    numGrassClean = 4

    count = 1
    while count > 0:
        count = waFuCo.countPlacedTiles()
        waFuCo.handle_events()
        waFuCo.prunePossibilities()
        waFuCo.randomEligibleTile()
        waFuCo.processVisuals()
    print("initial generation done!")

    waFuCo.cleanOcean(5)
    print("ocean cleaned!")

    waFuCo.heavyDutyOceanClean(4)
    print("islands deleted")

    waFuCo.cleanGrass(4)
    print("let it grow let it grow")

    waFuCo.spawnForestsInst(7)

    while True:
        waFuCo.handle_events()
        pass
        


