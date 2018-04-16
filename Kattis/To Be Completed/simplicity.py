from collections import Counter

string = input().strip()

mostCommon = Counter(string).most_common()

takenOff = 0

for i in reversed(range(len(mostCommon))):
    if len(mostCommon) > 2:
        mostCommon.pop(i)
        takenOff += 1

print(takenOff)
