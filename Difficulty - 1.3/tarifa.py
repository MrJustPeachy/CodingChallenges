import sys

principal = input().strip()

history = []

for line in sys.stdin:

    if line == '\n':
        break

    number = int(line)
    history.append(number)

allotted = int(principal) * (history[0] + 1)

for n in history[1:]:
    allotted -= n

print(allotted)