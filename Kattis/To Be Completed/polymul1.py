test_cases = int(input().strip())

while test_cases > 0:

    firstDegrees = int(input().strip())
    firstPolyData = [int(n) for n in input().strip().split()]

    secondDegrees = int(input().strip())
    secondPolyData = [int(n) for n in input().strip().split()]

    completePoly = []

    for i in range(len(firstPolyData)):
        for j in range(len(secondPolyData)):
            if i == 0 and j == 0:
                completePoly.append([firstPolyData[i] * secondPolyData])
            else:
                completePoly[i][j]