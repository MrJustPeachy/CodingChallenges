import sys

for line in sys.stdin:

    if line.strip() == '0':
        break

    listLength = int(line.strip())
    doubleListLength = listLength * 2

    firstList = []
    secondList = []

    while doubleListLength > 0:
        number = int(input().strip())

        if listLength >= doubleListLength:
            secondList.append(number)
        else:
            firstList.append(number)

        doubleListLength -= 1

    sortedFirstList = sorted(firstList)
    sortedSecondList = sorted(secondList)

    for num in firstList:
        firstSortedNum = sortedFirstList.index(num)

        print(sortedSecondList[firstSortedNum])

    print()