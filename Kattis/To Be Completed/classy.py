import collections
from operator import itemgetter

test_cases = int(input().strip())

while test_cases > 0:

    numberOfPeople = int(input().strip())

    upperPeople = []
    middlePeople = []
    lowerPeople = []

    while numberOfPeople > 0:

        person = input().strip().split()
        name = person[0][:len(person[0]) - 1]
        classDescription = person[1].split('-')
        finalClass = classDescription[-1]

        points = 0

        for c in classDescription:
            if c == 'lower':
                points += 1
            elif c == 'middle':
                points += 2
            elif c == 'upper':
                points += 3

        if finalClass == 'upper':
            upperPeople.append([name, points])
        elif finalClass == 'middle':
            middlePeople.append([name, points])
        elif finalClass == 'lower':
            lowerPeople.append([name, points])

        numberOfPeople -= 1

    upperPeople = sorted(upperPeople, key=itemgetter(1, 0))
    middlePeople = sorted(middlePeople, key=itemgetter(1, 0), reverse=True)
    lowerPeople = sorted(lowerPeople, key=itemgetter(1, 0))

    for person in upperPeople:
        print(person[0])
    for person in middlePeople:
        print(person[0])
    for person in lowerPeople:
        print(person[0])
    print('==============================')

    test_cases -= 1
