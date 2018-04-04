from collections import Counter

data = input().strip().split()

firstDie = int(data[0])
secondDie = int(data[1])

firstDieProbs = [i for i in range(1, firstDie + 1)]
secondDieProbs = [i for i in range(1, secondDie + 1)]

possibilities = []

for i in range(len(firstDieProbs)):
    for j in range(len(secondDieProbs)):
        sum = firstDieProbs[i] + secondDieProbs[j]
        possibilities.append(sum)

mostCommon = Counter(possibilities).most_common()

highest_val = 0

for i in range(len(mostCommon)):
    if highest_val == 0:
        highest_val = mostCommon[i][1]

    if mostCommon[i][1] == highest_val:
        print(mostCommon[i][0])
