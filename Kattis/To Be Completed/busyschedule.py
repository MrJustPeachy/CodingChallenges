import sys
import operator

for line in sys.stdin:

    if line.strip() == '0':
        break

    test_cases = int(line.strip())

    amTimes = []
    pmTimes = []

    while test_cases > 0:

        timeInput = input().strip().split()

        if timeInput[1] == 'a.m.':
            time = timeInput[0].split(':')
            amTimes.append([int(time[0]), int(time[1]), time[1]])
        else:
            time = timeInput[0].split(':')
            pmTimes.append([int(time[0]), int(time[1]), time[1]])

        test_cases -= 1

    sortedAMTimes = sorted(amTimes, key=operator.itemgetter(0, 1))
    sortedPMTimes = sorted(pmTimes, key=operator.itemgetter(0, 1))

    if len(sortedAMTimes) > 0 and sortedAMTimes[-1][0] == 12:
        sortedAMTimes.insert(0, sortedAMTimes[-1])
        sortedAMTimes.pop(-1)
    if len(sortedPMTimes) > 0 and sortedPMTimes[-1][0] == 12:
        sortedPMTimes.insert(0, sortedPMTimes[-1])
        sortedPMTimes.pop(-1)

    for i in range(len(sortedAMTimes)):
        print('%d:%s a.m.' % (sortedAMTimes[i][0], sortedAMTimes[i][2]))

    for i in range(len(sortedPMTimes)):
        print('%d:%s p.m.' % (sortedPMTimes[i][0], sortedPMTimes[i][2]))

    print()
