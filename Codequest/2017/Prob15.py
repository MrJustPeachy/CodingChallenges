from collections import Counter
import heapq

# Import file
filename = 'Prob15.in.txt'

with open(filename) as file:

    test_cases = int(file.readline().strip())

    while test_cases > 0:

        number = file.readline().strip()
        num = max(number)
        numberCounts = Counter(number.replace('0', '')).most_common()
        sortedNum = sorted(number.replace('0', ''))

        straight = False

        for i in range(len(sortedNum)):
            initialVal = int(sortedNum[i])
            sequenceList = [n for n in range(initialVal, initialVal + 5)]
            numberList = [int(sortedNum[n]) for n in range(i, i + 5) if i + 5 < len(sortedNum)]
            if sequenceList == numberList:
                straight = True

        if numberCounts[0][1] == 5 and numberCounts[0][0] != '0':
            print('%s = FIVE OF A KIND' % number)
        elif numberCounts[0][1] == 4 and numberCounts[0][0] != '0':
            print('%s = FOUR OF A KIND' % number)
        elif numberCounts[0][1] == 3 and numberCounts[1][1] == 2 and numberCounts[0][0] != '0' and numberCounts[1][0] != '0':
            print('%s = FULL HOUSE' % number)
        elif straight:
            print('%s = STRAIGHT' % number)
        elif numberCounts[0][1] == 3 and numberCounts[0][1] != 0:
            print('%s = THREE OF A KIND' % number)
        elif numberCounts[0][1] == 2 and numberCounts[0][0] != '0' and numberCounts[1][1] == 2 and numberCounts[1][0] != '0':
            print('%s = TWO PAIR' % number)
        elif numberCounts[0][1] == 2 and numberCounts[0][0] != '0':
            print('%s = PAIR' % number)
        else:
            print('%s = %s' % (number, num))



        test_cases -= 1