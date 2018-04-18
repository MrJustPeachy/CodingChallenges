data = input().strip()

cards = [0, 0, 0]
points = 0

for card in data:
    if card == 'T':
        cards[0] += 1
    elif card == 'C':
        cards[1] += 1
    elif card == 'G':
        cards[2] += 1

minCards = min(cards)
cards = [c ** 2 for c in cards]

points += sum(cards)
points += minCards * 7

print(points)