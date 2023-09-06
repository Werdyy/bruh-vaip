import sys


f = open("vaipsis.txt", "r")
readRaw = f.readlines()

Room = readRaw[0].split()


CarpetCount = int(Room[0])  #amount of carpets
if CarpetCount > 3 or CarpetCount < 1:
    print("Amount of carpets has to be between 1-3")
    sys.exit()


ETW = int(Room[1]) #east to west size
NTS = int(Room[2]) #north to south size
Area = ETW * NTS # area of room









with open("vaipsis.txt", "r") as f:
    for i, line in enumerate(f.readlines(), 0):
        if i >= 1:
            print(line)
            CarpetSize = line.split()
            y = int(Room[1]) - int(CarpetSize[0]) - int(CarpetSize[1])
            x = int(Room[2]) - int(CarpetSize[2]) - int(CarpetSize[3])
            cArea = x * y
            print(cArea)
            

            














