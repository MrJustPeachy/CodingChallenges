import math

test_cases = int(input().strip())

while test_cases > 0:

    calories = int(input().strip())

    bottles = 0

    if calories > 400:
        bottles = math.ceil(calories / 400)
    elif calories != 0:
        bottles = 1

    print(bottles)

    test_cases -= 1