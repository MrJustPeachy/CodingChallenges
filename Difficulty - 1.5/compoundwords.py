import sys

words = []
combinations = []

for line in sys.stdin:

    if line == '\n':
        break

    data = [n for n in line.strip().split()]

    for string in data:
        if string != '/':
            words.append(string)

for i in range(len(words)):
    for j in range(len(words)):
        if i != j:
            combine = words[i] + words[j]
            try:
                combinations.index(combine)
            except ValueError:
                combinations.append(combine)


combinations = sorted(combinations)

for combo in combinations:
    print(combo)
