import math
import sys

linesOfText = []

for line in sys.stdin:

    if line == '\n':
        break

    linesOfText.append(line.strip())

longestString = len(max(linesOfText, key=len))

linesOfText.pop(-1)

differences = 0

for line in linesOfText:
    differences += math.pow((longestString - len(line)), 2)

print(int(differences))