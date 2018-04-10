test_cases = int(input().strip())

battlesWon = 0

while test_cases > 0:

    moves = input().strip()

    if not moves.__contains__('CD'):
        battlesWon += 1

    test_cases -= 1

print(battlesWon)