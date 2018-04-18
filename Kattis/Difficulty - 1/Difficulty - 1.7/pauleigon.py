data = [int(n) for n in input().strip().split()]

N = data[0]
paulScore = data[1]
opponentScore = data[2]
round = paulScore + opponentScore + 1
NMultiplier = round // N


if round % N == 0:
    NMultiplier -= 1

if NMultiplier % 2 == 0:
    print('paul')
else:
    print('opponent')