test_cases = int(input().strip())

while test_cases > 0:

    number = int(input().strip())

    targetNum = 0

    palindromicNum = []

    for i in range(number, 999999):
        if str(i) == str(i)[::-1]:
            palindromicNum.append(i)
            break

    for i in reversed(range(100000, number)):
        if str(i) == str(i)[::-1]:
            palindromicNum.append(i)
            break

    if len(palindromicNum) > 1:
        smallestDiff = abs(palindromicNum[1] - number)
        biggestDiff = abs(palindromicNum[0] - number)

        if smallestDiff <= biggestDiff:
            print(palindromicNum[1])
        else:
            print(palindromicNum[0])
    else:
        print(palindromicNum[0])

    test_cases -= 1
