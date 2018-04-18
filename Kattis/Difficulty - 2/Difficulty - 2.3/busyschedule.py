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

    am12Times = []
    pm12Times = []

    for i in reversed(range(len(amTimes))):
        if amTimes[i][0] == 12:
            am12Times.append(amTimes[i])
            amTimes.pop(i)

    for i in reversed(range(len(pmTimes))):
        if pmTimes[i][0] == 12:
            pm12Times.append(pmTimes[i])
            pmTimes.pop(i)

    sortedAMTimes = sorted(amTimes, key=operator.itemgetter(0, 1))
    sortedAM12Times = sorted(am12Times, key=operator.itemgetter(1))
    sortedPMTimes = sorted(pmTimes, key=operator.itemgetter(0, 1))
    sortedPM12Times = sorted(pm12Times, key=operator.itemgetter(1))

    for i in range(len(sortedAM12Times)):
        print('%d:%s a.m.' % (sortedAM12Times[i][0], sortedAM12Times[i][2]))
    for i in range(len(sortedAMTimes)):
        print('%d:%s a.m.' % (sortedAMTimes[i][0], sortedAMTimes[i][2]))

    for i in range(len(sortedPM12Times)):
        print('%d:%s p.m.' % (sortedPM12Times[i][0], sortedPM12Times[i][2]))
    for i in range(len(sortedPMTimes)):
        print('%d:%s p.m.' % (sortedPMTimes[i][0], sortedPMTimes[i][2]))

    print()
