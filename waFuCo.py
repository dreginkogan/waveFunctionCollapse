import pygame
import sys
from tilesheet import Tilesheet
import random
import time

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
        self.tiles =  Tilesheet('tiles.png', cellWidth, cellHeight, 4, 7)

        self.tileMap = [[[0, 1, 2] for i in range(tilesWidth)] for j in range(tilesHeight)]


    def spawnPier(self):
        for y in range(1, self.tilesHeight-1):
            for x in range(1, self.tilesWidth-1):

                if self.tileMap[y][x][0]==5:

                    # left facing pier
                    if self.tileMap[y][x-2][0] == 0 and self.tileMap[y][x-1][0] == 0:
                        self.tileMap[y][x-1][0] = 11

                    # right facing pier
                    if self.tileMap[y][x+1][0] == 0 and self.tileMap[y][x+2][0] == 0:
                        self.tileMap[y][x+1][0] = 13

                    # down facing pier
                    if self.tileMap[y+1][x][0] == 0 and self.tileMap[y+2][x][0] == 0:
                        self.tileMap[y+1][x][0] = 14

                    # north facing pier
                    if self.tileMap[y-1][x][0] == 0 and self.tileMap[y-2][x][0] == 0:
                        self.tileMap[y-1][x][0] = 12

                self.processVisuals()
                self.handle_events()



    def testTileMap(self):
        self.tileMap = [[[0],[0],[0],[0],[0]], [[0],[2],[2],[2],[0]], [[0],[2],[3],[2],[0]], [[0],[2],[2],[2],[0]], [[0],[0],[0],[0],[0]]]

    def spawnVillage(self, num, treeDist = 1, waterDist = 2):
        eligible = [] # elligible spots for village spawning
        count = num

        for y in range(max(treeDist, waterDist), self.tilesWidth- max(treeDist, waterDist) - 1):
            for x in range(max(treeDist, waterDist), self.tilesHeight - max(treeDist, waterDist) - 1):

                if self.tileMap[y][x][0] == 1: #only allow grass tiles to be eligible
                    
                    numTrees = 0
                    numWater = 0

                    for j in range(y-treeDist, y+treeDist+1):
                        for i in range(x-treeDist, x+treeDist+1):
                            numTrees+=self.checkForest(self.tileMap[j][i][0])

                    for j in range(y-waterDist, y+waterDist+1):
                        for i in range(x-waterDist, x+waterDist+1):
                            numWater+=self.checkOcean(self.tileMap[j][i][0])
                            
                    if numTrees>2 and numWater>2:
                        eligible.insert(0,(x,y))
                        print((x,y))

        for i in range(count):
            if len(eligible)<2:
                break
            rand = random.randint(0, len(eligible)-1)
            p, q = eligible[rand]
            eligible.remove((p,q))
            self.tileMap[q][p][0]=5
            self.processVisuals()
            self.handle_events()
            count-=1



    def spawnForestsInst(self, treeCondition): # do i make forest like a tile or an overlay feature
        boomerMap = self.tileMap.copy() # for some reason this tends to not do anything at larger sizes??

        for y in range(1, self.tilesHeight-1): # run cellular automata
            for x in range(1, self.tilesWidth-1):
                grassSumTop = self.checkGrass(boomerMap[y-1][x-1][0]) + self.checkGrass(boomerMap[y-1][x][0]) + self.checkGrass(boomerMap[y-1][x+1][0])
                grassSumLR = self.checkGrass(boomerMap[y][x-1][0]) + self.checkGrass(boomerMap[y][x+1][0])
                grassSumBottom = self.checkGrass(boomerMap[y+1][x-1][0]) + self.checkGrass(boomerMap[y+1][x][0]) + self.checkGrass(boomerMap[y+1][x+1][0])

                forSumTop = self.checkForest(boomerMap[y-1][x-1][0]) + self.checkForest(boomerMap[y-1][x][0]) + self.checkForest(boomerMap[y-1][x+1][0])
                forSumLR = self.checkForest(boomerMap[y][x-1][0]) + self.checkForest(boomerMap[y][x+1][0])
                forSumBottom = self.checkForest(boomerMap[y+1][x-1][0]) + self.checkForest(boomerMap[y+1][x][0]) + self.checkForest(boomerMap[y+1][x+1][0])


                grassSum = grassSumBottom + grassSumLR + grassSumTop + forSumBottom + forSumLR + forSumTop

                if grassSum>=treeCondition and boomerMap[y][x][0] == 1 and random.random()>0.1:
                    self.tileMap[y][x] = [3]

            self.processVisuals()
            self.handle_events()



        time.sleep(0.5)

        self.processVisuals()

    def cleanForest(self):
        boomerMap = self.tileMap.copy()

        for y in range(1, self.tilesHeight-1): # run cellular automata
            for x in range(1, self.tilesWidth-1):
                grassTop = self.checkGrass(boomerMap[y-1][x-1][0]) + self.checkGrass(boomerMap[y-1][x][0]) + self.checkGrass(boomerMap[y-1][x+1][0])
                grassLR = self.checkGrass(boomerMap[y][x-1][0]) + self.checkGrass(boomerMap[y][x+1][0])
                grassBottom = self.checkGrass(boomerMap[y+1][x-1][0]) + self.checkGrass(boomerMap[y+1][x][0]) + self.checkGrass(boomerMap[y+1][x+1][0])

                if grassTop + grassLR + grassBottom > 2 and random.random()>0.5 and self.tileMap[y][x] == [3]:
                    self.tileMap[y][x] = [1]

        self.processVisuals()
        time.sleep(0.25)

        for y in range(1, self.tilesHeight-1): # run cellular automata
            for x in range(1, self.tilesWidth-1):
                grassTop = self.checkGrass(boomerMap[y-1][x-1][0]) + self.checkGrass(boomerMap[y-1][x][0]) + self.checkGrass(boomerMap[y-1][x+1][0])
                grassLR = self.checkGrass(boomerMap[y][x-1][0]) + self.checkGrass(boomerMap[y][x+1][0])
                grassBottom = self.checkGrass(boomerMap[y+1][x-1][0]) + self.checkGrass(boomerMap[y+1][x][0]) + self.checkGrass(boomerMap[y+1][x+1][0])

                if grassTop + grassLR + grassBottom > 6 and self.tileMap[y][x] == [3]:
                    self.tileMap[y][x] = [1]


        self.processVisuals()
        self.handle_events()

    def cleanOcean(self, runs, oceanThreshold = 5): # if not next to grass tile, standards are higher???
        # duplicate tileMap values to new 2d list
        # cellular automata off the copied list to the tileMap
        # only do this once here, multiple iterations will be handled in main <- subject to change

        counter = runs

        while counter>0:

            boomerMap = self.tileMap.copy()

            for y in range(1, self.tilesHeight-1): # run cellular automata
                for x in range(1, self.tilesWidth-1):
                    if boomerMap[y][x][0] == 2:
                        # split up so it's easier to read code
                        oceanSumTop = self.checkOcean(boomerMap[y-1][x-1][0]) + self.checkOcean(boomerMap[y-1][x][0]) + self.checkOcean(boomerMap[y-1][x+1][0])
                        oceanSumLR = self.checkOcean(boomerMap[y][x-1][0]) + self.checkOcean(boomerMap[y][x+1][0])
                        oceanSumBottom = self.checkOcean(boomerMap[y+1][x-1][0]) + self.checkOcean(boomerMap[y+1][x][0]) + self.checkOcean(boomerMap[y+1][x+1][0])

                        if oceanSumTop + oceanSumLR + oceanSumBottom>oceanThreshold:
                            self.tileMap[y][x][0] = 0 

            self.processVisuals()
            counter-=1
            time.sleep(0.5)

    def heavyDutyOceanClean(self, runs, oceanThreshold = 2, grassThreshold = 1):

        counter = runs

        while counter>0:

            boomerMap = self.tileMap.copy()
            
            for y in range(1, self.tilesHeight-1): # run cellular automata
                for x in range(1, self.tilesWidth-1):
                    grassSumTop = self.checkGrass(boomerMap[y-1][x-1][0]) + self.checkGrass(boomerMap[y-1][x][0]) + self.checkGrass(boomerMap[y-1][x+1][0])
                    grassSumLR = self.checkGrass(boomerMap[y][x-1][0]) + self.checkGrass(boomerMap[y][x+1][0])
                    grassSumBottom = self.checkGrass(boomerMap[y+1][x-1][0]) + self.checkGrass(boomerMap[y+1][x][0]) + self.checkGrass(boomerMap[y+1][x+1][0])

                    grassSum = grassSumBottom + grassSumLR + grassSumTop
                    
                    oceanSumTop = self.checkOcean(boomerMap[y-1][x-1][0]) + self.checkOcean(boomerMap[y-1][x][0]) + self.checkOcean(boomerMap[y-1][x+1][0])
                    oceanSumLR = self.checkOcean(boomerMap[y][x-1][0]) + self.checkOcean(boomerMap[y][x+1][0])
                    oceanSumBottom = self.checkOcean(boomerMap[y+1][x-1][0]) + self.checkOcean(boomerMap[y+1][x][0]) + self.checkOcean(boomerMap[y+1][x+1][0])

                    oceanSum = oceanSumBottom + oceanSumLR + oceanSumTop

                    if grassSum<grassThreshold and oceanSum>oceanThreshold: # if at least 1 grass

                        self.tileMap[y][x][0] = 0 

            self.processVisuals()
            counter-=1
            time.sleep(0.5)

    def cleanGrass(self, runs, grassThreshold = 4):
        counter = runs

        while counter>0:

            boomerMap = self.tileMap.copy()

            for y in range(1, self.tilesHeight-1): # run cellular automata
                for x in range(1, self.tilesWidth-1):

                    if boomerMap[y][x][0] == 2: # if the tile is sand
                        # split up so it's easier to read code
                        oceanSumTop = self.checkGrass(boomerMap[y-1][x-1][0]) + self.checkGrass(boomerMap[y-1][x][0]) + self.checkGrass(boomerMap[y-1][x+1][0])
                        oceanSumLR = self.checkGrass(boomerMap[y][x-1][0]) + self.checkGrass(boomerMap[y][x+1][0])
                        oceanSumBottom = self.checkGrass(boomerMap[y+1][x-1][0]) + self.checkGrass(boomerMap[y+1][x][0]) + self.checkGrass(boomerMap[y+1][x+1][0])

                        if oceanSumTop + oceanSumLR + oceanSumBottom>grassThreshold:
                            self.tileMap[y][x][0] = 1 

            self.processVisuals()
            counter-=1
            time.sleep(0.5)

    def checkOcean(self, num):
        if num==0:
            return 1
        else:
            return 0
        
    def checkGrass(self, num):
        if num==1: # need to change this later
            return 1
        else:
            return 0
        
    def checkForest(self, num):
        if num==3:
            return 1
        else:
            return 0

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

    def grassVomit(self, count: int, border: int): # puts random grass in places
        for i in range(count):
            xLoc = random.randint(border, self.tilesWidth-border-1)
            yLoc = random.randint(border, self.tilesHeight-border-1)
            self.tileMap[yLoc][xLoc] = [1]

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
                elif len(self.tileMap[col][row]) == 2:
                    self.placeTile(row, col, -2)
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
        elif tile==3: # forest
            self.screen.blit(self.tiles.get_tile(3,0), (x*self.cellWidth, y*self.cellHeight))
        elif tile==5: # vilage
            self.screen.blit(self.tiles.get_tile(5,0), (x*self.cellWidth, y*self.cellHeight))
        elif tile==11: # pier
            self.screen.blit(self.tiles.get_tile(6,0), (x*self.cellWidth, y*self.cellHeight))
        elif tile==12: # pier
            self.screen.blit(self.tiles.get_tile(6,1), (x*self.cellWidth, y*self.cellHeight))
        elif tile==13: # pier
            self.screen.blit(self.tiles.get_tile(6,2), (x*self.cellWidth, y*self.cellHeight))
        elif tile==14: # pier
            self.screen.blit(self.tiles.get_tile(6,3), (x*self.cellWidth, y*self.cellHeight))
        elif tile == -1: # 3 possibilities
            self.screen.blit(self.tiles.get_tile(4,0), (x*self.cellWidth, y*self.cellHeight))
        elif tile == -2: # 2 possibilities
            self.screen.blit(self.tiles.get_tile(4,1), (x*self.cellWidth, y*self.cellHeight))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()