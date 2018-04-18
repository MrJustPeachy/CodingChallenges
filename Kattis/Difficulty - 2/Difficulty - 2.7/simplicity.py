from collections import Counter

string = input().strip()

mostCommon = Counter(string).most_common()

takenOff = 0

for i in reversed(range(len(mostCommon))):
    if i > 1:
        takenOff += mostCommon[i][1]

print(takenOff)
