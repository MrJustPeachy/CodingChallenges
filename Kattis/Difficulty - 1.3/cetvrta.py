firstCoord = [int(n) for n in input().strip().split()]
secondCoord = [int(n) for n in input().strip().split()]
thirdCoord = [int(n) for n in input().strip().split()]

xCoords = [firstCoord[0], secondCoord[0], thirdCoord[0]]
yCoords = [firstCoord[1], secondCoord[1], thirdCoord[1]]

point = []

for coord in xCoords:
    if xCoords.count(coord) < 2:
        point.append(coord)

for coord in yCoords:
    if yCoords.count(coord) < 2:
        point.append(coord)

print(str(point[0]) + ' ' + str(point[1]))
