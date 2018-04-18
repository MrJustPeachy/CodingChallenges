import sys

contestants = []
score = []

for line in sys.stdin:

    if line == '\n':
        break

    data = sum([int(n) for n in line.split()])
    contestants.append(data)

maxScore = max(contestants)

index = contestants.index(maxScore)

print(str(index + 1) + ' ' + str(maxScore))