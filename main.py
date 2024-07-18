from waFuCo import WaFuCo
import time

# keep the world 2d array as 3d, so that each tile can also store additional information

# 0 - tile
# 1 - structure
# 2 - resources???
# 3 territory???

xDim = int(input("Bonvolu eniri la 'x'-n dimension: "))
yDim = int(input("Bonvolu eniri la 'y'-n dimension: "))

if __name__ == '__main__':
    waFuCo = WaFuCo(xDim, yDim, 6 ,6, True)

    waFuCo.oceanBorder()
    # waFuCo.grassVomit(30, 5)


    numClean = 8
    numGrassClean = 4


    print("kreas la mondon...")

    count = 1
    while count > 0:
        count = waFuCo.countPlacedTiles()
        waFuCo.handle_events()
        waFuCo.prunePossibilities()
        waFuCo.randomEligibleTile()
        waFuCo.processVisuals()

    print("purigxas la maron...")
    waFuCo.cleanOcean(5)
    waFuCo.heavyDutyOceanClean(4)

    print("kreskas herbojn...")
    waFuCo.cleanGrass(4)

    print("kreskas arbarojn...") # the trees are being placed, visuals are just not processing
    waFuCo.spawnForestsInst(7) # why does this often just not fucking work
    waFuCo.cleanForest()
    time.sleep(0.25)

    print("konstruas urbetojn...")
    waFuCo.spawnVillage(40, 2, 2)

    print("konstruas havenojn")
    waFuCo.spawnPier()

    print("estas bela mondo, cxu ne?")

    while True:
        waFuCo.handle_events()
        pass
        


