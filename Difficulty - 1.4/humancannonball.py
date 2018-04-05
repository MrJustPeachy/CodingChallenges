import math

test_cases = int(input().strip())

while test_cases > 0:

    data = [float(n) for n in input().strip().split()]

    velocity = data[0]
    theta = math.radians(data[1])
    distanceFromWall = data[2]
    bottomHeight = data[3] + 1
    topHeight = data[4] - 1

    xPos = velocity * math.cos(theta)

    time = distanceFromWall / xPos

    yPos = (velocity * math.sin(theta) * time) - (.5 * 9.81 * (time ** 2))

    if yPos < bottomHeight or yPos > topHeight:
        print("Not Safe")
    else:
        print("Safe")

    test_cases -= 1
