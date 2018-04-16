# Import file
filename = 'Prob03.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        sides = [int(n) for n in file.readline().strip().split(', ')]

        sideA = sides[0]
        sideB = sides[1]
        sideC = sides[2]

        if (sideA + sideB) > sideC and (sideB + sideC) > sideA and (sideA + sideC) > sideB:
            if sideA == sideB and sideA == sideC:
                print('Equilateral')
            elif (sideA == sideB and sideA != sideC) or (sideB == sideC and sideB != sideA) or (sideC == sideA and sideC != sideB):
                print('Isosceles')
            else:
                print('Scalene')
        else:
            print('Not a Triangle')

        test_cases -= 1