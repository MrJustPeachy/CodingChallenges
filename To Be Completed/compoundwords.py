import sys

words = []
combinations = []

for line in sys.stdin:

    if line == '\n':
        break

    data = [n for n in line.strip().split()]

    for string in data:
        words.append(string)


for i in range(len(words)):
    for j in range(len(words)):
        char = words[i]

        if i != j:
            combine = char + words[j]
            try:
                combinations.index(combine)
            except ValueError:
                combinations.append(combine)

for combo in combinations:
    print(combo)