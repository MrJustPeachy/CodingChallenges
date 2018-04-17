import operator

# Import file
filename = 'Prob08.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        distanceBetween, speedOfShip = [float(n) for n in file.readline().strip().split()]

        timeToTravel = (distanceBetween * 1000000) / (speedOfShip * (1 / 3600))



        print(timeToTravel / 3600)


        test_cases -= 1