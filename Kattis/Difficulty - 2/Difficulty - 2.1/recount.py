import sys
from collections import Counter

names = []

for line in sys.stdin:

    if line.strip() == '***':
        break

    names.append(line.strip())

voteCounts = Counter(names).most_common()


if voteCounts[0][1] > voteCounts[1][1]:
    print(voteCounts[0][0])
else:
    print('Runoff!')