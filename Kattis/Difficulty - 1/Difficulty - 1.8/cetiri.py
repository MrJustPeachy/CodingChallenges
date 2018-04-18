from collections import Counter

data = [int(n) for n in input().strip().split()]

sortedData = sorted(data)

differenceList = [sortedData[i + 1] - sortedData[i] for i in range(len(sortedData)) if i != len(sortedData) - 1]

if len(Counter(differenceList)) == 1:
    nextNum = differenceList[0] + sortedData[-1]
    print(nextNum)
else:
    difference = min(differenceList)

    if differenceList.index(max(differenceList)) == 0:
        nextNum = sortedData[0] + difference
        print(nextNum)
    else:
        nextNum = sortedData[1] + difference
        print(nextNum)