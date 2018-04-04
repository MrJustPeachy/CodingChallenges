import sys

setup = input().strip().split()
hands = setup[0]
dominantSuit = setup[1]

values = {
    'A': [11, 11],
    'K': [4, 4],
    'Q': [3, 3],
    'J': [20, 2],
    'T': [10, 10],
    '9': [14, 0],
    '8': [0, 0],
    '7': [0, 0]
}

total = 0

for line in sys.stdin:

    if line == '\n':
        break

    hand = line.strip()
    cardType = hand[:1]
    suit = hand[-1]

    if suit == dominantSuit:
        total += values[cardType][0]
    else:
        total += values[cardType][1]

print(total)
