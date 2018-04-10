import sys
from collections import Counter
from collections import OrderedDict

listCount = 1

for line in sys.stdin:

    if line.strip() == '0':
        break

    animals = int(line.strip())

    animalsList = []

    while animals > 0:

        animal = input().strip().split()
        animalsList.append(animal[-1].lower())

        animals -= 1

    sortedAnimals = sorted(set(animalsList))
    animalCount = Counter(animalsList)

    # print(animalCount)

    print('List %d:' % listCount)

    for animal in sortedAnimals:
        animalsCounted = animalCount[animal]

        print('%s | %d' % (animal, animalsCounted))

    listCount += 1
