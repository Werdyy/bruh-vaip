import sys
import time

startTime = time.time()

f = open("vaipsis.txt", "r")
readRaw = f.readlines()

Room = readRaw[0].split()


CarpetCount = int(Room[0])  #amount of carpets
if CarpetCount > 3 or CarpetCount < 1:
    print("Amount of carpets has to be between 1-3")
    sys.exit()

roomGrid = []
gridX = int(Room[2]) #east to west size
gridY = int(Room[1]) #north to south size
Area = gridX * gridY # area of room

for row in range(gridX):
    for column in range(gridY):
        roomGrid.append((row, column))

carpetGrid = []

totalCarpet = []

with open("vaipsis.txt", "r") as input:
    for i, line in enumerate(input.readlines(), 0):
        if i >= 1:
            CarpetSize = line.split()
            carpetXlen = gridX - int(CarpetSize[0]) - int(CarpetSize[1])
            carpetYlen = gridY - int(CarpetSize[2]) - int(CarpetSize[3])
            for x in range(carpetXlen):
                for y in range(carpetYlen):
                    carpetGrid.append((x + int(CarpetSize[0]), y + int(CarpetSize[3])))
            for CarpetCoordinates in roomGrid:
                for CarpetCoordinates in carpetGrid:
                    if CarpetCoordinates not in totalCarpet:
                        totalCarpet.append(CarpetCoordinates)

with open("vaipval.txt", "w") as output:
    output.write(str(len(totalCarpet)))

endTime = time.time()
print(endTime - startTime)


           













