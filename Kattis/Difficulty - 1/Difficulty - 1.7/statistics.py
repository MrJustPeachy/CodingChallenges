import sys

cases = 1

for line in sys.stdin:

    data = [int(n) for n in line.strip().split()]

    data.remove(data[0])

    print('Case %d: %d %d %d' % (cases, min(data), max(data), max(data) - min(data)))

    cases += 1