# Import file
filename = 'Prob07.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        shipsNum = int(file.readline().strip())

        ships = []

        while shipsNum > 0:

            shipData = file.readline().strip().split(':')
            shipName = shipData[0][:len(shipData[0]) - 2]
            shipType = shipData[0][-1]
            shipCoords = shipData[1]

            ships.append([shipName, shipType, shipCoords])

            shipsNum -= 1

        print(ships)

        test_cases -= 1