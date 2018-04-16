# Import file
filename = 'Prob08.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        plane_cases = int(file.readline().strip())

        while plane_cases > 0:

            shipName = file.readline().strip()
            shipCoords = [int(n) for n in file.readline().strip().split(',')]
            startLandingZone = [int(n) for n in file.readline().strip().split(',')]
            endLandingZone = [int(n) for n in file.readline().strip().split(',')]

            rightAngle = [shipCoords[0], startLandingZone[1]]

            startSlope = ((startLandingZone[1] - shipCoords[1]) / (startLandingZone[0] - shipCoords[0]))
            endSlope = ((endLandingZone[1] - shipCoords[1]) / (endLandingZone[0] - shipCoords[0]))

            if -1.6 <= startSlope and endSlope <= -.8:
                print('%s, Clear To Land!' % shipName)
            else:
                print('%s, Abort Landing!' % shipName)

            plane_cases -= 1

        test_cases -= 1