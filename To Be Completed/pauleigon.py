data = [int(n) for n in input().strip().split()]

N = data[0]
paulScore = data[1]
opponentScore = data[2]
round = paulScore + opponentScore + 1

print('N: %d, round: %d' % (N % round, round))

# if N > round:
#
# else:
#