import sys

for line in sys.stdin:
    data = line.strip().split()

    name = ''
    heartbeatData = []

    for d in data:
        try:
            d = float(d)
            heartbeatData.append(d)
        except ValueError:
            name += d + ' '

    print('%f %s' % ((sum(heartbeatData) / len(heartbeatData)), name.strip()))