import sys

listCount = 1

for line in sys.stdin:

    if line.strip == '0':
        break

    animals = int(line.strip())

    animalsList = []

    for animalInput in sys.stdin:
        if len(animalsList) > animals - 1:
            break
        else:
            animalsList.append(animalInput.strip().split()[-1].lower())

    print(animalsList)