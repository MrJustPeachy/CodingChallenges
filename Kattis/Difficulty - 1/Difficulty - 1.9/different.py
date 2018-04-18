import sys

for line in sys.stdin:

    data = [int(n) for n in line.strip().split()]

    print(abs(data[0] - data[1]))