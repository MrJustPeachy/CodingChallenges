import sys
import operator

for line in sys.stdin:

    if line.strip() == '0':
        break

    test_cases = int(line.strip())

    names = []

    while test_cases > 0:

        names.append(input().strip())

        test_cases -= 1

    sortedNames = sorted(names)

    for i in range(len(names) - 1):
        if sortedNames[i].startswith(sortedNames[i + 1][:2]) and names.index(sortedNames[i + 1]) < names.index(sortedNames[i]):
            holder = sortedNames[i + 1]
            sortedNames[i + 1] = sortedNames[i]
            sortedNames[i] = holder

    for name in sortedNames:
        print(name)
    print()
