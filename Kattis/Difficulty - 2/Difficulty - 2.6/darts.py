import math

test_cases = int(input().strip())

while test_cases > 0:

    numOfThrows = int(input().strip())

    throwPoints = 0

    firstCircle = 20.0  # 10
    secondCircle = 40.0  # 9
    thirdCircle = 60.0  # 8
    fourthCircle = 80.0  # 7
    fifthCircle = 100.0  # 6
    sixthCircle = 120.0  # 5
    seventhCircle = 140.0  # 4
    eighthCircle = 160.0  # 3
    ninthCircle = 180.0  # 2
    tenthCircle = 200.0  # 1

    while numOfThrows > 0:

        dartX, dartY = [int(n) for n in input().strip().split()]

        distance = math.sqrt(math.pow(dartX - 0, 2) + math.pow(dartY - 0, 2))

        if distance <= firstCircle:
            throwPoints += 10
        elif firstCircle < distance <= secondCircle:
            throwPoints += 9
        elif secondCircle < distance <= thirdCircle:
            throwPoints += 8
        elif thirdCircle < distance <= fourthCircle:
            throwPoints += 7
        elif fourthCircle < distance <= fifthCircle:
            throwPoints += 6
        elif fifthCircle < distance <= sixthCircle:
            throwPoints += 5
        elif sixthCircle < distance <= seventhCircle:
            throwPoints += 4
        elif seventhCircle < distance <= eighthCircle:
            throwPoints += 3
        elif eighthCircle < distance <= ninthCircle:
            throwPoints += 2
        elif ninthCircle < distance <= tenthCircle:
            throwPoints += 1

        numOfThrows -= 1

    print(throwPoints)

    test_cases -= 1