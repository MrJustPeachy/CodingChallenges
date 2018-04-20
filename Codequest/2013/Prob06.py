import operator

# Import file
filename = 'Prob06.in.txt'

golfers = []

for line in open(filename):

    name, scores = line.strip().split(':')
    scores = [int(n) for n in scores.split(',')]
    golfers.append([name, sum(scores)])

sortedGolfers = sorted(golfers, key=operator.itemgetter(1))

print('FIRST:%s' % sortedGolfers[0][0])
print('SECOND:%s' % sortedGolfers[1][0])
print('THIRD:%s' % sortedGolfers[2][0])
print('LAST:%s' % sortedGolfers[-1][0])
