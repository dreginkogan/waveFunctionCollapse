from waFuCo import WaFuCo
import time

# keep the world 2d array as 3d, so that each tile can also store additional information

# 0 - tile
# 1 - structure
# 2 - resources???
# 3 territory???

if __name__ == '__main__':
    waFuCo = WaFuCo(64, 64, 6 ,6, True)

    waFuCo.oceanBorder()
    # waFuCo.grassVomit(30, 5)


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

    waFuCo.spawnForestsInst(7) # why does this often just not fucking work
    print("arbarojn kreskita!") # the trees are being placed, visuals are just not processing

    waFuCo.cleanForest()
    time.sleep(0.25)

    waFuCo.spawnVillage(30, 2, 2)

    waFuCo.SpawnPier()

    while True:
        waFuCo.handle_events()
        pass
        


