import sys
import operator

names = []
firstNames = []
lastNames = []

for line in sys.stdin:

    if line == '\n':
        break

    name = line.strip().split()
    names.append(name)
    firstNames.append(name[0])
    lastNames.append(name[1])

sortedList = sorted(names, key=operator.itemgetter(1, 0))

for name in sortedList:
    if firstNames.count(name[0]) <= 1:
        print(name[0])
    else:
        print(name[0], name[1])
