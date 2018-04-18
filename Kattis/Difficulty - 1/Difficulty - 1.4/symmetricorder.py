import sys

setCounter = 1

for line in sys.stdin:

    if line.strip() == '0':
        break

    test_cases = int(line.strip())

    names = []

    while test_cases > 0:

        names.append(input().strip())

        test_cases -= 1

    evenNames = []
    oddNames = []

    for i in range(len(names)):
        if i % 2 == 0 or i == 0:
            evenNames.append(names[i])
        else:
            oddNames.append(names[i])

    print('SET ' + str(setCounter))

    for name in evenNames:
        print(name)
    for name in oddNames[::-1]:
        print(name)

    setCounter += 1