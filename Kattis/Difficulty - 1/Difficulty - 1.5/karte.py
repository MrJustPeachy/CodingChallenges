from collections import Counter

data = input().strip()

cards = [data[i: i+3] for i in range(0, len(data), 3)]

count = Counter(cards).most_common()[0][1]

suitP = 13
suitK = 13
suitH = 13
suitT = 13

if count >= 2:
    print('GRESKA')
else:

    for card in cards:
        suit = card[0]

        if suit == 'P':
            suitP -= 1
        elif suit == 'K':
            suitK -= 1
        elif suit == 'H':
            suitH -= 1
        elif suit == 'T':
            suitT -= 1

    print('%d %d %d %d' % (suitP, suitK, suitH, suitT))